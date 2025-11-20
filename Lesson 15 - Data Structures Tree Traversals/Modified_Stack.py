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
CLASSE PILA (STACK)
Costruita servendosi of the Struttura Data of LISTA PUNTATA SINGOLA and modificata
nel suo funzionamento for essere usata for the VISITA IN PREORDINE iterative 
of a ALBERO BINARIO.
The Stack si serve of Record Singoli while l'tree binario of Record Doppi. 
The segreto consiste nell'immagazzinare the riferimento to ciascun nodo dell'tree
nel campo Given and the riferimento al record singolo successivo nel campo Next.
The Stack is therefore costituita from a successione of record singoli that si puntano
to vicenda in sequenza and where ciascuno of essi contiene the riferimento to 
ciascun nodo corrispondente dell'Tree Binario.
Therefore...
 - Campo DATA : Riferimento to Nodo Tree Binario
 - Campo NEXT : Riferimento to Record Singolo Successivo in the Stack
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
 def push(self,el): # T(n)
 nuovoRecord=RecordSingolo(el,None) # Θ(1)
 nuovoRecord.setNext(self._top) # Θ(1)
 self._top=nuovoRecord # Θ(1)
 return # Θ(1)

 'POP' 
 def pop(self): # T(n)
 if self._top==None: # Θ(1)
 return None # Θ(1)
 else: # Θ(1)
 el=self._top.getData() # Θ(1)
 self._top=self._top.getNext() # Θ(1)
 return el # Θ(1)
 
 'LENGTH'
 def length(self): # T(n)
 refRecord=self._top # Θ(1)
 the=0 # Θ(1)
 while refRecord!=None: # n*Θ(1)+Θ(1)
 the+=1 # Θ(1)
 refRecord=refRecord.getNext() # Θ(1)
 return the # Θ(1)
 
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
 
