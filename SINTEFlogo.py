#### import the simple module from the paraview
from os.path import expanduser
from paraview.simple import *
# get active view

def insertSINTEFlogo(renderview,color='white'):
	home = expanduser("~")
	logo1 = Logo(registrationName='SINTEF logo ('+color+')')
	logo1.Texture = CreateTexture(home+'/kode/paraUtils/sources/SINTEF_'+color+'.png')
	logo1Display = Show(logo1, renderview, 'LogoSourceRepresentation')
	logo1Display.Position = [0.84, 0.0]
	logo1Display.Interactivity = 0
