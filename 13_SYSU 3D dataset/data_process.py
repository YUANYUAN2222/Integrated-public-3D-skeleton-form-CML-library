import os
import sys
from scipy import io as sio
import pdb
from tqdm import tqdm

data_path = r'../SYSU3DAction/3DvideoNorm'
save_path = r'./processed_15'

def mkdir_if_not_exists(path):
	if not os.path.exists(path):
		os.mkdir(path)
mkdir_if_not_exists(save_path)

persons = next(os.walk(data_path))[1] 
persons.sort()

#对应节点
# nodes = [4, 3, 2, 9, 10, 12, 5, 6, 8, 17, 18, 20, 13, 14, 16]#原节点bvh可视化之后，腿部反了
# nodes = [4, 3, 2, 9, 10, 12, 5, 6, 8, 17, 18, 20, 13, 14, 16, 1, 11, 19, 7, 15]#原节点
# nodes = [4, 3, 2, 9, 10, 12, 5, 6, 8, 13, 14, 16, 17, 18, 20, 1, 11, 15, 7, 19] #把左腿和右腿的节点位置对调
nodes = [4, 3, 2, 9, 10, 12, 5, 6, 8, 13, 14, 16, 17, 18, 20]
for person in tqdm(persons):
	person_fdr_path = os.path.join(data_path,person)
	actions = sorted(next(os.walk(person_fdr_path))[1])
	for action in actions:
		load_file_path = os.path.join(person_fdr_path,action,'sklWorld.mat')
		act_fdr_path = os.path.join(save_path,action)
		mkdir_if_not_exists(act_fdr_path)
		save_file_path = os.path.join(act_fdr_path,'{}_{}.txt'.format(action,person))
		data = sio.loadmat(load_file_path)
		data = data['SW']
		# pdb.set_trace()
		nframes = data.shape[2]

		nodeinfos = []
		# pdb.set_trace()
		for iframe in range(nframes):
			nodeinfo = []
			for node in nodes:
				nodeinfo.extend([float(data[node-1,2,iframe]),float(data[node-1,0,iframe]),float(data[node-1,1,iframe])])
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



