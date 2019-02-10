from tkinter import *
import tkinter as tk 
import tkinter.messagebox
top=tkinter.Tk()
def helloCallBack():
    tkinter.messagebox.showinfo("hello python",\
                          "Hello wrold")
B=tkinter.Button(top,text="hello",command=helloCallBack)
B.pack()
#top.mainloop()


#canvas
#import tkinter as tk 
#top=tkinter.Tk()
C =tkinter.Canvas(top, bg="black", height=250, width=250)
coord = 0, 50, 200, 200
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
#top.mainloop()
#checkbox
#from Tkinter import *
#import tkMessageBox
#import Tkinter

#top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Marks1", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C2 = Checkbutton(top, text = "Marks2", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)

C1.pack()
C2.pack()
#top.mainloop()

#from Tkinter import *

#top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

#top.mainloop()
#from tkinter import *

#root = Tk()
frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="HELLO", fg="cyan")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="WORLD", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="TO", fg="blue")
bluebutton.pack( side = RIGHT )

blackbutton = Button(bottomframe, text="PYTHON :')", fg="black")
blackbutton.pack( side = BOTTOM)

#top.mainloop()


#from Tkinter import *

#root = Tk()
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)

var.set("How you doin? ;)")
label.pack()
#top.mainloop()

#from Tkinter import *
#import tkMessageBox
#import Tkinter

#top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "C++")
Lb1.insert(5, "IronPython")
Lb1.insert(6, "Ruby")
Lb1.insert(7, "JAVA")
Lb1.insert(8, "Go")

Lb1.pack()
top.mainloop()

#from Tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
top.mainloop()
'''from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()
top.mainloop()'''
'''from Tkinter import *

root = Tk()
var = StringVar()
label = Message( root, textvariable=var, relief=RAISED )

var.set("Hello :)\
	Python is easy :')")
label.pack()
root.mainloop()'''
'''from Tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Python", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Perl", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="JAVA", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()'''

