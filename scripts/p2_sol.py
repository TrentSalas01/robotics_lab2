# import the required modules
import math
import numpy as np

#function to translate X
def trans_x(theta):
	trans = np.array([[1.0,  0.0, 0.0, theta],
				    [0.0, 1.0, 0.0, 0.0],
					[0.0, 0.0, 1.0, 0.0],
					[0.0, 0.0, 0.0, 1.0]])
					
	return trans
#function to translate y				
def trans_y(theta):
	trans = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, 1.0, 0.0, theta],
					[0.0, 0.0, 1.0, 0.0],
					[0.0, 0.0, 0.0, 1.0]])
					
	return trans
#function to translate z					
def trans_z(theta):
	trans = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, 1.0, 0.0, 0.0],
					[0.0, 0.0, 1.0, theta],
					[0.0, 0.0, 0.0, 1.0]])
	return trans
#function to rotate x	
def rot_x(theta):
	rot = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, math.cos(theta), -math.sin(theta), 0.0],
					[0.0, math.sin(theta), math.cos(theta), 0.0],
					[0.0, 0.0, 0.0, 1.0]])
	return rot
#function to rotate y
def rot_y(theta):
	rot = np.array([[math.cos(theta),  0.0, math.sin(theta), 0.0],
				    [0.0, 1.0, 0.0, 0.0],
					[-math.sin(theta), 0.0, math.cos(theta), 0.0],
					[0.0, 0.0, 0.0, 1.0]])
	return rot
#function to rotate z	
def rot_z(theta):
	rot = np.array([[math.cos(theta),  -math.sin(theta), 0.0, 0.0],
					[math.sin(theta),   math.cos(theta), 0.0, 0.0],
				    [0.0, 0.0, 1.0, 0.0],
				    [0.0, 0.0, 0.0, 1.0]])
	return rot
#function to create vector	
def vec(x,y,z, w):
	#Define a vector as an numpy and transpose it to a column vector.
	vec = np.array([[x, y, z, w]]).T 
	return vec
