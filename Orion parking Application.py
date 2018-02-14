# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:58:56 2018

@author: sonur
"""

import datetime

class orion():
    
    
    
    def __init__(self,gatename):
        self.gatename = gatename
        
    def calculate_parking_fee(self,no_of_hours_parked,parked_vehicle_type):
        self.no_of_hours_parked = no_of_hours_parked
        self.parked_vehicle_type = parked_vehicle_type
        date = datetime.datetime.today().day
        if(date % 2 == 0):
            print('Even Day')
            if(self.parked_vehicle_type == 2):
                print('Parking Fee for Bike: ',self.no_of_hours_parked*30)
            if(self.parked_vehicle_type == 4):
                print('Parking Fee for Car : ',self.no_of_hours_parked*60)
        else:
            print('Odd Day')
            if(self.parked_vehicle_type == 2):
                print('Parking Fee for Bike: ',self.no_of_hours_parked*40)
            if(self.parked_vehicle_type == 4):
                print('Parking Fee for Car : ',self.no_of_hours_parked*80)
        
if __name__ == '__main__':
    northgate = orion('North Gate')
    
    northgate.calculate_parking_fee(2,2)
    northgate.calculate_parking_fee(2,4)
