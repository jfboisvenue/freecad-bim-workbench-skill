# Arch Component — propriétés communes à tous les objets Arch

> Source : wiki FreeCAD « Arch Component » (CC-BY-3.0, © contributeurs FreeCAD).

## Rôle de cette fiche

Arch Component est l'objet de base **partagé par tous les autres objets Arch**
(Wall, Structure, Window, Space, etc., sauf les outils ne produisant pas de solide
comme SectionPlane ou Axis). Les groupes de propriétés **Component**, **IFC** et
**IFC Attributes** listés ici sont donc **communs** — les fiches `walls.md`,
`structure.md`, etc. renvoient ici plutôt que de les répéter.

La commande `Arch.makeComponent` crée un composant Arch **non paramétrique** à partir
de n'importe quel objet basé sur Part, ce qui lui donne les mêmes attributs qu'un
objet Arch et permet de fixer son export IFC via la propriété **Ifc Type**.

## Propriétés (Data)

### Component
- **Additions** *(LinkList)* : liste d'objets basés sur Shape dont la forme est
  **unie** à la forme de base du composant pour produire la forme finale.
- **Axis** *(Link)* : axe ou système d'axes optionnel sur lequel dupliquer l'objet.
- **Base** *(Link)* : objet base (basé sur Shape) sur lequel repose le composant.
  Certains types l'utilisent tel quel, d'autres (ex. Wall) l'extrudent. La base
  n'est pas obligatoire pour certains types (ex. Structure).
- **Clone Of** *(Link)* : un composant peut être le clone d'un autre du **même
  type** (un Wall ne clone qu'un Wall). Seule exception : le Component générique
  peut cloner n'importe quel type, ce qui permet d'écraser le type d'un autre.
- **Hi Res** *(Link)* : forme d'un autre objet servant de version haute résolution
  (n'affecte que la représentation 3D, pas la forme réelle).
- **Horizontal Area** *(Area)* : aire de la projection sur le plan XY (lecture seule).
- **Material** *(Link)* : matériau (`Material`) ou multi-matériau (`MultiMaterial`)
  attaché ; définit couleur/transparence et est exporté vers IFC/OBJ/DAE.
- **Move Base** *(Bool)* : si vrai, déplacer l'objet déplace sa base à la place.
- **Move With Host** *(Bool)* : si vrai, un composant intégré dans un hôte (ex. une
  fenêtre dans un mur) se déplace/tourne avec l'hôte lors d'un Draft Move/Rotate.
- **Perimeter Length** *(Length)* : longueur du périmètre de l'aire horizontale
  (lecture seule).
- **Standard Code** *(String)* : code de standard optionnel (OmniClass, etc.).
- **Subtractions** *(LinkList)* : liste d'objets basés sur Shape dont la forme est
  **soustraite** de la forme de base du composant.
- **Vertical Area** *(Area)* : aire de toutes les faces verticales (lecture seule).

### IFC
- **Ifc Data** *(Map, caché)*.
- **Ifc Properties** *(Map, caché)*.
- **Ifc Type** *(Enumeration)* : définit le **type d'objet IFC** vers lequel exporter.
  Précise la fonction au-delà du type FreeCAD (ex. une Structure peut avoir le rôle
  poutre ou poteau). Un Component générique peut prendre n'importe quel rôle.

### IFC Attributes
- **Description** *(String)* : texte libre, utilisé à l'export IFC.
- **Global Id** *(String)* : identifiant global IFC.
- **Object Type** *(String)*.
- **Predefined Type** *(Enumeration)*.
- **Tag** *(Enumeration)* : champ texte pour donner une identité personnalisée
  supplémentaire à l'objet.

## Notes
- Le **Placement** du composant est appliqué **après** les additions/soustractions :
  celles-ci se font contre la base à sa position d'origine, puis le résultat est
  déplacé au Placement.
- On ajoute/retire des objets aux listes Additions/Subtractions avec les commandes
  Arch Add / Arch Remove (ou via le panneau de tâches).
