import vtk

#renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("F:/ass3/SMRX.vtk")
reader.UpdateWholeExtent()

#outline (color: white)
outline = vtk.vtkOutlineFilter()
outline.SetInput(reader.GetOutput())
mapOutline = vtk.vtkPolyDataMapper()
mapOutline.SetInput(outline.GetOutput())
outlineActor = vtk.vtkActor()
outlineActor.SetMapper(mapOutline)





# Create source for streamtubes
seeds = vtk.vtkPointSource()
seeds.SetRadius (40)
seeds.SetCenter (outlineActor.GetCenter())
seeds.SetNumberOfPoints (1000)



integ = vtk.vtkRungeKutta4()
#create streamer
streamer = vtk.vtkStreamTracer()
streamer.SetInputConnection(reader.GetOutputPort())
print streamer
streamer.SetSourceConnection(seeds.GetOutputPort())
##streamer.SetStartPosition(0,0,0)
streamer.SetMaximumPropagation (700)
streamer.SetMinimumIntegrationStep(0.1)
streamer.SetMaximumIntegrationStep(1.0)
streamer.SetInitialIntegrationStep(0.2)
streamer.SetIntegrationDirectionToBoth()
streamer.SetIntegrator(integ)


#tube filter
streamTube = vtk.vtkTubeFilter()
streamTube.SetInputConnection(streamer.GetOutputPort())
streamTube.SetRadius(0.1)
streamTube.SetVaryRadiusToVaryRadiusByVector()

#ribbon filter
##ribbonFilter = vtk.vtkRibbonFilter()
##ribbonFilter.SetInputConnection(streamer.GetOutputPort())
##ribbonFilter.SetWidth(0.1)
##ribbonFilter.VaryWidthOff()





streamMapper = vtk.vtkPolyDataMapper()
streamMapper.SetInputConnection(streamTube.GetOutputPort())
streamMapper.SetScalarRange(reader.GetOutput().GetPointData().GetScalars().GetRange())
streamActor = vtk.vtkActor()
streamActor.SetMapper(streamMapper)
streamActor.VisibilityOn()




#reactor geometry
iso = vtk.vtkContourFilter()
iso.SetInput(reader.GetOutput())
iso.SetValue(0, 10)

isoMapper = vtk.vtkPolyDataMapper()
isoMapper.SetInput(iso.GetOutput())
isoMapper.ScalarVisibilityOff()

isoActor = vtk.vtkActor()
isoActor.SetMapper(isoMapper)
isoActor.GetProperty().SetOpacity(0.25)

ren.AddActor(outlineActor)

ren.AddActor(streamActor)
ren.AddActor(isoActor)
ren.SetBackground(1, 1, 1)
renWin.SetSize(500,500)

renWin.Render()

# initialize and start the interactor
iren.Initialize()
iren.Start()


                    
