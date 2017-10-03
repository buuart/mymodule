#!/usr/bin/python3
import os
frstSplit=0
lstSplit=0
def post_proc():
	common_path='C:\\Users\\Buuart\\Desktop\\Для тони'
	result_path='C:\\Users\\Buuart\\Desktop\\tony_compatible'
	file_list=os.listdir(common_path)
	for name in range(len(file_list)):
		file=open(os.path.join(common_path,file_list[name]))
		text=file.read()
		file.close()
		text=text.split('\n')
		for i in range(len(text)):
			if(text[i][:2]=='M3'):
				global frstSplit
				frstSplit=i
				break
		for i in range(len(text)):
			if(text[i][:2]=='M5'):
				global lstSplit
				lstSplit=i
				break
		text=text[frstSplit:lstSplit+1]
		for i in range(len(text)):
			if (text[i].find('[')==0):
				text[i]=''
			elif (not(text[i].find('[')==-1)):
				text[i]=text[i][:text[i].find('[')-1]
		text[-2]='G0Z20.000'
		new_name=file_list[name][:-3]+'_tony_compatible.nc'
		file=open(os.path.join(result_path,new_name),'a')
		for i in range(len(text)):
			file.write(text[i]+'\n')
		file.close()

post_proc()