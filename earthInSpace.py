import getpass
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Manipulating texture images:
#convert -crop 50%x100% lightBlueMarble2.jpg converted_lBM2.jpg
#convert converted_lBM2-1.jpg converted_lBM2-0.jpg +append converted_lBM2.jpg
#rm converted_lBM2-*

username = getpass.getuser()
dir = '/home/'+username+'/kode/paraUtils/'
Rpole = 6356e3
Requator = 6378e3
#textureMapPic = "transparentEarth.png"
textureMapPic = "converted_lBM2.jpg"

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.UseSkyboxBackground = 1
renderView1.BackgroundTexture = CreateTexture(dir+"/sources/universe.png")
renderView1.BackgroundNorth = [0.0, 0.0, 1.0]
renderView1.BackgroundEast = [0.0, 1.0, 0.0]
renderView1.OrientationAxesVisibility = 0 # Hide orientation axes

# create a new 'Sphere'
sphere1 = Sphere()
sphere1.Radius = Requator
sphere1.PhiResolution = 100
sphere1.ThetaResolution = 100
sphere1.EndTheta = 359.9999999999999

calculator3 = Calculator(Input=sphere1)
calculator3.Function = 'coordsX*iHat+coordsY*jHat+'+str(Rpole/Requator)+'*coordsZ*kHat'
calculator3.ResultArrayName = 'Ellipsoid'
calculator3.CoordinateResults = 1

# create a new 'Texture Map to Sphere'
textureMaptoSphere1 = TextureMaptoSphere(Input=calculator3)
textureMaptoSphere1.PreventSeam = 0

# show data in view
textureMaptoSphere1Display = Show(textureMaptoSphere1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
textureMaptoSphere1Display.Representation = 'Surface'
textureMaptoSphere1Display.ColorArrayName = [None, '']
textureMaptoSphere1Display.SeamlessU = 1
textureMaptoSphere1Display.SeamlessV = 1
textureMaptoSphere1Display.Texture = CreateTexture(dir+"/sources/"+textureMapPic)

# update the view to ensure updated data information
renderView1.ResetCamera()

RenderAllViews()
