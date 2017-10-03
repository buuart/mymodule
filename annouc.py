#!/usr/bin/env python
import time as t
import winsound
import random as r

curiculum=[[8, 40, 1, 0, 0], [8, 45, 1, 0, 1], [8, 55, None, 0, 2], [9, 0, None, 0, 3], [9, 15, None, 0, 4], [10, 0, None, 0, 5], [10, 55, None, 0, 6], [11, 0, None, 0, 7], [11, 15, None, 0, 8], [12, 0, None, 0, 9], [12, 55, None, 0, 10], [13, 0, None, 0, 11], [13, 45, None, 0, 12], [14, 0, None, 0, 13], [15, 0, None, 0, 14], [15, 25, None, 0, 15], [15, 30, None, 0, 16], [15, 45, None, 0, 17], [18, 15, None, 0, 18], [18, 25, None, 0, 19], [18, 30, None, 0, 20], [19, 0, None, 0, 21], [20, 0, None, 0, 22], [21, 0, None, 0, 23], [22, 0, None, 0, 24], [23, 0, None, 0, 25]]

trackList=['announcer sounds\\Announcer_mp_hub_return01_ru.wav', 'announcer sounds\\Announcer_prehub46_ru.wav', 'announcer sounds\\Fact_core_fact06_ru.wav', 'announcer sounds\\Fact_core_fact11_ru.wav', 'announcer sounds\\Fact_core_fact15_ru.wav', 'announcer sounds\\Fact_core_fact25_ru.wav', 'announcer sounds\\Fact_core_fact32_ru.wav', 'announcer sounds\\Fact_core_fact38_ru.wav', 'announcer sounds\\Fact_core_fact50_ru.wav', 'announcer sounds\\Fact_core_fact61_ru.wav', 'announcer sounds\\Fact_core_fact63_ru.wav', 'announcer sounds\\glados.wav']

trackList
['\\storage\\sdcard0\\anouncerSound\\phrase0.wav', '\\storage\\sdcard0\\anouncerSound\\phrase1.wav', '\\storage\\sdcard0\\anouncerSound\\phrase2.wav', '\\storage\\sdcard0\\anouncerSound\\phrase3.wav', '\\storage\\sdcard0\\anouncerSound\\phrase4.wav', '\\storage\\sdcard0\\anouncerSound\\phrase5.wav', '\\storage\\sdcard0\\anouncerSound\\phrase6.wav', '\\storage\\sdcard0\\anouncerSound\\phrase7.wav', '\\storage\\sdcard0\\anouncerSound\\phrase8.wav', '\\storage\\sdcard0\\anouncerSound\\phrase9.wav', '\\storage\\sdcard0\\anouncerSound\\phrase10.wav', '\\storage\\sdcard0\\anouncerSound\\phrase11.wav', '\\storage\\sdcard0\\anouncerSound\\phrase12.wav', '\\storage\\sdcard0\\anouncerSound\\phrase13.wav', '\\storage\\sdcard0\\anouncerSound\\phrase14.wav', '\\storage\\sdcard0\\anouncerSound\\phrase15.wav', '\\storage\\sdcard0\\anouncerSound\\phrase16.wav', '\\storage\\sdcard0\\anouncerSound\\phrase17.wav', '\\storage\\sdcard0\\anouncerSound\\phrase18.wav', '\\storage\\sdcard0\\anouncerSound\\phrase19.wav', '\\storage\\sdcard0\\anouncerSound\\phrase20.wav', '\\storage\\sdcard0\\anouncerSound\\phrase21.wav', '\\storage\\sdcard0\\anouncerSound\\phrase22.wav', '\\storage\\sdcard0\\anouncerSound\\phrase23.wav', '\\storage\\sdcard0\\anouncerSound\\phrase24.wav', '\\storage\\sdcard0\\anouncerSound\\phrase25.wav']
resT=[4,0]

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
					winsound.PlaySound(trackList[curiculum[i][4]],winsound.SND_FILENAME)
					curiculum[i][3]=1
	print(h,m)


def aa(h,m):
	h=int(h)
	m=int(m)
	if(h==resT[0] and m==resT[1]):
		for i in range(len(curiculum)):
			curiculum[i][3]=0



while(1):
	announcer(t.localtime()[3],t.localtime()[4])
	aa(t.localtime()[3],t.localtime()[4])
	t.sleep(20)



8:40>4/8:45>4/8:55>6/9:00>1/9:00>6/9:15>6/10:00>7/10:55>6/11:00>1/11:00>6/11:15>6/12:00>7/12:55>6/13:00>6/13:00>1/13:45>6/14:00>7/15:00>7/15:25>6/15:30>6/15:45>6/16:00>1/17:00>1/18:00>1/18:15>6/18:25>6/18:30>6/19:00>7/20:00>7/21:00>7/22:00>7/23:00>7



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
					winsound.PlaySound(trackList[curiculum[i][4]],winsound.SND_FILENAME)
					curiculum[i][3]=1


for a in range(7):
	for b in range(8,24):
		for c in range(0,60,5):
			print(a,b,c)



