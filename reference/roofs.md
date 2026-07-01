# Arch Roof — création d'un toit en pente paramétrique

> Source : wiki FreeCAD « Arch Roof » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Roof permet de créer un toit en pente à partir d'un fil (wire) sélectionné. L'objet toit créé est paramétrique et conserve sa relation avec l'objet de base. Le principe est que chaque arête reçoit un profil de toit (pente, largeur, débord, épaisseur). L'outil est toujours en développement et peut échouer avec des formes très complexes.

## Signature
```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```
- Crée un objet `Roof` à partir du `baseobj` fourni, qui peut être un fil fermé (closed wire) ou un objet solide.
- Si `baseobj` est un fil, vous pouvez fournir des listes pour `angles`, `run`, `idrel`, `thickness` et `overhang`, pour chaque arête du fil, afin de définir la forme du toit.
- Les listes sont automatiquement complétées pour correspondre au nombre d'arêtes du fil.

## Exemple
```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```

## Propriétés (Data)

### Roof
- **Angles**: La liste des angles des segments du toit.
- **Border Length**: La longueur totale des bords du toit.
- **Face**: Le numéro de face de l'objet de base utilisé pour construire le toit (non utilisé).
- **Flip**: Indique si la direction du toit doit être inversée.
- **Heights**: La liste des hauteurs calculées des segments du toit.
- **Id Rel**: La liste des IDs des profils relatifs des segments du toit.
- **Overhang**: La liste des débords des segments du toit.
- **Ridge Length**: La longueur totale des faîtes et arêtiers du toit.
- **Runs**: La liste des projections horizontales de longueur des segments du toit.
- **Subvolume**: Le volume à soustraire. S'il est spécifié, il est utilisé à la place du sous-volume auto-généré. (v1.0)
- **Thickness**: La liste des épaisseurs des segments du toit.

Les toits partagent les propriétés et comportements communs de tous les Arch Components.
- Voir la fiche Arch Component (propriétés communes).
