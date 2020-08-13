# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

import os
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Manipulating texture images:
#convert -crop 50%x100% lightBlueMarble2.jpg converted_lBM2.jpg
#convert converted_lBM2-1.jpg converted_lBM2-0.jpg +append converted_lBM2.jpg
#rm converted_lBM2-*

dir = os.getcwd()
# create a new 'Sphere'
sphere1 = Sphere()
R = 6370e3
#textureMapPic = "transparentEarth.png"
textureMapPic = "converted_lBM2.jpg"
# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1573, 887]

# get layout
layout1 = GetLayout()

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# show data in view
sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
sphere1Display.Representation = 'Surface'
sphere1Display.ColorArrayName = [None, '']
sphere1Display.OSPRayScaleArray = 'Normals'
sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
sphere1Display.SelectOrientationVectors = 'None'
sphere1Display.ScaleFactor = 0.1
sphere1Display.SelectScaleArray = 'None'
sphere1Display.GlyphType = 'Arrow'
sphere1Display.GlyphTableIndexArray = 'None'
sphere1Display.GaussianRadius = 0.005
sphere1Display.SetScaleArray = ['POINTS', 'Normals']
sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
sphere1Display.OpacityArray = ['POINTS', 'Normals']
sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
sphere1Display.PolarAxes = 'PolarAxesRepresentation'
sphere1Display.SelectInputVectors = ['POINTS', 'Normals']
sphere1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
sphere1Display.OSPRayScaleFunction.Points = [-0.00206091040046649, 0.0, 0.5, 0.0, -0.00019589119265828528, 0.46875, 0.5, 0.0, 0.0020624312911391206, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sphere1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, -0.09299310279758932, 0.46875, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sphere1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, -0.09299310279758932, 0.46875, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.Radius = R

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.PhiResolution = 100

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.ThetaResolution = 100

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1Display
sphere1Display.SeamlessU = 1

# Properties modified on sphere1Display
sphere1Display.SeamlessV = 1

# create a new 'Texture Map to Sphere'
textureMaptoSphere1 = TextureMaptoSphere(Input=sphere1)

# show data in view
textureMaptoSphere1Display = Show(textureMaptoSphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
textureMaptoSphere1Display.Representation = 'Surface'
textureMaptoSphere1Display.ColorArrayName = [None, '']
textureMaptoSphere1Display.OSPRayScaleArray = 'Normals'
textureMaptoSphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
textureMaptoSphere1Display.SelectOrientationVectors = 'None'
textureMaptoSphere1Display.ScaleFactor = 0.2
textureMaptoSphere1Display.SelectScaleArray = 'None'
textureMaptoSphere1Display.GlyphType = 'Arrow'
textureMaptoSphere1Display.GlyphTableIndexArray = 'None'
textureMaptoSphere1Display.GaussianRadius = 0.01
textureMaptoSphere1Display.SetScaleArray = ['POINTS', 'Normals']
textureMaptoSphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
textureMaptoSphere1Display.OpacityArray = ['POINTS', 'Normals']
textureMaptoSphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
textureMaptoSphere1Display.DataAxesGrid = 'GridAxesRepresentation'
textureMaptoSphere1Display.PolarAxes = 'PolarAxesRepresentation'
textureMaptoSphere1Display.SelectInputVectors = ['POINTS', 'Normals']
textureMaptoSphere1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
textureMaptoSphere1Display.OSPRayScaleFunction.Points = [-0.00206091040046649, 0.0, 0.5, 0.0, -0.00019589119265828528, 0.46875, 0.5, 0.0, 0.0020624312911391206, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
textureMaptoSphere1Display.ScaleTransferFunction.Points = [-0.9998741149902344, 0.0, 0.5, 0.0, -0.09537258719136887, 0.46875, 0.5, 0.0, 0.9998741149902344, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
textureMaptoSphere1Display.OpacityTransferFunction.Points = [-0.9998741149902344, 0.0, 0.5, 0.0, -0.09537258719136887, 0.46875, 0.5, 0.0, 0.9998741149902344, 1.0, 0.5, 0.0]

# hide data in view
Hide(sphere1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on textureMaptoSphere1Display
textureMaptoSphere1Display.SeamlessU = 1

# Properties modified on textureMaptoSphere1Display
textureMaptoSphere1Display.SeamlessV = 1

# change texture
textureMaptoSphere1Display.Texture = CreateTexture(dir+"/sources/"+textureMapPic)

# set active source
SetActiveSource(sphere1)

# Properties modified on sphere1
sphere1.EndTheta = 359.9999999999999

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(textureMaptoSphere1)

# Properties modified on sphere1
sphere1.EndTheta = 359.9999999999

# Properties modified on sphere1
sphere1.EndTheta = 359.9999999999999

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on textureMaptoSphere1
textureMaptoSphere1.PreventSeam = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.UseSkyboxBackground = 1

# change texture
renderView1.BackgroundTexture = CreateTexture(dir+"/sources/universe.png")
renderView1.BackgroundNorth = [0.0, 0.0, 1.0]
renderView1.BackgroundEast = [1.0, 0.0, 0.0]

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.4425769997854951, -5.513131367953405, 1.2258657565564577]
renderView1.CameraViewUp = [0.7250858227355821, 0.32475736866637134, 0.6072752268656764]
renderView1.CameraParallelScale = 0.8516115354228021

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
