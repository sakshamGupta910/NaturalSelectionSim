# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:11:26 2020

@author: CORE_i5
"""


import tkinter
import time
import DayRunner
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as font


class GridPlane(object):
    """
    Each particle is 20 pixels
    Each letter here represents a particle
    B = Null particle
    C = Character particle
    F = Food particle
    
    BBB
    CFC
    BBB
    
    
    """    
    
    
    def __init__(self):
        self.root = tkinter.Tk()
#        plt.bar(x, height, kwargs)
        
        self.myfont = font.Font(family='Helvetica', size=20, weight='bold')
        

        self.daylabel = tkinter.Label(self.root, font = self.myfont, text="Days Passed: 0")
        self.daylabel.pack(side="top")
        
        self.fig = plt.Figure()
        self.subplot1 = self.fig.add_subplot()
        self.graph = self.subplot1.bar(['Doves', 'Hostiles', 'Total Food'], [0, 0, 200] , 0.5)
#        self.graph2 = self.subplot1.bar(2, 10, 0.5)
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.graph_canvas.get_tk_widget().pack(side=tkinter.RIGHT)
        
        self.subplot1.set_title('Populations of Doves and Hostiles')
        self.subplot1.set_ylabel('Population')
        
        
        
        self.canvas = tkinter.Canvas(self.root, width = 1000, height = 1000)
        self.canvas.pack()
        self.foodimg = tkinter.PhotoImage(file="FoodImg.png")
                
        for x in range(10):
            for y in range(10):
                self.canvas.create_image((x+1)*80, (y+1)*80, image = self.foodimg)
        
        self.doveimg = tkinter.PhotoImage(file="CharacterImg.png")
        self.hostimg = tkinter.PhotoImage(file="hostimg.png")
        
        
    def doveplace(self, tag):
        self.canvas.create_image(10,10, image = self.doveimg, tags = tag)
        
    def show(self):
        self.root.mainloop()
        
        
    def moveTo(self, name,x,y, charnum):

        xcurrent, ycurrent = self.canvas.coords(name)
        
        if (charnum == 1):
            self.canvas.coords(name,((x)*80)-20, ((y)*80))
        else:
            self.canvas.coords(name,((x)*80)+20, ((y)*80))
    
    def setLabel(self, num):
        var = "Days Passed: " + str(num)
#        self.canvas.delete(dayLabel)
#        self.daylabel = tkinter.Label(self.root, font = self.myfont, text=var)
#        self.daylabel.pack(side="top")
        self.daylabel.configure(text=var)
        
    def updateall(self):         
        self.root.update()
        self.graph_canvas.draw()
        
        
        
    def hostplace(self, tag):
        self.canvas.create_image(880,10, image = self.hostimg, tags = tag)
    
    def delete(self, tag):
        self.canvas.delete(tag)
        
    def pltbar(self, num1, num2):
        
#        self.fig = plt.Figure()
#        self.subplot1 = self.fig.add_subplot()
#        self.graph1 = self.subplot1.bar(1, 10, 0.5)
#        self.graph2 = self.subplot1.bar(2, 10, 0.5)
#        self.graph_canvas = FigureCanvasTkAgg(self.fig)
#        self.graph_canvas.get_tk_widget().pack(side=tkinter.RIGHT)
        self.subplot1.cla()    
        
        self.graph = self.subplot1.bar(['Doves', 'Hostiles', 'Total Food'], [num1, num2, 200] , 0.5, color=('blue', 'red', 'green'))
        
        self.subplot1.set_title('Populations of Doves and Hostiles')
        self.subplot1.set_ylabel('Population')
#        self.graph2 = self.subplot1.bar(2, num2, 0.5)
    def anticrash(self):
        self.root.mainloop()
        
grid = GridPlane()

dovenum = 0 #FIX THIS LATER (maybe get it from dayrunner instance in Main)





#grid.moveTo("1,1", 1, 1, 1)
#grid.moveTo("2,1", 1, 1, 2)









