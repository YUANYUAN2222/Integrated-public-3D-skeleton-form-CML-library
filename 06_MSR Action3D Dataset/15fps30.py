import os
import numpy as np
import pdb

def mkdir_if_not_exists(path):
	if not os.path.exists(path): os.mkdir(path)
data_path = r'./15nodes/processed'
save_path = r'./15nodes_30fps'
mkdir_if_not_exists(save_path)

fdrs = sorted(next(os.walk(data_path))[1])
# pdb.set_trace()
for fdr in fdrs:
	fdr_path = os.path.join(data_path,fdr)
	save_fdr_path = os.path.join(save_path,fdr)
	mkdir_if_not_exists(save_fdr_path)
	files = sorted(next(os.walk(fdr_path))[2])
	for file in files:
		file_path = os.path.join(fdr_path,file)
		print(file_path)
		save_file_path = os.path.join(save_fdr_path,file)
		data = np.loadtxt(file_path,delimiter=',')
		# pdb.set_trace()
		# data = data[:,1:]
		new_data = np.zeros((data.shape[0]*2,data.shape[1]),dtype=np.float32)
		nframes = data.shape[0]
		cnt = 1
		for iframe in range(nframes-1):
			new_data[2*iframe] = np.copy(data[iframe])
			new_data[2*iframe][0] = cnt
			new_data[2*iframe+1] = (np.copy(data[iframe]) + np.copy(data[iframe+1])) / 2
			new_data[2*iframe+1][0] = cnt + 1
			cnt += 2
		new_data[2*nframes-2] = np.copy(data[nframes-1])
		new_data[2*nframes-2][0] = cnt
		new_data[2*nframes-1] = np.copy(data[nframes-1])
		new_data[2*nframes-1][0] = cnt + 1
		# pdb.set_trace()
		# fmt = '%d', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f'\
		# 	, '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f'\
		# 	, '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f' 
		fmt = '%d', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f'\
			, '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f'\
			, '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f', '%.06f','%.06f','%.06f' 
		np.savetxt(save_file_path,new_data,fmt=fmt,delimiter=',')





