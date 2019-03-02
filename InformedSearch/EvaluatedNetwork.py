#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:33:25 2019

@author: john
"""


import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

class EuclideanNetwork():
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.con_matrix = np.zeros([num_nodes,num_nodes])
        self.euc_matrix = np.zeros([num_nodes,num_nodes])
  
    def EuclideanDistance(self,i,j):
        return self.euc_matrix[i][j]
    
    def Randomize(self, max_cost):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                self.con_matrix[i][j] = random.randrange(0,max_cost+1)
               
    def set_euc(self,i,j,dist):
        self.euc_matrix[i][j] = dist
                
    def Connect(self,i,j, cost = 1):
        self.con_matrix[i][j] = cost
        
    def DisConnect(self,i,j):
        self.con_matrix[i][j] = 0
        
    def DoubleConnect(self,i,j, cost_ij, cost_ji):
        self.con_matrix[i][j] = cost_ij
        self.con_matrix[j][i] = cost_ji  
    
    def DoubleDisConnect(self,i,j):
        self.con_matrix[i][j] = 0
        self.con_matrix[j][i] = 0
    
    def _ExpandNode(self, place, null_elems, stack):
        node = stack[place][1]
        cost = stack[place][0]
        for i in range(self.con_matrix.shape[0]):
            if ((self.con_matrix[node][i] != 0) and (i not in null_elems)):
                cost+=self.con_matrix[node][i]
                new_pos = len(stack)
                stack.append([cost, i])
                for x in stack[place][1:]:
                    stack[new_pos].append(x)
                cost = stack[place][0]
        del stack[place]
        return stack
    
    def FindMinCost(self,stack):
        place = 0
        min_cost = stack[0][0]
        for i in range(len(stack)):
            if stack[i][0] < min_cost:
                min_cost = stack[i][0]
                place = i
        return place
            
    def FindMinDistance(self,stack,goal):
        place = 0
        node = stack[0][1]
        min_dist = self.euc_matrix[node][goal]
        for i in range(len(stack)):
            node = stack[i][1]
            dist = self.euc_matrix[node][goal]
            if dist < min_dist:
                min_dist = dist
                place = i
        return place
    
    def MinDistMinCost(self,stack,goal):
        place = 0
        node = stack[0][1]
        min_discost = stack[0][0] + self.euc_matrix[node][goal]
        for i in range(len(stack)):
            node = stack[i][1]
            discost = stack[i][0] + self.euc_matrix[node][goal]
            if discost < min_discost:
                min_discost = discost
                place = i
        return place
    
    def TreeSearch(self, start_node, goal_node, strategy,init_cost = 0):
        stack = [[init_cost,start_node]]
        null_elems = list()
        while (stack):
            place =  strategy(stack,goal_node)
            node = stack[place][1]
            if node == goal_node:
                print("Goal", stack[place][1], "found at cost", stack[place][0],"!")
                stack[place].reverse()
                return stack[place]
            null_elems.append(node)
            stack = self._ExpandNode(place,null_elems,stack)
        print("Goal not found :(")
        return -1

    def UniformCostSearch(self, start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self.FindMinCost)
    
    
    def GreedySearch(self,start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self.FindMinDistance)
    
    def Astar(self,start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self.MinDistMinCost)
