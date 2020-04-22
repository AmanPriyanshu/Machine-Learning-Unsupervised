import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import gauss
import math

def imager(X, Y):
	plt.scatter(X[0], Y[0], color='green', marker='.')
	plt.scatter(X[1], Y[1], color='red', marker='.')
	plt.scatter(X[2], Y[2], color='blue', marker='.')
	plt.scatter(X[3], Y[3], color='black', marker='.')
	plt.scatter(X[4], Y[4], color='yellow', marker='.')
	plt.savefig('gaussian.png')
	plt.clf()

def g_cure(mean, variance):
	std_dev = math.sqrt(variance)
	x_list = [i/100 for i in range(-1000, 1000, 1)]
	y_list = []
	for x in x_list:
		exp = (((x-mean)/std_dev)**2)*(-0.5)
		y = math.exp(exp)/(std_dev*((2*math.pi)**0.5))
		y_list.append(y)
	return x_list, y_list



def data():
	g_mean = [0, 0, 0, 2, 3]
	v_mean = [1, 2, 3, 5, 1]
	X = []
	Y = []
	for i, j in zip(g_mean, v_mean):
		x_list, y_list = g_cure(i, j)
		X.append(x_list)
		Y.append(y_list)
	imager(X,Y)

data()


