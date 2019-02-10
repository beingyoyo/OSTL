from tkinter import *
import tkinter as tk
import tkinter.messagebox

top = tkinter.Tk()


def helloCallBack():
    tkinter.messagebox.showinfo("Hello Python", "Hello World")


B = tkinter.Button(top, text='Hello', command=helloCallBack)
B.pack()
# top.mainloop()


# CANVAS
C = tkinter.Canvas(top, bg="orange", height=250, width=250)
coord = 0, 50, 200, 200
arc = C.create_arc(coord, start=0, extent=150, fill="yellow")
C.pack()

# CHECKBOX
CheckVar1 = IntVar()
CheckVar2 = IntVar()
B1 = Checkbutton(top, text="Mark-1", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=10)
B2 = Checkbutton(top, text="Mark-2", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=10)
B1.pack()
B2.pack()

# LABEL
L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)

# FRAME
frame = Frame(top)
frame.pack
bottomframe = Frame(top)
bottomframe.pack(side=BOTTOM)

redbutton = Button(bottomframe, text="HELLO", fg="cyan")
redbutton.pack(side=LEFT)

greenbutton = Button(bottomframe, text="WORLD", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(bottomframe, text="TO", fg="blue")
bluebutton.pack(side=RIGHT)

blackbutton = Button(bottomframe, text="PYTHON :')", fg="black")
blackbutton.pack(side=BOTTOM)

# STRING
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)
var.set("How you doin? ;)")
label.pack()

# ListBox
Lb = Listbox(top)
Lb.insert(1, "Boo")
Lb.insert(2, "Perl")
Lb.insert(3, "C++")
Lb.insert(4, "PHP")
Lb.insert(5, "JavaScript")
Lb.insert(6, "IronPython")
Lb.insert(7, "JAVA")
Lb.insert(8, "Swift")
Lb.pack()


def donothing():
    filewin = Toplevel(top)
    button = Button(filewin, text="Do nothing button")
    button.pack()


menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=top.quit)
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
top.config(menu=menubar)

mb=Menubutton(top,text="condiments",relief=RAISED)
#mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb["menu"]=mb.menu
mayoVar=IntVar()
ketchVar=IntVar()
mb.menu.add_checkbutton(label="mayo",variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup",variable=ketchVar)
mb.pack()

var = StringVar()
label=Message(top,textvariable=var,relief=RAISED )
var.set("Hello :)\Python is easy :')")
label.pack()




def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)


var = IntVar()
R1 = Radiobutton(top, text="Python", variable=var, value=1, command=sel)
R1.pack(anchor=W)

R2 = Radiobutton(top, text="Perl", variable=var, value=2, command=sel)
R2.pack(anchor=W)

R3 = Radiobutton(top, text="JAVA", variable=var, value=3, command=sel)
R3.pack(anchor=W)
label = Label(top)
label.pack()

top.mainloop()

