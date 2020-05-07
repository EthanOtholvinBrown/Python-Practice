# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:39:30 2020

@author: Ethan
"""

class Pet():
    def __init__(self,nme,tpe,ag):
        self.name = nme
        self.animalType = tpe
        self.age = ag
    def set_name(self):
        self.aName = self.name
    def set_animal_type(self):
        self.aType = self.animalType
    def set_age(self):
        self.animalAge = self.age
    def get_name(self):
        return self.aName
    def get_animal_type(self):
        return self.animalType
    def get_age(self):
        return self.animalAge
