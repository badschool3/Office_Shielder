#필요 라이브러리 및 파일 호출
from tkinter import *
import tkinter.ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
import os
import time
import platform
from PIL import Image
import subprocess

pathvar = os.path.dirname( os.path.abspath( __file__ ) ).split('\\')[2]
os.system("taskkill /f /im cmd.exe")

def employee():
	os.system("taskkill /f /im cmd.exe")
	os.system("spst_employee.exe")
	os.system("taskkill /f /im cmd.exe")
	"""
	os.system("spst_employee.exe")
	os.system("taskkill /f /im spst_main.exe")
	"""

#데이터베이스 생성
if(platform.system()=='Windows'):
	pathvar = os.path.dirname( os.path.abspath( __file__ ) ).split('\\')[2]
	if os.path.isfile("C:/Users/"+ pathvar + "/Users.db"):
		print ("해당 파일이 있습니다. 데이터베이스를 불러옵니다.")
		conf = sqlite3.connect("C:/Users/"+ pathvar + "/Users.db")
		cursor = conf.cursor()
	else:
		print ("그런 이름의 파일은 없습니다. 새 데이터베이스를 생성합니다.")
		conf = sqlite3.connect("C:/Users/"+ pathvar + "/Users.db")
		cursor = conf.cursor() 
		cursor.execute('create table user_info(id, name, address)')
		cursor.execute('create table user_analysis(id, active_time, subject, emotion)')
		cursor = conf.cursor()
elif(platform.system()=='Darwin'):
	file = "Users.db"
	if os.path.isfile(file):
		print ("해당 파일이 있습니다. 데이터베이스를 불러옵니다.")
		conf = sqlite3.connect(file)
		cursor = conf.cursor()
	else:
		print ("그런 이름의 파일은 없습니다. 새 데이터베이스를 생성합니다.")
		conf = sqlite3.connect(file)
		cursor = conf.cursor()
		cursor.execute('create table user_info(id, name, address)')
		cursor.execute('create table user_analysis(id, active_time, subject, emotion)')
		cursor = conf.cursor()

userset = pd.read_sql("SELECT * FROM user_info",conf)
userlist = list(userset["id"])
cols = list(userset)
print (userset)

ids = userset["id"].tolist()
nas = userset["name"].tolist()
ads = userset["address"].tolist()

lists = []
for x in range(len(ids)):
	lists.append(tuple(ids[x]))

#실수 종료 방지
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"): 
        root.destroy()

#메인 화면
def center_window(width=300, height=200):
	screen_width = root.winfo_screenwidth() 	# get screen width and height
	screen_height = root.winfo_screenheight()

	x = (screen_width/2) - (width/2) 			# calculate position x and y coordinates
	y = (screen_height/2) - (height/2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = Tk()
root.resizable(0, 0)
x0, y0 = 820, 490
center_window(x0, y0)
root.title("메인 화면")
try:
	root.iconbitmap(default=r'C:/Users/' + pathvar + '/Downloads/SPST_S-master/project_icon.ico')
except:
	root.iconbitmap(default=r'project_icon.ico')
image = Image.open("logo.gif") 					#창 크기에 맞게 이미지 크기 조절
resize_image = image.resize((x0,y0))
resize_image.save('logo.gif')
images = PhotoImage(file = "logo.gif") 			#이미지 배치
lbl = Label(root, image=images)
lbl.pack(side="bottom",fill="both",expand="True")

btn1 = Button(root, text="사원관리",command=employee) 	#command=employee_manage
btn1.place(x=700, y = 400)

btn = Button(root, text="훈련관리")						#command=analysis_manage
btn.place(x=700, y = 440)

Button(root, text="종   료",command=on_closing).place(x=30, y = 440) #

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()