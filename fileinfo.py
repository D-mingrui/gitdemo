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
