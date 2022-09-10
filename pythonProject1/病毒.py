# coding:utf-8
'''
pip install pyinstaller
'''
import  tkinter as tk #导入tkinter库并重命名tk
import threading #导入多线程库
import random #导入随机数生成库

def dow():#定义一个函数
    t = tk.Tk() #初始化一个窗口
    width = t.winfo_screenwidth()
    height = t.winfo_screenheight()
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    t.title("送给某个师师")
    t.geometry('400x200'+'+' + str(a) + '+' + str(b))
    tk.Label(t,
             text="兄弟，兄弟，嫁给俺师师嘛~，跟着俺师师，吃香的喝辣的",
             bg="pink",
             font=("楷体",17),
             width=30,
             height=8,
             wraplength="320",
             justify="left",
             ).pack()
    t.mainloop()
    threads = []
    for i in range(10):
        t = threading.Thread(target=dow)
        threads.append(t)
        threads[i].start()
dow()


