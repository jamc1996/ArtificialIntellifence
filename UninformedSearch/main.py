#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:34:19 2019

@author: john
"""

from Networks import Network

RomaniaMap = Network(4)

RomaniaMap.Randomize()

print(RomaniaMap.con_matrix)

#RomaniaMap.plot()

pathd = RomaniaMap.DepthFirstSearch(0,2)
pathb = RomaniaMap.BreadthFirstSearch(0,2)

print("Using depth first, path is",pathd)
print("Using breadth first, path is",pathb)