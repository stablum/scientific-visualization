import vtk


skinReader = vtk.vtkImageReader() 
skinReader.SetFilePrefix("c:/Users/Rinske/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frog.")
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






tissueReader = vtk.vtkImageReader() 
tissueReader.SetFilePrefix("c:/Users/Rinske/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frogTissue.")
tissueReader.SetFilePattern('%s%03d.raw')
tissueReader.SetDataScalarTypeToUnsignedChar()
tissueReader.SetFileDimensionality(2)
tissueReader.SetDataSpacing(1,1,1.5)
tissueReader.SetDataExtent(0,499,0,469,1,136)
tissueReader.Update()

compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(tissueReader.GetOutputPort())


opacityTransferFunction = vtk.vtkPiecewiseFunction()
opacityTransferFunction.AddPoint(0, 0)
opacityTransferFunction.AddPoint(1, .1)
opacityTransferFunction.AddPoint(2, .1)
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
##
	
colorTransferFunction = vtk.vtkColorTransferFunction()
colorTransferFunction.AddRGBPoint(0,0,0,0)
colorTransferFunction.AddRGBPoint(1 , 227/255,23/255, 31/255) #blood

colorTransferFunction.AddRGBPoint(2 , 1,0,0) #brain
colorTransferFunction.AddRGBPoint(3 , 255/255,253/255,229/255)#duodenum
colorTransferFunction.AddRGBPoint(4 , 0,0,0) #eye retina
colorTransferFunction.AddRGBPoint(5 , 175/255,235/255,  238/255) #eye white
colorTransferFunction.AddRGBPoint(6 , 128/255,0, 0) #heart
colorTransferFunction.AddRGBPoint(7 , 1,1,1) #ileum
colorTransferFunction.AddRGBPoint(8 , 1, 1, 1)#kidney
colorTransferFunction.AddRGBPoint(9 , 204/255,168/255,143/255)#large intestine
colorTransferFunction.AddRGBPoint(10, 221/255,130/255,101/255)#liver
colorTransferFunction.AddRGBPoint(11, 0,0,1)#lung
colorTransferFunction.AddRGBPoint(12, 255/255,234/255, 92/255)#nerve
colorTransferFunction.AddRGBPoint(13, 1,0,0)#skeleton
colorTransferFunction.AddRGBPoint(14, 157/255,108/255,162/255)#spleen
colorTransferFunction.AddRGBPoint(15, 0,1,0)#stomach

volumeProp= vtk.vtkVolumeProperty()
volumeProp.SetColor(colorTransferFunction)
volumeProp.SetScalarOpacity(opacityTransferFunction)
volumeProp.SetInterpolationTypeToLinear()


volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProp)






#renderer
ren = vtk.vtkRenderer()
ren.AddActor(skinActor)
ren.AddVolume(volume)
ren.AddViewProp(volume)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.SetInteractive(1)
ren.GradientBackgroundOn()
##ren.SetBackground(119,136,153)
##ren.SetBackground(192,192,192)



#	Set window size
renWin.SetSize(640,480)

#	Start visualization
iren.Initialize()
iren.Start()
