from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image,ImageTk
from twilio.rest import Client
import pymysql
db=pymysql.connect(host="localhost",user="root",password="yash",db="project")
'''class SampleApp1():
    #def __init__():
        #tkinter.Tk.__init__()
    self.configure(background="#757cc4")
    self.title("Customer Information")
    self.geometry('1920x1080')'''
class SampleApp(tkinter.Tk):
    def menu(self):
        tkinter.Tk.__init__(self)
        self.configure(background="#757cc4")
        self.title("Menu")
        self.geometry('1920x1000+0+0')
        #frame
        self.frame1=Frame(self,width=1900,height=100,bg="#e2d62f",bd=12,relief=RAISED)
        self.frame1.pack(side=TOP)

        self.frametitle=Label(self,font=('arial',40,'bold'),text="MENU",bg="#e2d62f")
        self.frametitle.place(x=700,y=10)
        

        self.bframe=Frame(self,width=1900,height=700,bg="#62e0da",bd=12,relief=RAISED)
        self.bframe.pack(side=BOTTOM)
        
        self.f1=Frame(self.bframe,width=500,height=680,bd=12,relief=RAISED)
        self.f1.pack(side=LEFT)
        
        self.f2=Frame(self.bframe,width=500,height=680,bd=12,relief=RAISED)
        self.f2.pack(side=LEFT)
        self.f2top=Frame(self.f2,width=500,height=350,bd=4,relief=RAISED)
        self.f2top.pack(side=TOP)
        self.f2bottom=Frame(self.f2,width=500,height=300,bd=4,relief=RAISED)
        self.f2bottom.pack(side=BOTTOM)
        
        self.f3=Frame(self.bframe,width=500,height=680,bd=12,relief=RAISED)
        self.f3.pack(side=RIGHT)

        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()
        self.var7=IntVar()
        self.var8=IntVar()
        self.var9=IntVar()
        self.var10=IntVar()
        self.var11=IntVar()
        self.var12=IntVar()
        self.var13=IntVar()
        self.var14=IntVar()
        self.var15=IntVar()
        self.var16=IntVar()
        self.var17=IntVar()
        self.var18=IntVar()
        self.var19=IntVar()
        self.var20=IntVar()
        self.var21=IntVar()
        self.var22=IntVar()
        self.var23=IntVar()

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)
        self.var17.set(0)
        self.var18.set(0)
        self.var19.set(0)
        self.var20.set(0)
        self.var21.set(0)
        self.var22.set(0)
        self.var23.set(0)

        self.Pizza1=Checkbutton(self.f1,text="Pizza1",variable=self.var1,onvalue=1,offvalue=0,font=('arial',18,'bold')).place(x=20,y=5)
        





        
    def putData(self,db):
        print("In")
        name1=self.nameentry.get()
        phoneno=self.phoneno.get()
        mailid=self.mailentry.get()
        add=self.addentry.get()
        try:
            p=db.cursor()
            with db.cursor()as p:
                t=("INSERT INTO detail VALUES(%s,%s,%s,%s)")
                if(p.execute(t,(name1,phoneno,mailid,add))):
                    db.commit()
                    tkinter.messagebox.showinfo("Submit Prompt", "Submission Successful\nPress OK for MENU")
                    self.menu()
                else:
                    self.destroy()
        finally:
            db.close()   
        
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.configure(background="#757cc4")
        self.title("Customer Information")
        self.geometry('1920x1000+0+0')
        self.frame=Frame(self,width=1480,height=675,bg="#e2d62f",bd=10,relief=SUNKEN).place(x=30,y=110)
        #Header
        self.label1=Label(self,font=('Times New Roman',50,'bold'),text="Customer Details",bd=10,fg="#a54a5f",relief=GROOVE).place(x=500,y=10)
        
        #Name
        self.name=Label(self,font=('Times New Roman',30,'bold'),text="Name:",bd=5,bg="#e2d62f",relief=GROOVE)
        self.name.place(x=50,y=130)
        self.name1=StringVar()
        self.nameentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.name1,width=30,bd=9,bg="WHITE")
        self.nameentry.place(x=350,y=130)
        
        #PhoneNo
        self.phoneno=Label(self,font=('Times New Roman',30,'bold'),text="Phone Number:",bd=5,bg="#e2d62f",relief=GROOVE).place(x=50,y=250)
        self.phoneno=StringVar()
        self.phentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.phoneno,width=30,bd=9,bg="WHITE")
        self.phentry.place(x=350,y=250)

        #mail
        self.mail=Label(self,font=('Times New Roman',30,'bold'),text="Email:",bd=5,bg="#e2d62f",relief=GROOVE).place(x=50,y=400)
        self.mailid=StringVar()
        self.mailentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.mailid,width=30,bd=9,bg="WHITE")
        self.mailentry.place(x=350,y=400)

        #address
        self.address=Label(self,font=('Times New Roman',30,'bold'),text="Address:",bd=5,bg="#e2d62f",relief=GROOVE).place(x=50,y=500)
        self.add=StringVar()
        self.addentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.add,width=60,bd=9,bg="WHITE")
        self.addentry.place(x=350,y=500)

        #Submit Button
        self.B=Button(self,font=('Times New Roman',40,'bold'),text='Submit',relief=GROOVE,command=lambda:self.putData(db))
        self.B.place(x=550,y=600)

        '''#Menu Button
        self.B1=Button(self,font=('Times New Roman',40,'bold'),text='Menu',relief=GROOVE,command=self.menu)
        self.B1.place(x=800,y=600)'''
        
        self.bind('<Return>')


def getData(parent):
    default=parent.top.E1.get()
    default1=parent.top.E2.get()
    try:
        c=db.cursor()
        with db.cursor()as c:
            c.execute("SELECT * FROM login")
            r=c.fetchone()
        if(r[0]==default and r[1]==default1):
            tkinter.messagebox.showinfo("Login Prompt", "Login Successful\nPress OK for DETAILS")
            #s=SampleApp()
        else:
            parent.top.destroy()
        s=SampleApp()
    finally:
        print("")
        #db.close()    
def GUI(self):
    self.top=Tk()
    self.top.configure(background="#f73d3d"+"#e2d62f")
    self.top.title("Welcome")
    self.top.geometry('1920x1000+0+0')
    self.top.frame=Frame(self.top,width=1900,height=100,bg="#e2d62f",bd=10,relief=SUNKEN)
    self.top.frame.pack(side=TOP)
    self.top.label1=Label(self.top,font=('Times New Roman',50,'bold'),text="The Pizzateria",fg="#a54a5f",bg="#e2d62f",relief=RAISED)
    self.top.label1.place(x=560,y=10)
    self.top.frame1=Frame(self.top,width=1000,height=700,bg="#17edd0",bd=5,relief=RAISED)
    self.top.frame1.pack(side=BOTTOM)
    self.top.label2=Label(self.top,font=('Times New Roman',50,'bold'),text="LOGIN",fg="BLACK",bg="#17edd0").place(x=650,y=110)
    self.top.label3=Label(self.top,font=('Times New Roman',30,'bold'),text="User Name:",fg="BLACK",bg="#17edd0").place(x=400,y=375)
    self.top.label4=Label(self.top,font=('Times New Roman',30,'bold',),text="Password:",fg="BLACK",bg="#17edd0").place(x=400,y=475)
    self.default=StringVar()
    self.top.E1=Entry(self.top,font=('Times New Roman',20,'bold'),textvariable=self.default,bd=3,bg="WHITE")
    self.top.E1.place(x=650,y=387)
    self.default1=StringVar()
    self.top.E2=Entry(self.top,font=('Times New Roman',20,'bold'),textvariable=self.default1,bd=3,bg="WHITE",show='*')
    self.top.E2.place(x=650,y=487)
    self.top.B=Button(self.top,font=('Times New Roman',20,'bold'),text='Login',relief=GROOVE,command=lambda:getData(self))
    self.top.B.place(x=750,y=587)
    self.top.frame1.pack(side=BOTTOM)
    self.top.bind('<Return>')
    self.top.mainloop()
GUI(db)
