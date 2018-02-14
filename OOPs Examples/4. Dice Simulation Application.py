# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:24:57 2018

@author: Rajath Kumar K S

Hello All,
Please Solve this Question using OOPS Concept.
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that 
simulates rolling dice. When the program runs, it will randomly choose a number 
between 1 and 6. (Or whatever other integer you prefer — the number of sides on 
the die is up to you.) The program will print what that number is. It should 
then ask you if you’d like to roll again. For this project, you’ll need to set 
the min and max number that your dice can produce. For the average die, that 
means a minimum of 1 and a maximum of 6. You’ll also want a function that 
randomly grabs a number within that range and prints it.
Concepts to keep in mind:

*Random
*Integer
*While Loops

"""

import random

class dice():
    
    player_no = 0
    
    def __init__(self,name):
        self.name = name
        dice.player_no += 1
        self.player_no = dice.player_no
        
    def rolldice(self):
        self.roll = random.randint(1,7)
        with open('log.txt','a') as fl:
            fl.write(' \n '+str(self.player_no)+' '+str(self.roll)+' '+self.name)
        print(self.roll)