import p2_sol
import math
import numpy as np

#function to test translation functions and vector function in current frame
def H_1():
	vec = p2_sol.vec(0,1,1,1)
	tx = p2_sol.trans_x(2.5)
	tz = p2_sol.trans_z(.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tx, tz)
	t = np.matmul(t, ty)
	vec1 = t.dot(vec)
	print("Current \n", vec1)
#function to test translation functions and vector function in current frame	
def H_2():
	vec = p2_sol.vec(0,1,1,1)
	tz = p2_sol.trans_z(.5)
	tx = p2_sol.trans_x(2.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tz, tx)
	t = np.matmul(t, ty)
	vec1 = t.dot(vec)
	print("Current \n", vec1)
#function to test translation functions and vector function in fixed frame	
def H_3():
	vec = p2_sol.vec(0,1,1,1)
	tx = p2_sol.trans_x(2.5)
	tz = p2_sol.trans_z(.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tx, tz)
	t = np.matmul(t, ty)
	vec1 = t.dot(vec)
	t = np.matmul(tx, tz)
	t = np.matmul(t, ty)
	vec1= t.dot(vec)
	print("Fixed \n", vec1)
#function to test translation functions and vector function in fixed frame	
def H_4():
	vec = p2_sol.vec(0,1,1,1)
	tz = p2_sol.trans_z(.5)
	tx = p2_sol.trans_x(2.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tz, tx)
	t = np.matmul(t, ty)
	vec1 = t.dot(vec)
	t = np.matmul(tz, tx)
	t = np.matmul(t, ty)
	vec1 = t.dot(vec)
	print("Fixed \n", vec1)
#function to test translation and rotation functions and vector function in current frame
def H_5():
	vec = p2_sol.vec(0,1,1,1)
	rx = p2_sol.rot_x(math.pi/2)
	tx = p2_sol.trans_x(3)
	tz = p2_sol.trans_z(-3)
	rz = p2_sol.rot_z(-(math.pi/2))
	t = np.matmul(rx, tx)
	t2 = np.matmul(tz, rz)
	t = np.matmul(t, t2)
	vec1 = t.dot(vec)
	print("Current", vec1)
#main function to test above functions
def main():
	H_1()
	H_2()
	H_3()
	H_4()
	H_5()
#call main
main()

