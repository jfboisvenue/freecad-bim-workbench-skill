# Arch IFC — import/export IFC natif (Native-IFC / IfcOpenShell)

> Source : wiki FreeCAD « Arch IFC » (CC-BY-3.0, © contributeurs FreeCAD).

## Description
La BIM Workbench supporte nativement les fichiers IFC (Industry Foundation Classes) et fournit aussi un importateur et un exportateur. À partir de la version 1.0, FreeCAD ouvre et importe les fichiers IFC nativement (voir la page NativeIFC).

Toute la fonctionnalité IFC dépend de la bibliothèque **IfcOpenShell**, incluse dans certaines distributions de FreeCAD. Pour vérifier sa présence, entrer `import ifcopenshell` dans la console Python : si aucune erreur n'apparaît, IfcOpenShell est installé. L'outil BIM Setup recherche aussi IfcOpenShell et notifie s'il n'est pas installé.

IfcOpenShell supporte toutes les entités IFC2x3 et IFC4. L'import démarre par toutes les entités dérivées de IfcProduct (murs, fenêtres, tuyaux…) ; les entités non convertibles en objets BIM sont importées comme simples formes Part. Les préférences IFC permettent de choisir le mode d'import :
- **full parametric Arch objects** : la géométrie est autant que possible éditable dans FreeCAD.
- **non-parametric Arch objects** : les objets portent l'information et les propriétés IFC mais ne sont pas éditables.
- **non-parametric Part shapes** : la géométrie est fidèlement rendue mais l'information IFC est écartée.
- **one Part shape per floor** : un objet tout-en-un, pour référence uniquement.

Un dernier type permet d'écarter entièrement l'import des objets Arch (utile pour les modèles d'analyse structurelle). Les structures Sites, Buildings et Storeys sont fidèlement importées, ainsi que les groupes (IfcGroups), IfcAnnotation, et les entités IfcStructuralItem. Les quantités du fichier IFC ne sont PAS importées (mais restent calculables depuis la géométrie recréée). L'option **show debug messages** des préférences IFC affiche un rapport des échecs d'import. La BIM Workbench propose un IFC explorer pour ouvrir un fichier en mode texte rapide et n'importer que les parties voulues.

À l'export, tous les objets sélectionnés et leurs descendants sont exportés. Tous les objets Arch/BIM sont supportés. Objets non pleinement supportés : PartDesign Bodies, Std Parts, App Links, LinkGroups. Les objets non-Arch sont exportés comme IfcBuildingElementProxy ; les Arch References comme IfcBuildingElementProxies. Les objets Arch sont exportés avec le type défini dans leur propriété « IFC Type », leurs IfcProperties, et l'UID IFC conservé si issu d'un import précédent. L'export se fait en IFC2x3 ou IFC4 selon la version d'IfcOpenShell (à partir de v0.6, la version IFC des préférences Arch est utilisée). Les formes basées sur extrusion ou opération booléenne sont exportées comme telles ; sinon la forme est exportée en IfcFacetedBrep (courbes triangulées, sauf si le serializer IfcOpenShell v0.5+ est activé, qui gère les objets NURBS).

## Scripting / Export-Import

Vérifier la disponibilité d'IfcOpenShell :
```python
import ifcopenshell
```

L'importateur original du module Arch (désactivé dans FreeCAD 1.0, mais toujours disponible depuis Python) :
```python
from importers import importIFC
importIFC.open("C:\\Path\\To\\My\\File.ifc")
```

L'importateur historique (« legacy », sans dépendance à IfcOpenShell — obsolète, non recommandé) :
```python
from importers import importIFClegacy
importIFClegacy.open("C:\\Path\\To\\My\\File.ifc")
```

_La page ne documente pas d'appel Python pour l'export ; l'export IFC se fait via le menu Fichier→Export, ou par le code du module importers/exportIFC.py — à extraire en couche 2._
