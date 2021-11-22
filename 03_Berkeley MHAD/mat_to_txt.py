import os
import sys
import pdb
from tqdm import tqdm
from scipy import io as sio

def make_if_not_exists(path):
	if not os.path.exists(path):  #if not ，exist（）返回ture或者false,也可以认为返回1或者0
		os.mkdir(path)           #新建一个文件夹   os.mkdir(path)



data_path = r'../matlab-bvh-berkelely/processed'
save_path = r'./processed15_unit_moving'
make_if_not_exists(save_path) #判断路径是否存在，不存在就新建一个。                            新建文件夹
acts = next(os.walk(data_path))[1] #walk返回三个列表，next，#root, dirs, files
acts.sort()

#对应节点

nodes=[7,5,3,16,18,20,9,11,22,29,31,33,22,24,26]
#20nodes=[7,5,3,16,18,20,9,11,22,29,31,33,22,24,26,1 缺少wrist和ankle的数据]


framerate = 16
# pdb.set_trace()
# for act in tqdm(acts): 
for act in acts:  
	act_path = os.path.join(data_path,act)  #joint把两个字符串写成一个路径   ../matlab-AMC-CMU/processed/01'  #读processed文件夹里面的文件夹01文件夹的名字
	save_act_path = os.path.join(save_path,act) #在processd20文件夹里面写入01文件夹，  './processed20/01'，01
	make_if_not_exists(save_act_path)   
	files = next(os.walk(act_path))[2] 
	files.sort()
	for file in files:
		file_name = str(file.strip().split('.')[0])
		data = sio.loadmat(os.path.join(act_path,file))['data']   #  ['data']  返回一个字典，data相当于是KEY值
		# pdb.set_trace()
		save_file_path = os.path.join(save_act_path,'{}.txt'.format(file_name))   # 新建立文件 用 open(),和write()函数，
		nframe = data.shape[0]  #输出数组的行数
		nodeinfos = []
		for iframe in range(0,nframe,framerate):# 
			str1 = str(iframe+1)
			for node in nodes:
				str2 = ',{:.3f},{:.3f},{:.3f}'.format(float(data[iframe][node-1][2])/100,float(data[iframe][node-1][0])/100,float(data[iframe][node-1][1])/100-1.60)   # str2  ',{:.3f},{:.3f},{:.3f}'看到‘’就知道肯定是一个字符串
				#str2 = ',{:.3f},{:.3f},{:.3f}'.format(float(data[iframe][node-1][2])*0.0254/0.45,float(data[iframe][node-1][0])*0.0254/0.45,float(data[iframe][node-1][1])*0.0254/0.45-1) 

				str1 += str2  #字符串拼接，拼接每行的帧号加节点坐标，str1=帧号    str2=每次三个数字
			nodeinfos.append(str1)
		savefile = open(save_file_path,'a')  # 路径+模式
		for str1 in nodeinfos:
			savefile.write(str1+'\n') # str1=str2+str2+str2+str2  #写什么
		savefile.close()

