from os.path import expanduser
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

home = expanduser("~")
paraUtilsDir = home+'/kode/paraUtils'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.UseSkyboxBackground = 1
renderView1.BackgroundTexture = CreateTexture(paraUtilsDir+"/sources/universe.png")
#renderView1.BackgroundNorth = [0.0, 0.0, 1.0]
#renderView1.BackgroundEast = [0.0, 1.0, 0.0]
renderView1.OrientationAxesVisibility = 0 # Hide orientation axes

RenderAllViews()
