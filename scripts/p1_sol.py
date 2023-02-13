# import the required modules
import math
import rbm
import numpy as np

#function to rotate x
def rot_x():
    a = (math.pi)/2
    print("X: \n", rbm.rot_x(a))
#function to rotate y	
def rot_y():
    b = (math.pi)/2
    print("y: \n", rbm.rot_y(b))
#function to rotate z		
def rot_z():
    c = (math.pi)/2
    print("z: \n", rbm.rot_z(c))

	
def main():
    rot_x()
    rot_y()
    rot_z()
main()