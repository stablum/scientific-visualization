import vtk

#read in frog data
frogReader =  vtk.vtkImageReader()
frogReader.SetFilePrefix("C:/Users/Asus/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frog.")
frogReader.SetFilePattern("%s%03d.raw")
frogReader.SetFileDimensionality(2)
frogReader.SetDataOrigin(1, 1, 1)
frogReader.SetDataSpacing(1, 1, 1.5)
frogReader.SetDataExtent(0, 499, 0, 469, 1, 136)
frogReader.SetDataScalarTypeToUnsignedShort()


frogReader.UpdateWholeExtent()
frogData = frogReader.GetOutput()

#read in tissue data
tissueReader = vtk.vtkImageReader()
tissueReader.SetFilePrefix("C:/Users/Asus/Documents/GitHub/scientific-visualization/ass4/WholeFrog/frogTissue.")
tissueReader.SetFilePattern("%s%03d.raw")
tissueReader.SetFileDimensionality(2)
tissueReader.SetDataOrigin(1, 1, 1)
tissueReader.SetDataSpacing(1, 1, 1.5)
tissueReader.SetDataExtent(0, 499, 0, 469, 1, 136)
tissueReader.SetDataScalarTypeToUnsignedShort()

tissueReader.UpdateWholeExtent()
tissueData = tissueReader.GetOutput()

#Create isosurface frog
frogContour =  vtk.vtkContourFilter()
frogContour.SetInput(frogData)
frogContour.SetValue(0, 50)

#map contour
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(frogContour.GetOutput())
mapper.ScalarVisibilityOff()



actor = vtk.vtkActor()
actor.SetMapper(mapper)
##actor.GetProperty().SetColor(0, 1, 0) 
##actor.GetProperty().SetOpacity(0.1)

ren = vtk.vtkRenderer()
ren.AddActor(actor)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)



# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()
