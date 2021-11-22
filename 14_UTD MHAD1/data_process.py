import os
import sys
import pdb
from tqdm import tqdm
import scipy.io as sio

def mkdir_if_not_exists(path):
	if not os.path.exists(path): os.mkdir(path)

data_path = r'../Data'

save_path = r'./processed'
mkdir_if_not_exists(save_path)
files = next(os.walk(data_path))[2]

files.sort()

#对应节点
nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20]
#nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
for file in files:
	if not file.endswith('skel_K2.mat'):
		continue
	print(file)
	data = sio.loadmat(os.path.join(data_path,file))['S_K2'].tolist()[0][0][0]
	# pdb.set_trace()
	act = str(file.split('_')[0])
	save_act_fdr = os.path.join(save_path,act)
	mkdir_if_not_exists(save_act_fdr)

	nodeinfos = []
	for iframe in range(data.shape[-1]):
		# pdb.set_trace()
		# lineinfo = data[iframe-1].split(' ')
		nodeinfo = [str(iframe)]
		for node in nodes:
			# start_id = (node-1)*3
			nodeinfo.extend([data[node-1,2,iframe],data[node-1,0,iframe],data[node-1,1,iframe]])	
		# nodeinfo = list(map(str,nodeinfo))	
		nodeinfos.append(nodeinfo)
	save_act_file = os.path.join(save_act_fdr,file.replace('mat','txt'))	
	savefile = open(save_act_file,'a')
	for str1 in nodeinfos:
		str2 = str1[0]
		for xyz in str1[1:]:
			str2 += ',{:6f}'.format(xyz)
		# pdb.set_trace()
		savefile.write(str2+'\n')
	savefile.close()




