# Arch Wall — Arch.makeWall

> Source : wiki FreeCAD « Arch Wall » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Wall construit un objet Wall (mur), soit de zéro, soit par-dessus n'importe quel objet basé sur une shape (Part) ou un mesh. Sans objet de base, il se comporte comme un volume cubique défini par ses propriétés length, width et height. Construit sur une base, il peut s'appuyer sur : un objet 2D linéaire (ligne, wire, arc, sketch) où l'on règle épaisseur, alignement (Right, Left, Center) et hauteur (length sans effet) ; une face plane (seule la hauteur change ; si la face est verticale, il utilise width au lieu de height) ; un solide (length, width, height sans effet, la shape du solide est utilisée telle quelle) ; ou un mesh fermé et manifold. Les murs peuvent recevoir des additions/soustractions (Arch Add / Arch Remove) et adopter automatiquement la hauteur de leur floor parent si Height vaut 0.

## Signature
```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

> ⚠️ **Vérité-code (FreeCAD 1.0.2) — l'ordre du wiki est FAUX.** La vraie
> signature est `makeWall(baseobj=None, height=None, length=None, width=None, align=None, face=None, name=None)`
> : **`height` vient AVANT `length` et `width`**. Ne jamais passer ces trois en
> positionnel selon l'ordre du wiki. Toujours nommer les arguments
> (`Arch.makeWall(baseline, width=150, height=2000)`). Réf. `_generated/discrepancies.md`.
> 💡 **Piège du mur périmétrique (vécu).** Pour des murs de contour à partir d'un
> tracé fermé, créer le wire avec **`Draft.make_wire(pts, closed=True, face=False)`**
> (et au besoin `wire.MakeFace = False`). Un wire fermé **avec face** est une
> **surface pleine** : le mur construit dessus extrude le bloc entier (length/width
> ignorés) au lieu de suivre l'axe avec son épaisseur. Symptôme : volume =
> emprise × hauteur au lieu de périmètre × épaisseur × hauteur.

- Crée un objet `Wall` à partir de `baseobj`, qui peut être un objet Draft, un Sketch, une face ou un solide.
- Si aucun `baseobj` n'est fourni, on donne les valeurs numériques de `length`, `width` (épaisseur) et `height`.
- `face` peut indiquer l'index d'une face de l'objet sous-jacent sur laquelle construire le mur, au lieu d'utiliser l'objet entier.
- `align` peut être `"Center"`, `"Left"` ou `"Right"`.
- Retourne `None` si l'opération échoue.

## Exemple
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```

## Propriétés (Data)

### Blocks
- **Block Height**: la hauteur de chaque bloc.
- **Block Length**: la longueur de chaque bloc.
- **Count Broken**: le nombre de blocs cassés (lecture seule).
- **Count Entire**: le nombre de blocs entiers (lecture seule).
- **Joint**: la taille des joints (espace vide) entre les blocs.
- **Make Blocks**: active la génération de blocs.
- **Offset First**: le décalage horizontal de la première ligne de blocs et de chaque ligne impaire.
- **Offset Second**: le décalage horizontal de la deuxième ligne de blocs et de chaque ligne paire.

### Component
- Voir la fiche Arch Component (propriétés communes Component / IFC / IFC Attributes).

### IFC
- Voir la fiche Arch Component (propriétés communes Component / IFC / IFC Attributes).

### IFC Attributes
- Voir la fiche Arch Component (propriétés communes Component / IFC / IFC Attributes).

### Wall
- **Align**: l'alignement du mur sur sa baseline : Left, Right ou Center. La direction des arêtes individuelles de l'objet Base (Sketch/ArchSketch) est prise en compte. Voir aussi **Override Align**.
- **Area**: aire du mur entier, indépendante de la séparation en blocs (lecture seule).
- **Face**: l'index de la face de l'objet base à utiliser. Si non défini ou 0, l'objet entier est utilisé.
- **Height**: la hauteur du mur. Ignorée si le mur est basé sur un solide. Si 0 et que le mur est dans un floor avec hauteur définie, le mur prend automatiquement la hauteur du floor.
- **Length**: la longueur du mur. Éditable si le mur est basé sur un sketch non contraint à une seule arête, ou sur un Draft Wire à une seule arête, sinon lecture seule. (v1.0) La valeur en lecture seule est plus précise.
- **Normal**: la direction d'extrusion du mur. Si (0,0,0), la direction est automatique.
- **Offset**: la distance entre le mur et sa baseline. Fonctionne seulement si **Align** est Right ou Left. Voir aussi **Override Offset**.
- **Override Align**: surcharge **Align** pour définir l'alignement de chaque segment. Ignorée si l'objet Base fournit les Aligns via getAligns() (valeur autre que 'Left, Right, Center' → 'Align' est suivi).
- **Override Width**: surcharge **Width** pour définir la largeur de chaque segment. Ignorée si l'objet Base fournit les Widths via getWidths() (valeur zéro → 'Width' est suivi).
- **Override Offset**: (v1.0) surcharge **Offset** pour définir l'offset de chaque segment. Ignorée si l'objet Base fournit les Offsets via getOffsets() (valeur zéro → 'Offset' est suivi).
- **Width**: la largeur du mur. Ignorée si le mur est basé sur une face ou un solide. Voir aussi **Override Width**.
