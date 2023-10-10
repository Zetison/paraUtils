from os.path import expanduser
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Manipulating texture images:
#convert -crop 50%x100% lightBlueMarble2.jpg converted_lBM2.jpg
#convert converted_lBM2-1.jpg converted_lBM2-0.jpg +append converted_lBM2.jpg
#rm converted_lBM2-*
home = expanduser("~")
paraUtilsDir = home+'/kode/paraUtils'
Rpole = 6356e3
Requator = 6378e3
#textureMapPic = "transparentEarth.png"
textureMapPic = "converted_lBM2.jpg"

#import universeBackground

# create a new 'Sphere'
sphere1 = Sphere()
sphere1.Radius = Requator
sphere1.PhiResolution = 100
sphere1.ThetaResolution = 100
sphere1.EndTheta = 359.9999999999999

# create a new 'Texture Map to Sphere'
textureMaptoSphere1 = TextureMaptoSphere(Input=sphere1)
textureMaptoSphere1.PreventSeam = 0

ellipsoid = Calculator(Input=textureMaptoSphere1)
ellipsoid.Function = 'coordsX*iHat+coordsY*jHat+'+str(Rpole/Requator)+'*coordsZ*kHat'
ellipsoid.ResultArrayName = 'Ellipsoid'
ellipsoid.CoordinateResults = 1

# show data in view
textureMaptoSphere1Display = Show(ellipsoid, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
textureMaptoSphere1Display.Representation = 'Surface'
textureMaptoSphere1Display.ColorArrayName = [None, '']
textureMaptoSphere1Display.SeamlessU = 1
textureMaptoSphere1Display.SeamlessV = 1
textureMaptoSphere1Display.Texture = CreateTexture(paraUtilsDir+"/sources/"+textureMapPic)

# update the view to ensure updated data information
renderView1.ResetCamera()

RenderAllViews()
