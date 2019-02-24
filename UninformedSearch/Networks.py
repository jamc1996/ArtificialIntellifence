#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:39:16 2019

@author: john
"""

import numpy as np
import random

class Network:
    """Represents any network of interconnected nodes.
    attributes: num_nodes, A."""
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.con_matrix = np.empty([num_nodes,num_nodes])
       
    def InitSearchStack(self,start_node):
        stack = list()
        null_elems = list()
        stack.append(list())
        stack[0].append(start_node)
        return stack
        
    def TreeSearch(self, start_node, goal_node,  strategy):
        """Basic Tree Search allows for choice of depth first 
        search or breadth first search."""
        stack = InitSearchStack(self,start_node)

    

class PricedNetwork(Network):

    def Randomize(self, max_cost):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                self.A[i][j] = random.randint(max_cost)
                
    def UniformCostSearch(self):
        stack = InitSearchStack()