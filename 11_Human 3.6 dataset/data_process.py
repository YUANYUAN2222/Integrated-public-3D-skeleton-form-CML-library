import os
import sys
from scipy import io as sio
import pdb
from tqdm import tqdm

data_path = r'../annotations'
save_path = r'./processed_15'

def mkdir_if_not_exists(path):
	if not os.path.exists(path):
		os.mkdir(path)
mkdir_if_not_exists(save_path)

subjects_ori = next(os.walk(data_path))[2] 
subjects = []
for subject in subjects_ori:
	if subject.endswith('3d.txt'):
		subjects.append(subject)
subjects.sort()

#对应节点
nodes = [11,9,8,12,13,14,15,16,17,5,6,7,2,3,4]


for subject in tqdm(subjects):
	subject_name = str(subject[9:-13])
	subject_path = os.path.join(data_path,subject)
	with open(subject_path,'r') as f:
		data = f.readlines()
		data = eval(data[0])
		actions = data.keys()
		for action in actions:
			save_act_path = os.path.join(save_path,action)
			mkdir_if_not_exists(save_act_path)
			indexes = data[action].keys()
			for index in indexes:
				frames = data[action][index].keys()
				frames = list(map(int,frames))
				frames.sort()
				# pdb.set_trace()
				save_file_path = os.path.join(save_act_path,'{}_{}.txt'.format(subject_name,index))

				nodeinfos = []
				# pdb.set_trace()
				for iframe in frames:
					nodedata = data[action][index]['{:s}'.format(str(iframe))]
					nodeinfo = []
					# pdb.set_trace()
					for node in nodes:
						nodeinfo.extend([float(nodedata[node-1][1])/1000.0,float(nodedata[node-1][0])/1000.0,float(nodedata[node-1][2])/1000.0])
						#2,0,1
					nodeinfo = list(map(float,nodeinfo))
					str1 = str(iframe)
					for nodexyz in nodeinfo:
						str1 += ',{:.3f}'.format(nodexyz)
					# pdb.set_trace()
					nodeinfos.append(str1)

				savefile = open(save_file_path,'a')
				for str1 in nodeinfos:
					savefile.write(str1+'\n')
				savefile.close()
				# pdb.set_trace()



