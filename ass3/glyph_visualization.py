import vtk

#renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("C:/Users/Rinske/Documents/GitHub/scientific-visualization/ass3/SMRX.vtk")
reader.UpdateWholeExtent()

#include only every 20th point
mask = vtk.vtkMaskPoints()
mask.SetInput(reader.GetOutput())
mask.SetOnRatio(15)

#create geometry unsing a cylinder and a cone
cyl = vtk.vtkCylinderSource()
cyl.SetResolution(10)
cyl.SetRadius(0.2)
cyl.SetHeight(2)

cylTrans = vtk.vtkTransform()
cylTrans.Identity()
cylTrans.RotateZ(90)
cylTrans.Translate(0, 1.5, 0)

cylTransFilter = vtk.vtkTransformPolyDataFilter()
cylTransFilter.SetInput(cyl.GetOutput())
cylTransFilter.SetTransform(cylTrans)

cone = vtk.vtkConeSource()
cone.SetResolution(20)

arrow = vtk.vtkAppendPolyData()
arrow.AddInput(cylTransFilter.GetOutput())
arrow.Update()

arrows = vtk.vtkGlyph3D()
arrows.SetInput(mask.GetOutput())
arrows.SetSource(arrow.GetOutput())
arrows.SetScaleFactor(0.2)
arrows.SetScaleModeToScaleByVector()

#create lookup table
lut = vtk.vtkLookupTable()
lut.SetHueRange(.667, 0.0)
lut.Build()

vecMapper = vtk.vtkPolyDataMapper()
vecMapper.SetInput(arrows.GetOutput())
vecMapper.SetScalarRange(2, 10)
vecMapper.SetLookupTable(lut)

vecActor = vtk.vtkActor()
vecActor.SetMapper(vecMapper)

#create reactor geometry
geometry = vtk.vtkContourFilter()
geometry.SetInput(reader.GetOutput())
geometry.SetValue(0, 10)

geometryMapper = vtk.vtkPolyDataMapper()
geometryMapper.SetInput(geometry.GetOutput())
geometryMapper.ScalarVisibilityOff()

geometryActor = vtk.vtkActor()
geometryActor.SetMapper(geometryMapper)
##geometryActor.GetProperty().SetRepresentationToWireframe()
geometryActor.GetProperty().SetOpacity(0.25)

#add actors to render and create render window
ren.AddActor(vecActor)
ren.AddActor(geometryActor)
ren.SetBackground(1, 1, 1)
renWin.SetSize(500,500)

renWin.Render()

# initialize and start the interactor
iren.Initialize()
iren.Start()


                    
