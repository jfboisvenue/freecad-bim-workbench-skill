# Arch SectionPlane — plan de coupe pour générer des vues 2D natives

> Source : wiki FreeCAD « Arch SectionPlane » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch SectionPlane place dans le document courant un plan de coupe (« section plane ») qui définit un plan de coupe ou de vue. Il prend son placement selon le plan de travail Draft courant et peut être déplacé et réorienté jusqu'à décrire la vue 2D souhaitée. Le plan de coupe ne considère qu'un certain ensemble d'objets : les objets sélectionnés lors de sa création y sont ajoutés automatiquement (on peut ensuite en ajouter/retirer via Arch Add / Arch Remove). C'est la voie NATIVE de génération de plans et coupes 2D SANS TechDraw : une fois le SectionPlane positionné, on applique `Draft.makeShape2DView` (Draft Shape2DView) sur ce plan pour projeter la coupe en 2D directement dans le document. (Alternativement, TechDraw ArchView permet d'obtenir une vue sur une page TechDraw.)

## Signature
```python
Section = makeSectionPlane(objectslist=None, name="Section")
```
- Crée un objet `Section` à partir de `objectslist`, qui est une liste d'objets.

## Exemple
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```

## Propriétés (Data)
- **Only Solids**: Si `True`, les objets non-solides de l'ensemble seront ignorés.
- **Display Length**: La longueur du gizmo du plan de coupe dans la vue 3D. N'affecte pas la vue résultante.
- **Display Height**: La hauteur du gizmo du plan de coupe dans la vue 3D. N'affecte pas la vue résultante.
- **Arrow Size**: La taille des flèches du gizmo du plan de coupe dans la vue 3D. N'affecte pas la vue résultante.
- **Cut View**: Si `True`, toute la vue 3D sera coupée à l'emplacement de ce plan de coupe.
- **Clip view**: Si `True`, la vue est écrêtée à la hauteur et la longueur d'affichage du plan de coupe. Cela transforme le plan de coupe en caméra orthographique, limitant le champ de vision.

---

# Draft Shape2DView — projection 2D d'un solide ou d'un plan de coupe

> Source : wiki FreeCAD « Draft Shape2DView » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
La commande Draft Shape2DView crée des projections 2D à partir d'objets sélectionnés, généralement des solides 3D ou des Arch SectionPlanes. Les projections sont placées dans la vue 3D. C'est la voie NATIVE pour produire des plans et coupes 2D SANS TechDraw : appliquée à un Arch SectionPlane, elle projette la coupe en 2D directement dans le document. On peut aussi afficher ces projections sur une page TechDraw via TechDraw DraftView. Pour produire des dessins avec des épaisseurs de trait différentes pour les lignes vues et coupées, on utilise deux objets shape2Dview issus d'un même Arch SectionPlane (l'un en mode **Solid**, l'autre en **Cut lines** ou **Cut faces**), placés au même emplacement l'un sur l'autre.

## Signature
```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```
- `baseobj` est l'objet à projeter.
- `projectionVector` est le vecteur de projection. S'il n'est pas fourni, l'axe Z est utilisé.
- `facenumbers` est une liste de numéros de face (base 0). Si fourni, seules ces faces sont considérées.
- `shape2dview` est renvoyé avec la projection 2D créée.
- Note : `make_shape2dview` (v0.19) remplace la méthode dépréciée `makeShape2DView`.
- Modifier la propriété `ProjectionMode` de l'objet créé si nécessaire. Elle peut valoir : `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` ou `"Solid faces"`.

## Exemple
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```

## Propriétés (Data)
Un objet Draft Shape2DView dérive d'un Part Part2DObject et hérite de toutes ses propriétés. Il possède en plus les propriétés suivantes :

### Draft
- **Auto Update**: Indique si la projection doit être recalculée automatiquement quand l'objet **Base** change. `False` peut être utile s'il y a de nombreux Draft Shape2DViews dans un document ou s'ils sont complexes. Si `False`, la commande Std Refresh doit être utilisée pour mettre à jour la projection.
- **Base**: Spécifie l'objet à projeter.
- **Clip**: Si `True`, le contenu est écrêté aux bords du plan de coupe, le cas échéant. Ceci remplace la propriété Clip de l'objet de base.
- **Face Numbers**: Spécifie les indices des faces à projeter. Ne fonctionne que si **Projection Mode** vaut `Individual Faces`.
- **Fuse Arch**: Indique si les objets BIM de même type et matériau sont fusionnés ou non.
- **Hidden Lines**: Indique si les lignes cachées sont affichées ou non.
- **In Place**: Ne fonctionne que si l'objet sélectionné est un Arch SectionPlane et que **Projection Mode** vaut `Cutlines` ou `Cutfaces` ; indique si la projection apparaîtra coplanaire avec le plan de coupe.
- **Projection**: Spécifie la direction de la projection. Ignoré si **Base** est un Arch SectionPlane.
- **Projection Mode**: Spécifie le mode de projection. Modes disponibles :
    - `Solid` : projette l'objet sélectionné entier.
    - `Individual Faces` : projette uniquement les faces de la liste **Face Numbers**.
    - `Cutlines` : ne fonctionne que si l'objet sélectionné est un Arch SectionPlane ; projette uniquement les arêtes coupées par le plan de coupe.
    - `Cutfaces` : ne fonctionne que si l'objet sélectionné est un Arch SectionPlane ; projette comme faces les zones coupées à travers les solides par le plan de coupe.
    - `Solid faces` : projette l'objet sélectionné entier en coupant les faces une par une. Utilisable si le mode `Solid` donne de mauvais résultats.
- **Segment Length**: Spécifie la taille en millimètres des segments linéaires si **Tessellation** vaut `True`.
- **Tessellation**: Indique si la tessellation doit être effectuée. La tessellation remplace les courbes par des séquences de segments de droite. Peut être coûteux en calcul si **Segment Length** est trop court.
- **Visible Only**: Indique si la projection ne doit être recalculée que si elle est visible.
- **Exclusion Points**: Une liste de points d'exclusion. Toute arête passant par un de ces points ne sera pas dessinée.
- **Exclusion Names**: Une liste de noms d'objets. Tout objet enfant vu ou coupé dont le nom figure dans cette liste ne sera pas dessiné. (v0.21)

### View
- **Pattern**: non utilisé.
- **Pattern Size**: non utilisé.
