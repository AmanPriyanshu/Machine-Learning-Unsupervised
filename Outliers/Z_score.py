import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import gauss, seed
import math

seed(0)

def dataset_developer(n, mean=5, variance=2):
	X = []
	for i in range(n):
		X.append(gauss(mean, variance))
	X = np.array(X)
	return X
	

def imager(X, Y, outlier_X, outlier_Y, pic_name):
	plt.scatter(X, Y, color='green', marker='.')
	plt.scatter(outlier_X, outlier_Y, color='red', marker='*')
	plt.savefig(pic_name)
	plt.clf()

def g_plot(x, mean, variance):
	std_dev = math.sqrt(variance)
	exp = (((x-mean)/std_dev)**2)*(-0.5)
	y = math.exp(exp)/(std_dev*((2*math.pi)**0.5))
	return y

def z_score(data, mean, variance, N):
	outliers_index = []
	for element, i in zip(data, range(data.shape[0])):
		n = abs((element-mean)/variance)
		if n>=N:
			outliers_index.append(i)
	outliers = [data[i] for i in outliers_index]
	outliers_index = np.array(outliers_index)
	outliers = np.array(outliers)
	return outliers



def main():
	X = dataset_developer(1000)
	print(X[:10])
	X_out = z_score(X, 5, 2, 2)
	Y = [g_plot(x, 5, 2) for x in X]
	Y_out = [g_plot(x_out, 5, 2) for x_out in X_out]
	imager(X, Y, X_out, Y_out, pic_name='z_score_gaussian_visualisation.png')
	imager(X, [0 for i in range(X.shape[0])], X_out, [0 for i in range(X_out.shape[0])], 'z_score_simple_visualisation.png')
	print(X_out)

main()