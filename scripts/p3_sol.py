import p2_sol
import math
import numpy as np

def H_1():
	vec = p2_sol.vec(0,1,1)
	tx = p2_sol.trans_x(2.5)
	tz = p2_sol.trans_z(.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tx, tz, ty)
	vec1 = t.dot(vec)
	print("Current", vec)
	
def H_2():
	vec = p2_sol.vec(0,1,1)
	tz = p2_sol.trans_z(.5)
	tx = p2_sol.trans_x(2.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tz, tx, ty)
	vec1 = t.dot(vec)
	print("Current", vec1)
	
def H_3():
	vec = p2_sol.vec(0,1,1)
	tx = p2_sol.trans_x(2.5)
	tz = p2_sol.trans_z(.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tx, tz, ty)
	vec1 = t.dot(vec)
	t = np.matmul(tx, tz, ty)
	vec1= t.dot(vec)
	print("Fixed", vec1)
	
def H_4():
	vec = p2_sol.vec(0,1,1)
	tz = p2_sol.trans_z(.5)
	tx = p2_sol.trans_x(2.5)
	ty = p2_sol.trans_y(-1.5)
	t = np.matmul(tz, tx, ty)
	vec1 = t.dot(vec)
	t = np.matmul(tz, tx, ty)
	vec1 = t.dot(vec)
	print("Fixed", vec1)

def H_5():
	vec = p2_sol.vec(0,1,1)
	rx = p2_sol.rot_x(math.pi/2)
	tx = p2_sol.trans_x(3)
	tz = p2_sol.trans_z(-3)
	rz = p2_sol.rot_z(-(math.pi/2))
	t = np.matmul(tz, tx, ty)
	vec1 = t.dot(vec)
	print("Current", vec1)
	

