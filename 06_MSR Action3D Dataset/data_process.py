import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../MSRAction3DSkeletonReal3D--zhun'
save_path = r'./processed20'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[0] #walk返回三个列表，next
# _,_,files = os.walk(data_path)
files.sort()
pdb.set_trace()
#对应节点
# nodes = [20,3,4,1,8,12,2,9,13,5,14,18,6,15,19]
nodes = [20,3,4,1,8,12,2,9,13,5,14,18,6,15,19,7,10,16,11,17]
# pdb.set_trace()
# for file in tqdm(files):  # file: S017C003P020R002A058.skeleton
for file in files:  # file: S017C003P020R002A058.skeleton
	print(file)
	openfile = open(os.path.join(data_path,file))
	data = openfile.readlines()
	openfile.close()
	act, file_name = file[:3], file[4:11]
	save_act_fdr = os.path.join(save_path,act)
	if not os.path.exists(save_act_fdr): os.mkdir(save_act_fdr)
	save_act_file = os.path.join(save_act_fdr,'{}.txt'.format(file_name))
	nodeinfos = []
	assert len(data) % 20 == 0, "{} wrong lines".format(file)
	nframe = int(len(data)//20)
	for i in range(nframe):
		nodeinfo = []
		for node in nodes:
			line_id = 20*i-1 + node
			lineinfo = data[line_id].strip().split()
			nodeinfo.extend([lineinfo[2],lineinfo[0],lineinfo[1]])
		nodeinfo = list(map(float,nodeinfo))
		str1 = str(i+1)
		for nodexyz in nodeinfo:
			str1 += ',{}'.format(nodexyz)
		nodeinfos.append(str1)
	savefile = open(save_act_file,'a')
	for str1 in nodeinfos:
		savefile.write(str1+'\n')
	savefile.close()



