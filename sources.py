import vtk
import copy
import vtk.util.numpy_support as vtknp
from scipy.spatial.transform import Rotation as Rot
import numpy as np

def addCoordData(grid,gridpoints):
	for i, n in enumerate('xyz'):
	    data = vtknp.numpy_to_vtk(gridpoints[:,i], deep=True)
	    data.SetName(n)
	    grid.GetPointData().AddArray(data)

def cone(c1,h_max,phi,n=100,name='temp'):
	c1 = np.array(c1)
	phi = np.radians(phi)
	r_max = h_max/np.tan(phi)
	hyp = h_max/np.sin(phi)
	circ = 2*np.pi*r_max
	nr = np.round(n*hyp/circ).astype('int')
	nr1 = nr+1	
	
	theta = np.linspace(0,2*np.pi,n+1)
	h = np.linspace(0,h_max,nr+1)
	r = h/np.tan(phi)
	X = np.outer(np.cos(theta), r)
	Y = np.outer(np.sin(theta), r)
	Z = np.outer(np.ones(theta.shape[0]), h)
	
	gridpoints = np.stack([X.flat, Y.flat, Z.flat], axis=1)
	gridpoints += c1
	
	points = vtk.vtkPoints()
	points.SetData(vtknp.numpy_to_vtk(gridpoints))
	
	grid = vtk.vtkStructuredGrid()
	grid.SetDimensions(nr1, n+1, 1)
	grid.SetPoints(points)
	addCoordData(grid,gridpoints)

	writer = vtk.vtkStructuredGridWriter()
	writer.SetFileName(name+'.vtk')
	writer.SetInputData(grid)
	writer.Write()

def coffeeFilter(c1,c2,h_max,phi1,phi2,n=100,name='temp'):
	c1 = np.array(c1)
	c2 = np.array(c2)
	c2mc1 = c2[:2]-c1[:2]
	L = np.linalg.norm(c2mc1)
	phi1 = np.radians(phi1)
	phi2 = np.radians(phi2)
	phi = (phi1+phi2)/2
	
	r_max = h_max/np.tan(phi)
	hyp = h_max/np.sin(phi)
	circ = np.pi*r_max/2
	nr = np.round(n*hyp/circ).astype('int')
	nL = np.round(n*L/circ).astype('int') 
	nr1 = nr+1	
	nL1 = nL+1	
	theta = np.linspace(0,np.pi,n+1)
	h = np.linspace(0,h_max,nr1)
	r1 = h/np.tan(phi1)
	X = np.outer(np.cos(theta), r1)
	Y = np.outer(np.sin(theta), r1)
	Z = np.outer(np.ones(theta.shape[0]), h)
	
	halfCone = np.stack([X.flat, Y.flat, Z.flat], axis=1)
	r2 = h/np.tan(phi2)
	X = np.outer(np.cos(theta), r2)
	Y = np.outer(np.sin(theta), r2)
	halfCone2 = np.stack([X.flat, Y.flat, Z.flat], axis=1)
	R = Rot.from_euler('z', 180, degrees=True)
	halfCone2 = R.apply(halfCone2)
	halfCone2[:,1] -= L
	y = np.linspace(L/2,-L/2,nL1)
	X = -(np.outer(y/L+0.5, r1)+np.outer(-y/L+0.5, r2))
	Y = np.outer(y, np.ones(r1.shape[0]))
	Z = np.outer(np.ones(nL1), h)
	
	plane = np.stack([X.flat, Y.flat, Z.flat], axis=1)
	y = np.linspace(-L/2,L/2,nL1)
	X = np.outer(y/L+0.5, r1)+np.outer(-y/L+0.5, r2)
	Y = np.outer(y, np.ones(r1.shape[0]))
	Z = np.outer(np.ones(nL1), h)
	plane2 = np.stack([X.flat, Y.flat, Z.flat], axis=1)
	plane[:,1] -= L/2
	plane2[:,1] -= L/2
	gridpoints = np.concatenate([halfCone,plane[nr1:,:],halfCone2[nr1:,:],plane2[nr1:,:]], axis=0)
	
	
	R = Rot.from_euler('z', np.arctan2(c2mc1[1],c2mc1[0]) + np.pi/2)
	gridpoints = R.apply(gridpoints)
	gridpoints += c1
	
	points = vtk.vtkPoints()
	points.SetData(vtknp.numpy_to_vtk(gridpoints))
	
	grid = vtk.vtkStructuredGrid()
	grid.SetDimensions(nr1, 2*(n+nL)+1, 1)
	grid.SetPoints(points)
	addCoordData(grid,gridpoints)
	
	writer = vtk.vtkStructuredGridWriter()
	writer.SetFileName(name+'.vtk')
	writer.SetInputData(grid)
	writer.Write()

			
if __name__ == "__main__":
  # execute only if run as a script
	cone([0,0,0],2000,3,n=100,name='temp')
	#coffeeFilter([4,5,6],[2,3,5],h_max=10,phi1=30,phi2=50,n=100,name='temp')
