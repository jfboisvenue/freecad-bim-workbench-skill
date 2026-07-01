# Arch Structure — Arch.makeStructure

> Source : wiki FreeCAD « Arch Structure » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Structure permet de construire des éléments structurels tels que des poteaux (columns) ou des poutres (beams), en spécifiant leur width, length et height, ou en les basant sur un profil 2D (face, wire ou sketch). Si aucun profil n'est fourni, un ensemble de presets est disponible pour construire rapidement un élément structurel à partir d'un profil standard prédéfini (profils métalliques industriels comme HEA, HEB, INP, ou éléments en béton préfabriqué). Un objet structure peut aussi afficher des nodes structurels (linéaires ou surfaciques).

## Signature
```python
structure = makeStructure(baseobj=None, height=None)
structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```
- Crée un objet `structure` à partir de `baseobj`, qui est un profil fermé, et de la hauteur d'extrusion `height`.
- Si aucun `baseobj` n'est fourni, on donne les valeurs numériques de `length`, `width` et `height` pour créer une structure en bloc.
- Le `baseobj` peut aussi être n'importe quel objet solide existant.

## Exemple
```python
import FreeCAD, Draft, Arch

rect = Draft.make_rectangle(200, 300)
structure1 = Arch.makeStructure(rect, height=2000)
FreeCAD.ActiveDocument.recompute()

structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```

## Propriétés (Data)

### Data
- **Tool**: chemin d'extrusion optionnel, de tout type de wire. Si vide, l'extrusion est droite, dans la direction donnée par Normal.
- **Normal**: la direction dans laquelle la face de base sera extrudée. Si (0,0,0), la direction est automatiquement la normale de la face de base.
- **Face Maker**: le type d'algorithme de génération de face pour construire le profil. Options : None ; Simple (fait des faces depuis tous les wires fermés, ignore les recouvrements) ; Cheese (fait des faces avec trous, mais pas de faces dans les trous) ; Bullseye (fait des faces avec trous, y compris les îlots dans les trous).
- **Length**: la longueur de la structure. Utilisée seulement si la structure n'est pas basée sur un profil.
- **Width**: la largeur de la structure. Utilisée seulement si la structure n'est pas basée sur un profil.
- **Height**: la hauteur de la structure, ou la longueur d'extrusion quand basée sur un profil. Si aucune hauteur n'est donnée et que la structure est dans un Arch Floor avec hauteur définie, elle prend automatiquement la hauteur du floor.
- **Nodes Offset**: décalage optionnel entre la ligne centrale et la ligne des nodes.
