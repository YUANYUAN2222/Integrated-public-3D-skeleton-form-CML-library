import os
import sys
import pdb
from tqdm import tqdm


def make_if_not_exist(path):
	if not os.path.exists(path): os.mkdir(path)

data_path = r'../UCFKinect/dg1public/'
save_path = r'./processed'
make_if_not_exist(save_path)#判断路径是否存在，不存在就新建一个。
fdrs = next(os.walk(data_path))[1] #walk返回三个列表，next
fdrs.sort()

#对应节点
nodes = [1,2,3,7,8,9,4,5,6,13,14,15,10,11,12]
# pdb.set_trace()
for fdr in fdrs: 
	print(fdr)
	person_fdr = os.path.join(data_path,fdr)
	files = next(os.walk(person_fdr))[2]
	files.sort()
	for file in files:
		act, id, appendix = file.split('.')
		save_act_fdr = os.path.join(save_path,act)
		make_if_not_exist(save_act_fdr)
		save_file_path = os.path.join(save_act_fdr,'{}-{}.txt'.format(fdr,id))
		readfile = os.path.join(person_fdr,file)
		# pdb.set_trace()
		openfile = open(readfile)
		data = openfile.readlines()
		openfile.close()
		nframe = len(data)
		nodeinfos = []
		for iframe in range(nframe):
			lineinfo = data[iframe].split('|')
			pos_id = [i for i,x in enumerate(lineinfo) if x=='pos']
			nodeinfo = []
			for node in nodes:
				line_id = pos_id[node-1]
				nodeinfo.extend([float(lineinfo[line_id+3])/1000,float(lineinfo[line_id+1])/1000,float(lineinfo[line_id+2])/1000])
			nodeinfo = list(map(float,nodeinfo))
			str1 = str(iframe+1)
			for nodexyz in nodeinfo:
				str1 += ',{:06f}'.format(nodexyz)
			nodeinfos.append(str1)
		savefile = open(save_file_path,'a')
		for str1 in nodeinfos:
			savefile.write(str1+'\n')
		savefile.close()



