# Draft — primitives 2D & placement (support des objets BIM)

> Signatures **vérifiées par introspection** sur FreeCAD 1.0.2 installé
> (`inspect.signature`). Les objets BIM (murs, dalles…) se construisent presque
> toujours sur une base Draft : une ligne, un fil (wire) ou un rectangle.

Les fonctions Draft ont un **alias `makeX` (déprécié) et `make_x` (v0.19+)** ;
les deux sont identiques. Préférer `make_x`. Toujours `import Draft` et terminer
par `FreeCAD.ActiveDocument.recompute()`.

## Vecteurs, placements, rotations (cœur FreeCAD)

```python
import FreeCAD
v = FreeCAD.Vector(x, y, z)                       # un point / une direction (mm)
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1), 90) # axe, angle en degrés
pl  = FreeCAD.Placement(FreeCAD.Vector(0,0,3000), rot)  # position + orientation
```
`FreeCAD` est aliasé `App`. Unités en millimètres, angles en degrés.

## Lignes et fils (axes de murs)

```python
Draft.make_line(first_param, last_param=None)
# first_param, last_param = FreeCAD.Vector. Une ligne droite entre 2 points.

Draft.make_wire(pointslist, closed=False, placement=None, face=None, support=None, bs2wire=False)
# pointslist = liste de FreeCAD.Vector. closed=True ferme le contour (utile pour
# une dalle ou une emprise). face=True crée une face si fermé.
```

## Rectangle, cercle, polygone

```python
Draft.make_rectangle(length, height=0, placement=None, face=None, support=None)
# length, height en mm. placement positionne le coin. face=True -> face pleine.

Draft.make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)

Draft.make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

## Point

```python
Draft.make_point(X=0, Y=0, Z=0, color=None, name='Point', point_size=5)
```

## Déplacer / tourner / mettre à l'échelle

```python
Draft.move(objectslist, vector, copy=False)
# objectslist = un objet ou une liste. vector = FreeCAD.Vector du déplacement.
# copy=True laisse l'original et déplace une copie.

Draft.rotate(objectslist, angle, center=FreeCAD.Vector(0,0,0), axis=FreeCAD.Vector(0,0,1), copy=False)
# angle en degrés.

Draft.scale(objectslist, scale=FreeCAD.Vector(1,1,1), center=FreeCAD.Vector(0,0,0), copy=False)
```

## Patron typique : un mur sur une ligne

```python
import FreeCAD, Draft, Arch
doc = FreeCAD.ActiveDocument or FreeCAD.newDocument("Projet")
baseline = Draft.make_line(FreeCAD.Vector(0,0,0), FreeCAD.Vector(4000,0,0))
wall = Arch.makeWall(baseline, width=200, height=2700)   # arguments NOMMÉS
doc.recompute()
```
> Voir `views-2d.md` pour `make_shape2dview` (projection 2D / plans de coupe).
