# freecad-bim-workbench-skill

**A Claude skill that grounds an LLM in the *real* FreeCAD BIM Workbench (Arch) Python
API — so it stops hallucinating signatures when driving FreeCAD via `execute_code`.**

*(Documentation en français — le contenu du skill est en français.)*

---

## Le problème

On peut piloter FreeCAD depuis un LLM via un serveur MCP qui expose `execute_code` :
tout le module Arch/BIM est alors accessible (`Arch.makeWall`, `makeStructure`,
`makeWindow`, `makeSectionPlane`, export IFC…). Le goulot n'est pas la *capacité* —
c'est la *justesse* : le modèle écrit du Python plausible mais **faux**
(`Arch.makeWall(length=3000)` au mauvais ordre d'arguments) et ça échoue.

Ce skill est le **rempart anti-hallucination** : les vraies signatures et propriétés
de l'API BIM, prêtes à être consultées avant de générer du code.

## Deux couches

1. **Couche 1 — fiches distillées du wiki FreeCAD** (`reference/*.md`) : signatures
   Scripting + propriétés paramétriques, bruit GUI éliminé.
2. **Couche 2 — vérité-code extraite par AST** (`reference/_generated/`,
   `tools/extract_api.py`) : les `def make…` et `obj.addProperty(...)` réels, parsés
   du code source FreeCAD **sans lancer FreeCAD**. En cas de conflit, la couche 2 fait foi.

> La couche 2 a détecté **2 signatures fausses dans le wiki officiel**
> (`makeWall` : ordre `height`/`length`/`width` ; `makeBuildingPart` : incomplet) —
> preuve que l'approche à deux couches est nécessaire. Voir
> `reference/_generated/discrepancies.md`.

## Contenu

```
SKILL.md                     manifeste (règle d'or, conventions, index)
reference/*.md               fiches par objet (murs, structure, ouvertures, espaces,
                             niveaux, site/bâtiment, toits, escaliers, vues 2D, IFC,
                             matériaux, cotes) + recettes (ouverture, traçabilité,
                             ossature bois, gestion des vues)
reference/_generated/        vérité-code (signatures.md, properties.md,
                             discrepancies.md, api.json) — snapshot FreeCAD 1.0.2
tools/extract_api.py         extracteur AST (stdlib pur, sans FreeCAD)
```

**Cible : FreeCAD 1.0.**

## Installation (Claude Code)

Copier ce dépôt comme dossier de skill :

```bash
git clone https://github.com/jfboisvenue/freecad-bim-workbench-skill \
  .claude/skills/bim-workbench
```

(ou dans `~/.claude/skills/bim-workbench` pour un skill utilisateur global).

## Régénérer la couche 2

```bash
# contre une copie locale du dossier src/Mod/BIM (clone ou FreeCAD installé)
python3 tools/extract_api.py --src /chemin/vers/Mod/BIM --out reference/_generated
# ou télécharger un tag directement (réseau requis)
python3 tools/extract_api.py --download-tag 1.0.2 --out reference/_generated
```

## ⚠️ Avertissement / Disclaimer

Ce dépôt est fourni **à titre de référence et d'aide, SANS AUCUNE GARANTIE**
(voir LICENSE). Il **n'est pas** un avis professionnel d'ingénierie ou
d'architecture. Certaines fiches (ossature, linteaux) **citent des numéros
d'articles de codes du bâtiment** uniquement pour la traçabilité : toute décision
dimensionnelle ou structurelle **doit être vérifiée** à la source officielle et
validée par un professionnel qualifié et l'autorité compétente. Les auteurs
déclinent toute responsabilité liée à l'usage de ce contenu.

## Licence & attribution

- Contenu **original** (extract_api.py, SKILL.md, portions rédactionnelles) :
  **Apache-2.0** (voir `LICENSE`).
- Contenu **dérivé de FreeCAD** : fiches du wiki sous **CC-BY-3.0**, données API
  extraites du code sous **LGPL** — attribution dans `NOTICE`.

© contributeurs FreeCAD pour le contenu dérivé. Projet non affilié à FreeCAD.
