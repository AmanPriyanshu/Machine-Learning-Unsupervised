import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_extractor(path):
	data = pd.read_csv(path)
	data = data.values
	return data

def labelizer(data):
	X = data.T[:-1]
	X = X.T
	Y = data.T[-1]
	Y = Y.T
	y = [0 if i=='no' else 1 for i in Y]
	y = np.array(y)
	return X, y

def normalizer(X):
	x = [(i-np.min(i))/(np.max(i)-np.min(i)) for i in X.T]
	return np.array(x).T

def main_data(path):
	data = data_extractor(path)
	np.random.seed(0)
	np.random.shuffle(data)
	X, Y = labelizer(data)
	X = normalizer(X)
	return X, Y



if __name__ == "__main__": 
	path = './Data/abalone_C1_P02_V01_CA0.csv'
	X, Y = main(path)
	print(X)
	print(Y)