import sqlite3
import platform
from tkinter import *
import tkinter.ttk
from tkinter import messagebox
import pandas as pd
import os

#데이터베이스 로딩
if(platform.system()=='Windows'):
	pathvar = os.path.dirname( os.path.abspath( __file__ ) ).split('\\')[2]
	conf = sqlite3.connect("C:/Users/"+ pathvar + "/Users.db")
	cursor = conf.cursor()
elif(platform.system()=='Darwin'):
	file = "Users.db"
	conf = sqlite3.connect(file)
	cursor = conf.cursor()

def inter(ids):
	f = open("analysid.txt","w")
	data = ids
	f.write(data)
	f.close()

	#os.system("spst_analy_crawl.exe")

def my_table(self):
	treeview.tag_configure("tag2", background="red")

#훈련 관리
class MyFrames(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=True)

        #id
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lblId = Label(frame1, text ="분석할 아이디",width=10)
        lblId.pack(side=LEFT,padx=10,pady=10)
        entryId = Entry(frame1)
        entryId.pack(fill=X, padx=10, expand=True)

        #훈련
        frame2 = Frame(self)
        frame2.pack(fill=X)
        btanaly = Button(frame2, text="훈련 시작",command=lambda:inter(entryId.get()))
        btanaly.pack(side=RIGHT, padx=10,pady=10)


#사원 관리 메인
global x0, y0,hides
analys= Tk()
analys.resizable(0, 0)
analys.title("훈련관리")
x0, y0 = 820, 490
width3,height3 = x0+20,y0+30
screen3_wid = analys.winfo_screenwidth()
screen3_hei = analys.winfo_screenheight()
x3 = ((screen3_wid/2) - (width3/2))
y3 = (screen3_hei/2) - (height3/2)
analys.geometry('%dx%d+%d+%d' % (width3, height3, x3, y3))

userlist = pd.read_sql("SELECT * FROM user_info",conf)
userlist = list(userlist["id"])

userset = pd.read_sql("SELECT * FROM user_analysis",conf)
cols = list(userset)

ids = userset["id"].tolist()
ats = userset["active_time"].tolist()
sus = userset["subject"].tolist()
ems = userset["emotion"].tolist()

e_lbl = Label(analys,text="훈련 관리 테이블")
e_lbl.pack()
e_but = Label(analys,text="My_Table")
e_but.pack()

treeview=tkinter.ttk.Treeview(analys, columns=["one", "two","three","four"])
treeview.column("#0", width=50)
treeview.heading("#0",text="num") #index
treeview.column("one", width=70,anchor="w")
treeview.heading("one", text=cols[0],anchor="center") #id
treeview.column("two", width=50,anchor="w")
treeview.heading("two", text=cols[1],anchor="center") #active time
treeview.column("three", width=100,anchor="w")
treeview.heading("three", text=cols[2],anchor="center") #subject
treeview.column("four", width=100, anchor="w")
treeview.heading("four", text=cols[3], anchor="center") #emotion

treelists = []
for x in range(len(ids)):
    treelist = []
    treelist.append(ids[x])
    treelist.append(ats[x])
    treelist.append(sus[x])
    treelist.append(ems[x])
    treelists.append(tuple(treelist))

for i in range(len(treelists)):
    treeview.insert('', 'end', text=i, values=treelists[i], iid=str(i)+"번")

treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=my_table)
treeview.pack(side=TOP,fill=X)

try:
	analys.iconbitmap(default='C:/Users/' + pathvar + '/Downloads/SPST_S-master/project_icon.ico')
except:
	analys.iconbitmap(default='project_icon.ico')

app = MyFrames(analys)
analys.mainloop()
