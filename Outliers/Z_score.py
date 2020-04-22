import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def dataset_developer(n, probability=[0.05, 0.05, 0.15, 0.5, 0.15]):
	X = []
	while len(X)<n:
		t = random.random()
		if t<probability[0]:
			X.append(random.random()*0.2)
		elif t>=probability[0] and t<probability[1]+probability[0]:
			X.append(random.random()*0.2+0.2)
		elif t>= probability[1]+probability[0] and t<probability[0]+probability[1]+probability[2]:
			X.append(random.random()*0.2+0.2*2)
		elif t>=probability[0]+probability[1]+probability[2] and t<probability[0]+probability[1]+probability[2]+probability[3]:
			X.append(random.random()*0.2+0.2*3)
		else:
			X.append(random.random()*0.2+0.2*4)
	return X

def imager(X, Y, outlier_X, outlier_Y, l):
	X = random.sample(X, len(X))
	outlier_X = random.sample(outlier_X, l)
	plt.scatter(X, Y, color='green', marker='.')
	plt.scatter(outlier_X, outlier_Y, color='red', marker='*')
	plt.savefig('numeric_outlier.png')
	plt.clf()

