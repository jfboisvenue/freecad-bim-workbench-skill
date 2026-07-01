# Cotes & annotations — Draft.make_dimension

> Signatures **vérifiées par introspection** sur FreeCAD 1.0.2. Alias
> `makeDimension` (déprécié) = `make_dimension`.

## Cote linéaire (la plus courante)

```python
Draft.make_dimension(p1, p2, p3=None, p4=None)
```
- `p1`, `p2` = `FreeCAD.Vector` — les deux points à coter.
- `p3` = `FreeCAD.Vector` — point **par lequel passe la ligne de cote** (décalage).
- Retourne l'objet cote ; sa propriété **Distance** donne la valeur mesurée.

```python
import FreeCAD, Draft
# cote horizontale de 8000, ligne de cote décalée sous l'objet
d = Draft.make_dimension(FreeCAD.Vector(0,0,0),
                         FreeCAD.Vector(8000,0,0),
                         FreeCAD.Vector(4000,-1000,0))
doc.recompute()
print(d.Distance)     # 8000.0 mm
```

## Autres

```python
Draft.make_linear_dimension(p1, p2, dim_line=None)
Draft.make_angular_dimension(center=Vector(0,0,0), angles=None,
                             dim_line=Vector(10,10,0), normal=None)   # angles en degrés
```

## Lisibilité (ViewObject)

Les cotes sont des **annotations 3D** : place-les dans le plan que tu vas
regarder (ex. z = hauteur de coupe pour un plan). Pour les rendre lisibles :
```python
d.ViewObject.FontSize = 400      # taille du texte (unités du modèle)
d.ViewObject.ArrowSize = 60
d.ViewObject.ExtLines = 200      # longueur des lignes d'attache
```
> Pour une **planche de plan propre** (masquer les solides, ne montrer que la
> projection 2D + les cotes, vue de dessus), voir la recette dans `recettes.md`.
