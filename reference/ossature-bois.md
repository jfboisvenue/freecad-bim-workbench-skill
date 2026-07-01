# Recette — ossature de bois (mur à colombage 2×6)

Comment représenter la **structure** d'un mur à ossature (et pas seulement son
volume). Deux natures d'objet selon le besoin :

- **Volume / surfaces / IFC de mur** → un `Arch.makeWall` (bloc paramétrique),
  éventuellement multicouche (`materials.md`).
- **Charpente membre par membre** (métré bois, détail structurel) → un membre =
  une pièce. `Part::Box` (rapide, pour visualiser) ou `Arch.makeStructure`
  (sémantique BIM, exportable IFC individuellement, plus lourd).

## ⚠️ Toute dimension structurelle passe par le Code (RBQ)

Section, entraxe, portée de linteau, encadrement d'ouverture : **ne jamais les
fixer de mémoire.** Consulter le skill **`rbq-autoconstruction`** (MCP officiel).
Repères rencontrés (CNB 2020 mod., Partie 9) :
- **9.23.12.3 + Tableaux 9.23.12.3.-A à -D** — dimensions/portées des linteaux.
- **9.23.12.2** — linteau : 2+ pièces clouées ; 3) éléments **séparés par des
  cales** (comble l'épaisseur du mur).
- **9.23.10.6** — poteaux d'ouverture **jumelés** (≤ 3 m) ou **triplés** (> 3 m).
- **9.23.11.3** — sablière qui fait **liaison au-dessus** du linteau.

La charpente porteuse relève d'un **ingénieur** : le modèle est un brouillon tracé,
pas un calcul.

## Membres d'un mur (2×6 = 38 × 140 mm)

- **Lisse basse** : pièce horizontale à plat en pied (38 en Z, 140 en Y).
- **Sablière double** : deux pièces horizontales en tête.
- **Poteaux** : montants verticaux (38 en X le long du mur, 140 en Y),
  à l'entraxe prescrit. Hauteur = `H − lisse − 2×sablière`.

### Encadrement d'ouverture
- **Poteau roi (king)** : montant pleine hauteur de chaque côté.
- **Poteau nain (jack/trimmer)** : contre le roi, de la lisse à la **sous-face du
  linteau** ; il **porte** le linteau.
- **Linteau (header)** : 2 pièces **posées sur chant** (140 en Z = profondeur qui
  reprend la flexion) au-dessus de l'ouverture, appui sur les nains + un peu de
  portée. Section selon Tableau 9.23.12.3.-A.
- **Cales** : entre les 2 plis du linteau, comblent l'épaisseur du mur (9.23.12.2 3)).
- **Appui brut** : traverse horizontale au **bas** de l'ouverture.
- **Poteaux nains** : courts montants **au-dessus** du linteau et **sous** l'appui,
  alignés sur l'entraxe.

## Patron (positions calculées)

```python
def box(doc, grp, name, x, y, z, dx, dy, dz, color):
    b = doc.addObject("Part::Box", name)
    b.Length, b.Width, b.Height = dx, dy, dz
    b.Placement.Base = FreeCAD.Vector(x, y, z)
    b.ViewObject.ShapeColor = color
    grp.addObject(b); return b

L, T, H, th, d = 8000, 140, 2700, 38, 140      # mur ; membre 2x6 = 38x140
# lisse basse / sablière double
box(doc, grp, "Lisse", 0,0,0, L,T,th, WOOD)
box(doc, grp, "Sabliere_1", 0,0,H-2*th, L,T,th, WOOD)
box(doc, grp, "Sabliere_2", 0,0,H-th,   L,T,th, WOOD)
# poteaux à 400 mm (sauter la zone d'ouverture)
for x in range(0, L, 400):
    box(doc, grp, f"Poteau_{x}", x,0,th, th,T,H-3*th, WOOD)
# linteau : 2 plis aux faces + cales entre eux (comble T)
box(doc, grp, "Linteau_ext", hx0,0,    RO, hlen,th,d, HEADER)
box(doc, grp, "Linteau_int", hx0,T-th, RO, hlen,th,d, HEADER)
for xc in positions_cales:
    box(doc, grp, "Cale", xc, th, RO, 90, T-2*th, d, CALE)  # y = th..T-th
```
> Trace la référence Code du linteau dans la propriété `Description` de l'objet —
> voir `recettes.md`.
