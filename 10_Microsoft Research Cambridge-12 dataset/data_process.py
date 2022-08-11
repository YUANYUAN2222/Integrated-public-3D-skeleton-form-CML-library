import os
import sys
import pdb
from tqdm import tqdm
import csv


def make_if_not_exist(path):
	if not os.path.exists(path): os.mkdir(path)

data_path = r'../MicrosoftGestureDataset/MicrosoftGestureDataset-RC/data/'
save_path = r'./processed21'
make_if_not_exist(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[2] #walk返回三个列表，next

#pdb.set_trace()

files = [x for x in files if x.endswith('.csv')]
files.sort()
#对应节点
# 
nodes=[4,3,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
# nodes=[4,3,2,5,6,8,9,10,12,13,14,16,17,18,20]


# 
for file in files: 
	print(file)
	act = file.split('_')[2]
	if act.endswith('A'): act = act[:-1] 
	save_act_fdr = os.path.join(save_path,act)
	make_if_not_exist(save_act_fdr)
	save_file_path = os.path.join(save_act_fdr,'{}.txt'.format(file[:-4]))
	readfile = os.path.join(data_path,file)
	# pdb.set_trace()
	with open(readfile) as f:
		data = []
		f_csv = csv.reader(f)
		for row in f_csv:
			data.append(row[0])
	nframe = len(data)-20
	nodeinfos = []
	for iframe in range(nframe):
		# pdb.set_trace()
		lineinfo = data[iframe+20].split(' ')
		frame_id = int(lineinfo[0])
		nodeinfo = []
		for node in nodes:
			start_id = 4 * (node-1) + 1
			nodeinfo.extend([lineinfo[start_id+2],lineinfo[start_id],lineinfo[start_id+1]])
		nodeinfo = list(map(float,nodeinfo))
		str1 = str(frame_id+1)
		for nodexyz in nodeinfo:
			str1 += ',{:.3f}'.format(nodexyz)
		nodeinfos.append(str1)
	savefile = open(save_file_path,'a')
	for str1 in nodeinfos:
		savefile.write(str1+'\n')
	savefile.close()



