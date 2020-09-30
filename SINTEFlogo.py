#### import the simple module from the paraview
from os.path import expanduser
from paraview.simple import *
# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

home = expanduser("~")
logo1 = Logo()
logo1.Texture = CreateTexture(home+'/kode/paraUtils/sources/SINTEF_white.png')
logo1Display = Show(logo1, renderView1, 'LogoSourceRepresentation')
logo1Display.Position = [0.84, 0.0]
logo1Display.Interactivity = 0
