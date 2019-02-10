from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1920x1080')
root.title("Welcome")
canvas=Canvas(root,bg="YELLOW",width=1920,height=1080)
canvas.pack()
img=Image.open("Screenshot_20171022-002410.png")
render=ImageTk.PhotoImage(img)
canvas.create_image(0,0,anchor=NW,image=render)
root.mainloop()
