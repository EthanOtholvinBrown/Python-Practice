# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:00:20 2020

@author: Ethan
"""
import random
class RockPaperScissor():
    def __init__(self):
        self.rps_value = 'rock'
    def set_rpsValue(self):
        value = random.randint(1,3)
        if (value == 1):
            self.rps_value = 'rock'
        elif (value == 2):
            self.rps_value = 'paper'
        else:
            self.rps_value = 'scissors'
    def get_rpsValue(self):
        return self.rps_value