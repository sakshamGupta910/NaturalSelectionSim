# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:53:52 2020

@author: CORE_i5
"""



class Character(object):
    dovetagmax = 0
    hosttagmax = 0
    
    def setCords (self, x, y):
        self.x = x
        self.y = y
    
    def getCords(self):
        return self.x, self.y
    
    def getfoodcount(self):
        return self.foodcount
    
    def setFoodCount(self, foodcount):
        self.foodcount = foodcount
    
    def gettag(self):
        return self.tag
    
    
    
    
    
class Dove(Character):
    
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.foodcount = 1.0
        
        
    def settag(self):
        self.tag = "1," + str(Character.dovetagmax)
        Character.dovetagmax += 1
        
    def getCharType(self):
        return 1

class Hostile(Character):
    
    
    def __init__(self):
        self.x = 0
        self.y = 10
        self.foodcount = 1.0
        
        
    def settag(self):
        self.tag = "2," + str(Character.hosttagmax)
        Character.hosttagmax += 1
        
        
    def getCharType(self):
        return 2