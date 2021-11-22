import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../nturgbd_skeletons_s018_to_s032'
save_path = r'./processed(18-32)_20'
if not os.path.exists(save_path): os.mkdir(save_path)
files = next(os.walk(data_path))[2] 
files.sort()

#对应节点
#nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20]
nodes =[4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19] #(1-25)

def data_process(file_path, save_path):
	# print(file_path)
	openfile = open(os.path.join(data_path,file),'r')   #
	data = openfile.readlines()  
	openfile.close()
	nframes = int(data[0])
	cnt = 1
	nodeinfos = []
	for iframe in range(nframes):
		nodeinfo = []
		nsamples = int(data[cnt])
		if nsamples == 0:
			cnt += 1
			continue
		for node in nodes:
			line = cnt + 2 + node  
			nodeinfo.extend([data[line].split()[2],data[line].split()[0],data[line].split()[1]])
		nodeinfo = list(map(float,nodeinfo))
		str1 = str(iframe+1)
		for nodexyz in nodeinfo:
			str1 += ',{}'.format(nodexyz)
		nodeinfos.append(str1)	
		if nsamples == 1:
			cnt += 28
		elif nsamples == 2:
			cnt += 55	


	savefile = open(save_path_file,'a')
	for str1 in nodeinfos:
		savefile.write(str1+'\n')
	savefile.close()



for file in tqdm(files): 
	file_name = str(file.split('.')[0])  #
	save_path_file = os.path.join(save_path,'{}.txt'.format(file_name))  
	if os.path.exists(save_path_file):
		print('{} is exists!'.format(save_path_file))
		continue
	file_path = os.path.join(data_path,file)
	data_process(file_path,save_path_file)




