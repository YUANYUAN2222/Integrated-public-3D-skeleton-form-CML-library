import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../joints'
save_path = r'./processed_20nodes'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[2] #walk返回三个列表，next
# _,_,files = os.walk(data_path)
files.sort()

label2seq_path = r'./label2seq.txt'
with open(label2seq_path,'r') as f:
	labels = f.readlines()
labels = list(map(lambda x: x.strip(), labels)) #去掉换行符
#对应节点
nodes = [4,3,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
# pdb.set_trace()
# for file in tqdm(files):  # file: S017C003P020R002A058.skeleton
for file in files:  # file: S017C003P020R002A058.skeleton
	print(file)
	openfile = open(os.path.join(data_path,file))
	data = openfile.readlines()
	openfile.close()
	file_name = str(file.split('.')[0])[7:]  # file_name:截取filename的一部分,s01_e01
	start_line = labels.index(file_name)
	for j in range(10):
		label_data = labels[start_line+1+j]
		act = str(label_data.split(':')[0])
		print(act)
		try:
			start_frame, end_frame = map(int,label_data.split(':')[-1].strip().split())
		except: continue
		save_act_fdr = os.path.join(save_path,act)
		if not os.path.exists(save_act_fdr): os.mkdir(save_act_fdr)
		save_act_file = os.path.join(save_act_fdr,'{}.txt'.format(file_name))
		nodeinfos = []
		isreal = 0.0
		for k in range(len(data)):
			lineinfo = data[k].split()  #最关键的一行，
			nframe = int(lineinfo[0])
			if nframe < start_frame: continue
			if nframe > end_frame: break
			if nframe == start_frame: isreal += 1.0
			if nframe == end_frame: isreal += 1.0
			nodeinfo = []
			for node in nodes:
				start_id = (node-1)*3+1
				nodeinfo.extend([lineinfo[start_id+2],lineinfo[start_id],lineinfo[start_id+1]])

			nodeinfo = list(map(float,nodeinfo))
			str1 = str(nframe)
			for nodexyz in nodeinfo:
				str1 += ',{}'.format(nodexyz)
			nodeinfos.append(str1)
		savefile = open(save_act_file,'a')
		for str1 in nodeinfos:
			savefile.write(str1+'\n')
		savefile.close()
		if not isreal>0.5: print('file:{} - act:{} is not wrong!'.format(file_name,act))



