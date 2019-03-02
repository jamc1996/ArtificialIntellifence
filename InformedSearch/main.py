#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:05:41 2019

@author: john
"""

from EvaluatedNetwork import EuclideanNetwork

TestMap = EuclideanNetwork(8)

TestMap.Connect(0,1,1)
TestMap.Connect(1,2,1)
TestMap.Connect(1,7,2)
TestMap.Connect(7,4,1)
TestMap.Connect(1,5,8)
TestMap.Connect(2,3,1)
TestMap.Connect(4,6,2)
TestMap.Connect(5,4,3)

TestMap.set_euc(0,6,6)
TestMap.set_euc(1,6,5)
TestMap.set_euc(2,6,6)
TestMap.set_euc(3,6,7)
TestMap.set_euc(4,6,2)
TestMap.set_euc(5,6,1)
TestMap.set_euc(6,6,0)
TestMap.set_euc(7,6,3)

print("Using Greedy Search:")
path = TestMap.GreedySearch(0,6)
if path[0] != -1:
    print(path[:-1])

print("\nUsing A* Search:")
path2 = TestMap.Aprime(0,6)
if path[0] != -1:
    print(path2[:-1])