# Signatures API (vérité code) — `make…`

> Extrait par AST du code source FreeCAD. Le **code fait foi**.

## `makeAxis`  <sub>Arch.py:57</sub>
```python
def makeAxis(num=1, size=1000, name=None)
```

## `makeAxisSystem`  <sub>Arch.py:86</sub>
```python
def makeAxisSystem(axes, name=None)
```

## `makeBuilding`  <sub>Arch.py:131</sub>
```python
def makeBuilding(objectslist=None, baseobj=None, name=None)
```

## `makeBuildingPart`  <sub>Arch.py:103</sub>
```python
def makeBuildingPart(objectslist=None, baseobj=None, name=None)
```

## `makeComponent`  <sub>ArchCommands.py:232</sub>
```python
def makeComponent(baseobj=None, name=None, delete=False)
```

## `makeCompoundFromSelected`  <sub>ArchCommands.py:1181</sub>
```python
def makeCompoundFromSelected(objects=None)
```

## `makeCurtainWall`  <sub>Arch.py:190</sub>
```python
def makeCurtainWall(baseobj=None, name=None)
```

## `makeEquipment`  <sub>Arch.py:210</sub>
```python
def makeEquipment(baseobj=None, placement=None, name=None)
```

## `makeFace`  <sub>ArchCommands.py:324</sub>
```python
def makeFace(wires, method=2, cleanup=False)
```

## `makeFence`  <sub>Arch.py:236</sub>
```python
def makeFence(section, post, path)
```

## `makeFloor`  <sub>Arch.py:121</sub>
```python
def makeFloor(objectslist=None, baseobj=None, name=None)
```

## `makeFrame`  <sub>Arch.py:254</sub>
```python
def makeFrame(baseobj, profile, name=None)
```

## `makeGrid`  <sub>Arch.py:277</sub>
```python
def makeGrid(name=None)
```

## `makeIfcSpreadsheet`  <sub>ArchCommands.py:1355</sub>
```python
def makeIfcSpreadsheet(archobj=None)
```

## `makeMaterial`  <sub>Arch.py:292</sub>
```python
def makeMaterial(name=None, color=None, transparency=None)
```

## `makeMultiMaterial`  <sub>Arch.py:315</sub>
```python
def makeMultiMaterial(name=None)
```

## `makePanel`  <sub>Arch.py:359</sub>
```python
def makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name=None)
```

## `makePanelCut`  <sub>Arch.py:388</sub>
```python
def makePanelCut(panel, name=None)
```

## `makePanelSheet`  <sub>Arch.py:403</sub>
```python
def makePanelSheet(panels=[], name=None)
```

## `makePipe`  <sub>Arch.py:419</sub>
```python
def makePipe(baseobj=None, diameter=0, length=0, placement=None, name=None)
```

## `makePipeConnector`  <sub>Arch.py:452</sub>
```python
def makePipeConnector(pipes, radius=0, name=None)
```

## `makeProfile`  <sub>Arch.py:472</sub>
```python
def makeProfile(profile=[0, 'REC', 'REC100x100', 'R', 100, 100])
```

## `makeProject`  <sub>Arch.py:503</sub>
```python
def makeProject(sites=None, name=None)
```

## `makeRailing`  <sub>Arch.py:860</sub>
```python
def makeRailing(stairs)
```

## `makeRebar`  <sub>Arch.py:539</sub>
```python
def makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name=None)
```

## `makeReference`  <sub>Arch.py:590</sub>
```python
def makeReference(filepath=None, partname=None, name=None)
```

## `makeRoof`  <sub>Arch.py:612</sub>
```python
def makeRoof(baseobj=None, facenr=0, angles=[45.0], run=[250.0], idrel=[-1], thickness=[50.0], overhang=[100.0], name=None)
```

## `makeSectionPlane`  <sub>Arch.py:673</sub>
```python
def makeSectionPlane(objectslist=None, name=None)
```

## `makeSite`  <sub>Arch.py:704</sub>
```python
def makeSite(objectslist=None, baseobj=None, name=None)
```

## `makeSpace`  <sub>Arch.py:730</sub>
```python
def makeSpace(objects=None, baseobj=None, name=None)
```

## `makeStairs`  <sub>Arch.py:760</sub>
```python
def makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name=None)
```

## `makeStructuralSystem`  <sub>ArchStructure.py:131</sub>
```python
def makeStructuralSystem(objects=[], axes=[], name=None)
```

## `makeStructure`  <sub>ArchStructure.py:66</sub>
```python
def makeStructure(baseobj=None, length=None, width=None, height=None, name=None)
```

## `makeTruss`  <sub>Arch.py:907</sub>
```python
def makeTruss(baseobj=None, name=None)
```

## `makeWall`  <sub>Arch.py:929</sub>
```python
def makeWall(baseobj=None, height=None, length=None, width=None, align=None, face=None, name=None)
```

## `makeWindow`  <sub>Arch.py:1082</sub>
```python
def makeWindow(baseobj=None, width=None, height=None, parts=None, name=None)
```

## `makeWindowPreset`  <sub>ArchWindowPresets.py:31</sub>
```python
def makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```
