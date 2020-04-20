import numpy as np
import random
import matplotlib.pyplot as plt

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

def numeric_outlier(X, k):
	Q1 = X[int((len(X)+1)/4)]
	Q3 = X[int(((len(X)+1)*3)/4)]
	IQR = Q3 - Q1
	outliers_index = [i for i in range(len(X)) if X[i]<Q1-k*IQR or X[i]>Q3+k*IQR]
	return outliers_index

def imager(X, Y):
	plt.scatter(X, Y, color='green', marker='.')
	plt.savefig('numeric_outlier.png')
	plt.clf()

def accuracy(outliers_index, X):
	accuracy = 0
	for j in range(len(X)):
		if j in outliers_index:
			if X[j]<0.5 or X[j]>0.9:
				accuracy += 1
		else:
			if X[j]>=0.5 and X[j]<=0.9:
				accuracy += 1
	return accuracy/len(X)

def main(X, k):
	outliers_index = numeric_outlier(X, k)
	return accuracy(outliers_index, X)

if __name__ == "__main__": 
	k = 0.45
	random.seed(1)
	X = dataset_developer(1000)
	X.sort()
	acc = main(X, k)
	print(acc)
