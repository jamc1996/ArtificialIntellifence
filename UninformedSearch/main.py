#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:34:19 2019

@author: john
"""

from Networks import BinaryNetwork, PricedNetwork

RomaniaMap = BinaryNetwork(10)
RomaniaMapCosted = PricedNetwork(10)

RomaniaMap.Randomize()
RomaniaMapCosted.Randomize(10)

RomaniaMap.DisConnect(0,2)
RomaniaMapCosted.DisConnect(0,2)

print("\nBasic Connection Matrix:\n")
print(RomaniaMap.con_matrix)

print("\nPriced Connection Matrix:\n")
print(RomaniaMapCosted.con_matrix)

#RomaniaMap.plot()


print("\nUsing Depth First Search:")
pathd = RomaniaMap.DepthFirstSearch(0,2)
if (pathd[0] != -1):
    print("Path is",pathd)

print("\nUsing Breadth First Search:")
pathb = RomaniaMap.BreadthFirstSearch(0,2)
if (pathb[0] != -1):
    print("Path is",pathb)

print("\nUsing Uniform Cost Search:")
pathco = RomaniaMapCosted.UniformCostSearch(0,2)
if (pathco[0] != -1):
    print("Path is ",pathco[:-1])



