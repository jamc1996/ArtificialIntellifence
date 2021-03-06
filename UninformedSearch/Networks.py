#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:39:16 2019

@author: john
"""

import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx



class PricedNetwork():
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.con_matrix = np.empty([num_nodes,num_nodes])
    
    def Randomize(self, max_cost):
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                self.con_matrix[i][j] = random.randrange(0,max_cost+1)
                
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
            
    def TreeSearch(self, start_node, goal_node, strategy,init_cost = 0):
        stack = [[init_cost,start_node]]
        null_elems = list()
        while (stack):
            place =  strategy(stack)
            node = stack[place][1]
            if node == goal_node:
                stack[place].reverse()
                print("Goal", stack[place][0], "found at cost", stack[place][len(stack[place])-1],"!")
                return stack[place]
            null_elems.append(node)
            stack = self._ExpandNode(place,null_elems,stack)
        print("Goal not found :(")
        return -1

    def UniformCostSearch(self, start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self.FindMinCost)
    
        
class BinaryNetwork(PricedNetwork):
    """Represents any network of interconnected nodes.
    attributes: num_nodes, A."""
    
    
    def __init__(self, num_nodes):
        super(BinaryNetwork,self).__init__(num_nodes)
    
    def Randomize(self):
        super(BinaryNetwork,self).Randomize(1)
        
    def Connect(self,i,j):
        super(BinaryNetwork,self).Connect(i,j)
        self.con_matrix[i][j] = 1
        
    def DisConnect(self,i,j):
        super(BinaryNetwork,self).DisConnect(i,j)
        
    def DoubleDisConnect(self,i,j):
        super(BinaryNetwork,self).DoubleDisConnect(i,j)
        
    def DoubleConnect(self,i,j):
        super(BinaryNetwork.self).DoubleConnect(i,j)
       

    # I need to get back to making the plot nice.
# =============================================================================
#     def plot(self):
#         G = nx.from_numpy_matrix(self.con_matrix)
#         pos = nx.layout.spring_layout(G)
#         
#         M = G.number_of_edges()
#         node_sizes = [3 + 10 * i for i in range(len(G))]
# 
#         edge_colors = range(2,M+2)
#         nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='blue')
#         edges = nx.draw_networkx_edges(G, pos, node_size=node_sizes, arrowstyle='->', arrowsize=10, edge_color=edge_colors, edge_cmap=plt.cm.Blues, width=2)
#         
#         pc = mpl.collections.PatchCollection(nodes, cmap=plt.cm.Blues)
#         pc.set_array(edge_colors)
#         plt.colorbar(pc)
# 
#         ax = plt.gca()
#         ax.set_axis_off()
#         
#         plt.title("Adjacency Matrix")
# =============================================================================
        
    def _ExpandNode(self, place, null_elems, stack):
        node = stack[place][0]
        for i in range(self.con_matrix.shape[0]):
            if ((self.con_matrix[node][i] != 0) and (i not in null_elems)):
                new_pos = len(stack)
                stack.append([i])
                for x in stack[place]:
                    stack[new_pos].append(x)
        del stack[place]
        return stack
        
    def TreeSearch(self, start_node, goal_node,  strategy):
        """Basic Tree Search allows for choice of depth first 
        search or breadth first search."""
        stack = [[start_node]]
        null_elems = list()
        while (stack):
            place = strategy(stack)
            node = stack[place][0]
            if node == goal_node:
                stack[place].reverse()
                print("Goal", node, "found !")
                return stack[place]
            null_elems.append(node)
            stack = self._ExpandNode(place, null_elems, stack)
        print("Goal not found :(")
        return [-1]
            
    def _BF(self,stack):
        return 0
    
    def _DF(self,stack):
        return len(stack)-1
    
    def BreadthFirstSearch(self, start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self._BF)
    
    def DepthFirstSearch(self, start_node,goal_node):
        return self.TreeSearch(start_node, goal_node, self._DF)     
        