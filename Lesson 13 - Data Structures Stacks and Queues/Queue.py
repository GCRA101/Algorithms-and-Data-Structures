# -*- coding: utf-8 -*-
"""
Created on Thu Jun 1 20:48:46 2023
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
CLASSE CODA (QUEUE)
Costruita servendosi of the Struttura Data of LISTA PUNTATA SINGOLA
'''

class Queue:
 
 # ATTRIBUTES
 _head=None
 _tail=None
 
 # CONSTRUCTOR
 'Default and Overloaded'
 def __init__(self,_head=None,_tail=None):
 self._head=_head
 self._tail=_tail
 
 # METHODS
 
 'ENQUEUE'
 def enqueue(self,el): # T(n)
 if self._tail==None: # Θ(1)
 self._tail=el # Θ(1)
 self._head=el # Θ(1) 
 else:
 self._tail.setNext(el) # Θ(1)
 el.setNext(None) # Θ(1)
 self._tail=el # Θ(1)
 return # Θ(1)

 'DEQUEUE' 
 def dequeue(self): # T(n)
 if self._head==None: # Θ(1)
 return None # Θ(1)
 else: # Θ(1)
 e=self._head # Θ(1)
 self._head=self._head.getNext() # Θ(1)
 if self._head==None: # Θ(1)
 self._tail=None # Θ(1)
 return and # Θ(1)
 
 'ToString'
 def __str__(self):
 p_corr=self._head
 output=""
 while p_corr!=None:
 if p_corr.getNext()!=None:
 output+="["+str(p_corr)+"]" + " - "
 else:
 output+="["+str(p_corr)+"]"
 p_corr=p_corr.getNext()
 return output
 
