#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:33:37 2019

@author: john
"""


class CSP():
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.binaryConstraints = [[] for i in range(num_variables)]
        self.domains = [[] for i in range(num_variables)]
        self.assignments = [-1 for i in range(num_variables)]
    
    def set_domain(self,variable,value):
        self.domains[variable].append(value)
        
    def UnaryConstrain(self,node,value):
        if value in self.domains[node]:
            self.domains[node].remove(value)
    
    def BinaryConstrain(self,node1,node2):
        self.binaryConstraints[node1].append(node2)
        self.binaryConstraints[node2].append(node1)
        
    def RmvConstr(self,i,j):
        self.constr_matrix[i][j] = 0
        
    def DoubleConnect(self,i,j, cost_ij=1, cost_ji=1):
        self.constr_matrix[i][j] = cost_ij
        self.constr_matrix[j][i] = cost_ji  
    
    def DoubleDisConnect(self,i,j):
        self.constr_matrix[i][j] = 0
        self.constr_matrix[j][i] = 0
        
    def Select_Unassigned(self):
        for i in range(self.num_variables):
            if self.assignments[i] == -1:
                return i
        return -1
            
    def failed_constraints(self,var,variable):
        for i in self.binaryConstraints[var]:
            if variable == self.assignments[i]:
                return True
        return False
    
    def BackTracking_Search(self):
        return self.Recursive_Backtracking()
        
    def Recursive_Backtracking(self):
        var = self.Select_Unassigned()
        if var == -1:
            return True
        for value in self.domains[var]:
            if self.failed_constraints(var,value):
                continue
            self.assignments[var] = value
            result = self.Recursive_Backtracking()
            if result != False:
                return True
            self.assignments[var] = -1
        return False
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        