
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:55:15 2020

@author: CORE_i5
"""

import Character
import numpy as np
import GridPlane
import time

class Food(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.charaCount = 0
        self.chara1 = None
        self.chara2 = None
        
    def getCharaCount(self):
        return self.charaCount
    
    def incCharCount(self):
        self.charaCount += 1
        
    def getCords(self):
        return (self.x, self.y)
    
    def set1(self, chara1):
        self.chara1 = chara1
        
    def set2(self, chara2):
        self.chara2 = chara2
        
    def get1(self):
        return self.chara1
    
    def get2(self):
        return self.chara2

    

class DayRunner(object):
    def __init__(self, charaList):
        self.foodList = []
        self.charaList = charaList
        self.dovenumber = 0
        self.hostilenumber = 0

#this is the battle system that assignes foodcounts
    def battle(self, chara1, chara2):
        
        if (chara2 == None):
            chara1.setFoodCount(2.0)
            return
        if (chara1 == None):
            chara2.setFoodCount(2.0)
            return
        
        if ((chara1.getCharType() == 1) and (chara2.getCharType() == 1)):
            chara1.setFoodCount(1.0)
            chara2.setFoodCount(1.0)
            return
        
        if ((chara1.getCharType() == 1) and (chara2.getCharType() != 1)):
            chara1.setFoodCount(0.5)
            chara2.setFoodCount(1.5)         
            return
        
        if ((chara1.getCharType() != 1) and (chara2.getCharType() == 1)):
            chara1.setFoodCount(1.5)
            chara2.setFoodCount(0.5)           
            return
        
        if ((chara1.getCharType() != 1) and (chara2.getCharType() != 1)):
            chara1.setFoodCount(0.0)
            chara2.setFoodCount(0.0)
            return
        
#This calculates number of each type of character    
    def getCounts(self):
        """
        returns dn, hn
        
        dn : dove number
            
        hn : hostile number
          
        """
        dn = 0
        hn = 0
        
        for chara in self.charaList:
            if (chara.getCharType() == 1):
                dn += 1
            else:
                hn += 1
        
        self.dovenumber = dn
        self.hostilenumber = hn
#        print("Doves = " + str(dn))
#        print("Hostiles = " + str(hn))
        
        return dn, hn
    
    def day(self):
        
        #This creates all the food particles
        for x in range(10):
            for y in range(10):
                self.foodList += [Food(x+1,y+1)]
                
        for chara in self.charaList:
            randfail = False

           
            #This tries to randomly assign food to a character            
            for tries in range(10):
                food = self.foodList[np.random.randint(100)-1]
                if (food.get1() == None) or (food.get2() == None):
                        food.incCharCount()
                        (xf, yf) = food.getCords()
                        chara.setCords(xf, yf)
                        if (food.get1() == None):
                            food.set1(chara)
                        else:
                            food.set2(chara)
                        break
                    
                if (tries == 10):
                    randfail = True
                  
            
#            randfail = True 
            #If a random food cannot be assigned, this assignes an empty food particle systematically
            if randfail:            
                for food in self.foodList:
                    if ((food.get1() == None) or (food.get2() == None)):
                        food.incCharCount()
                        (xf, yf) = food.getCords()
                        chara.setCords(xf, yf)
                        if (food.get1() == None):
                            food.set1(chara)
                        else:
                            food.set2(chara)
                        break
                        
#            print(chara.getCords())

        
        #This makes everyone fight
        for food in self.foodList:
            if ((food.get1() != None) or (food.get2() != None)):
                self.battle(food.get1(), food.get2())
            
#            print([food.get1(), food.get2()])
        
        for chara in self.charaList:
            thisx, thisy = chara.getCords()
            GridPlane.grid.moveTo(chara.gettag(), thisx, thisy, chara.getCharType())
        
        GridPlane.grid.updateall()
        
        
        newclist = []
        #This checks for much food everyone ate and does things accordingly                      
        for chara in self.charaList:
           
#            if (len(self.charaList) == 1):
#            print(chara.getfoodcount())
#            print(chara.gettag())
            
            if (chara.getfoodcount() < 1):
                if bool(chara.getfoodcount()<=np.random.rand(1)):
#                    if(chara.getCharType() == "dove"):
#                        self.dovenumber -= 1
#                    else:
#                        self.hostilenumber -= 1
                    self.charaList.remove(chara)
                    GridPlane.grid.delete(chara.gettag())
                    del chara
            else:
                if (bool((chara.getfoodcount()-1)>=np.random.rand(1)) or (chara.getfoodcount()==2)):
                    
                    if(chara.getCharType() == 1):
#                        self.dovenumber += 1
                        newc = Character.Dove()
                        newc.settag()
                        GridPlane.grid.doveplace(newc.gettag())  
                        newclist.append(newc)
                        del newc
#                        print ("REPRODUCE DOVE")
             
                    else:
#                        self.hostilenumber += 1
                        newc = Character.Hostile()
                        newc.settag()
                        GridPlane.grid.hostplace(newc.gettag()) 
                        newclist.append(newc)
                        del newc
#                        print ("REPRODUCE HOSTILE")

        

#This resets all characters to start position on the grid
        time.sleep(1)
        for chara in self.charaList:
            if(chara.getCharType() == 1):
                thisx, thisy = 0, 0
                
            else:
                thisx, thisy = 10.75, 0.125
                
            GridPlane.grid.moveTo(chara.gettag(), thisx, thisy, chara.getCharType())
        #print (self.charaList)
        self.charaList += newclist
        del newclist
#        print (self.charaList)
#        print(len(self.charaList))
        
        GridPlane.grid.updateall()
#This resets the day defaults                        

        self.foodList = []
        for chara in self.charaList:
            chara.setCords(0, 0)
            chara.setFoodCount(0.0)
        
        time.sleep(1)
        
              
        

    
    
    
    