import pygame, sys
from pygame.locals import *
import tkinter
from tkinter import *

def close():
    exit()

pygame.init()

window = Tk()

b1 = Button(window, text = "Start", command = close)
b1.pack()

#window.mainloop()



menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Close", command = close)

menubar.add_cascade(label = "File", menu =filemenu)

window.config(menu = menubar)
window.mainloop()






