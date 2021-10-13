# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:31:23 2020

@author: CORE_i5
"""
import Character
import DayRunner
import GridPlane
import time

chara2List = []

Character.Character.dovetagmax = 0
Character.Character.hosttagmax = 0




for x in range (10):
    newch = Character.Dove()
    newch.settag()
    GridPlane.grid.doveplace(newch.gettag())
    chara2List += [newch]
    
    
    
for x in range (10):
    newch = Character.Hostile()
    newch.settag()
    GridPlane.grid.hostplace(newch.gettag())
    chara2List += [newch]


#dn, hn = 100, 100
#GridPlane.grid.pltbar(dn, hn)

#GridPlane.grid.show()

dayrun = DayRunner.DayRunner(chara2List)

for znmd in range(100):
    dayrun.day()
#    print("ooga")
    dn, hn = dayrun.getCounts()
#    print(dn, hn)
    GridPlane.grid.pltbar(dn, hn)
    GridPlane.grid.setLabel(znmd)

GridPlane.grid.anticrash()