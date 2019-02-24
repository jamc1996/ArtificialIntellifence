#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:34:19 2019

@author: john
"""

from Networks import Network


Romania = Network(4)

Romania.Randomize()

print(Romania.con_matrix)