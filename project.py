from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import pymysql
db=pymysql.connect(host="localhost",user="root",password="yash",db="pizza_shop")
class SampleApp(tkinter.Tk):
    
    def menu(self):
        tkinter.Tk.__init__(self)
        self.configure(background="#757cc4")
        self.title("Menu")
        self.geometry('1920x1000+0+0')
       
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

        self.var27=StringVar()

       
        self.Pizza1=Label(self.f1,text="Farmhouse Pizza\t  ₹545".expandtabs(15),font=('arial',14,'bold'))
        self.Pizza1.place(x=20,y=5)
        self.Pizza1S=StringVar()
        self.Pizza1S.set(0)
        self.Pizza1E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza1S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza1E.place(x=350,y=10)

        self.Pizza2=Label(self.f1,text="Deluxe Veggie\t\t\t   ₹665".expandtabs(8),font=('arial',14,'bold'))
        self.Pizza2.place(x=20,y=75)
        self.Pizza2S=StringVar()
        self.Pizza2S.set(0)
        self.Pizza2E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza2S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza2E.place(x=350,y=80)

        self.Pizza3=Label(self.f1,text="Marhgerita\t             ₹455",font=('arial',14,'bold'),)
        self.Pizza3.place(x=20,y=145)        
        self.Pizza3S=StringVar()
        self.Pizza3S.set(0)
        self.Pizza3E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza3S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza3E.place(x=350,y=150)

        self.Pizza4=Label(self.f1,text="Cheese Blast\t             ₹570",font=('arial',14,'bold'))
        self.Pizza4.place(x=20,y=215)        
        self.Pizza4S=StringVar() 
        self.Pizza4S.set(0)
        self.Pizza4E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza4S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza4E.place(x=350,y=220)

        self.Pizza5=Label(self.f1,text="Vegetarian Dominator\t ₹350".expandtabs(9),font=('arial',14,'bold'))
        self.Pizza5.place(x=20,y=285)        
        self.Pizza5S=StringVar()
        self.Pizza5S.set(0)
        self.Pizza5E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza5S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza5E.place(x=350,y=290)

        self.Pizza6=Label(self.f1,text="Chef's Favourite\t             ₹550",font=('arial',14,'bold'))
        self.Pizza6.place(x=20,y=355)        
        self.Pizza6S=StringVar()
        self.Pizza6S.set(0)
        self.Pizza6E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza6S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza6E.place(x=350,y=360)

        self.Pizza7=Label(self.f1,text="Mother's Recipe\t             ₹475",font=('arial',14,'bold'))
        self.Pizza7.place(x=20,y=425)        
        self.Pizza7S=StringVar()
        self.Pizza7S.set(0)
        self.Pizza7E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza7S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza7E.place(x=350,y=430)

        self.Pizza8=Label(self.f1,text="Veg Garlic Bread\t             ₹75",font=('arial',14,'bold'))
        self.Pizza8.place(x=20,y=495)        
        self.Pizza8S=StringVar()
        self.Pizza8S.set(0)
        self.Pizza8E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza8S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza8E.place(x=350,y=500)

        self.Pizza9=Label(self.f1,text="Cheese Garlic Bread          ₹75",font=('arial',14,'bold'))
        self.Pizza9.place(x=20,y=560)        
        self.Pizza9S=StringVar()
        self.Pizza9S.set(0)
        self.Pizza9E=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.Pizza9S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza9E.place(x=350,y=560)

        self.Pizzatop=Label(self.f1,text="Extra Cheese                       ₹75",font=('arial',14,'bold'))
        self.Pizzatop.place(x=20,y=615)        
        self.PizzatopS=StringVar()
        self.PizzatopS.set(0)
        self.PizzatopE=Entry(self.f1,font=('Times New Roman',12,'bold'),textvariable=self.PizzatopS,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.PizzatopE.place(x=350,y=615)

       
        self.Drink1=Label(self.f2top,text="Coca Cola\t\t           ₹55".expandtabs(15),font=('arial',14,'bold'))
        self.Drink1.place(x=20,y=5)
        self.Drink1S=StringVar()
        self.Drink1S.set(0)
        self.Drink1E=Entry(self.f2top,font=('Times New Roman',12,'bold'),textvariable=self.Drink1S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Drink1E.place(x=350,y=10)

        self.Drink2=Label(self.f2top,text="Thumbs Up\t\t        ₹55".expandtabs(15),font=('arial',14,'bold'))
        self.Drink2.place(x=20,y=75)
        self.Drink2S=StringVar()
        self.Drink2S.set(0)
        self.Drink2E=Entry(self.f2top,font=('Times New Roman',12,'bold'),textvariable=self.Drink2S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Drink2E.place(x=350,y=80)

        self.Drink3=Label(self.f2top,text="Sprite\t   \t               ₹55",font=('arial',14,'bold'))
        self.Drink3.place(x=20,y=145)        
        self.Drink3S=StringVar()
        self.Drink3S.set(0)
        self.Drink3E=Entry(self.f2top,font=('Times New Roman',12,'bold'),textvariable=self.Drink3S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Drink3E.place(x=350,y=150)

        self.Drink4=Label(self.f2top,text="Chocolate Smoothie             ₹75",font=('arial',14,'bold'))
        self.Drink4.place(x=20,y=215)        
        self.Drink4S=StringVar() 
        self.Drink4S.set(0)
        self.Drink4E=Entry(self.f2top,font=('Times New Roman',12,'bold'),textvariable=self.Drink4S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Drink4E.place(x=350,y=220)

        self.Drink5=Label(self.f2top,text="Fruit Smoothie                       ₹100".expandtabs(9),font=('arial',14,'bold'))
        self.Drink5.place(x=20,y=285)        
        self.Drink5S=StringVar()
        self.Drink5S.set(0)
        self.Drink5E=Entry(self.f2top,font=('Times New Roman',12,'bold'),textvariable=self.Drink5S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Drink5E.place(x=350,y=290)
        
       
        self.Pizza10=Label(self.f3,text="Butter Chicken\t \t     ₹545".expandtabs(15),font=('arial',14,'bold'))
        self.Pizza10.place(x=20,y=5)
        self.Pizza10S=StringVar()
        self.Pizza10S.set(0)
        self.Pizza10E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza10S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza10E.place(x=350,y=10)

        self.Pizza11=Label(self.f3,text="Barbecued Chicken\t     ₹665".expandtabs(8),font=('arial',14,'bold'))
        self.Pizza11.place(x=20,y=75)
        self.Pizza11S=StringVar()
        self.Pizza11S.set(0)
        self.Pizza11E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza11S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza11E.place(x=350,y=80)

        self.Pizza12=Label(self.f3,text="Pepperoni\t             ₹455",font=('arial',14,'bold'))
        self.Pizza12.place(x=20,y=145)        
        self.Pizza12S=StringVar()
        self.Pizza12S.set(0)
        self.Pizza12E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza12S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza12E.place(x=350,y=150)

        self.Pizza13=Label(self.f3,text="Meat Feast\t             ₹570",font=('arial',14,'bold'))
        self.Pizza13.place(x=20,y=215)        
        self.Pizza13S=StringVar() 
        self.Pizza13S.set(0)
        self.Pizza13E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza13S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza13E.place(x=350,y=220)

        self.Pizza14=Label(self.f3,text="Chicken Dominator\t          ₹350".expandtabs(10),font=('arial',14,'bold'))
        self.Pizza14.place(x=20,y=285)        
        self.Pizza14S=StringVar()
        self.Pizza14S.set(0)
        self.Pizza14E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza14S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza14E.place(x=350,y=290)

        self.Pizza15=Label(self.f3,text="Chicken Delight\t             ₹550",font=('arial',14,'bold'))
        self.Pizza15.place(x=20,y=355)        
        self.Pizza15S=StringVar()
        self.Pizza15S.set(0)
        self.Pizza15E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza15S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza15E.place(x=350,y=360)

        self.Pizza16=Label(self.f3,text="Chicken Feast\t             ₹575",font=('arial',14,'bold'))
        self.Pizza16.place(x=20,y=425)        
        self.Pizza16S=StringVar()
        self.Pizza16S.set(0)
        self.Pizza16E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza16S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza16E.place(x=350,y=430)

        self.Pizza17=Label(self.f3,text="Keema Garlic Bread           ₹150",font=('arial',14,'bold'))
        self.Pizza17.place(x=20,y=495)        
        self.Pizza17S=StringVar()
        self.Pizza17S.set(0)
        self.Pizza17E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza17S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza17E.place(x=350,y=500)

        self.Pizza18=Label(self.f3,text="Supreme Garlic Bread        ₹175",font=('arial',14,'bold'))
        self.Pizza18.place(x=20,y=560)        
        self.Pizza18S=StringVar()
        self.Pizza18S.set(0)
        self.Pizza18E=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.Pizza18S,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.Pizza18E.place(x=350,y=560)

        self.PizzatopC=Label(self.f3,text="Extra Chicken                       ₹100",font=('arial',14,'bold'))
        self.PizzatopC.place(x=20,y=615)        
        self.PizzatopCS=StringVar()
        self.PizzatopCS.set(0)
        self.PizzatopCE=Entry(self.f3,font=('Times New Roman',12,'bold'),textvariable=self.PizzatopCS,justify='right',width=10,bd=4,bg="WHITE",state=NORMAL)
        self.PizzatopCE.place(x=350,y=615)


       
        self.lblPaymentMethod=Label(self.f2bottom,font=('arial',14,'bold'),text="Payment Method",bd=10,width=16).place(x=0,y=5)
        self.lblTotal=Label(self.f2bottom,font=('arial',14,'bold'),text="Total",bd=10,width=16).place(x=220,y=185)
        self.varTotal=StringVar()
        self.varTotal.set(0)
        self.txtTotal=Entry(self.f2bottom,font=('arial',14,'bold'),textvariable=self.varTotal,width=6,bg='WHITE',justify='right',state=NORMAL)
        self.txtTotal.place(x=400,y=195)

        def bill():
            tkinter.Tk.__init__(self)
            self.configure(background="#757cc4")
            self.title("Bill")
            self.geometry('1920x1000+0+0')
            self.frameb1=Frame(self,width=800,height=8500,bg="#e2d62f",bd=12,relief=RAISED)
            self.frameb1.pack(side=LEFT)
            self.billtxt=Text(self.frameb1,width=70,height=30,bg="WHITE",bd=8,font=('Times New Roman',15,'bold'))
            self.billtxt.place(x=20,y=20)
            u=db.cursor()
            with db.cursor() as u:
                selectcustid=("select cust_id from customer where contact='%s'")
                u.execute(selectcustid % phoneno)
                custidb=u.fetchone()
                print(custidb)
                selectorderidb=("select order_id from orderfood where cust_id='%s'")
                u.execute(selectorderidb,custidb[0])
                orderidb=u.fetchone()
                print(orderidb)
                selectordercust=("select * from subitem where order_id='%s'")
                u.execute(selectordercust % orderidb[0])
                orderfoodc=u.fetchall()
                print(orderfoodc)
                lenoforder=len(orderfoodc)
                selectfood=("select name from food where food_id='%s'")
                self.billtxt.insert(END,'Items\t\t\t\t\t'+"Quantity\n\n")
                for i in range(lenoforder):
                    u.execute(selectfood % orderfoodc[i][2])
                    nameb=u.fetchone()
                    print(nameb)
                    self.billtxt.insert(END,str(nameb[0])+'\t\t\t\t\t'+str(orderfoodc[i][1])+"\n\n")
            self.billtxt.insert(END,'\n\n\n\n\n\nTotal\t\t\t\t\t'+str(self.iCost))                
            self.Exit=Button(self.frameb1,font=('arial',18,'bold'),text='Exit',command=lambda:iExit(self),relief=RAISED)
            self.Exit.place(x=130,y=1000)
                    
            
            
        def iExit(self):
            qExit=tkinter.messagebox.askyesno("Quit System","Do you want to quit?")
            if qExit>0:
                self.destroy()
                return
            
        def costofmeal(self):
            self.item1=int(self.Pizza1S.get()) 
            self.item2=int(self.Pizza2S.get()) 
            self.item3=int(self.Pizza3S.get())
            self.item4=int(self.Pizza4S.get())
            self.item5=int(self.Pizza5S.get())
            self.item6=int(self.Pizza6S.get())
            self.item7=int(self.Pizza7S.get())
            self.item8=int(self.Pizza8S.get())
            self.item9=int(self.Pizza9S.get())
            self.item11=int(self.Pizza10S.get())
            self.item12=int(self.Pizza11S.get())
            self.item13=int(self.Pizza12S.get())
            self.item14=int(self.Pizza13S.get())
            self.item15=int(self.Pizza14S.get())
            self.item16=int(self.Pizza15S.get())
            self.item17=int(self.Pizza16S.get())
            self.item18=int(self.Pizza17S.get())
            self.item19=int(self.Pizza18S.get())
            self.item10=int(self.PizzatopS.get())
            self.item20=int(self.PizzatopCS.get())
            self.item21=int(self.Drink1S.get())
            self.item22=int(self.Drink2S.get())
            self.item23=int(self.Drink3S.get())
            self.item24=int(self.Drink4S.get())
            self.item25=int(self.Drink5S.get())
            items=[]
            items.append(self.item1)
            items.append(self.item2)
            items.append(self.item3)
            items.append(self.item4)
            items.append(self.item5)
            items.append(self.item6)
            items.append(self.item7)
            items.append(self.item8)
            items.append(self.item9)
            items.append(self.item10)
            items.append(self.item11)
            items.append(self.item12)
            items.append(self.item13)
            items.append(self.item14)
            items.append(self.item15)
            items.append(self.item16)
            items.append(self.item17)
            items.append(self.item18)
            items.append(self.item19)
            items.append(self.item20)
            items.append(self.item21)
            items.append(self.item22)
            items.append(self.item23)
            items.append(self.item24)
            items.append(self.item25)
           
            self.Qty=(self.item1+self.item2+self.item3+self.item4+self.item5+self.item6+self.item7+self.item8+self.item9+self.item10+self.item11+self.item12+self.item13+self.item14+self.item15+self.item16+self.item17+self.item18+self.item19+self.item20+self.item21+self.item22+self.item23+self.item24+self.item25)
            print((self.Qty))
            self.iTotal=((self.item1*545)+(self.item2*665)+(self.item3*445)+(self.item4*570)+(self.item5*350)+(self.item6*550)+(self.item7*475)+(self.item8*75)+
                         (self.item9*75)+(self.item10*545)+(self.item11*665)+(self.item12*445)+(self.item13*570)+(self.item14*350)+(self.item15*550)+(self.item16*575)+
                         (self.item17*150)+(self.item18*175)+(self.item19*75)+(self.item20*100)+(self.item21*55)+(self.item22*55)+(self.item23*55)+(self.item24*75)+
                         (self.item25*100))
            self.iCost=float(self.iTotal)
            self.varTotal.set(self.iCost)
            print((self.iCost))
            eid=default
            try:
                p=db.cursor()
                with db.cursor() as p:
                    selectcustid=("select cust_id from customer where contact='%s'")
                    p.execute(selectcustid % phoneno)
                    custid=p.fetchone()
                   
                    
                    insertfood=("insert into orderfood (cost,cust_id,emp_id) values (%s,%s,%s)")
                    p.execute(insertfood,(self.iCost,custid[0],eid))
                    
                    selectorderid=("select order_id from orderfood where cust_id='%s'")
                    p.execute(selectorderid % custid)
                    orderid=p.fetchone()
                   

                    quantitylist=[]
                   
                    for i in range(len(items)):
                       
                        emp=[]
                        if(items[i]!=0):
                            emp.append(i+1)
                            emp.append(items[i])
                            quantitylist.append(emp)
                            insertsuborder=("insert into subitem (qty,food_id,order_id) values (%s,%s,%s)")
                            p.execute(insertsuborder,(emp[1],emp[0],orderid))   

                db.commit()
            finally:
                print("")
               
        
        def iReset(self):
            self.Pizza1S.set(0)
            self.Pizza2S.set(0)
            self.Pizza3S.set(0)
            self.Pizza4S.set(0)
            self.Pizza5S.set(0)
            self.Pizza6S.set(0)
            self.Pizza7S.set(0)
            self.Pizza8S.set(0)
            self.Pizza9S.set(0)
            self.Pizza10S.set(0)
            self.Pizza11S.set(0)
            self.Pizza12S.set(0)
            self.Pizza13S.set(0)
            self.Pizza14S.set(0)
            self.Pizza15S.set(0)
            self.Pizza16S.set(0)
            self.Pizza17S.set(0)
            self.Pizza18S.set(0)
            self.PizzatopS.set(0)
            self.PizzatopCS.set(0)
            self.Drink1S.set(0)
            self.Drink2S.set(0)
            self.Drink3S.set(0)
            self.Drink4S.set(0)
            self.Drink5S.set(0)
            self.varD.set("")
            self.varTotal.set(0)    
        Total=Button(self.f2bottom,font=('arial',18,'bold'),text='Total',relief=RAISED,command=lambda:costofmeal(self)).place(x=10,y=235)
        Reset=Button(self.f2bottom,font=('arial',18,'bold'),text='Reset',command=lambda:iReset(self),relief=RAISED).place(x=120,y=235)
       
        Confirmation=Button(self.f2bottom,font=('arial',18,'bold'),text='Confirmation',command=lambda:bill(),relief=RAISED).place(x=310,y=235)
        self.varD=StringVar()
        self.varD.set(0)
        self.txtD=Entry(self.f2bottom,font=('arial',18,'bold'),textvariable=self.varD,width=6,bg='WHITE',justify='right')
        self.txtD.place(x=80,y=120)
        
    def putData(self,db):
        global name1
        name1=self.nameentry.get()
        global phoneno
        phoneno=int(self.phentry.get())
        self.phoneno.set(phoneno)
        global mailid
        mailid=self.mailentry.get()
        try:
            p=db.cursor()
            with db.cursor()as p:
               
                insertcust=("INSERT INTO Customer (name,contact,email) VALUES(%s,%s,%s)")  
                if(p.execute(insertcust,(name1,self.phoneno.get(),mailid))):
                    db.commit()
                    tkinter.messagebox.showinfo("Submit Prompt","Submission Successful\nPress OK for MENU")
                    self.destroy()
                    self.menu()
                else:
                    self.destroy()
        finally:
           
            print("")   
        
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.configure(background="#757cc4")
        self.title("Customer Information")
        self.geometry('1920x1000+0+0')
        self.frame=Frame(self,width=1480,height=675,bg="#e2d62f",bd=10,relief=SUNKEN).place(x=30,y=110)
       
        self.label1=Label(self,font=('Times New Roman',50,'bold'),text="Customer Details",bd=10,fg="#a54a5f",relief=GROOVE).place(x=500,y=10)
        
       
        self.name=Label(self,font=('Times New Roman',30,'bold'),text="Name:",bd=5,bg="#e2d62f",relief=GROOVE)
        self.name.place(x=50,y=130)
        self.name1=StringVar()
        self.nameentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.name1,width=30,bd=9,bg="WHITE")
        self.nameentry.place(x=350,y=130)
        
       
        self.phoneno=Label(self,font=('Times New Roman',30,'bold'),text="Phone Number:",bd=5,bg="#e2d62f",relief=GROOVE).place(x=50,y=250)
        self.phoneno=StringVar()
        self.phentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.phoneno,width=30,bd=9,bg="WHITE")
        self.phentry.place(x=350,y=250)

       
        self.mail=Label(self,font=('Times New Roman',30,'bold'),text="Email:",bd=5,bg="#e2d62f",relief=GROOVE).place(x=50,y=400)
        self.mailid=StringVar()
        self.mailentry=Entry(self,font=('Times New Roman',20,'bold'),textvariable=self.mailid,width=30,bd=9,bg="WHITE")
        self.mailentry.place(x=350,y=400)

       
        self.B=Button(self,font=('Times New Roman',40,'bold'),text='Submit',relief=GROOVE,command=lambda:self.putData(db))
        self.B.place(x=550,y=600)
        self.bind('<Return>')

def getData(parent):
    global default
    default=parent.top.E1.get()
    global default1
    default1=parent.top.E2.get()
    try:
        c=db.cursor()
        with db.cursor()as c:
            c.execute("SELECT * FROM employee")
            r=c.fetchall()
           
            for i in range(len(r)):
                if(int(r[i][0])==int(default) and r[i][3]==default1):
                    tkinter.messagebox.showinfo("Login Prompt", "Login Successful\nPress OK for DETAILS")
                    s=SampleApp()
                    parent.top.destroy()
                else:
                    print("")
                   
    finally:
        print("")
       
       
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
    self.top.label3=Label(self.top,font=('Times New Roman',30,'bold'),text="Employee ID:",fg="BLACK",bg="#17edd0").place(x=400,y=375)
    self.top.label4=Label(self.top,font=('Times New Roman',30,'bold',),text="Password:",fg="BLACK",bg="#17edd0").place(x=400,y=475)
    self.default=IntVar()
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