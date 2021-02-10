#from pyproj import Proj
from os.path import expanduser
from paraview.simple import *
import numpy as np
def prsLatLonStr(dmsStr):
    i = dmsStr.find('.')
    return [dmsStr[:i-4], dmsStr[i-4:i-2], dmsStr[i-2:]]

def dms2dd(dms):
    return float(dms[0]) + float(dms[1])/60 + float(dms[2])/3600

#myProj = Proj("+proj=utm +zone=33K, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
#def latLonUTM(lat,lon,z):
#    declat = dms2dd(prsLatLonStr(lat))
#    declon = dms2dd(prsLatLonStr(lon))
#    lonUTM, latUTM = myProj(declon,declat)
#    return np.array([lonUTM,latUTM,z*0.3048])

def annotateTimeStep(obj,renderview,location='UpperLeftCorner',SAVE_HIST=1,color=[0.0, 0.0, 0.0]):
    pythonAnnotation = PythonAnnotation(registrationName='Time annotation', Input=obj)
    pythonAnnotation.ArrayAssociation = 'Point Data'
    pythonAnnotation.Expression = '"Step: %d\\nTime: %0.2fs" % ((time_index+1)*'+str(SAVE_HIST)+', time_value)'
    pythonAnnotationDisplay = Show(pythonAnnotation, renderview, 'TextSourceRepresentation')
    pythonAnnotationDisplay.WindowLocation = location 
    pythonAnnotationDisplay.Color = color 
    pythonAnnotationDisplay.FontSize = 5

def insertSINTEFlogo(renderview,color='white',position=[0.84, 0.0]):
    home = expanduser("~")
    logo1 = Logo(registrationName='SINTEF logo ('+color+')')
    logo1.Texture = CreateTexture(home+'/kode/paraUtils/sources/SINTEF_'+color+'.png')
    logo1Display = Show(logo1, renderview, 'LogoSourceRepresentation')
    logo1Display.Position = position
    logo1Display.Interactivity = 0

def saveScreenShot(renderView,name,saveScreenShots=True,viewSize=[1920,1080],useTransparentBackground=False,saveAllViews=0,separatorWidth=0):
    if saveScreenShots:
        SaveScreenshot(name+'.png', renderView, SaveAllViews=saveAllViews,SeparatorWidth=separatorWidth,
                FontScaling='Do not scale fonts', #'Scale fonts proportionally',
                TransparentBackground=useTransparentBackground,
                ImageResolution=viewSize,
                ImageQuality=100)

def saveAnimation(renderViewOrLayout,name,noSteps,makeVideo=True,viewSize=[1920,1080],frameRate=15,animStart=0,saveAllViews=0,separatorWidth=0):
    if makeVideo:
        animationScene1 = GetAnimationScene()
        SaveAnimation(name+'.ogv', renderViewOrLayout,SaveAllViews=saveAllViews,SeparatorWidth=separatorWidth,
                FontScaling='Do not scale fonts', #'Scale fonts proportionally',
                OverrideColorPalette='',
                StereoMode='No change',
                TransparentBackground=0,
                ImageQuality=100,
                FrameRate=frameRate,
                ImageResolution=viewSize,
                FrameWindow=[animStart, animStart+noSteps-1])

def copyCamera(renderview1,renderview2):
    renderview2.CameraPosition = renderview1.CameraPosition
    renderview2.CameraFocalPoint = renderview1.CameraFocalPoint
    renderview2.CameraViewUp = renderview1.CameraViewUp
    renderview2.CameraParallelScale = renderview1.CameraParallelScale

if __name__ == "__main__":
    runwayEndWest = latLonUTM("623323.41","0060532.89",35.3)
    runwayEndEast = latLonUTM("623351.26","0060740.31",49.2)
    runwayEndEast = latLonUTM("623353.33","0060749.80",49.2)
    runwayEndEast = latLonUTM("623350.14","0060735.18",35.3)
    runwayEndEast = latLonUTM("623321.34","0060523.40",35.3)
    runwayEndEast = latLonUTM("623321.34","0060523.40",49.2)
