#import vtk python module
import sys
from vtk import *
from vtk.util.misc import vtkGetDataRoot



def callback(obj, event):
    global contour
    sliderRep = obj.GetRepresentation()
    pos = sliderRep.GetValue()
    contour.SetValue(0, pos)
    

#read in data
reader = vtk.vtkImageReader()
reader.SetFilePrefix("c:/Users/Rinske/Documents/GitHub/scientific-visualization/ass2/MysteryData/slice")
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
contour.SetComputeScalars(0)


# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(contour.GetOutput())
mapper.ScalarVisibilityOff()

#actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.9,0.9,0.8)

# assign actor to the renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

#set camera
cam = vtk.vtkCamera()
cam.SetViewUp(0, 0, -1)

cam.ComputeViewPlaneNormal()
cam.SetPosition(128,1000,250)
cam.SetFocalPoint(128,0,100)
ren.SetActiveCamera(cam)

#create BoundingBox
bb = vtkOutlineFilter()
bb.SetInput(data)
bb.Update()
bbdata = bb.GetOutput()
bbmapper = vtkDataSetMapper()
bbmapper.SetInput(bbdata)
bbactor = vtk.vtkActor()
bbactor.SetMapper(bbmapper)
bbren = vtk.vtkRenderer()
ren.AddActor(bbactor)
bbactor.GetProperty().SetColor(1,1,0)


#create slider widget

sliderRep = vtk.vtkSliderRepresentation2D()
sliderRep.GetSliderProperty().SetColor(1,0,0)
sliderRep.GetTubeProperty().SetColor(0,0,0)
sliderRep.GetCapProperty().SetColor(0,0,0)
sliderRep.SetMinimumValue(500)
sliderRep.SetMaximumValue(3500)
sliderRep.SetValue(1000)
sliderRep.SetTitleText("Attenuation coefficient")
sliderRep.GetTitleProperty().SetColor(0,0,0)
sliderRep.SetSliderLength(0.02)
sliderRep.SetSliderWidth(0.01)
sliderRep.SetTubeWidth(0.01)

sliderRep.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
sliderRep.GetPoint1Coordinate().SetValue(0.2, 0.1)
sliderRep.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()
sliderRep.GetPoint2Coordinate().SetValue(0.8, 0.1)

sliderWidget = vtk.vtkSliderWidget()
sliderWidget.SetInteractor(iren)
sliderWidget.SetRepresentation(sliderRep)
sliderWidget.EnabledOn()
sliderWidget.AddObserver("InteractionEvent", callback)

#renderer
ren.AddActor(actor)
ren.SetInteractive(1)
ren.GradientBackgroundOn()
ren.SetBackground(119,136,153)
ren.SetBackground(192,192,192)
renWin.SetFullScreen(1)


# enable user interface interactor
iren.Initialize()
renWin.Render()
sliderWidget.On()
iren.Start()


