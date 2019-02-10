from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
a=10
def bill():
    #tkinter.Tk.__init__(self)
    top=Tk()
    top.configure(background="#757cc4")
    top.title("Bill")
    top.geometry('1920x1000+0+0')
    top.frameb1=Frame(width=800,height=9500,bg="#e2d62f",bd=12,relief=RAISED)
    top.frameb1.pack(side=LEFT)
    '''top.entryb=Entry(font=('Times New Roman',10,'bold'),bd=3,bg="WHITE",width=50)
    top.entryb.place(x=50,y=50)'''
    top.billtxt=Text(top.frameb1,width=100,height=48,bg="WHITE",bd=8,font=('Times New Roman',10,'bold'))
    top.billtxt.place(x=20,y=20)
    top.bind('<Return>')
    top.mainloop()
bill()
    
    
