import android
import os
import time as t
import random as r
import shutil
droid = android.Android()
reset_time=[4,0]
curiculum=[]
root_path='c:/Users/Buuart/Desktop/test_tablet'
koto_path='c:/Users/Buuart/Desktop/test_tablet/koto'
basement_root_path='//192.168.0.222/Basement/Документы/Голос Ядра/anouncerSound'
basement_koto_path='//192.168.0.222/Basement/Документы/Голос Ядра/anouncerSound/koto'

def rename(input_string_value):
	original_file_name=input_string_value
	result_file_name=original_file_name.split('_')
	result_file_name[2]=result_file_name[2][:-4]
	result_file_name[0]=int(result_file_name[0])
	result_file_name[1]=int(result_file_name[1])
	result_file_name[2]=result_file_name[2][1:-1]
	result_file_name[2]=result_file_name[2].split(',')
	for i in range(len(result_file_name[2])):
		result_file_name[2][i]=int(result_file_name[2][i])
	result_file_name.append(0)
	result_file_name.append(original_file_name)
	return(result_file_name)

def update_curiculum():
	e=os.listdir(root_path)
	e.remove('koto')
	global curiculum
	curiculum=[]
	for i in range(len(e)):
		curiculum.append(rename(e[i]))
	curiculum.sort()

def anouncer_update():
	main_upd=0
	koto_upd=0
	anouncer_sound_array=os.listdir(basement_root_path)
	anouncer_sound_array.remove('koto')
	koto_sound_array=os.listdir(basement_koto_path)
	for i in range(len(anouncer_sound_array)):
		if (anouncer_sound_array[i][-3:]=='txt'):
			#del txt
			txt_name=basement_root_path+'/'+anouncer_sound_array[i]
			os.remove(txt_name)
			del txt_name
			del anouncer_sound_array[i]
			#clear
			local_anouncer_array=os.listdir(root_path)
			local_anouncer_array.remove('koto')
			for i in range(len(local_anouncer_array)):
				file_name=root_path+'/'+local_anouncer_array[i]
				os.remove(file_name)
			#relocation
			track_list_array=os.listdir(basement_root_path)
			track_list_array.remove('koto')
			for i in range(len(track_list_array)):
				name=basement_root_path+'/'+track_list_array[i]
				res=root_path+'/'+track_list_array[i]
				shutil.copyfile(name,res)
			main_upd=1
	for i in range(len(koto_sound_array)):# koto update
		if (koto_sound_array[i][-3:]=='txt'):
			# del txt
			txt_name=basement_koto_path+'/'+koto_sound_array[i]
			os.remove(txt_name)
			del koto_sound_array[i]
			#clear
			local_koto_array=os.listdir(koto_path)
			for i in range(len(local_koto_array)):
				file_name=koto_path+'/'+local_koto_array[i]
				os.remove(file_name)
			#relocation
			track_list_array=os.listdir(basement_koto_path)
			for i in range(len(track_list_array)):
				name=basement_koto_path+'/'+track_list_array[i]
				res=koto_path+'/'+track_list_array[i]
				shutil.copy(name,res)
			koto_upd=1
	if (main_upd==0):
		print('main V',end='')
	else:
		print('main X',end='')
	if (koto_upd==0):
		print(' - koto V')
	else:
		print(' - koto X')

def test():
	print('должен был быть звук кото')

def play(n):
	n='storage/sdcard0/anouncerSound/'+n
	droid.mediaPlay(n)

def koto():
	koto_list=os.listdir('storage/sdcard0/anouncerSound/koto')
	koto_list_len=len(koto_list)
	for i in range(koto_list_len):
		koto_list[i]='/storage/sdcard0/anouncerSound/koto/'+koto_list[i]
		track_number=r.randint(0,koto_list_len-1)
		droid.mediaPlay(koto_list[track_number])

def announcer(h,m,d):
	global curiculum
	h=int(h)
	m=int(m)
	d=int(d)
	for i in range(len(curiculum)):
		if(h==curiculum[i][0] and m==curiculum[i][1] and curiculum[i][3]==0):
				if (d not in curiculum[i][2]):
					curiculum[i][3]=1
				if (d in curiculum[i][2]):
					koto()
					t.sleep(3)
					play(curiculum[i][4])
					curiculum[i][3]=1
					print('sample',h,m,'on w_day_number',d,'just played')

	print(h,m)

def sound_sample_reload(h,m):
	h=int(h)
	m=int(m)
	if(h==reset_time[0] and m==reset_time[1]):
		for i in range(len(curiculum)):
			curiculum[i][3]=0
		print('flags cleared')
koto()
koto()
koto()
test()
print('Concrete Jungle announcer automate')
print('v0.2c')
print('voice_ready')
print('Do not lockScreen')
print('start at:',t.localtime()[3],'h',t.localtime()[4],'m')
while(1):
	announcer(t.localtime()[3],t.localtime()[4],t.localtime()[6])
	sound_sample_reload(t.localtime()[3],t.localtime()[4])
#	print(t.localtime()[3],t.localtime()[4])
	print('.',end='')
	anouncer_update()
	t.sleep(20)