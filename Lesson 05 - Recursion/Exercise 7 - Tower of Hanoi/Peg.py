# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:43:13 2023

@author: giorg
"""

# IMPORT LIBRARIES
import copy

# IMPORT PACKAGE CLASSES
from Disk import Disco


# CLASS PEG

class Piolo:
    
    # ATTRIBUTES
    disks=list()
    
    # CONSTRUCTORS
    'Default and Overloaded'
    def __init__(self,n=None):
        self.disks=list()
        if n!=None:
            for the in range(n,0,-1):
                self.disks.append(Disco(the))
            
            
    # METHODS
    'Remove disk from top of stack'
    def rimuoviDisco(self):
        if len(self.disks)!=0:
            return self.disks.pop()
    
    'Add disk to top of stack'
    def aggiungiDisco(self,disk):
        '''If the stack is empty or the disk to add has to smaller diameter
         than the disk at the top of the stack...add the disk'''
        if len(self.disks)==0 or disk.minoreDi(self.disks[-1]):
            self.disks.append(disk)

    def getCopiaDischi(self):
        return copy.copy(self.disks)
        