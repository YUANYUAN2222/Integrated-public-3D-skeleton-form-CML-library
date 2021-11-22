from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

from utils import *
import os
import numpy as np
import pdb
from tqdm import tqdm
import matplotlib
import matplotlib.pyplot as plt
import random
from sklearn.neural_network import MLPRegressor

def mkdir_if_not_exists(path):
	if not os.path.exists(path): os.mkdir(path)

root_path = r'../15nodes/processed_15'
save_path = r'../20nodes_pred'
mkdir_if_not_exists(save_path)

def save(x_test,y_test,path):
	# pdb.set_trace()
	nframes = x_test.shape[0]
	index = np.array(range(1,nframes+1)).astype(np.int8).reshape(nframes,1)
	res = np.concatenate((index,x_test,y_test),1)
	np.savetxt(path,res,fmt='%1.4f',delimiter=',') #numpy保存为txt


def main(root_path):
	## load data
	# nsample * 15  --> nsample * 5
	# pdb.set_trace()
	x_train, y_train = load_data(root_path,istrain=True)  # trainset
	# x_test, y_test = load_data(root_path,istrain=False)
	regressor = MLPRegressor(random_state=1, max_iter=10000).fit(x_train,y_train)  #训练模型
	print(regressor.score(x_train,y_train))
	fdrs = sorted(next(os.walk(root_path))[1])
	for fdr in fdrs:
		fdr_path = os.path.join(root_path,fdr)
		save_fdr_path = os.path.join(save_path,fdr)
		mkdir_if_not_exists(save_fdr_path)
		files = sorted(next(os.walk(fdr_path))[2])
		for file in files:
			file_path = os.path.join(fdr_path,file)
			save_file_path = os.path.join(save_fdr_path,file)
			x_test = load_data(file_path,istrain=False)
			res = regressor.predict(x_test)
			save(x_test,res,save_file_path)
			print(file_path)


if __name__ == '__main__':
	random.seed(0)
	main(root_path)