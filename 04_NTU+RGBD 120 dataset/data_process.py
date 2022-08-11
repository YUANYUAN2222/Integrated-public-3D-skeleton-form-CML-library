import os
import sys
import pdb
from tqdm import tqdm

data_path = r'../nturgbd_skeletons_s001_to_s017'
save_path = r'./processed(01-17)_15'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[2] #walk返回三个列表，next
# _,_,files = os.walk(data_path)
files.sort()

#对应节点
# nodes = [4,3,21,5,6,8,9,10,12,13,14,16,17,18,20]  错误节点
nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20]
#nodes=[4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
20nodes =[4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19] #(1-25)



for file in tqdm(files):  # file: S017C003P020R002A058.skeleton      带着.skeleton后缀
# for file in files:  # file: S017C003P020R002A058.skeleton           
	file_name = str(file.split('.')[0])  # file_name: S017C003P020R002A058，不带后缀
	save_path_file = os.path.join(save_path,'{}.txt'.format(file_name))  # save_path_file: ./processed/S017C003P020R002A058.txt
	if os.path.exists(save_path_file):
		print('{} is exists!'.format(save_path_file))
		continue
	openfile = open(os.path.join(data_path,file),'r')   #打开文件夹/文件 '../nturgbd_skeletons_s018_to_s032/S001C001P001R001A001.skeleton'
	data = openfile.readlines()  #把文件中的每一行当作一个元素，返回给一个列表
	openfile.close()
	nsample = int(data[1])
	if nsample != 1: continue  #如果文件夹采集到的数据不为1，则跳出
	try:
		nodeinfos = []
		nframe = int(data[0])
		for i in range(nframe):
			nodeinfo = []
			for node in nodes:
				line = 28*i + 3 + node   #定位到数据
				nodeinfo.extend([data[line].split()[2],data[line].split()[0],data[line].split()[1]])
			nodeinfo = list(map(float,nodeinfo))
			str1 = str(i+1)
			for nodexyz in nodeinfo:
				str1 += ',{}'.format(nodexyz)
			nodeinfos.append(str1)
	except:
		continue

	savefile = open(save_path_file,'a')
	for str1 in nodeinfos:
		savefile.write(str1+'\n')
	savefile.close()
	# pdb.set_trace()



