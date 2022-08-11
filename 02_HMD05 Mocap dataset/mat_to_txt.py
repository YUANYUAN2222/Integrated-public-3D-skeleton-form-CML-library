import os
import sys
import pdb
from tqdm import tqdm
from scipy import io as sio

def make_if_not_exists(path):
	if not os.path.exists(path):  #if not ，exist（）返回ture或者false,也可以认为返回1或者0
		os.mkdir(path)           #新建一个文件夹   os.mkdir(path)



data_path = r'../matlab-AMC-HDM05/processed'
save_path = r'./processed20_unit_moving'
make_if_not_exists(save_path) #判断路径是否存在，不存在就新建一个。                            新建文件夹
acts = next(os.walk(data_path))[1] #walk返回三个列表，next，#root, dirs, files
acts.sort()

#对应节点
#nodes = [17,15,12,18,19,22,25,26,29,2,3,5,7,8,10]
nodes = [17,15,12,18,19,22,25,26,29,2,3,5,7,8,10,1,21,4,28,9]
framerate = 4
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
				#str2 = ',{:.3f},{:.3f},{:.3f}'.format(data[iframe][node-1][2],data[iframe][node-1][0],data[iframe][node-1][1])   # str2  ',{:.3f},{:.3f},{:.3f}'看到‘’就知道肯定是一个字符串
				str2 = ',{:.3f},{:.3f},{:.3f}'.format(float(data[iframe][node-1][2])*0.0254/0.45,float(data[iframe][node-1][0])*0.0254/0.45,float(data[iframe][node-1][1])*0.0254/0.45-1.0) 
				str1 += str2  #字符串拼接，拼接每行的帧号加节点坐标，str1=帧号    str2=每次三个数字
			nodeinfos.append(str1)
		savefile = open(save_file_path,'a')  # 路径+模式
		for str1 in nodeinfos:
			savefile.write(str1+'\n') # str1=str2+str2+str2+str2  #写什么
		savefile.close()

