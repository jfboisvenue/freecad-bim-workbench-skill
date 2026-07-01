# Propriétés paramétriques (vérité code) — `addProperty`

> Extrait par AST du code source FreeCAD. Le **code fait foi**.

## `ArchGrid`  <sub>ArchGrid.py</sub>

### Grid
- **Rows** *(Integer)*
- **Columns** *(Integer)*
- **RowSize** *(FloatList)*
- **ColumnSize** *(FloatList)*
- **Spans** *(StringList)*
- **PointsOutput** *(Enumeration)*
- **Width** *(Length)*
- **Height** *(Length)*
- **AutoWidth** *(Length)*
- **AutoHeight** *(Length)*
- **Reorient** *(Bool)*
- **HiddenFaces** *(IntegerList)*

## `ArchReference`  <sub>ArchReference.py</sub>

### Reference
- **File** *(File)*
- **Part** *(String)*
- **ReferenceMode** *(Enumeration)*
- **FuseArch** *(Bool)*

## `BuildingPart`  <sub>ArchBuildingPart.py</sub>

### BuildingPart
- **Height** *(Length)*
- **LevelOffset** *(Distance)*
- **Area** *(Area)*
- **Shape** *(Part::PropertyPartShape)*
- **SavedInventor** *(FileIncluded)*
- **OnlySolids** *(Bool)*
- **MaterialsTable** *(Map)*

### Children
- **HeightPropagate** *(Bool)*

### Component
- **Description** *(String)*
- **Tag** *(String)*

## `Component`  <sub>ArchComponent.py</sub>

### Component
- **Base** *(Link)*
- **CloneOf** *(Link)*
- **Additions** *(LinkList)*
- **Subtractions** *(LinkList)*
- **Description** *(String)*
- **Tag** *(String)*
- **StandardCode** *(String)*
- **Material** *(Link)*
- **MoveBase** *(Bool)*
- **MoveWithHost** *(Bool)*
- **VerticalArea** *(Area)*
- **HorizontalArea** *(Area)*
- **PerimeterLength** *(Length)*
- **HiRes** *(Link)*
- **Axis** *(Link)*

## `CurtainWall`  <sub>ArchCurtainWall.py</sub>

### CurtainWall
- **Host** *(Link)*
- **Height** *(Length)*
- **VerticalMullionNumber** *(Integer)*
- **VerticalMullionAlignment** *(Bool)*
- **VerticalSections** *(Integer)*
- **VerticalMullionHeight** *(Length)*
- **VerticalMullionWidth** *(Length)*
- **VerticalMullionProfile** *(Link)*
- **HorizontalMullionNumber** *(Integer)*
- **HorizontalMullionAlignment** *(Bool)*
- **HorizontalSections** *(Integer)*
- **HorizontalMullionHeight** *(Length)*
- **HorizontalMullionWidth** *(Length)*
- **HorizontalMullionProfile** *(Link)*
- **DiagonalMullionNumber** *(Integer)*
- **DiagonalMullionSize** *(Length)*
- **DiagonalMullionProfile** *(Link)*
- **PanelNumber** *(Integer)*
- **PanelThickness** *(Length)*
- **SwapHorizontalVertical** *(Bool)*
- **Refine** *(Bool)*
- **CenterProfiles** *(Bool)*
- **VerticalDirection** *(Vector)*
- **OverrideEdges** *(StringList)*

## `IfcRoot`  <sub>ArchIFC.py</sub>

### IFC
- **IfcData** *(Map)*
- **IfcType** *(Enumeration)*
- **IfcProperties** *(Map)*

## `PanelCut`  <sub>ArchPanel.py</sub>

### PanelCut
- **Source** *(Link)*
- **TagText** *(String)*
- **TagSize** *(Length)*
- **TagPosition** *(Vector)*
- **TagRotation** *(Angle)*
- **FontFile** *(File)*
- **MakeFace** *(Bool)*
- **AllowedAngles** *(FloatList)*
- **CutOffset** *(Distance)*

## `PanelSheet`  <sub>ArchPanel.py</sub>

### PanelSheet
- **Group** *(LinkList)*
- **TagText** *(String)*
- **TagSize** *(Length)*
- **TagPosition** *(Vector)*
- **TagRotation** *(Angle)*
- **FontFile** *(File)*
- **Width** *(Length)*
- **Height** *(Length)*
- **FillRatio** *(Percent)*
- **MakeFace** *(Bool)*
- **GrainDirection** *(Angle)*
- **Scale** *(Float)*
- **Rotations** *(FloatList)*

## `StructureTaskPanel`  <sub>ArchStructure.py</sub>

### Structure
- **Tool** *(LinkSubList)*

## `Truss`  <sub>ArchTruss.py</sub>

### Truss
- **TrussAngle** *(Angle)*
- **SlantType** *(Enumeration)*
- **Normal** *(Vector)*
- **HeightStart** *(Length)*
- **HeightEnd** *(Length)*
- **StrutStartOffset** *(Distance)*
- **StrutEndOffset** *(Distance)*
- **StrutHeight** *(Length)*
- **StrutWidth** *(Length)*
- **RodType** *(Enumeration)*
- **RodDirection** *(Enumeration)*
- **RodSize** *(Length)*
- **RodSections** *(Integer)*
- **RodEnd** *(Bool)*
- **RodMode** *(Enumeration)*

## `ViewProviderArchReference`  <sub>ArchReference.py</sub>

### Reference
- **TimeStamp** *(Float)*
- **UpdateColors** *(Bool)*

## `ViewProviderBuildingPart`  <sub>ArchBuildingPart.py</sub>

### AutoGroup
- **AutogroupSize** *(IntegerList)*
- **AutogroupBox** *(Bool)*
- **AutogroupAutosize** *(Bool)*
- **AutogroupMargin** *(Length)*

### BuildingPart
- **LineWidth** *(Float)*
- **OverrideUnit** *(String)*
- **DisplayOffset** *(Placement)*
- **ShowLevel** *(Bool)*
- **ShowUnit** *(Bool)*
- **OriginOffset** *(Bool)*
- **ShowLabel** *(Bool)*
- **FontName** *(Font)*
- **FontSize** *(Length)*
- **DiffuseColor** *(ColorList)*

### Children
- **ChildrenOverride** *(Bool)*
- **ChildrenLineWidth** *(Float)*
- **ChildrenLineColor** *(Color)*
- **ChildrenShapeColor** *(Material)*
- **ChildrenTransparency** *(Percent)*

### Clip
- **CutView** *(Bool)*
- **CutMargin** *(Length)*
- **AutoCutView** *(Bool)*

### Interaction
- **SetWorkingPlane** *(Bool)*
- **AutoWorkingPlane** *(Bool)*
- **ViewData** *(FloatList)*
- **RestoreView** *(Bool)*
- **DoubleClickActivates** *(Bool)*
- **SaveInventor** *(Bool)*
- **SavedInventor** *(FileIncluded)*

## `ViewProviderComponent`  <sub>ArchComponent.py</sub>

### Component
- **UseMaterialColor** *(Bool)*

## `ViewProviderPanelCut`  <sub>ArchPanel.py</sub>

### Arch
- **Margin** *(Length)*
- **ShowMargin** *(Bool)*

## `ViewProviderPanelSheet`  <sub>ArchPanel.py</sub>

### PanelSheet
- **Margin** *(Length)*
- **ShowMargin** *(Bool)*
- **ShowGrain** *(Bool)*

## `_ArchMaterial`  <sub>ArchMaterial.py</sub>

### Material
- **Description** *(String)*
- **StandardCode** *(String)*
- **ProductURL** *(String)*
- **Transparency** *(Percent)*
- **Color** *(Color)*
- **SectionColor** *(Color)*

## `_ArchMultiMaterial`  <sub>ArchMaterial.py</sub>

### Arch
- **Description** *(String)*
- **Names** *(StringList)*
- **Materials** *(LinkList)*
- **Thicknesses** *(FloatList)*

## `_ArchPipe`  <sub>ArchPipe.py</sub>

### Pipe
- **Diameter** *(Length)*
- **Width** *(Length)*
- **Height** *(Length)*
- **Length** *(Length)*
- **Profile** *(Link)*
- **OffsetStart** *(Length)*
- **OffsetEnd** *(Length)*
- **WallThickness** *(Length)*
- **ProfileType** *(Enumeration)*

## `_ArchPipeConnector`  <sub>ArchPipe.py</sub>

### PipeConnector
- **Radius** *(Length)*
- **Pipes** *(LinkList)*
- **ConnectorType** *(Enumeration)*

## `_ArchSchedule`  <sub>ArchSchedule.py</sub>

### Arch
- **Description** *(StringList)*
- **Value** *(StringList)*
- **Unit** *(StringList)*
- **Objects** *(StringList)*
- **Filter** *(StringList)*
- **CreateSpreadsheet** *(Bool)*
- **DetailedResults** *(Bool)*
- **AutoUpdate** *(Bool)*
- **Schedule** *(Link)*

## `_ArchWindowTaskPanel`  <sub>ArchWindow.py</sub>

### Arch
- **HoleWire** *(Integer)*

## `_Axis`  <sub>ArchAxis.py</sub>

### Axis
- **Distances** *(FloatList)*
- **Angles** *(FloatList)*
- **Labels** *(StringList)*
- **CustomNumber** *(String)*
- **Length** *(Length)*
- **Limit** *(Length)*

### Base
- **Placement** *(Placement)*
- **Shape** *(Part::PropertyPartShape)*

## `_AxisSystem`  <sub>ArchAxisSystem.py</sub>

### AxisSystem
- **Axes** *(LinkList)*
- **Placement** *(Placement)*

## `_Equipment`  <sub>ArchEquipment.py</sub>

### Equipment
- **Model** *(String)*
- **ProductURL** *(String)*
- **StandardCode** *(String)*
- **SnapPoints** *(VectorList)*
- **EquipmentPower** *(Float)*

## `_Fence`  <sub>ArchFence.py</sub>

### Fence
- **Section** *(Link)*
- **Post** *(Link)*
- **Path** *(Link)*
- **NumberOfSections** *(Integer)*
- **NumberOfPosts** *(Integer)*

## `_Frame`  <sub>ArchFrame.py</sub>

### Frame
- **Profile** *(Link)*
- **Align** *(Bool)*
- **Offset** *(VectorDistance)*
- **BasePoint** *(Integer)*
- **ProfilePlacement** *(Placement)*
- **Rotation** *(Angle)*
- **Edges** *(Enumeration)*
- **Fuse** *(Bool)*

## `_Panel`  <sub>ArchPanel.py</sub>

### Panel
- **Length** *(Length)*
- **Width** *(Length)*
- **Thickness** *(Length)*
- **Sheets** *(Integer)*
- **Offset** *(Distance)*
- **WaveLength** *(Length)*
- **WaveHeight** *(Length)*
- **WaveOffset** *(Distance)*
- **WaveDirection** *(Angle)*
- **WaveType** *(Enumeration)*
- **WaveBottom** *(Bool)*
- **Area** *(Area)*
- **FaceMaker** *(Enumeration)*
- **Normal** *(Vector)*

## `_Precast`  <sub>ArchPrecast.py</sub>

### Structure
- **Length** *(Distance)*
- **Width** *(Distance)*
- **Height** *(Distance)*
- **Nodes** *(VectorList)*

## `_PrecastBeam`  <sub>ArchPrecast.py</sub>

### Beam
- **Chamfer** *(Distance)*
- **DentLength** *(Distance)*
- **DentHeight** *(Distance)*
- **Dents** *(StringList)*

## `_PrecastIbeam`  <sub>ArchPrecast.py</sub>

### Beam
- **Chamfer** *(Distance)*
- **BeamBase** *(Distance)*

## `_PrecastPanel`  <sub>ArchPrecast.py</sub>

### Panel
- **Chamfer** *(Distance)*
- **DentWidth** *(Distance)*
- **DentHeight** *(Distance)*

## `_PrecastPillar`  <sub>ArchPrecast.py</sub>

### Column
- **Chamfer** *(Distance)*
- **GrooveDepth** *(Distance)*
- **GrooveHeight** *(Distance)*
- **GrooveSpacing** *(Distance)*
- **GrooveNumber** *(Integer)*
- **Dents** *(StringList)*

## `_PrecastSlab`  <sub>ArchPrecast.py</sub>

### Slab
- **SlabType** *(Enumeration)*
- **SlabBase** *(Distance)*
- **HoleNumber** *(Integer)*
- **HoleMajor** *(Distance)*
- **HoleMinor** *(Distance)*
- **HoleSpacing** *(Distance)*

## `_PrecastStairs`  <sub>ArchPrecast.py</sub>

### Stairs
- **DownLength** *(Distance)*
- **RiserNumber** *(Integer)*
- **Riser** *(Distance)*
- **Tread** *(Distance)*

## `_ProfileC`  <sub>ArchProfile.py</sub>

### Draft
- **OutDiameter** *(Length)*
- **Thickness** *(Length)*

## `_ProfileH`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*
- **WebThickness** *(Length)*
- **FlangeThickness** *(Length)*

## `_ProfileL`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*
- **Thickness** *(Length)*

## `_ProfileR`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*

## `_ProfileRH`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*
- **Thickness** *(Length)*

## `_ProfileT`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*
- **WebThickness** *(Length)*
- **FlangeThickness** *(Length)*

## `_ProfileU`  <sub>ArchProfile.py</sub>

### Draft
- **Width** *(Length)*
- **Height** *(Length)*
- **WebThickness** *(Length)*
- **FlangeThickness** *(Length)*

## `_Rebar`  <sub>ArchRebar.py</sub>

### Rebar
- **Diameter** *(Length)*
- **OffsetStart** *(Distance)*
- **OffsetEnd** *(Distance)*
- **Amount** *(Integer)*
- **Spacing** *(Length)*
- **Distance** *(Length)*
- **Direction** *(Vector)*
- **Rounding** *(Float)*
- **PlacementList** *(PlacementList)*
- **Host** *(Link)*
- **CustomSpacing** *(String)*
- **Length** *(Distance)*
- **TotalLength** *(Distance)*
- **Mark** *(String)*

## `_Roof`  <sub>ArchRoof.py</sub>

### Roof
- **Angles** *(FloatList)*
- **Runs** *(FloatList)*
- **IdRel** *(IntegerList)*
- **Thickness** *(FloatList)*
- **Overhang** *(FloatList)*
- **Heights** *(FloatList)*
- **Face** *(Integer)*
- **RidgeLength** *(Length)*
- **BorderLength** *(Length)*
- **Flip** *(Bool)*
- **Subvolume** *(Link)*

## `_SectionPlane`  <sub>ArchSectionPlane.py</sub>

### SectionPlane
- **Placement** *(Placement)*
- **Shape** *(Part::PropertyPartShape)*
- **Objects** *(LinkList)*
- **OnlySolids** *(Bool)*
- **Clip** *(Bool)*
- **UseMaterialColorForFill** *(Bool)*
- **Depth** *(Length)*

## `_Site`  <sub>ArchSite.py</sub>

### IFC
- **IfcType** *(Enumeration)*

### Site
- **Terrain** *(Link)*
- **Address** *(String)*
- **PostalCode** *(String)*
- **City** *(String)*
- **Region** *(String)*
- **Country** *(String)*
- **Latitude** *(Float)*
- **Longitude** *(Float)*
- **Declination** *(Angle)*
- **Elevation** *(Length)*
- **Url** *(String)*
- **Additions** *(LinkList)*
- **Subtractions** *(LinkList)*
- **ProjectedArea** *(Area)*
- **Perimeter** *(Length)*
- **AdditionVolume** *(Volume)*
- **SubtractionVolume** *(Volume)*
- **ExtrusionVector** *(Vector)*
- **RemoveSplitter** *(Bool)*
- **OriginOffset** *(Vector)*
- **TimeZone** *(Integer)*
- **EPWFile** *(FileIncluded)*

## `_Space`  <sub>ArchSpace.py</sub>

### Space
- **Boundaries** *(LinkSubList)*
- **Area** *(Area)*
- **FinishFloor** *(String)*
- **FinishWalls** *(String)*
- **FinishCeiling** *(String)*
- **Group** *(LinkList)*
- **SpaceType** *(Enumeration)*
- **FloorThickness** *(Length)*
- **NumberOfPeople** *(Integer)*
- **LightingPower** *(Float)*
- **EquipmentPower** *(Float)*
- **AutoPower** *(Bool)*
- **Conditioning** *(Enumeration)*
- **Internal** *(Bool)*
- **AreaCalculationType** *(Enumeration)*

## `_Stairs`  <sub>ArchStairs.py</sub>

### Segment and Parts
- **LastSegment** *(Link)*
- **AbsTop** *(Vector)*
- **OutlineLeft** *(VectorList)*
- **OutlineRight** *(VectorList)*
- **RailingLeft** *(LinkHidden)*
- **RailingRight** *(LinkHidden)*
- **OutlineLeftAll** *(VectorList)*
- **OutlineRightAll** *(VectorList)*
- **RailingHeightLeft** *(Length)*
- **RailingHeightRight** *(Length)*
- **RailingOffsetLeft** *(Length)*
- **RailingOffsetRight** *(Length)*

### Stairs
- **Length** *(Length)*
- **Width** *(Length)*
- **Height** *(Length)*
- **Align** *(Enumeration)*
- **WidthOfLanding** *(FloatList)*

### Steps
- **NumberOfSteps** *(Integer)*
- **TreadDepth** *(Length)*
- **RiserHeight** *(Length)*
- **Nosing** *(Length)*
- **TreadThickness** *(Length)*
- **BlondelRatio** *(Float)*
- **RiserThickness** *(Length)*
- **LandingDepth** *(Length)*
- **TreadDepthEnforce** *(Length)*
- **RiserHeightEnforce** *(Length)*

### Structure
- **Flight** *(Enumeration)*
- **Landings** *(Enumeration)*
- **Winders** *(Enumeration)*
- **Structure** *(Enumeration)*
- **StructureThickness** *(Length)*
- **StringerWidth** *(Length)*
- **StructureOffset** *(Length)*
- **StringerOverlap** *(Length)*
- **DownSlabThickness** *(Length)*
- **UpSlabThickness** *(Length)*
- **ConnectionDownStartStairs** *(Enumeration)*
- **ConnectionEndStairsUp** *(Enumeration)*

## `_StructuralSystem`  <sub>ArchStructure.py</sub>

### Arch
- **Axes** *(LinkList)*
- **Exclude** *(IntegerList)*
- **Align** *(Bool)*

## `_Structure`  <sub>ArchStructure.py</sub>

### ExtrusionPath
- **Tool** *(LinkSubList)*
- **ComputedLength** *(Distance)*
- **ToolOffsetFirst** *(Distance)*
- **ToolOffsetLast** *(Distance)*
- **BasePerpendicularToTool** *(Bool)*
- **BaseOffsetX** *(Distance)*
- **BaseOffsetY** *(Distance)*
- **BaseMirror** *(Bool)*
- **BaseRotation** *(Angle)*

### Structure
- **Length** *(Length)*
- **Width** *(Length)*
- **Height** *(Length)*
- **Normal** *(Vector)*
- **Nodes** *(VectorList)*
- **Profile** *(String)*
- **NodesOffset** *(Distance)*
- **FaceMaker** *(Enumeration)*
- **ArchSketchEdges** *(StringList)*

## `_ViewProviderAxis`  <sub>ArchAxis.py</sub>

### Axis
- **BubbleSize** *(Length)*
- **NumberingStyle** *(Enumeration)*
- **DrawStyle** *(Enumeration)*
- **BubblePosition** *(Enumeration)*
- **LineWidth** *(Float)*
- **LineColor** *(Color)*
- **StartNumber** *(Integer)*
- **FontName** *(Font)*
- **FontSize** *(Length)*
- **ShowLabel** *(Bool)*
- **LabelOffset** *(Placement)*

## `_ViewProviderFence`  <sub>ArchFence.py</sub>

### Fence
- **UseOriginalColors** *(Bool)*

## `_ViewProviderRebar`  <sub>ArchRebar.py</sub>

### Rebar
- **RebarShape** *(String)*

## `_ViewProviderSectionPlane`  <sub>ArchSectionPlane.py</sub>

### SectionPlane
- **DisplayLength** *(Length)*
- **DisplayHeight** *(Length)*
- **ArrowSize** *(Length)*
- **Transparency** *(Percent)*
- **LineWidth** *(Float)*
- **CutDistance** *(Length)*
- **LineColor** *(Color)*
- **CutView** *(Bool)*
- **CutMargin** *(Length)*
- **ShowLabel** *(Bool)*
- **FontName** *(Font)*
- **FontSize** *(Length)*

## `_ViewProviderSite`  <sub>ArchSite.py</sub>

### Compass
- **Compass** *(Bool)*
- **CompassRotation** *(Angle)*
- **CompassPosition** *(Vector)*
- **UpdateDeclination** *(Bool)*

### Site
- **WindRose** *(Bool)*
- **SolarDiagram** *(Bool)*
- **SolarDiagramScale** *(Float)*
- **SolarDiagramPosition** *(Vector)*
- **SolarDiagramColor** *(Color)*
- **Orientation** *(Enumeration)*

## `_ViewProviderSpace`  <sub>ArchSpace.py</sub>

### Space
- **Text** *(StringList)*
- **FontName** *(Font)*
- **TextColor** *(Color)*
- **FontSize** *(Length)*
- **FirstLine** *(Length)*
- **LineSpacing** *(Float)*
- **TextPosition** *(VectorDistance)*
- **TextAlign** *(Enumeration)*
- **Decimals** *(Integer)*
- **ShowUnit** *(Bool)*

## `_ViewProviderStructure`  <sub>ArchStructure.py</sub>

### Nodes
- **NodeLine** *(Float)*
- **NodeSize** *(Float)*
- **NodeColor** *(Color)*
- **NodeType** *(Enumeration)*
- **ShowNodes** *(Bool)*

## `_Wall`  <sub>ArchWall.py</sub>

### Blocks
- **MakeBlocks** *(Bool)*
- **BlockLength** *(Length)*
- **BlockHeight** *(Length)*
- **OffsetFirst** *(Length)*
- **OffsetSecond** *(Length)*
- **Joint** *(Length)*
- **CountEntire** *(Integer)*
- **CountBroken** *(Integer)*

### Wall
- **Length** *(Length)*
- **Width** *(Length)*
- **OverrideWidth** *(FloatList)*
- **OverrideAlign** *(StringList)*
- **OverrideOffset** *(FloatList)*
- **Height** *(Length)*
- **Area** *(Area)*
- **Align** *(Enumeration)*
- **Normal** *(Vector)*
- **Face** *(Integer)*
- **Offset** *(Distance)*
- **ArchSketchData** *(Bool)*
- **ArchSketchEdges** *(StringList)*

## `_Window`  <sub>ArchWindow.py</sub>

### Window
- **Hosts** *(LinkList)*
- **WindowParts** *(StringList)*
- **HoleDepth** *(Length)*
- **Subvolume** *(Link)*
- **Width** *(Length)*
- **Height** *(Length)*
- **Normal** *(Vector)*
- **Preset** *(Integer)*
- **Frame** *(Length)*
- **Offset** *(Length)*
- **Area** *(Area)*
- **LouvreWidth** *(Length)*
- **LouvreSpacing** *(Length)*
- **Opening** *(Percent)*
- **HoleWire** *(Integer)*
- **SymbolPlan** *(Bool)*
- **SymbolElevation** *(Bool)*
