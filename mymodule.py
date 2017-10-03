#  ███╗   ███╗██╗   ██╗    ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
#  ████╗ ████║╚██╗ ██╔╝    ████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
#  ██╔████╔██║ ╚████╔╝     ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  
#  ██║╚██╔╝██║  ╚██╔╝      ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  
#  ██║ ╚═╝ ██║   ██║       ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗
#  ╚═╝     ╚═╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
# by buuart
#from PyQt5.QtWidgets import QApplication, QWidget
#from tkinter import *
import math as m
import codecs as c
import hashlib as h
import os
import time as t
import sys
import shutil as sh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

e=open('mymodule.txt','r', encoding="utf-8")
f=e.read()
e.close()
f=f.split('\n')
del e
for i in range(len(f)):
	print(f[i])
del f



def md5z(u):#same as md5.cz
	u=str(u)
	u=h.md5(c.encode(u)).hexdigest()
	return u

def bezumie():
	e=input("input number: ")
	e=md5z(e)
	print(e)

def md5q(string,salt):
	f=md5z(md5z(str(string))+str(salt))
	return f

def form(e,c,d):
	result=(e+c)/(1/d)
	print (result)

def demo():
	res=[[0],[0]]
	prew=0
	prewI=0
	prewA=0
	demo=input("first order comma sep. : ")
	demo=demo.split(',')
	for i in range(len(demo)):
		demo[i] =float(demo[i])
	demo2=input("second order comma sep. : ")
	demo2=demo2.split(',')
	for i in range(len(demo2)):
		demo2[i]=float(demo2[i])
	res[0]=demo
	res[1]=demo2
	startTime=t.clock()
	print(len(demo),len(demo2),' ', "total operations = ",(len(demo)*len(demo2)))
	print(res[0],res[1])
	for i in range(len(res[0])):
		for a in range(len(res[1])):
			resultat=res[0][i]*res[1][a]
			if resultat>prew:
				prew=resultat
				prewI=res[0][i]
				prewA=res[1][a]
			print(resultat,'{', prew,'}',end='')
			print(' ',res[0][i],res[1][a])
	print (prew,'with',prewI,prewA)
	stopTime=t.clock()
	endTime=stopTime - startTime
	print('finished in ',round(endTime,2),'sec.')

def testin():#need to define des=[[],[],[]]
	startTime=t.clock()
	for i in range(len(des[0])):
		for a in range(len(des[1])):
			for b in range(len(des[2])):
				result=(des[0][i]+des[1][a])*des[2][b]
				print (result, end='')
				print ('=',(des[0][i],'+',des[1][a]),'*',des[2][b])
	stopTime=t.clock()
	endTime=stopTime - startTime
	print('finished in ',round(endTime,2),'sec.')


class test:
	__test1=""
	__test2=""
	def __init__(self,test1,test2):
		self.__test1=test1
		self.__test2=test2
	def set_test1(self,name):
		self.__name=name
	def get_test1(self):
		return self.__name

class user2:
	__name=""

	def __init__(self,name):
		self.__name=name
	def set_name(self,name):
		self.__name=name
	def get_name(self):
		return self.__name

class building:
	__number=""
	__street=""
	
	def __init__(self,number,street):
		self.__number=number
		self.__street=street
	def get_number(self):
		return self.__number
	def get_street(self):
		return self.__street
	def set_number(self,number):
		self.__number=number
	def set_street(self,street):
		self.__street=street

def update_cont():
	file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"r")
	content=file.read()
	file.close()
	return content

def clear_file():
	file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"w")
	file.write('')
	file.close()

def wtf(string):
	file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"a")
	file.write(string)
	file.write('\n')
	file.close()

def send_byte(dev,pack):
	if pack>255:pack=255
	print('pool',hex(int(dev/pool_size)),'dev#',hex((dev%pool_size)),hex(pack))
	print(bin(int(dev/pool_size)),bin(dev%pool_size),bin(pack))

#e=md5z('e')
#e=tableMake(e)

def tableMake(var):
	result=[]
	for i in range(len(var)):
		result.append(md5z(var[i]).upper())
	return result

def tablePrint(var):
	for i in range(len(var)):
		print(var[i])

def new_md5_from_table(var):
	temp=md5z(var)
	temp=tableMake(temp)
	pr=[]
	for i in range(32):
		v1=randint(0,31)
		v2=randint(0,31)
		pr.append(temp[v1][v2])
	temp=''.join(pr)
	return temp


#0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30


"""
for i in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
	q1=int(e[i],16)
	q2=int(e[i+1],16)
	print(text[q1][q2])

for i in range(len(text)):
	text[i]=text[i].split('\t')
for i in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
	print(int(e[i],16),int(e[i+1],16)

for i in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
	print(e[i],e[i+1])
"""
def crypt(md5_var):
	md5_var=md5z(md5_var)
	crypt=[]
	for i in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
		q1=int(md5_var[i],16)
		q2=int(md5_var[i+1],16)
		crypt.append(text[q1][q2])
	return ''.join(crypt)

def crypt32(md5_var):
	md5_var=h.sha256(c.encode(str(md5_var))).hexdigest()
	md5_var=str(md5_var)
	crypt=[]
	for i in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62):
		q1=int(md5_var[i],16)
		q2=int(md5_var[i+1],16)
		crypt.append(text[q1][q2])
	return ''.join(crypt)

def makeCrypt(q1,q2):
	file=open('c:\\Users\\Buuart\\Desktop\\file_for_test.txt',"a")
	for i in range(q1):
		for a in range(q2):
			c=a,i
			file.write(crypt(c))
			file.write('\n')
	file.close()

def new_user(name, pasw):
	if not md5z(name) in l: l[md5z(name)]=crypt(pasw)
	else: print("User is already exist, change name")
#inSessinon=[False,False]
def login():
	name=input("enter User Name: ")
	pasw=input("enter password: ")
	pass1=False
	pass2=False
	if md5z(name) in l: pass1=True
	if l.get(md5z(name))==crypt(pasw): pass2=True
	if pass1==True and pass2==True:print("loggin in")
	else: print("error while loggin in")

def find_in_ar(string,name):
	res=''
	for i in range(len(name)):
		if name[i]==string:res=i
	#res=str(res)
	return res

encode_ar=['0','1','2','3','4','5','6','7','8','9']
decode_ar=['4','8','1','0','5','9','3','6','7','2']
test_str_ar=[]

#lineS
#lineSR



test={'Picrtures':['jpeg','jpg','gif'],'vector':['ai','svg','pdf','eps']}

folders=['archives','docs','presentations','execs','ini_txt','vector','fonts','music','photoshop','pictures','video']
extens=[['7z','gz','rar','zip'],['doc','docx','txt','pdf'],['ppt','pptx'],['exe','apk'],['ini'],['ai','svg','eps'],['ttf','otf'],['mp3','wav','wave','ogg'],['psd','tiff'],['jpeg','jpg','gif','png'],['mov','avi','mpg','mpeg']]

def new_name(full_name):
	name=str(time_stamp()),str(full_name)
	name=''.join(name)
	return name

def dres(test):
	test1=test.split('.')
	test1=test1[(len(test1))-1]
	name=test[0:-1*(len(test1)+1)]
	for i in range(len(folders)):
		if test1 in extens[i]:
			#print(time_stamp(),name, folders[i],extens[i],test)
			print('from downloads to ', end='')
			print(os.path.join('c:\\downloads',folders[i],new_name(test)))
			break
	if i == len(folders)-1:
		print('from downloads to ', end='')
		print(os.path.join('c:\\downloads','others',new_name(test)))





def sorting(test):
	test1=test.split('.')
	test1=test1[(len(test1))-1]
	name=test[0:-1*(len(test1)+1)]
	for i in range(len(folders)):
		if test1 in extens[i]:
			#print(time_stamp(),name, folders[i],extens[i],test)
			#print('from downloads to ', end='')
			#print(os.path.join('c:\\downloads',folders[i],new_name(test)))
			sh.move(os.path.join('c:\\','test_download',test),os.path.join('c:\\downloads',folders[i],test))
			break
	if not test1 in extens[i]:
		#print('from downloads to ', end='')
		#print(os.path.join('c:\\downloads','others',new_name(test)))
		sh.move(os.path.join('c:\\','test_download',test),os.path.join('c:\\downloads','others',test))

def time_stamp():
	stamp=t.localtime()
	return('{}_{}_{}-{}:{}:{}_'. format(stamp[2],stamp[1],stamp[0],stamp[3],stamp[4],stamp[5]))

def mapping(x, minimal_input, maximal_input, minimal_output, maximal_output):
	"""remap value x in range of in&out"""
	return (x - minimal_input) * (maximal_output - minimal_output) / (maximal_input - minimal_input) + minimal_output

#for i in range(len(extens)):
#	for a in range(len(extens[i])):
#		print(folders[i],extens[i][a])

#test1=test.split('.')
#test[0:-1*(len(test1)+1)]

def active_sort():
	fililist=os.listdir('C:\\test_download')
	for i in range(len(fililist)):
		sorting(fililist[i])	



#АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&**(_+)~<>?"[]{}|\/.,№;:

#['№', 'ё', 'я', 'ю', 'э', 'ь', 'ы',' ', 'ъ', 'щ', 'ш', 'ч', 'ц', 'х', 'ф', 'у', 'т', 'с', 'р', 'п', 'о', 'н', 'м', 'л', 'к', 'й', 'и', 'з', 'ж', 'е', 'д', 'г', 'в', 'б', 'а', 'Я', 'Ю', 'Э', 'Ь', 'Ы', 'Ъ', 'Щ', 'Ш', 'Ч', 'Ц', 'Х', 'Ф', 'У', 'Т', 'С', 'Р', 'П', 'О', 'Н', 'М', 'Л', 'К', 'Й', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А', 'Ё', '~', '}', '|', '{', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '_', '^', ']', '\\', '[', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '@', '?', '>', '<', ';', ':', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '/', '.', ',', '+', '*', '*', ')', '(', '&', '%', '$', '#', '"', '!']

#['!', '"', '#', '$', '%', '&', '(', ')', '*', '*', '+', ',', '.', '/',' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'Ё', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё', '№']


