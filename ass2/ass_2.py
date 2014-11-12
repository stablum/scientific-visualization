#import vtk python module
import sys
from vtk import *
from vtk.util.misc import vtkGetDataRoot


#read in data


reader = vtk.vtkImageReader()

reader.SetFilePrefix("c:/VTKdata/ass2/MysteryData/slice")
                     

reader.SetFileDimensionality(2)
reader.SetDataOrigin(0.0, 0.0, 0.0)
reader.SetDataSpacing(1, 1, 2)
reader.SetDataExtent(0, 255, 0, 255, 1, 94)
reader.SetDataScalarTypeToUnsignedShort()
reader.SetDataByteOrderToLittleEndian()

#update the reader
reader.UpdateWholeExtent()
data = reader.GetOutput()

#create isosurface contour
contour = vtkImageMarchingCubes()
contour.SetInput(data)
contour.SetValue(0, 1000)#float(sys.argv[1]))


# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(contour.GetOutput())

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
 
# assign actor to the renderer
ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetInteractive(1)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()

#DONE UP TO COLOURS

