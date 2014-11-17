import vtk

#renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("c:/Users/Rinske/Documents/GitHub/scientific-visualization/ass3/SMRX.vtk")
reader.ReadAllScalarsOn()
reader.ReadAllVectorsOn()
reader.Update()

data = reader.GetOutput()

outline = vtk.vtkStructuredGridOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())
mapOutline = vtk.vtkPolyDataMapper()
mapOutline.SetInputConnection(outline.GetOutputPort())
outlineActor = vtk.vtkActor()
outlineActor.SetMapper(mapOutline)
outlineActor.GetProperty().SetColor(0,0,0)

renWin.SetSize(300,200)
iren.Initialize()
