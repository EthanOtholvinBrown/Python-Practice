# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:07:53 2020

@author: Ethan
"""
import math
class Energy():
    def __init__(self,mss,vcty,hght):
        self.mass = mss
        self.velocity = vcty
        self.height = hght
    def set_ke(self):
        self.ke = math.pow((0.5 * self.mass *self.velocity),2)
    def set_pe(self):
        self.pe = self.mass * 9.8 * self.height
    def get_ke(self):
        return self.ke
    def get_pe(self):
        return self.pe