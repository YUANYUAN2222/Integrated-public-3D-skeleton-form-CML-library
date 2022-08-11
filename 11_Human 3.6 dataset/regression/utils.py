import xlrd
import numpy as np
import math
import pdb
from tqdm import tqdm
import os

def load_train_file_from_NTU(path,start_id, end_id):
	# pdb.set_trace()
	x_data_all = np.empty((0,60),dtype=np.float32)
	fdrs = sorted(next(os.walk(path))[1])
	for fdr in tqdm(fdrs[start_id:end_id]):
		fdr_path = os.path.join(path,fdr)
		files = sorted(next(os.walk(fdr_path))[2])
		for file in files[:6]:
			file_path = os.path.join(fdr_path,file)
			with open(file_path,'r') as f:
				data = f.readlines()
			for lineinfo in data:
				tmp = np.array(list(map(float,lineinfo.split(',')[1:]))).reshape(1,60)
				x_data_all = np.concatenate((x_data_all,tmp),0)	
	# pdb.set_trace()
	return x_data_all

def load_pred_file(path):
	# pdb.set_trace()
	x_data = np.empty((0,45),dtype=np.float32)
	with open(path,'r') as f:
		data = f.readlines()
	for lineinfo in data:
		tmp = np.array(list(map(float,lineinfo.split(',')[1:]))).reshape(1,45)
		x_data = np.concatenate((x_data,tmp),0)	
	# pdb.set_trace()
	return x_data


def load_data(path,istrain=True): 
	# pdb.set_trace()
	if istrain:
		x_data_all = load_train_file_from_NTU(path=r'G:\4_NTU\20nodes/processed(01-17)_20_split/', start_id=0,end_id=60)
		return x_data_all[:,:45], x_data_all[:,45:]
	else:
		x_data_all = load_pred_file(path=path)
		return x_data_all
	

