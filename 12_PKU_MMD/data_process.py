import os
import sys
import pdb
from tqdm import tqdm

def mkdir_if_not_exists(path):
	if not os.path.exists(path): os.mkdir(path)

data_path = r'../Skeleton/PKU_Skeleton_Renew/'
label_path = r'../Label_PKUMMD/Train_Label_PKU_final/'

save_path = r'./processed'
mkdir_if_not_exists(save_path)
files = next(os.walk(data_path))[2]

files.sort()

#对应节点
nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20]
# nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
for file in files:
	print(file)
	openfile = open(os.path.join(data_path,file))
	data = openfile.readlines()
	openfile.close()
	openfile = open(os.path.join(label_path,file))
	labels = openfile.readlines()
	openfile.close()
#通过label来处理data,从lable中提取需要的信息，
	for line in labels:
		act, start_frame, end_frame, _ = list(map(int,line.split(',')))
		save_act_fdr = os.path.join(save_path,str(act))
		mkdir_if_not_exists(save_act_fdr)

		nodeinfos = []
		for iframe in range(start_frame,end_frame+1):  #
			# pdb.set_trace()
			lineinfo = data[iframe-1].split(' ') #
			nodeinfo = [str(iframe)]
			for node in nodes:
				start_id = (node-1)*3
				nodeinfo.extend([lineinfo[start_id+2],lineinfo[start_id],lineinfo[start_id+1]])		
			nodeinfos.append(nodeinfo)
		save_act_file = os.path.join(save_act_fdr,file)	
		savefile = open(save_act_file,'a')
		for str1 in nodeinfos:
			savefile.write(','.join(str1)+'\n')
		savefile.close()




