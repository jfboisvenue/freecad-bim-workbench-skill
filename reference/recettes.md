# Recettes transverses (savoir-faire prouvé)

Patrons éprouvés qui ne sont pas de simples signatures. Tous validés sur FreeCAD 1.0.2.

## 1. Percer une ouverture dans un mur

**Voie fiable — soustraction :** un volume de vide soustrait à l'hôte perce une
ouverture nette.
```python
void = doc.addObject("Part::Box", "Ouverture_void")
void.Length, void.Width, void.Height = 1200, 400, 1000   # largeur, > ép. mur, hauteur
void.Placement.Base = FreeCAD.Vector(cx-600, -200, 900)  # centré, traverse le mur, allège 900
doc.recompute()
Arch.removeComponents(void, host=wall)                   # perce le mur
doc.recompute()
```
Vérifier que ça a mordu : le **volume du mur diminue** de `largeur×épaisseur×hauteur`.

**Voie BIM — fenêtre hôtée :** `Arch.makeWindowPreset(...)` puis `win.Hosts = [wall]`
(la fenêtre soustrait son emprise). Plus riche (cadre, vitrage) mais l'orientation
du placement sur la face du mur est délicate. Signatures : `windows-doors.md`.

## 2. Traçabilité réglementaire (le livrable du projet)

Chaque décision dimensionnelle issue du Code se **grave dans l'objet BIM**, pour
partir avec lui à l'export IFC :
```python
lintel.IfcType = "Beam"
lintel.Description = ("Linteau 2-38x140. Ref: CNB 2020 mod. Div.B art. 9.23.12.3 "
    "+ Tableau 9.23.12.3.-A. Hypotheses A VALIDER: toit+plafond seul, tributaire "
    "<=0.6 m, neige <=3.0 kPa.")
```
Le **contenu** de l'article vient du skill `rbq-autoconstruction` (MCP officiel) —
jamais de mémoire. Ici on ne fait que **consigner** la référence dans le modèle.

## 3. Gestion des vues & captures

Les objets `Draft`/annotations et la caméra sont un **état global** : après avoir
produit une planche 2D, il faut **restaurer** la vue 3D (sinon « où est passée la 3D ? »).
```python
import FreeCADGui as Gui
v = Gui.getDocument(doc.Name).ActiveView
v.viewIsometric()           # ou viewFront / viewTop / viewRight
Gui.SendMsgToActiveView("ViewFit")
Gui.updateGui()             # 2x parfois nécessaire avant capture
v.saveImage("/chemin/img.png", 1500, 950, "White")   # largeur, hauteur, fond
```

**Planche de plan propre** (ne montrer que la projection 2D + cotes) :
```python
keep = {plan_view.Name, d1.Name, d2.Name}
for o in doc.Objects:                 # masquer tout le reste
    if o.ViewObject: o.ViewObject.Visibility = (o.Name in keep)
v.viewTop(); Gui.SendMsgToActiveView("ViewFit"); Gui.updateGui()
v.saveImage(plan_png, 1500, 950, "White")
# … puis restaurer la visibilité et v.viewIsometric() pour l'écran
```

## 4. Rappels de pièges déjà capturés
- **Mur périmétrique** : `make_wire(closed=True, face=False)` — un wire fermé *avec
  face* remplit l'emprise. Voir `walls.md`.
- **Objet Arch** : jamais `doc.addObject("Arch::Wall")` — toujours `Arch.makeX`.
  Voir `SKILL.md` (préséance sur neka).
