# import the required modules
import math
import rbm
import numpy as np

#function to rotate x, y, x using rbm module
def rot_xyz():
    vec = rbm.vec(0,1,1)
    a = (math.pi)/2
    rx = rbm.rot_x(a)
    b = (math.pi)/2
    ry = rbm.rot_y(b)
    c = (math.pi)/2
    rz = rbm.rot_z(c)
    t = np.matmul(rx, ry, rz)
    vec1 = t.dot(vec)
    t = np.matmul(rx, ry, rz)
    vec1 = t.dot(vec)
    print("Fixed \n", vec1)

	
def main():
    rot_xyz()
main()
