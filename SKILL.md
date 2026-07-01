---
name: bim-workbench
description: >-
  À consulter AVANT d'écrire ou générer du code Python pilotant la FreeCAD BIM
  Workbench (module Arch) — création de murs, structures/dalles/poteaux,
  fenêtres/portes, espaces, étages/niveaux, site/bâtiment, toits, escaliers,
  plans de coupe et vues 2D, import/export IFC. Fournit les signatures Python
  réelles (Arch.makeWall, makeStructure, makeWindow, makeSpace, makeFloor,
  makeBuildingPart, makeSectionPlane, Draft.makeShape2DView…) et les propriétés
  paramétriques exactes, pour éviter d'halluciner l'API. Cible FreeCAD 1.0.
---

# BIM Workbench — base de connaissances API (ancrage anti-hallucination)

## Pourquoi ce skill existe

Le risque n°1 d'un LLM qui pilote FreeCAD via `execute_code`, ce n'est pas la
plomberie du MCP — c'est **halluciner une signature d'API**. Le modèle écrit du
Python plausible (`Arch.makeWall(length=3000)`) mais faux, et ça échoue à
l'exécution. Ce skill est le rempart : **les vraies signatures et propriétés**,
extraites de la doc officielle FreeCAD.

**Règle d'or : ne jamais inventer une signature `make…` ni un nom de propriété.**
Avant de générer du code Arch/BIM, ouvrir la fiche `reference/` correspondante et
copier la signature exacte. Si l'objet n'est pas couvert, le dire — ne pas deviner.

## Cible et conventions FreeCAD 1.0

- **Module :** `import Arch` (les objets BIM sont créés par `Arch.make…`). `Draft`
  pour les objets 2D de base (lignes, `makeShape2DView`). `FreeCAD` (alias `App`)
  pour le document et les `Vector`.
- **Unités :** millimètres. `height=2000` = 2 m.
- **Cycle :** créer l'objet, puis **`FreeCAD.ActiveDocument.recompute()`** — sinon
  la géométrie n'est pas construite. `make…` **retourne `None` si l'opération
  échoue** : toujours vérifier le retour.
- **Nature :** les objets Arch sont des `App::FeaturePython` à proxy — on les crée
  par `Arch.make…`, **jamais** par `doc.addObject("Arch::Wall")` direct (c'est le
  patron identique au FEM `ObjectsFem.make…`).
- **Base + paramètres :** la plupart des objets se construisent soit *from scratch*
  (valeurs numériques length/width/height), soit *sur un objet base* (une ligne
  Draft, un sketch, une face). Quand une base est fournie, certains paramètres
  numériques sont ignorés — voir chaque fiche.

## Préséance sur le workflow générique de neka (IMPORTANT)

Le serveur MCP neka-nat expose des outils (`create_object`, `insert_part_from_library`)
et un prompt par défaut (`ASSET_CREATION_STRATEGY`) orientés **formes génériques**
(cubes, cylindres, bibliothèque de pièces). **Pour l'architecture, ce workflow est
à ignorer :**

- **Ne PAS utiliser `create_object` pour un type `Arch::…`.** Il retombe sur
  `doc.addObject("Arch::Wall", …)`, ce qui crée un objet **cassé** (sans le proxy
  paramétrique Arch). Un objet BIM ne se crée QUE par `Arch.makeX(...)`.
- **Voie à suivre pour tout objet BIM : `execute_code`** avec le code Python
  `import Arch; Arch.makeWall(...)` ancré sur les signatures de ce skill.
- `create_object`/parts-library restent valables pour des solides Part génériques
  hors BIM, mais ce n'est pas notre cas d'usage.

## Comment utiliser ce skill

1. Identifier l'objet BIM à créer (mur, dalle, fenêtre…).
2. Ouvrir la fiche `reference/` correspondante (index ci-dessous).
3. Utiliser la **signature Scripting verbatim** + les **propriétés listées** pour
   régler l'objet après création (`obj.Height = 2500`, etc.).
4. Terminer par `recompute()` et vérifier le retour.

## Index des fiches (`reference/`)

| Fiche | Couvre | Fonction(s) clé |
|-------|--------|-----------------|
| `draft-primitives.md` | **Base 2D & placement** (Vector, lignes, wires, rectangles, move/rotate) — support de presque tous les objets BIM | `Draft.make_line`, `make_wire`, `make_rectangle` |
| `materials.md` | **Matériaux** simples et **multicouches** (murs) + assignation | `Arch.makeMaterial`, `makeMultiMaterial` |
| `annotations.md` | **Cotes** & annotations, lisibilité | `Draft.make_dimension` |
| `arch-component.md` | **Propriétés communes** à tous les objets Arch (Component / IFC / IFC Attributes) — les autres fiches y renvoient | `Arch.makeComponent` |
| `walls.md` | Murs | `Arch.makeWall` |
| `structure.md` | Poteaux, poutres, dalles, semelles | `Arch.makeStructure` |
| `windows-doors.md` | Fenêtres ET portes (même objet) | `Arch.makeWindow` |
| `spaces.md` | Espaces / pièces (surfaces, IFC Space) | `Arch.makeSpace` |
| `floors-levels.md` | Étages, niveaux, regroupements | `Arch.makeFloor`, `Arch.makeBuildingPart` |
| `site-building.md` | Site et bâtiment (hiérarchie IFC) | `Arch.makeSite`, `Arch.makeBuilding` |
| `roofs.md` | Toits | `Arch.makeRoof` |
| `stairs.md` | Escaliers | `Arch.makeStairs` |
| `views-2d.md` | Plans de coupe + vues 2D natives (sans TechDraw) | `Arch.makeSectionPlane`, `Draft.makeShape2DView` |
| `ifc.md` | Import / export IFC, Native-IFC | export/import IFC |
| `ossature-bois.md` | **Recette** — charpente d'un mur (poteaux, linteau, cales) ; **renvoie au skill RBQ** pour toute dimension structurelle | `Part::Box` / `Arch.makeStructure` |
| `recettes.md` | **Recettes transverses** — percer une ouverture, **traçabilité RBQ**, gestion des vues/captures, rappels de pièges | `removeComponents`, `saveImage` |

## Couche 2 — vérité-code extraite par AST (`tools/` + `reference/_generated/`)

La doc wiki (couche 1) donne le contexte, **mais peut être fausse ou périmée**.
La **vérité absolue** est le code source. `tools/extract_api.py` parse l'AST de
`src/Mod/BIM/Arch*.py` (sans lancer FreeCAD) pour extraire les `def make…` et les
`obj.addProperty(...)` réels.

**En cas de conflit entre une fiche `reference/*.md` et `reference/_generated/`,
c'est `_generated/` qui fait foi.** Les fiches wiki portent un encart ⚠️
« Vérité-code » là où un écart a été détecté.

Extraits générés (snapshot tag **1.0.2**) dans `reference/_generated/` :
- `signatures.md` — chaque `make…()` avec sa signature exacte + fichier:ligne ;
- `properties.md` — chaque classe Arch et ses propriétés (type, nom, groupe) ;
- `discrepancies.md` — écarts wiki↔code (à ce jour : `makeWall` et
  `makeBuildingPart` divergent — voir les encarts ⚠️ dans les fiches) ;
- `api.json` — le tout, structuré, pour diff/validation programmatique.

Régénérer (ex. contre le FreeCAD installé après mise à jour) :
```bash
python3 tools/extract_api.py --src /chemin/vers/Mod/BIM --out reference/_generated
# ou, sans clone local, télécharger un tag directement :
python3 tools/extract_api.py --download-tag 1.0.2 --out reference/_generated
```

## Source & licence

Fiches distillées du wiki FreeCAD via le miroir Markdown
[`FreeCAD/FreeCAD-documentation`](https://github.com/FreeCAD/FreeCAD-documentation).
Documentation FreeCAD sous **CC-BY-3.0** — attribution : © contributeurs FreeCAD.
