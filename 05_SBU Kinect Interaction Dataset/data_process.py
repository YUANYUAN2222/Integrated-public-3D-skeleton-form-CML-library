import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../'
save_path = r'./processed_unit_meter'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
fdrs = next(os.walk(data_path))[1] #walk返回三个列表，next
# _,_,fdrs = os.walk(data_path)
fdrs.sort()
fdrs = fdrs[:-3]
#对应节点
nodes = range(15)

for fdr in tqdm(fdrs):  # file: S017C003P020R002A058.skeleton
# for fdr in fdrs:  # file: S017C003P020R002A058.skeleton
	# pdb.set_trace()
	peoples = str(fdr.split('-')[-1])
	fdr_path = os.path.join(data_path,fdr,peoples)
	for i in range(1,9):
		act = '{:02d}'.format(i)
		save_path_act = os.path.join(save_path,act)
		if not os.path.exists(save_path_act):
			os.mkdir(save_path_act)
		fdr_path_act = os.path.join(fdr_path,act)
		for j in range(1,3):
			samples = '{:03d}'.format(j)
			fdr_path_act_sample = os.path.join(fdr_path_act,samples,'skeleton_pos.txt')
			if not os.path.isfile(fdr_path_act_sample): continue
			save_data_path = os.path.join(save_path_act,'{}_{}.txt'.format(peoples,samples))

			openfile = open(fdr_path_act_sample,'r')
			data = openfile.readlines()
			openfile.close()
			nodeinfos = []
			for line in data:
				lineinfo = line.strip().split(',')
				index = int(lineinfo[0])
				nodeinfo = []
				for node in nodes:
					start = 1 + 3 * node
					 #调整Z轴顺序
					nodeinfo.extend([float(lineinfo[start+2])*10/7.8125,(1280-(float(lineinfo[start])*2560))/1000,(960-(float(lineinfo[start+1])*1920))/1000]) #把单位毫米，变为了米
				  # nodeinfo.extend([float(lineinfo[start+2])*10000/7.8125,1280-(float(lineinfo[start])*2560),960-(float(lineinfo[start+1])*1920)]) 
					# 原始 nodeinfo.extend([float(lineinfo[start+2])*10000/7.8125,1280-(float(lineinfo[start])*2560),960-(float(lineinfo[start+1])*1920)])  #调整Z轴顺序	
				str1 = str(index)
				for nodexyz in nodeinfo:
					str1 += ',{:.3f}'.format(nodexyz)
				nodeinfos.append(str1)
			savefile = open(save_data_path,'a')
			for str1 in nodeinfos:
				savefile.write(str1+'\n')
			savefile.close()



