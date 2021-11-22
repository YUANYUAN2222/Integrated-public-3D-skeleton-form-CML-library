import os
import sys
import pdb
from tqdm import tqdm
from scipy import io as sio

def make_if_not_exists(path):
	if not os.path.exists(path):  #if not 
		os.mkdir(path)           #新建一个文件夹   os.mkdir(path)



data_path = r'../matlab-AMC-CMU/processed'
save_path = r'./processed20_unit_moving'
make_if_not_exists(save_path) #判断路径是否存在，不存在就新建一个。                            新建文件夹
persons = next(os.walk(data_path))[1] #walk返回三个列表，next，#root, dirs, files
persons.sort()

#对应节点
#nodes = [17,15,12,18,19,22,25,26,29,2,3,5,7,8,10]
nodes = [17,15,12,18,19,22,25,26,29,2,3,5,7,8,10,1,21,4,28,9]

framerate60 = '60,61,62,74,75,77,79,80,88,89'
framerate60 = list(map(int,framerate60.split(',')))
#pdb.set_trace()
# for person in tqdm(persons): 
for person in persons:  
	person_id = int(person) #文件夹的名字是字符串，
	if person_id in framerate60:
		framerate = 2
	else:
		framerate = 4
	print('person:{}-framerate:{}'.format(person,framerate))
	person_path = os.path.join(data_path,person)  #joint把两个字符串写成一个路径   ../matlab-AMC-CMU/processed/01'  #读processed文件夹里面的文件夹01文件夹的名字
	save_person_path = os.path.join(save_path,person) #在processd20文件夹里面写入01文件夹，  './processed20/01'，01
	make_if_not_exists(save_person_path)   
	files = next(os.walk(person_path))[2] 
	files.sort()
	for file in files:
		file_name = str(file.strip().split('.')[0])
		data = sio.loadmat(os.path.join(person_path,file))['data']   #  ['data']  ？？？
		# pdb.set_trace()
		save_file_path = os.path.join(save_person_path,'{}.txt'.format(file_name))   # 新建立文件 用 open(),和write()函数，
		nframe = data.shape[0]  #输出数组的行数
		nodeinfos = []
		for iframe in range(0,nframe,framerate):# 
			str1 = str(iframe+1)
			for node in nodes:
				str2 = ',{:.3f},{:.3f},{:.3f}'.format(float(data[iframe][node-1][2])*0.0254/0.45,float(data[iframe][node-1][0])*0.0254/0.45,float(data[iframe][node-1][1])*0.0254/0.45-1) 
				#str2 = ',{:.3f},{:.3f},{:.3f}'.format(data[iframe][node-1][2],data[iframe][node-1][0],data[iframe][node-1][1])   # str2  是一个字符串
				
				str1 += str2  #拼接每行的帧号加节点坐标，str1=帧号    str2=每次三个数字
			nodeinfos.append(str1)
		savefile = open(save_file_path,'a')  # 路径+模式
		for str1 in nodeinfos:
			savefile.write(str1+'\n') # str1=str2+str2+str2+str2  #写什么
		savefile.close()

