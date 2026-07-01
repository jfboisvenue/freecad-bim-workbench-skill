# Arch Window — Arch.makeWindow / Arch.makeWindowPreset

> Source : wiki FreeCAD « Arch Window » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
L'outil Arch Window crée un objet de base pour tous les objets « encastrables », notamment les fenêtres et les portes. Une porte est le même objet sous-jacent qu'une fenêtre (Arch Door = Arch Window avec un preset de porte) : toute l'information applicable à une fenêtre s'applique à une porte. L'objet peut être indépendant ou « hébergé » dans un composant hôte (Arch Wall, Arch Structure, Arch Roof) ; il possède sa propre géométrie (souvent un cadre et des panneaux internes) et définit un volume à soustraire de l'hôte pour créer une ouverture. Les fenêtres sont basées sur des objets 2D fermés (Draft Rectangle, Sketch) contenant plusieurs wires fermés. L'outil propose plusieurs presets (fenêtres et portes courantes) pour créer ces objets sans construire manuellement les composants.

## Signature
```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```
- Crée un objet `Window` basé sur `baseobj`, qui doit être un Draft Wire ou un Sketcher Sketch bien formé et fermé.
- Si disponibles, définit `width`, `height` et `name` (label) de la fenêtre.
- Si `baseobj` n'est pas une shape fermée, l'outil peut ne pas créer un solide correct.

## Exemple
```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

## Signature — preset (fenêtres et portes)
```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```
- Crée un objet `Window` basé sur `windowtype`, qui doit être l'un des noms définis dans `Arch.WindowPresets`.
- `width` et `height` définissent la taille totale de l'objet, en millimètres.
- Les paramètres `h1`, `h2`, `h3` (décalages verticaux), `w1`, `w2` (largeurs), `o1` et `o2` (décalages horizontaux) spécifient différentes distances en millimètres, et dépendent du type de preset créé.
- Si un `placement` est donné, il est utilisé.

## Exemple — preset (porte)
```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```

## Propriétés (Data)

### Window
- **Area**: l'aire de cette fenêtre.
- **Frame**: la taille (épaisseur/profondeur) du cadre de cette fenêtre.
- **Height**: la hauteur de cette fenêtre.
- **Hole Depth**: la profondeur du trou créé par cette fenêtre dans son hôte.
- **Hole Wire**: le numéro du wire de l'objet base utilisé pour créer le trou dans l'hôte. Réglable graphiquement en double-cliquant la fenêtre. La valeur 0 fait choisir automatiquement le plus grand wire pour le trou.
- **Hosts**: les objets (ex. mur) qui hébergent cette fenêtre.
- **Louvre Spacing**: si un composant est réglé sur "Louvres", définit l'espacement entre les éléments de louvre.
- **Louvre Width**: si un composant est réglé sur "Louvres", définit la taille des éléments de louvre.
- **Normal**: la direction normale de cette fenêtre, fixée (hardcoded) par l'outil en mode interactif. Réglée à (0,0,0) pour que la fenêtre déduise automatiquement sa direction Normal (utile si l'utilisateur tourne le Sketch de base, ex. quand le mur hôte est tourné).
- **Offset**: la taille de l'offset (depuis le sketch de base) de cette fenêtre.
- **Opening**: tous les composants dont l'opening mode est réglé, et pour lesquels une charnière (hinge) est définie dans eux ou dans un composant antérieur, apparaîtront ouverts d'un pourcentage défini par cette valeur.
- **Preset**: le numéro de preset sur lequel cette fenêtre est basée. (Hidden)
- **Subvolume**: un objet optionnel définissant un volume à soustraire des hôtes de cette fenêtre.
- **Symbol Elevation**: affiche le symbole d'ouverture 2D en élévation.
- **Symbol Plan**: affiche le symbole d'ouverture 2D en plan.
- **Width**: la largeur de cette fenêtre.
- **Window Parts**: les composants de cette fenêtre (5 chaînes par composant). (Hidden)
