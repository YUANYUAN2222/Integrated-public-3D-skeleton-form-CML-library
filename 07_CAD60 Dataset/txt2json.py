import os, sys
import json
import pdb
import numpy as np

#20节点为预测值



def mkdir_if_not_exists(path):
	if not os.path.exists(path): os.makedirs(path)

data_path = r'./15nodes/processed'
label_path = r'./sourcelabel2targetlabel.txt'
save_path = r'./json_data/15nodes'
mkdir_if_not_exists(save_path)
predict = 0
source_name = 'CAD'

# generate list of source labels and target labels
with open(label_path,'r') as f:
	labels = f.readlines()
sourcelabels, targetlabels, correlations = [], [], []
for idx, label in enumerate(labels):
	# print(label.strip())
	# sourcelabel, targetlabel, correlation = str(label.strip().split(',')[0]), str(label.strip().split(',')[1]), , str(label.strip().split(',')[-1])
	sourcelabel, targetlabel, correlation = map(str,label.strip().split(','))
	sourcelabels.append(sourcelabel)
	targetlabels.append(targetlabel)
	correlations.append(int(correlation))


acts = sorted(next(os.walk(data_path))[1])

for act in acts:
	act_path = os.path.join(data_path,act)
	files = sorted(next(os.walk(act_path))[2])
	for file in files:
		file_path = os.path.join(act_path,file)
		with open(file_path,'r') as f:
			data_tmp = f.readlines()
		# filter empty lines
		data = []
		for idata in data_tmp:
			if len(idata) < 40: continue
			data.append(idata)

		ncor = len(data[0].strip().split(',')) - 1
		nframes = len(data)
		source_file = act + '/' + file
		print(source_file)
		# pdb.set_trace()
		label_id = sourcelabels.index(act)
		targetlabel = targetlabels[label_id]
		correlation = correlations[label_id]
		#以targetlabel命名的文件夹
		save_label_path = os.path.join(save_path,targetlabel)
		mkdir_if_not_exists(save_label_path) 
		res = {} #70，71
		# head = {}
		body = {} #64
		res['source'] = source_name
		res['sourcelabel'] = act
		res['sourcefile'] = source_file
		res['targetlabel'] = targetlabel
		res['nframes'] = nframes
		res['format'] = 'xyz'
		res['correlation'] = correlation
		res['predict'] = predict
		# res['head'] = head
		assert ncor == 45 or ncor == 60, 'ncor wrong'
		jsondata = np.zeros((nframes,ncor),dtype=np.float32)#
		for frame_id in range(nframes):
			frameinfo = data[frame_id].split(',')[1:]
			frameinfo = list(map(float,frameinfo))
			jsondata[frame_id] = np.array(frameinfo) #
			body[frame_id] = frameinfo
		res['body'] = body
		res['data'] = jsondata.tolist() #jsondata 是numpy,nframe*45
		# pdb.set_trace()
		nfiles = len(os.listdir(save_label_path))#返回文件以及文件夹的名字，组成的列表。
		file_name = '{:05d}.json'.format(nfiles+1)
		save_file_path = os.path.join(save_label_path,file_name)
		with open(save_file_path,'w') as f:
			json.dump(res,f)
		#json.dump(需要写入的参数，位置)