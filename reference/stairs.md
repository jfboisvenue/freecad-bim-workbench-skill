# Arch Stairs — Arch.makeStairs

> Source : wiki FreeCAD « Arch Stairs » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Stairs permet de construire automatiquement plusieurs types d'escaliers. Les escaliers droits (avec ou sans palier central) peuvent être créés de zéro. Les escaliers plus complexes nécessitent des objets de base (Draft Lines, Draft Wires, Sketches) : les fils/sketches à deux segments ou plus servent à créer des paliers, ceux à une seule arête servent à créer des volées (flights). Les escaliers partagent les propriétés et comportements communs de tous les [Arch Components](Arch_Component.md).

## Signature
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```
- Crée un objet `Stairs` à partir du `baseobj` donné.
- Si `baseobj` n'est pas fourni, il utilise `length`, `width`, `height` et `steps` pour construire un objet solide.

## Exemple
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```

## Propriétés (Data)

### Segment and Parts
- **Abs Top**: (Vector, lecture seule) Le niveau absolu du sommet vers lequel mène l'escalier.
- **Last Segment**: (Link) Dernier segment (volée ou palier) d'un Arch Stairs se connectant à ce segment. Le niveau de départ de l'escalier sera le niveau d'arrivée de ce dernier segment.
- **Outline Left**: (VectorList) Le contour gauche de l'escalier (lecture seule).
- **Outline Left All**: (VectorList) Le contour gauche de tous les segments de l'escalier (lecture seule).
- **Outline Right**: (VectorList) Le contour droit de l'escalier (lecture seule).
- **Outline Right All**: (VectorList) Le contour droit de tous les segments de l'escalier (lecture seule).
- **Railing Height Left**: (Length) Hauteur du garde-corps gauche de l'escalier ou du palier.
- **Railing Height Right**: (Length) Hauteur du garde-corps droit de l'escalier ou du palier.
- **Railing Left**: (LinkHidden) L'objet garde-corps gauche.
- **Railing Offset Left**: (Length) Décalage du garde-corps gauche par rapport au bord de l'escalier ou du palier.
- **Railing Offset Right**: (Length) Décalage du garde-corps droit par rapport au bord de l'escalier ou du palier.
- **Railing Right**: (LinkHidden) L'objet garde-corps droit.

### Stairs
- **Align**: (Enumeration) L'alignement de l'escalier sur la baseline. Utilisé seulement si une baseline est définie. Peut être `Left`, `Right` ou `Center`.
- **Height**: (Length) La hauteur totale de l'escalier. Utilisée seulement si aucune baseline n'est définie, ou si la baseline est horizontale. Ignorée si **Riser Height Enforce** est non nul.
- **Length**: (Length) La longueur totale de l'escalier si aucune baseline n'est définie. Ignorée si **Tread Depth Enforce** est non nul.
- **Width**: (Length) La largeur de l'escalier.
- **Width of Landing**: (FloatList) Si **Number Of Steps** vaut 1, l'objet escalier agit comme un palier. Dans ce cas et si la baseline est multi-segments, la largeur du premier segment du palier suit **Width**, les largeurs des segments suivants suivent la liste définie ici.

### Steps
- **Blondel Ratio**: (Float, lecture seule) Le ratio de Blondel calculé. Ce ratio indique le confort de l'escalier et devrait être entre 62 et 64 cm ou 24.5 et 25.5 in.
- **Landing Depth**: (Length) La profondeur du palier de la volée, si activé dans **Landings**. Vaut par défaut **Width** si 0.
- **Nosing**: (Length) La taille du nez de marche.
- **Number Of Steps**: (Integer) Le nombre de marches (contremarches). Doit être au moins 2 pour une volée unique, et au moins 4 pour un escalier avec palier central.
- **Riser Height**: (Length, lecture seule) La hauteur des contremarches. Si **Riser Height Enforce** vaut 0, elle est calculée (**Height** / **Number of Steps**). Sinon elle est égale à **Riser Height Enforce**.
- **Riser Height Enforce**: (Length) La hauteur imposée des contremarches.
- **Riser Thickness**: (Length) L'épaisseur des contremarches.
- **Tread Depth**: (Length, lecture seule) La profondeur des marches. Si **Tread Depth Enforce** vaut 0, elle est calculée (**Length** / **Number of Steps**). Sinon elle est égale à **Tread Depth Enforce**.
- **Tread Depth Enforce**: (Length) La profondeur imposée des marches.
- **Tread Thickness**: (Length) L'épaisseur des marches.

### Structure
- **Connection Down Start Stairs**: (Enumeration) Le type de connexion entre la dalle de plancher inférieure et le début de l'escalier. Peut être `HorizontalCut`, `VerticalCut` ou `HorizontalVerticalCut`.
- **Connection End Stairs Up**: (Enumeration) Le type de connexion entre la fin de l'escalier et la dalle de plancher supérieure. Peut être `toFlightThickness` ou `toSlabThickness`.
- **Down Slab Thickness**: (Length) L'épaisseur de la dalle de plancher inférieure.
- **Flight**: (Enumeration) La direction de la volée après le palier. Peut être `Straight`, `HalfTurnLeft` ou `HalfTurnRight`.
- **Landings**: (Enumeration) Le type de paliers. Peut être `None` ou `At center` (`At each corner` pas encore implémenté).
- **Stringer Overlap**: (Length) Le chevauchement des limons au-dessus du bas des marches.
- **Stringer Width**: (Length) La largeur des limons.
- **Structure**: (Enumeration) Le type de structure de l'escalier. Peut être `None`, `Massive`, `One stringer` ou `Two stringers`.
- **Structure Offset**: (Length) Le décalage entre le bord de l'escalier et la structure.
- **Structure Thickness**: (Length) L'épaisseur de la structure.
- **Up Slab Thickness**: (Length) L'épaisseur de la dalle de plancher supérieure.
- **Winders**: (Enumeration) Le type de marches balancées (winders). Pas implémenté.
