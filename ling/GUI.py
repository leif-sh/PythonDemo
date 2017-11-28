#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/14 
"""
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'word'
        messagebox.showinfo('Message', 'Hello, %s' % name)
root = Tk()
root.title("hello world")
root.geometry('300x200')
app = Application(root)
app.master.title('Hello World!')
app.mainloop()