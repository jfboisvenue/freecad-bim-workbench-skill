# Arch Site — Arch.makeSite

> Source : wiki FreeCAD « Arch Site » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'Arch Site est un objet spécial combinant les propriétés d'un objet groupe FreeCAD standard et des objets Arch. Il est particulièrement adapté à la représentation d'un site de projet complet ou d'un terrain. Dans un travail architectural basé sur IFC, il sert surtout à organiser le modèle en contenant des objets [building](Arch_Building.md). Le site sert aussi à gérer et afficher un terrain physique, et peut calculer les volumes de terre à ajouter ou retirer.

## Signature
```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```
- Crée un objet `Site` à partir de `objectslist`, qui est une liste d'objets, ou de `baseobj`, qui est une `Shape` ou un `Terrain`.

## Exemple
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```

## Propriétés (Data)
- **Terrain**: Le terrain de base de ce site.
- **Address**: La rue et le numéro de ce site.
- **Postal Code**: Le code postal de ce site.
- **City**: La ville de ce site.
- **Country**: Le pays de ce site.
- **Latitude**: La latitude de ce site.
- **Longitude**: La longitude de ce site.
- **Url**: Une url montrant ce site sur un site de cartographie.
- **Projected Area**: L'aire de la projection de cet objet sur le plan XY.
- **Perimeter**: La longueur du périmètre de ce terrain.
- **Addition Volume**: Le volume de terre à ajouter à ce terrain.
- **Subtraction Volume**: Le volume de terre à retirer de ce terrain.
- **Extrusion Vector**: Un vecteur d'extrusion à utiliser lors des opérations booléennes.
- **Remove Splitter**: Retire les séparateurs (splitters) de la forme résultante.
- **Declination**: L'angle entre le Nord vrai et la direction Nord du document (l'axe Y). Par défaut le Nord pointe vers l'axe Y et l'Est vers l'axe X ; l'angle s'incrémente dans le sens antihoraire. Cette propriété était auparavant nommée **North Deviation**.
- **EPW File**: Permet d'attacher un fichier EPW (site Ladybug EPW data) à ce site. Nécessaire pour afficher les diagrammes de rose des vents.

### View
- **Solar Diagram**: Affiche ou masque le diagramme solaire.
- **Solar Diagram Color**: La couleur du diagramme solaire.
- **Solar Diagram Position**: La position du diagramme solaire.
- **Solar Diagram Scale**: L'échelle du diagramme solaire.
- **Wind Rose**: Affiche ou masque la rose des vents (nécessite la propriété **EPW File** remplie et le module Python Ladybug installé).

---

# Arch Building — Arch.makeBuilding

> Source : wiki FreeCAD « Arch Building » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'Arch Building est un type spécial d'objet groupe FreeCAD particulièrement adapté à la représentation d'une unité de bâtiment complète. Il sert surtout à organiser le modèle en contenant des objets [floor](Arch_Floor.md). À partir de FreeCAD 0.18, l'objet Building est en fait un [BuildingPart](Arch_BuildingPart.md) dont la propriété **IFC Type** est réglée sur « Building » ; tout BuildingPart peut être converti en Building simplement en changeant son IFC Type.

## Signature
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

> ✅ **Vérité-code (FreeCAD 1.0.2) — conforme.** Signature confirmée par le code :
> `makeBuilding(objectslist=None, baseobj=None, name=None)`. Réf. `_generated/signatures.md`.

- Crée un objet `Building` à partir de `objectslist`, qui est une liste d'objets, ou de `baseobj`, qui est une `Shape`.

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

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```

## Propriétés (Data)
- **Building Type**: Le type de ce bâtiment, à choisir dans une liste.
