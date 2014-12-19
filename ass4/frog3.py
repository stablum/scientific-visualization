import vtk

#read in skin data
skinReader = vtk.vtkImageReader() 
skinReader.SetFilePrefix("C:/Users/Asus/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frog.")
skinReader.SetFilePattern('%s%03d.raw')
skinReader.SetDataScalarTypeToUnsignedChar()
skinReader.SetFileDimensionality(2)
skinReader.SetDataSpacing(1,1,1.5)
skinReader.SetDataExtent(0,499,0,469,1,136)
skinReader.Update()


skin = vtk.vtkContourFilter()
skin.SetInputConnection(skinReader.GetOutputPort())
skin.SetValue(0,10)

skinMapper = vtk.vtkPolyDataMapper()
skinMapper.SetInputConnection(skin.GetOutputPort())
skinMapper.ScalarVisibilityOff()
skinMapper.SetScalarRange(skin.GetOutput().GetScalarRange())

skinActor = vtk.vtkActor()
skinActor.SetMapper(skinMapper)
skinActor.GetProperty().SetColor(0,100,0)
skinActor.GetProperty().SetOpacity(0.1)





#Read in tissue data
tissueReader = vtk.vtkImageReader() 
tissueReader.SetFilePrefix("C:/Users/Asus/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frogTissue.")
tissueReader.SetFilePattern('%s%03d.raw')
tissueReader.SetDataScalarTypeToUnsignedChar()
tissueReader.SetFileDimensionality(2)
tissueReader.SetDataSpacing(1,1,1.5)
tissueReader.SetDataExtent(0,499,0,469,1,136)
tissueReader.SetFileDimensionality(2)
tissueReader.Update()

#create volume
compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(tissueReader.GetOutputPort())
volumeMapper.SetSampleDistance(0.1)

#create opacity transfer function
opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(0, 0)
opacityTransferFunction.AddPoint(1, .1)
opacityTransferFunction.AddPoint(2, .05)
opacityTransferFunction.AddPoint(3, .1)
opacityTransferFunction.AddPoint(4, .1)
opacityTransferFunction.AddPoint(5, .1)
opacityTransferFunction.AddPoint(6, .1)
opacityTransferFunction.AddPoint(7, .1)
opacityTransferFunction.AddPoint(8, .1)
opacityTransferFunction.AddPoint(9, .1)
opacityTransferFunction.AddPoint(10, .1)
opacityTransferFunction.AddPoint(11, .1)
opacityTransferFunction.AddPoint(12, .1)
opacityTransferFunction.AddPoint(13, .1)
opacityTransferFunction.AddPoint(14, .1)
opacityTransferFunction.AddPoint(15, .1)

#create color transfer function	
colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(1, 1, 0, 0) #blood

colorTransferFunction.AddRGBPoint(2, 0.251, 0.451, 0.051) #brain
colorTransferFunction.AddRGBPoint(3 , 0, 0.2, 0.098)#duodenum
colorTransferFunction.AddRGBPoint(4 , 0,0,0) #eye 
colorTransferFunction.AddRGBPoint(5 , 0.5, 1, 1) #eye white
colorTransferFunction.AddRGBPoint(6 , 0.467, 0.047, 0.047) #heart
colorTransferFunction.AddRGBPoint(7 , 1,1,0.2) #ileum
colorTransferFunction.AddRGBPoint(8 , 0.9 , 0.5 , 0.8)#kidney
colorTransferFunction.AddRGBPoint(9 , 0.2, 0.98, 0)#large intestine
colorTransferFunction.AddRGBPoint(10, 1, 0.502, 0)#liver
colorTransferFunction.AddRGBPoint(11, 0,0,1)#lung
colorTransferFunction.AddRGBPoint(12, 0.6, 0.1, 0.8)#nerve
colorTransferFunction.AddRGBPoint(13, 0.757, 0.757, 0.663)#skeleton
colorTransferFunction.AddRGBPoint(14, 0.408, 0.275, 0.039)#spleen
colorTransferFunction.AddRGBPoint(15, 0.4, 0.4, 0)#stomach


volumeProp= vtk.vtkVolumeProperty()
volumeProp.SetColor(colorTransferFunction)
volumeProp.SetScalarOpacity(opacityTransferFunction)
volumeProp.SetInterpolationTypeToLinear()


volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProp)


#Legend
legend = vtk.vtkLegendBoxActor()

legend.SetNumberOfEntries(15)
legend.UseBackgroundOn()
legend.SetBackgroundColor([1, 1, 1])
legend.GetPositionCoordinate().SetCoordinateSystemToDisplay()
legend.GetPositionCoordinate().SetValue(0, 0)
legend.GetPosition2Coordinate().SetCoordinateSystemToDisplay()
legend.GetPosition2Coordinate().SetValue(150, 300)
legendBox = vtk.vtkSphereSource()

legendBox.Update()

organList = ["Blood", "Brain", "Duodenum", "Eye retina", "Eye white", "Heart",
             "Ileum", "Kidney", "Large intestine", "Liver", "Lung", "Nerve",
             "Skeleton", "Spleen", "Stomach"]

for i in range(len(organList)):
    legend.SetEntry(i,legendBox.GetOutput(),organList[i],colorTransferFunction.GetColor(i+1))





#renderer
ren = vtk.vtkRenderer()
ren.AddActor(skinActor)
ren.AddVolume(volume)
ren.AddActor(legend)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.SetInteractive(1)
ren.SetBackground(0.627, 0.627, 0.627)
ren.SetBackground(1, 1, 1)
ren.GradientBackgroundOn()



#	Set window size
renWin.SetSize(860, 640)

#	Start visualization
iren.Initialize()
iren.Start()
