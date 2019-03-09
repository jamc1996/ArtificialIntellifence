#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:18:09 2019

@author: john
"""

from CSP import CSP

ColourAustralia = CSP(7)

names = ["Western Australia","Northern Territory","Southern Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
colours = ["red","green","yellow"]

ColourAustralia.BinaryConstrain(0,1)
ColourAustralia.BinaryConstrain(0,2)
ColourAustralia.BinaryConstrain(1,2)
ColourAustralia.BinaryConstrain(1,3)
ColourAustralia.BinaryConstrain(2,3)
ColourAustralia.BinaryConstrain(2,4)
ColourAustralia.BinaryConstrain(2,5)
ColourAustralia.BinaryConstrain(3,4)
ColourAustralia.BinaryConstrain(4,5)

for i in range(7):
    for j in range(3):
        ColourAustralia.set_domain(i,j)
        
        
if ColourAustralia.BackTracking_Search():
    assigned = ColourAustralia.assignments
    for i in range(ColourAustralia.num_variables):
        print("%s is coloured %s!"%(names[i],colours[assigned[i]]))