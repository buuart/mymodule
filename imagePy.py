#
#  ██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ██████╗ ██╗   ██╗
#  ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗╚██╗ ██╔╝
#  ██║██╔████╔██║███████║██║  ███╗█████╗      ██████╔╝ ╚████╔╝ 
#  ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██╔═══╝   ╚██╔╝  
#  ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ██║        ██║   
#  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝        ╚═╝  
#  by buuart

from PIL import Image, ImageDraw, ImageFilter, ImageOps,ImageEnhance
import numpy as np
from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip

import os
print('from moviepy.editor import ImageSequenceClip','import os','from moviepy.editor import VideoFileClip','numpy as np','from PIL import Image, ImageDraw, ImageFilter, ImageOps,ImageEnhance',sep='\n')
e=open('module imagePy.txt','r', encoding="utf-8")
f=e.read()
e.close()
f=f.split('\n')
del e
for i in range(len(f)):
	print(f[i])
del f
def imageBW(inputArray,output_file):# for convertin to gif
	h=np.size(inputArray,axis=0)
	v=np.size(inputArray,axis=1)
	img=Image.new('L',(v,h),(255))
	draw = ImageDraw.Draw(img)
	for x in range(h):
		for y in range(v):
			if(int(inputArray[x][y])>255):
				color=255
			else:
				color=int(inputArray[x][y])
			draw.point((y,x),(color))
	img.save(output_file, "bmp")
	del draw

def imagePrew(name):
	img=Image.open(name)
	img=ImageOps.grayscale(img)
	e=img.load()
	for i in range(img.size[1]):
		for a in range(img.size[0]):
			if(e[a,i]==255):
				print('██',end='')
			else:
				print('  ',end='')
		print('')


def factorLess(array,F):
	h=np.size(array,axis=0)
	v=np.size(array,axis=1)
	array=array.flatten()
	for i in range(len(array)):
		if(array[i]<F):
			array[i]=0
	array=array.reshape(h,v)
	return array

def factorMore(array,F):
	h=np.size(array,axis=0)
	v=np.size(array,axis=1)
	array=array.flatten()
	for i in range(len(array)):
		if(array[i]>F):
			array[i]=255
	array=array.reshape(h,v)
	return array

def maps(x,  in_min,  in_max,  out_min,  out_max): # map wiring
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def gray(img):
	img=ImageOps.grayscale(img)
	return img

def invert(img):
	img=ImageOps.invert(img)
	return img

def colorize(img,black,white): #tuple
	ImageOps.colorize(img,black,white)
	return img

def prepIm(pictute):
	img=Image.open(pictute)
	pix=img.load()
	width=img.size[0]
	heigth=img.size[1]
	b=[]
	for w in range(width):
		for h in range(heigth):
			b.append(pix[w,h])
	b=np.array(b).reshape(width,heigth)
	img.close()
	del pix
	return b

def byteFromImg2(fileName): 
	# импортирует чб изображение, переводит его в серого градации для дальнейшей обработки
	# принимает значение в виде строки
	# родительская функия FelixScreen
	img=Image.open(fileName)
	img=ImageOps.flip(img)
	img=ImageOps.grayscale(img)
	e=img.load()
	imgW=img.size[0]
	imgH=img.size[1]
	q=[]
	for a in range(imgW):
		for b in range(imgH):
			q.append(e[a,b])
	q=np.array(q).reshape(imgW,imgH)
	img.close()
	q=q.swapaxes(0,1)
	return q

def byteFromImg(fileName): 
	# импортирует чб изображение, переводит его в серого градации для дальнейшей обработки
	# принимает значение в виде строки
	# родительская функия FelixScreen
	img=Image.open(fileName)
	img=ImageOps.grayscale(img)
	e=img.load()
	imgW=img.size[0]
	imgH=img.size[1]
	q=[]
	for a in range(imgW):
		for b in range(imgH):
			q.append(e[a,b])
	q=np.array(q).reshape(imgW,imgH)
	img.close()
	q=q.swapaxes(0,1)
	return q

def arrayTo595(array):
	# byte code for arduino
	# выводит значения для сдвиговых регистров ардуино
	r=[]
	q=0
	dim1=np.size(array,0)
	dim2=np.size(array,1)
	for i in range(dim1):
		q=0
		for b in range(dim2):
			q=(q<<1)|array[i][b]
		r.append(q)
	return r

def HexToBin(array,f=0):
	# переводит значения 0-255 в 0-1
	# необходимо для формирования байткода и визуализации
	for i in range(len(array)):
		for b in range(len(array[0])):
				if(array[i,b]>f):
					array[i,b]=1
				else:
					array[i,b]=0
	return array

def prePrint(array):
	# визуализация графики
	for i in range(len(array)):
		for b in range(len(array[0])):
				if(array[i,b]==1):
					print('██',end='')
				else:
					print('  ',end='')
		print('')

def arrayInvert(array):
	# инвертирование массива
	# указывается в родительской функции
	for i in range(len(array)):
		for b in range(len(array[0])):
				if(array[i,b]>0):
					array[i,b]=0
				else:
					array[i,b]=1
	return array

def FelixScreen(name,porog=0,invert=0,prew=0,showByte=1):
	# родительская функция
	# принимает имя файла в виде строки
	# остальные параметры по умолчанию:
	# инвертирование - invert - заменяет 0 на 1 и наоборот
	# prew - вывод предпросмотра в поток
	# showByte - показать байткод
	# porog пороговое значение грэйскейла для определения чб
	a=byteFromImg2(name)
	a=HexToBin(a,porog)
	if(invert==1): # применение параметра
		a=arrayInvert(a)
	b=a
	b=b.swapaxes(0,1)
	b=arrayTo595(b)
	if (showByte==1): # применение параметра
		print(b)
	if(prew==1): # применение параметра
		prePrint(a)

def stripVideo(fileName,startSec,stopSec,resolutionSec):
	fileName=str(fileName)
	clip=VideoFileClip(fileName).subclip(startSec,stopSec)
	sec=stopSec-startSec
	print('will create', str(sec*resolutionSec),'files')
	for i in range(sec*resolutionSec):
		name1='for images\\frame'+str(i)+'.bmp'
		clip.save_frame(name1, t=i/resolutionSec)
		print('[#]',end='')
	del clip
	print('\n','stripVideo: [Done]',sep='')

def totalResize():
	import os
	e=os.listdir('for images')#получаем список файлов директории
	for i in range(len(e)):#пережимаем всё под наше разрешение
		img=Image.open('for images\\'+e[i])
		img=img.resize((16,8))
		img.save('for images\\'+e[i])
		img.close()
	print('totalResize: [Done]')

def clearTempDir():
	e=os.listdir('for images')#получаем список файлов директории
	for i in range(len(e)):
		os.remove('for images\\'+str(e[i]))
	print("temp dir cleared, ", str(len(e))," files deleted", sep='')

def FS(p=128,inv=0,prew=1,show=1):
	e=os.listdir('for images')
	print(len(e),' files in dir')
	for i in range(len(e)):
		name='for images\\'+str(e[i])
		FelixScreen(name,p,inv,prew,show)

def refactoringGif(Fpss,invert):
	e=os.listdir('for images')
	invert=int(invert)
	for i in range(len(e)):
		e[i]='for images\\'+e[i]
	for i in range(len(e)):
		a=byteFromImg(e[i])
		img=Image.new('L',(16,8),0)
		r=img.load()
		if(invert==0):
			HexToHex(a,95)
		else:
			HexToHexInvert(a,95)
		imageBW(a,e[i])

	clipG=ImageSequenceClip(e,fps=Fpss)
	clipG.write_gif('for images\\test.gif')
	print('gif prewiev: [Done]')

def HexToHex(array,f=0):
	# переводит значения 0...255 в 0<->255
	# необходимо для формирования байткода и визуализации
	for i in range(len(array)):
		for b in range(len(array[0])):
				if(array[i,b]>f):
					array[i,b]=255
				else:
					array[i,b]=0


def HexToHexInvert(array,f=0):
	# переводит значения 0...255 в 0<->255
	# необходимо для формирования байткода и визуализации
	for i in range(len(array)):
		for b in range(len(array[0])):
				if(array[i,b]>f):
					array[i,b]=0
				else:
					array[i,b]=255

def newVideo():
	print('дериктория будет очищена')
	print('скопируйте нужные файлы, если они есть в конечной директории')
	ans=input('Нажмите ENTER для продолжения')
	del ans
	clearTempDir()
	file=input('расположение и имя файла: ')
	file=str(file)
	st=input('начать с секунды: ')
	st=int(st)
	fn=input('закончить на секунде: ')
	fn=int(fn)
	res=input('кадров в секунду: ')
	res=int(res)
	stripVideo(file,st,fn,res)
	totalResize()
	p=input('пороговое значение: ')
	p=int(p)
	inv=input('инверсия (0-нет, 1-да): ')
	inv=int(inv)
	pr=input('показывать превью (0-нет, 1-да): ')
	pr=int(pr)
	sh=input('показывать байты (0-нет, 1-да): ')
	sh=int(sh)
	FS(p,inv,pr,sh)
	refactoringGif(res,inv)
	print('gif превью создана в директории с картинками')
