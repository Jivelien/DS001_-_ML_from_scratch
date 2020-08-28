#!/usr/bin/python
from tkinter import *
import time

gui = Tk()
gui.geometry("800x400")

c = Canvas(gui ,width=800 ,height=400)
c.pack()

oval = c.create_oval(5,5,60,60,fill='red')
xd = 5
yd = 10

while True:
    c.move(oval,xd,yd)
    p=c.coords(oval)
    if p[3] >= 400 or p[1] <=0:
        yd = -yd
    if p[2] >=800 or p[0] <=0:
        xd = -xd
    gui.update()
    time.sleep(0.025) 
  
gui.title("First title")
gui.mainloop()