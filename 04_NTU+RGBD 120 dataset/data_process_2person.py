import os
import sys
import pdb
from tqdm import tqdm
# 这个文件夹用来处理 50-61，或者106-121双人数据集



data_path = r'../nturgbd_skeletons_s018_to_s032'
# save_path = r'./processed(01-17)_15_person1'   
save_path = r'./processed(18-32)_20_person2'
if not os.path.exists(save_path): os.mkdir(save_path)#判断路径是否存在，不存在就新建一个。
files = next(os.walk(data_path))[2] #walk返回三个列表，next
files.sort()

# nodes = [4,21,2,5,6,8,9,10,12,13,14,16,17,18,20]
nodes=[4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19]
# 20nodes =[4,21,2,5,6,8,9,10,12,13,14,16,17,18,20,1,7,15,11,19] #(1-25)

action = range(106,121) #18-31suject
#action = range(50,61) #1-17suject

for ifile, file in enumerate(files):  # file: S017C003P020R002A058.skeleton      带着.skeleton后缀
	if not int(file[17:20]) in action:
		print('{}/{}-{}: continue'.format(ifile,len(files),file))
		continue
	print('{}/{}-{}: process'.format(ifile,len(files),file))
	file_name = str(file.split('.')[0])  # file_name: S017C003P020R002A058，不带后缀
	save_path_file = os.path.join(save_path,'{}.txt'.format(file_name))  # save_path_file: ./processed/S017C003P020R002A058.txt
	if os.path.exists(save_path_file):
		print('{} is exists!'.format(save_path_file))
		continue
	openfile = open(os.path.join(data_path,file),'r')   #打开文件夹/文件 '../nturgbd_skeletons_s018_to_s032/S001C001P001R001A001.skeleton'
	data = openfile.readlines()  #把文件中的每一行当作一个元素，返回给一个列表
	openfile.close()
	try:
		nodeinfos = []
		nframe = int(data[0])
		for i in range(nframe):
			nodeinfo = []
			for node in nodes:
				line = 55*i + 30 + node   #定位到数据,person2,30
				# line = 55*i + 3 + node   #定位到数据,person1,3
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



