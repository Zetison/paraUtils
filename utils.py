from pyproj import Proj
import numpy as np
def prsLatLonStr(dmsStr):
	i = dmsStr.find('.')
	return [dmsStr[:i-4], dmsStr[i-4:i-2], dmsStr[i-2:]]

def dms2dd(dms):
	return float(dms[0]) + float(dms[1])/60 + float(dms[2])/3600

myProj = Proj("+proj=utm +zone=33K, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
def latLonUTM(lat,lon,z):
	declat = dms2dd(prsLatLonStr(lat))
	declon = dms2dd(prsLatLonStr(lon))
	lonUTM, latUTM = myProj(declon,declat)
	return np.array([lonUTM,latUTM,z*0.3048])


if __name__ == "__main__":
	runwayEndWest = latLonUTM("623323.41","0060532.89",35.3)
	runwayEndEast = latLonUTM("623351.26","0060740.31",49.2)
	runwayEndEast = latLonUTM("623353.33","0060749.80",49.2)
	runwayEndEast = latLonUTM("623350.14","0060735.18",35.3)
	runwayEndEast = latLonUTM("623321.34","0060523.40",35.3)
	runwayEndEast = latLonUTM("623321.34","0060523.40",49.2)
