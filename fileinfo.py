# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:48:13 2019

@author: dmr
"""
    
teacher={'admin':{'name':'dmr','pwd':'123'}}
student={'xm':'100','mg':'99'}
import tkinter.messagebox
import tkinter.simpledialog
import tkinter as tk
window=tk.Tk()
window.title('学生管理系统登录界面')
window.geometry('420x200')
tk.Label(window,text='用户名:').place(x=107,y=50)
var_name=tk.StringVar()
e1=tk.Entry(window,textvariable=var_name)#用户名输入框
e1.place(x=160,y=50)
var_pwd=tk.StringVar()
tk.Label(window,text='密码:').place(x=120,y=90)
e2=tk.Entry(window,textvariable=var_pwd,show='*')#密码输入框
e2.place(x=160,y=90)
#登陆按钮程序
def usr_quit():
    window.destroy()
def usr_login():
    tname=e1.get()
    tpwd=e2.get()
    if teacher['admin']=={'name':tname,'pwd':tpwd}:
        tkinter.messagebox.showinfo(title='登录成功',message='欢迎，教师Admin')
        window.destroy()
   
        def qt():
            w2.destroy()
        def search():
            for i in student.keys():
                a=student[i]
                print('姓名:'+' '+i+'  '+'成绩:'+' '+a)
        def add():
            n0=tkinter.simpledialog.askstring('提示', '请输入学生姓名',initialvalue='')
            if n0 in list(student.keys()):
                tkinter.messagebox.showwarning(title='错误',message='该学生已存在')
            else:
                mark=tkinter.simpledialog.askstring('提示','请输入学生成绩',initialvalue='')
                if float(mark)>=0 and float(mark)<=100:
                    student[n0]=mark
                else:
                    tkinter.messagebox.showwarning(title='提示',message='成绩不在范围内')
        w2=tk.Tk()
        w2.geometry('300x300')
        w2.title('学生管理系统')
        tk.Button(w2,text='添加成绩',command=add).place(x=120,y=50)
        tk.Button(w2,text='查看成绩',command=search).place(x=120,y=120)
        tk.Button(w2,text='退出系统',command=qt).place(x=120,y=190)
    
    else:
       tkinter.messagebox.showinfo(title='登录失败',message='用户名或密码错误')
tk.Button(window,text='登录',command=usr_login).place(x=150,y=130)
tk.Button(window,text='退出',command=usr_quit).place(x=240,y=130)
window.mainloop()

infile=open('article.txt','r')


#我是第二个开发者
#第一个开发者都把代码复制完了
#我就写几行注释吧
#要不没我啥事了
#哈哈哈哈哈
##
