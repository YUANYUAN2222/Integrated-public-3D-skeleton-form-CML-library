import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../data4'
save_path = r'./Suject4'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[2] #walk返回三个列表，next
# _,_,files = os.walk(data_path)
files.sort()
files = files[:-2]

#对应节点
nodes = [1,2,3,4,5,12,6,7,13,8,9,14,10,11,15]

for file in tqdm(files):  # file: S017C003P020R002A058.skeleton
# for file in files:  # file: S017C003P020R002A058.skeleton
	save_path_file = os.path.join(save_path,file)  # save_path_file: ./processed/S017C003P020R002A058.txt
	if os.path.exists(save_path_file):
		print('{} is exists!'.format(save_path_file))
		continue
	openfile = open(os.path.join(data_path,file),'r')
	data = openfile.readlines()
	openfile.close()
	try:
		nodeinfos = []
		for line in data[:-1]:
			lineinfo = line.split(',')
			index = int(lineinfo[0])
			nodeinfo = []
			# pdb.set_trace() 

			for node in nodes:
				if node < 12:
					start = 11 + (node-1) * 14
				else:
					start = 155 + 4 * (node - 12)
				# nodeinfo.extend(lineinfo[start:start+3])
				nodeinfo.extend([float(lineinfo[start+2])/1000.0,float(lineinfo[start])/1000.0,float(lineinfo[start+1])/1000.0])
			nodeinfo = list(map(float,nodeinfo))
			str1 = str(index)
			for nodexyz in nodeinfo:
				str1 += ',{:.3f}'.format(nodexyz)
			nodeinfos.append(str1)
	except:
		continue

	savefile = open(save_path_file,'a')
	for str1 in nodeinfos:
		savefile.write(str1+'\n')
	savefile.close()
	# pdb.set_trace()



