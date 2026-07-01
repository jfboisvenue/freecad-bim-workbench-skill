# Arch Space — Arch.makeSpace

> Source : wiki FreeCAD « Arch Space » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Space permet de définir un volume vide, soit à partir d'une forme solide, soit en définissant ses limites (boundaries), soit un mélange des deux. S'il repose uniquement sur des limites, le volume est calculé à partir de la boîte englobante de toutes les limites données, en soustrayant les espaces situés derrière chaque limite. L'objet Space définit toujours un volume solide. L'aire de plancher de l'espace, calculée par intersection d'un plan horizontal au centre de masse du volume, peut aussi être affichée.

## Signature
```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```
- Crée un objet `Space` à partir des `objects` ou de `baseobj` donnés, qui peuvent être :
  - un objet document, qui devient alors la forme de base de l'objet Space, ou
  - une liste d'objets de sélection tels que retournés par `FreeCADGui.Selection.getSelectionEx()`, ou
  - une liste de tuples `(object, subobjectname)`

## Exemple
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

Après la création d'un objet Space, des faces sélectionnées peuvent lui être ajoutées avec le code suivant :

```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Les limites peuvent aussi être retirées, à nouveau en sélectionnant les faces indiquées :

```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```

## Propriétés (Data)
- **Base**: L'objet de base, le cas échéant (doit être un solide).
- **Boundaries**: Une liste d'éléments de limite optionnels.
- **Area**: L'aire de plancher calculée de cet espace.
- **FinishFloor**: La finition du plancher de cet espace.
- **FinishWalls**: La finition des murs de cet espace.
- **FinishCeiling**: La finition du plafond de cet espace.
- **Group**: Objets inclus dans cet espace, comme du mobilier.
- **SpaceType**: Le type de cet espace.
- **FloorThickness**: L'épaisseur de la finition de plancher.
- **NumberOfPeople**: Le nombre de personnes occupant typiquement cet espace.
- **LightingPower**: La puissance électrique nécessaire pour éclairer cet espace, en Watts.
- **EquipmentPower**: La puissance électrique nécessaire aux équipements de cet espace, en Watts.
- **AutoPower**: Si True, Equipment Power est rempli automatiquement par les équipements inclus dans cet espace.
- **Conditioning**: Le type de conditionnement d'air de cet espace.
- **Internal**: Indique si cet espace est interne ou externe.
- **Text**: Le texte à afficher. Utiliser $area, $label, $tag, $floor, $walls, $ceiling pour insérer les données respectives.
- **FontName**: Le nom de la police.
- **TextColor**: La couleur du texte.
- **FontSize**: La taille du texte.
- **FirstLine**: La taille de la première ligne de texte (multiplie la taille de police ; 1 = même taille, 2 = double, etc.).
- **LineSpacing**: L'espace entre les lignes de texte.
- **TextPosition**: La position du texte. Laisser (0,0,0) pour un placement automatique.
- **TextAlign**: La justification du texte.
- **Decimals**: Le nombre de décimales à utiliser pour les textes calculés.
- **ShowUnit**: Afficher ou non le suffixe d'unité.
