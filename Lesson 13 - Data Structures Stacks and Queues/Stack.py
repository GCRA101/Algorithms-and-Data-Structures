# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import math as math
import time
import matplotlib.pyplot as plt
import random


# IMPORT PACKAGE CLASSES
from SingleRecord import RecordSingolo

'''
CLASSE PILA (STACK)
Costruita servendosi of the Struttura Data of LISTA PUNTATA SINGOLA
'''

class Stack:
    
    # ATTRIBUTES
    _top=None
    
    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,_top=None):
        self._top=_top
        
    # METHODS
    
    'PUSH'
    def push(self,el):                          # T(n)
        el.setNext(self._top)                   # Θ(1)
        self._top=el                            # Θ(1)
        return                                  # Θ(1)

    'POP'    
    def pop(self):                              # T(n)
        if self._top==None:                     # Θ(1)
            return None                         # Θ(1)
        else:                                   # Θ(1)
            self._top=self._top.getNext()       # Θ(1)
        return self._top                        # Θ(1)
    
    'ToString'
    def __str__(self):
        p_corr=self._top
        output=""
        while p_corr!=None:
            if p_corr.getNext()!=None:
                output+="["+str(p_corr)+"]" + " - "
            else:
                output+="["+str(p_corr)+"]"
            p_corr=p_corr.getNext()
        return output
        
