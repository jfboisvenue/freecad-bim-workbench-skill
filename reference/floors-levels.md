# Arch Floor — Arch.makeFloor

> Source : wiki FreeCAD « Arch Floor » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Floor est un type spécial d'objet groupe FreeCAD doté de quelques propriétés supplémentaires particulièrement adaptées aux étages de bâtiment. Il possède notamment une propriété de hauteur que ses objets enfants ([murs](Arch_Wall.md) et [structures](Arch_Structure.md)) peuvent utiliser pour définir automatiquement leur propre hauteur. Il sert surtout à organiser le modèle. Depuis la v0.18, l'Arch Floor dérive entièrement de l'objet [Arch BuildingPart](Arch_BuildingPart.md), un conteneur général non limité aux étages ; les anciens objets Floor peuvent être convertis au nouveau type via clic droit puis `Convert to BuildingPart`.

## Signature
```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```
- Crée un objet `Floor` à partir de `objectslist`, qui est une liste d'objets.

## Exemple
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```

## Propriétés (Data)
Un objet Arch Floor partage toutes les propriétés d'un [Arch BuildingPart](Arch_BuildingPart.md), avec la propriété **Ifc Type** réglée sur `"Building Storey"`. Voir la fiche Arch BuildingPart ci-dessous pour le détail des propriétés.

---

# Arch BuildingPart — Arch.makeBuildingPart

> Source : wiki FreeCAD « Arch BuildingPart » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'objet BuildingPart, produit par les commandes BIM Level ou BIM Building, remplace les anciens [Arch Floor](Arch_Floor.md) et [Arch Building](Arch_Building.md) par une version plus complète, utilisable non seulement pour créer des Floor/Storey/Levels mais aussi toutes sortes de situations où différents objets Arch/BIM doivent être groupés, le groupe pouvant être manipulé comme un seul objet ou répliqué. Il possède un [Arch SectionPlane](Arch_SectionPlane.md) implicite intégré, toujours parallèle au plan de base. Sa propriété **IFC Type** détermine son usage : réglée sur **Building Storey** il se comporte comme un niveau, sur **Building** comme un bâtiment, sur **Element Assembly** comme un assemblage.

## Signature
```python
BuildingPart = makeBuildingPart(objectslist=None)
```

> ⚠️ **Vérité-code (FreeCAD 1.0.2) — le wiki est incomplet.** La vraie signature
> accepte plus de paramètres : `makeBuildingPart(objectslist=None, baseobj=None, name=None)`.
> Réf. `_generated/discrepancies.md`.

- Crée un objet `BuildingPart` à partir de `objectslist`, qui est une liste d'objets.

## Exemple
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```

## Propriétés (Data)
Un Arch BuildingPart dérive d'un objet [App GeoFeature](App_GeoFeature.md) et hérite de toutes ses propriétés. Il possède aussi les propriétés additionnelles suivantes :

### Base
- **Group**: Liste des objets référencés (LinkList).
- **_ Group Touched**: (Bool, caché).

### Building Part
- **Area**: L'aire de plancher calculée de cet étage.
- **Height**: La hauteur de cet objet et de ses objets enfants (par ex. des [Arch Walls](Arch_Wall.md)). La hauteur de chaque mur doit être réglée à `0` (zéro) pour que la propriété Height du BuildingPart se propage aux objets contenus.
- **Level Offset**: Le niveau du point (0,0,0) de ce niveau. Cette valeur s'ajoute à l'attribut `Placement.Base.z` du BuildingPart, indiquant un décalage vertical sans déplacer réellement l'objet. Le décalage résultant est affiché si **Show Level** est `True`.
- **Materials Table**: (Map, caché) Une table MaterialName:SolidIndexesList reliant des noms de matériaux à des index de solides, utilisée lors du référencement de cet objet depuis d'autres fichiers.
- **Only Solids**: (Bool) Si vrai, seuls les solides sont collectés par cet objet lorsqu'il est référencé depuis d'autres fichiers.
- **Saved Inventor**: (FileIncluded, caché) Stocke une représentation inventor de cet objet.
- **Shape**: (PartShape, caché) La forme de cet objet.

### Children
- **Height Propagate**: (Bool) Si vrai, la valeur de hauteur se propage aux objets contenus. Voir la propriété **Height** pour les conditions additionnelles.

### IFC
- **Ifc Data**: (Map, caché) Données IFC.
- **Ifc Properties**: (Map, caché) Propriétés IFC de cet objet.
- **Ifc Type**: (Enumeration) Le type IFC de cet objet.

### IFC Attributes
- **Description**: (String) Une description optionnelle pour ce composant.
- **Global Id**: (String).
- **Object Type**: (String).
- **Overall Height**: (Length).
- **Overall Width**: (Length).
- **Partitioning Type**: (Enumeration).
- **Predefined Type**: (Enumeration).
- **Tag**: (String) Une étiquette optionnelle pour ce composant.
- **User Defined Partitioning Type**: (String).
