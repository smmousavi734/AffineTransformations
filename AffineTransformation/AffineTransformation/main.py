from matplotlib import pyplot as plt
import numpy as np
import cv2

def scaling(simg, srows, scols):
	pt1 = np.float32([[0.5, 0, 0],
				      [0, 0.5, 0],
				      [0,   0, 1]])

	simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
	dst = cv2.warpPerspective(simg,pt1,(scols*1,srows*1))

	matplotting(simg, dst)
	cv2.waitKey(0)
	
def rotation(simg, srows, scols):
	theta = np.radians(30)
	m = np.float32([[np.cos(theta), np.sin(theta), 150],
				    [-np.sin(theta), np.cos(theta), 150],
				    [0,					0,			 1]])
	
	simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
	dst = cv2.warpPerspective(simg,m,(srows*1,scols*1))

	matplotting(simg, dst)
	cv2.waitKey(0)

def translation(simg, srows, scols):
	m = np.float32([[1, 0, 150],
				    [0, 1, 150],
				    [0, 0,   1]])

	simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
	dst = cv2.warpPerspective(simg,m,(srows*1,scols*1))
	
	matplotting(simg, dst)
	cv2.waitKey(0)

def h_shearing(simg, srows, scols):
	m = np.float32([[1, 0.5, 0],
				    [0,   1, 0],
				    [0,   0, 1]])
	
	simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
	dst = cv2.warpPerspective(simg,m,(scols*2,srows*1))
	
	matplotting(simg, dst)
	cv2.waitKey(0)

def v_shearing(simg, srows, scols):
	m = np.float32([[1,   0, 0],
				    [0.5, 1, 0],
				    [0,   0, 1]])

	simg = cv2.cvtColor(simg, cv2.COLOR_BGR2RGB)
	dst = cv2.warpPerspective(simg,m,(scols*1,srows*2))
	
	matplotting(simg, dst)
	cv2.waitKey(0)

def matplotting(simg, sdst):
	
	plt.subplot(121)
	plt.imshow(simg)
	plt.title('Original')

	plt.subplot(122)
	plt.imshow(sdst)
	plt.title('Result')

	plt.show()

def plotting(func):
	img = cv2.imread('D:\\111.jpg',0)
	rows, colms = img.shape
	
	if func == 1:
		scaling(img, rows, colms)
	elif func == 2:
		rotation(img, rows, colms)
	elif func == 3:
		translation(img, rows, colms)
	elif func == 4:
		h_shearing(img, rows, colms)
	elif func == 5:
		v_shearing(img, rows, colms)
	else:
		print("Wrong input")

print("Please choose which transformation you would like to demonstrate: \n")
print("1.Scaling\n2.Rotation\n3.Translation\n4.Horizantal Shearing\n5.Vertical Shearing\n")
print("Choice: ")
choice = int(input())

plotting(choice)