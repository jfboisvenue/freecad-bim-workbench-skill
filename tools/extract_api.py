#!/usr/bin/env python3
"""
extract_api.py — Couche 2 de la base de connaissances BIM Workbench.

Extrait par analyse statique (AST) la VÉRITÉ de l'API BIM/Arch depuis le code
source FreeCAD, sans lancer FreeCAD :
  - toutes les fonctions `def make…(…)` avec leur signature exacte ;
  - toutes les propriétés paramétriques (`obj.addProperty(type, nom, groupe, desc)`)
    regroupées par classe.

C'est le rempart anti-hallucination final : la couche 1 (fiches wiki) donne le
contexte, mais le wiki peut être idéalisé/périmé. Ici, la source = le code.
Ex. réel : le wiki donne makeWall(baseobj, length, width, height, …) alors que le
code 1.0.x est makeWall(baseobj, height, length, width, …) — ordre différent.

Usage :
    # contre une copie locale du dossier src/Mod/BIM (clone ou FreeCAD installé)
    python3 extract_api.py --src /chemin/vers/Mod/BIM --out _generated

    # contre un tag GitHub, téléchargement automatique (nécessite le réseau)
    python3 extract_api.py --download-tag 1.0.2 --out _generated

Sorties dans --out :
    signatures.md     — chaque make…() avec signature exacte + fichier:ligne
    properties.md     — chaque classe Arch et ses propriétés (type, nom, groupe)
    api.json          — la même chose, structuré, pour diff/validation
    discrepancies.md  — écarts entre signatures du code et signatures du wiki

Ne dépend que de la bibliothèque standard. Compatible Python 3.9+ (ast.unparse).
"""

import argparse
import ast
import json
import os
import sys
import urllib.request

# Signatures telles qu'annoncées par le wiki (couche 1), pour la comparaison.
# Format : nom -> liste ordonnée des noms de paramètres attendus.
# Sert uniquement à signaler les écarts ; le code reste la vérité.
WIKI_SIGNATURES = {
    "makeWall": ["baseobj", "length", "width", "height", "align", "face", "name"],
    "makeStructure": ["baseobj", "length", "width", "height", "name"],
    "makeWindow": ["baseobj", "width", "height", "parts", "name"],
    "makeSpace": ["objects", "baseobj", "name"],
    "makeFloor": ["objectslist", "baseobj", "name"],
    "makeBuildingPart": ["objectslist"],
    "makeSite": ["objectslist", "baseobj", "name"],
    "makeBuilding": ["objectslist", "baseobj", "name"],
    "makeRoof": ["baseobj", "facenr", "angles", "run", "idrel", "thickness",
                 "overhang", "name"],
    "makeStairs": ["baseobj", "length", "width", "height", "steps", "name"],
    "makeSectionPlane": ["objectslist", "name"],
}


def _default_repr(node):
    """Rend la valeur par défaut d'un paramètre en source lisible."""
    try:
        return ast.unparse(node)
    except Exception:
        return "<?>"


def extract_signatures(tree, filename):
    """Fonctions `def make…` au niveau module -> dict nom -> infos signature."""
    sigs = {}
    for node in tree.body:  # niveau module uniquement
        if isinstance(node, ast.FunctionDef) and node.name.startswith("make"):
            a = node.args
            params = []          # liste de (nom, default_source|None)
            ordered_names = []   # ordre des noms de paramètres positionnels/kw
            posargs = a.posonlyargs + a.args
            n_def = len(a.defaults)
            offset = len(posargs) - n_def
            for i, arg in enumerate(posargs):
                default = a.defaults[i - offset] if i >= offset else None
                params.append((arg.arg, _default_repr(default) if default else None))
                ordered_names.append(arg.arg)
            if a.vararg:
                params.append(("*" + a.vararg.arg, None))
            for i, arg in enumerate(a.kwonlyargs):
                d = a.kw_defaults[i]
                params.append((arg.arg, _default_repr(d) if d else None))
                ordered_names.append(arg.arg)
            if a.kwarg:
                params.append(("**" + a.kwarg.arg, None))

            try:
                sig = "def %s(%s)" % (node.name, ast.unparse(a))
            except Exception:
                parts = [p if d is None else "%s=%s" % (p, d) for p, d in params]
                sig = "def %s(%s)" % (node.name, ", ".join(parts))

            sigs[node.name] = {
                "name": node.name,
                "signature": sig,
                "params": ordered_names,
                "defaults": {p: d for p, d in params if d is not None},
                "file": os.path.basename(filename),
                "line": node.lineno,
            }
    return sigs


def _addproperty_desc(call):
    """Extrait la description d'un appel addProperty (4e arg éventuel)."""
    if len(call.args) < 4:
        return ""
    arg = call.args[3]
    # cas QT_TRANSLATE_NOOP("App::Property", "texte")
    if isinstance(arg, ast.Call) and arg.args:
        last = arg.args[-1]
        if isinstance(last, ast.Constant) and isinstance(last.value, str):
            return last.value
    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
        return arg.value
    return ""


def _const_str(node):
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None


def extract_properties(tree, filename):
    """Propriétés addProperty regroupées par classe -> liste d'infos."""
    classes = {}
    for cls in ast.walk(tree):
        if not isinstance(cls, ast.ClassDef):
            continue
        props = []
        for node in ast.walk(cls):
            if (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "addProperty"
                    and len(node.args) >= 3):
                ptype = _const_str(node.args[0])
                pname = _const_str(node.args[1])
                pgroup = _const_str(node.args[2])
                if pname is None:
                    continue  # nom dynamique, non extractible statiquement
                props.append({
                    "name": pname,
                    "type": ptype,
                    "group": pgroup,
                    "desc": _addproperty_desc(node),
                    "line": node.lineno,
                })
        if props:
            # dédoublonnage par nom en gardant l'ordre d'apparition
            seen, uniq = set(), []
            for p in props:
                if p["name"] not in seen:
                    seen.add(p["name"])
                    uniq.append(p)
            classes[cls.name] = {
                "class": cls.name,
                "file": os.path.basename(filename),
                "properties": uniq,
            }
    return classes


def _parse_file(path):
    with open(path, encoding="utf-8") as fh:
        return ast.parse(fh.read(), filename=os.path.basename(path))


def public_signatures(src_dir):
    """Signatures du namespace public `Arch.*`.

    Les utilisateurs écrivent `import Arch; Arch.makeX(...)`. Ce qui compte est
    donc le namespace de `Arch.py` : ses `def make…` locales (prioritaires, elles
    écrasent tout import) + les fonctions ramenées par `from X import *`. Les
    autres fichiers (ArchBuilding.py, ArchWall.py…) sont importés comme *modules*
    (`import ArchBuildingPart`) : leurs fonctions internes s'appellent
    `ArchBuildingPart.makeX`, PAS `Arch.makeX` — il ne faut pas les mélanger,
    sinon une fonction interne homonyme masque la vraie (bug makeBuilding).

    Retourne None si `Arch.py` est absent (=> repli scan-all dans analyze()).
    """
    arch_path = os.path.join(src_dir, "Arch.py")
    if not os.path.isfile(arch_path):
        return None
    arch_tree = _parse_file(arch_path)
    star_mods = [n.module for n in arch_tree.body
                 if isinstance(n, ast.ImportFrom)
                 and n.module and any(a.name == "*" for a in n.names)]
    sigs = {}
    for mod in star_mods:  # ordre du fichier : un import* ultérieur écrase
        p = os.path.join(src_dir, mod + ".py")
        if os.path.isfile(p):
            try:
                sigs.update(extract_signatures(_parse_file(p), p))
            except (SyntaxError, UnicodeDecodeError):
                pass
    sigs.update(extract_signatures(arch_tree, arch_path))  # defs locales gagnent
    return sigs


def analyze(src_dir):
    all_classes = {}
    py_files = sorted(f for f in os.listdir(src_dir) if f.endswith(".py"))
    for fname in py_files:
        path = os.path.join(src_dir, fname)
        try:
            tree = _parse_file(path)
        except (SyntaxError, UnicodeDecodeError) as e:
            print("  ! %s ignoré (%s)" % (fname, e), file=sys.stderr)
            continue
        all_classes.update(extract_properties(tree, path))

    sigs = public_signatures(src_dir)
    if sigs is None:  # repli : pas de Arch.py -> scan-all (moins fiable)
        print("  ! Arch.py absent : repli scan-all des signatures", file=sys.stderr)
        sigs = {}
        for fname in py_files:
            path = os.path.join(src_dir, fname)
            try:
                sigs.update(extract_signatures(_parse_file(path), path))
            except (SyntaxError, UnicodeDecodeError):
                continue
    return sigs, all_classes


def write_signatures_md(sigs, out):
    lines = ["# Signatures API (vérité code) — `make…`", "",
             "> Extrait par AST du code source FreeCAD. Le **code fait foi**.", ""]
    for name in sorted(sigs):
        s = sigs[name]
        lines += ["## `%s`  <sub>%s:%d</sub>" % (name, s["file"], s["line"]),
                  "```python", s["signature"], "```", ""]
    with open(os.path.join(out, "signatures.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_properties_md(classes, out):
    lines = ["# Propriétés paramétriques (vérité code) — `addProperty`", "",
             "> Extrait par AST du code source FreeCAD. Le **code fait foi**.", ""]
    for cname in sorted(classes):
        c = classes[cname]
        lines += ["## `%s`  <sub>%s</sub>" % (cname, c["file"]), ""]
        groups = {}
        for p in c["properties"]:
            groups.setdefault(p["group"] or "(sans groupe)", []).append(p)
        for g in sorted(groups):
            lines.append("### %s" % g)
            for p in groups[g]:
                t = (p["type"] or "").replace("App::Property", "")
                lines.append("- **%s** *(%s)*" % (p["name"], t))
            lines.append("")
    with open(os.path.join(out, "properties.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_discrepancies_md(sigs, out):
    lines = ["# Écarts wiki ↔ code — signatures `make…`", "",
             "Compare l'ordre des paramètres annoncé par le wiki (couche 1) à celui",
             "réellement défini dans le code (vérité). Un écart d'ordre = risque de",
             "bug silencieux si le LLM passe des arguments positionnels.", ""]
    n_diff = 0
    for name, wiki_params in sorted(WIKI_SIGNATURES.items()):
        code = sigs.get(name)
        if not code:
            lines += ["## ⚠️ `%s` — introuvable dans le code analysé" % name, ""]
            n_diff += 1
            continue
        code_params = code["params"]
        if code_params == wiki_params:
            lines += ["## ✅ `%s` — identique" % name,
                      "`%s`" % ", ".join(code_params), ""]
        else:
            n_diff += 1
            lines += ["## ❌ `%s` — DIVERGENT" % name,
                      "- wiki : `%s`" % ", ".join(wiki_params),
                      "- code : `%s`" % ", ".join(code_params), ""]
    lines.insert(6, "**%d divergence(s) détectée(s).**\n" % n_diff)
    with open(os.path.join(out, "discrepancies.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return n_diff


BIM_FILES = [
    # Arch.py = namespace public ; ArchCommands/ArchWindowPresets/ArchStructure/
    # ArchSpace y sont ramenés par `from X import *` (nécessaires aux signatures).
    "Arch", "ArchCommands", "ArchWindowPresets",
    "ArchComponent", "ArchWall", "ArchStructure", "ArchWindow",
    "ArchSpace", "ArchFloor", "ArchBuildingPart", "ArchSite", "ArchBuilding",
    "ArchRoof", "ArchStairs", "ArchSectionPlane",
]


def download_tag(tag, dest):
    base = "https://raw.githubusercontent.com/FreeCAD/FreeCAD/%s/src/Mod/BIM" % tag
    os.makedirs(dest, exist_ok=True)
    for name in BIM_FILES:
        url = "%s/%s.py" % (base, name)
        out = os.path.join(dest, "%s.py" % name)
        print("  ↓ %s" % url, file=sys.stderr)
        urllib.request.urlretrieve(url, out)
    return dest


def main():
    ap = argparse.ArgumentParser(description="Extracteur AST de l'API BIM/Arch FreeCAD")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--src", help="dossier src/Mod/BIM (clone ou FreeCAD installé)")
    g.add_argument("--download-tag", help="tag FreeCAD à télécharger (ex. 1.0.2)")
    ap.add_argument("--out", default="_generated", help="dossier de sortie")
    args = ap.parse_args()

    if args.download_tag:
        src = download_tag(args.download_tag, os.path.join(args.out, "_src"))
    else:
        src = args.src
    if not os.path.isdir(src):
        ap.error("source introuvable : %s" % src)

    os.makedirs(args.out, exist_ok=True)
    sigs, classes = analyze(src)
    write_signatures_md(sigs, args.out)
    write_properties_md(classes, args.out)
    n_diff = write_discrepancies_md(sigs, args.out)
    with open(os.path.join(args.out, "api.json"), "w", encoding="utf-8") as f:
        json.dump({"signatures": sigs, "classes": classes}, f,
                  ensure_ascii=False, indent=2)

    print("OK — %d fonctions make…, %d classes, %d divergence(s) wiki↔code."
          % (len(sigs), len(classes), n_diff))
    print("Sorties dans %s/" % args.out)


if __name__ == "__main__":
    main()
