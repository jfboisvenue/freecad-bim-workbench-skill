# Matériaux — Arch.makeMaterial / makeMultiMaterial

> Signatures **vérifiées par introspection** sur FreeCAD 1.0.2.

## Matériau simple

```python
Material = makeMaterial(name=None, color=None, transparency=None)
```
- `color` = tuple RVB flottant `(r, g, b)` entre 0 et 1. `transparency` = 0–100.
- Propriétés de l'objet retourné : **Color**, **Transparency**, **Description**,
  **StandardCode** (code normatif optionnel), **ProductURL**.

**Assignation à un objet BIM** (mur, dalle, structure…) :
```python
import Arch
mat = Arch.makeMaterial("Beton", color=(0.66, 0.66, 0.68))
wall.Material = mat          # l'objet a une propriété Material
doc.recompute()
```
La couleur du matériau se reflète sur la forme. Pour forcer une couleur d'affichage
sans matériau : `obj.ViewObject.ShapeColor = (r, g, b)`.

## Multi-matériau (mur multicouche)

```python
MultiMaterial = makeMultiMaterial(name=None)
```
Objet à trois listes **parallèles** (même longueur, de l'extérieur vers l'intérieur) :
- **Names** *(list[str])* — noms des couches.
- **Materials** *(list[Material])* — objets `Material` correspondants.
- **Thicknesses** *(list[float])* — épaisseurs en **mm**.

Assigné au `Material` d'un mur, celui-ci devient **multicouche** : sa `Width` est
répartie selon les épaisseurs. Une épaisseur `0` prend l'espace restant.

```python
gypse   = Arch.makeMaterial("Gypse",     color=(0.95,0.95,0.92))
ossat   = Arch.makeMaterial("Ossature_2x6", color=(0.80,0.62,0.36))
revet   = Arch.makeMaterial("Revetement", color=(0.55,0.55,0.58))
mm = Arch.makeMultiMaterial("Mur_2x6")
mm.Names       = ["Revetement ext", "Ossature 2x6 + isolant", "Gypse"]
mm.Materials   = [revet, ossat, gypse]
mm.Thicknesses = [19.0, 140.0, 13.0]      # total 172 mm
wall.Material  = mm
doc.recompute()
```
> Pour représenter *visuellement* l'ossature membre par membre (poteaux, linteau…),
> voir `ossature-bois.md`. Le multi-matériau donne les **couches**, pas les montants.
