import numpy as np 
import matplotlib.pyplot as plt 
import random 
x=[]
y=[]
plt.ion()
for i in range(100):
	x.append(random.randint(1,1000)/1000)
	y.append(random.randint(2,1000)/100)
for i in range(100):
	x.append(random.randint(1400,3000)/1000)
	y.append(random.randint(10,1000)/100)
epochs=10
plt.scatter(x,y)
plt.draw()
plt.pause(1)
red_centroid =[0,0]
blue_centroid =[0,0.5]
blue_x=[]
blue_y=[]
red_x=[]
red_y=[]
def distance_red(x_,y_):
	return ((x_-red_centroid[0])**2+(y_-red_centroid[1])**2)**2
def distance_blue(x_,y_):
	return ((x_-blue_centroid[0])**2+(y_-blue_centroid[1])**2)**2
def change_color():
	for i in range(len(x)):
		if distance_red(x[i],y[i])<distance_blue(x[i],y[i]):
			red_x.append(x[i])
			red_y.append(y[i])
		else:
			blue_x.append(x[i])
			blue_y.append(y[i])
	plt.scatter(red_x,red_y,color="red")
	plt.scatter(blue_x,blue_y,color="blue")
	plt.scatter(red_centroid[0],red_centroid[1],color="green")
	plt.scatter(blue_centroid[0],blue_centroid[1],color="green")
	plt.pause(0.1)
	plt.clf()
def average():
	sum_x_red=0
	sum_y_red=0
	sum_x_blue=0
	sum_y_blue=0
	for i in red_x:
		sum_x_red+=i
	for i in red_y:
		sum_y_red+=i
	for i in blue_x:
		sum_x_blue+=i
	for i in blue_y:
		sum_y_blue+=i
	n1=len(red_x)
	n2=len(blue_x)
	return [sum_x_red/n1,sum_y_red/n1,sum_x_blue/n2,sum_y_blue/n2]
for i in range(epochs):
	blue_x=[]
	blue_y=[]
	red_x=[]
	red_y=[]
	plt.title(f"epochs {i}")
	change_color()
	[red_centroid[0],red_centroid[1],blue_centroid[0],blue_centroid[1]]=average()

