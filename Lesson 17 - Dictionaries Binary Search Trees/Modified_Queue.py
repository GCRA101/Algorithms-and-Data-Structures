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
Costruita servendosi of the Struttura Data of LISTA PUNTATA SINGOLA and modificata
nel suo funzionamento for essere usata for the VISITA PER LIVELLI of a ALBERO
BINARIO.
The Queue si serve of Record Singoli while l'tree binario of Record Doppi. 
The segreto consiste nell'immagazzinare the riferimento to ciascun nodo dell'tree
nel campo Given and the riferimento al record singolo successivo nel campo Next.
The Queue is therefore costituita from a successione of record singoli that si puntano
to vicenda in sequenza and where ciascuno of essi contiene the riferimento to 
ciascun nodo corrispondente dell'Tree Binario.
Therefore...
 - Campo DATA : Riferimento to Nodo Tree Binario
 - Campo NEXT : Riferimento to Record Singolo Successivo in the Queue

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
 # Creiamo a nuovo Record Singolo that contiene the riferimento 
 # al nodo dell'tree binario nel suo campo Given.
 self._tail=RecordSingolo() # Θ(1)
 self._tail.setData(el) # Θ(1)
 self._tail.setNext(None) # Θ(1) 
 self._head=self._tail # Θ(1) 
 else: # Θ(1)
 # Creiamo a nuovo Record Singolo that contiene the riferimento 
 # al nodo dell'tree binario nel suo campo Given.
 nuovoRecord=RecordSingolo(el,None) # Θ(1)
 self._tail.setNext(nuovoRecord) # Θ(1)
 self._tail=self._tail.getNext() # Θ(1)
 return # Θ(1)


 'DEQUEUE' 
 def dequeue(self): # T(n)
 if self._head==None: # Θ(1)
 return None # Θ(1)
 else: # Θ(1)
 # Si scoda the record singolo of testa (head) and si ritorna 
 # to the user the given contained in the suo campo Given...that is 
 # the riferimento al corrispondente Nodo dell'tree binario.
 e=self._head.getData() # Θ(1)
 self._head=self._head.getNext() # Θ(1)
 if self._head==None: # Θ(1)
 self._tail=None # Θ(1)
 return and # Θ(1)
 
 
 'SIZE'
 def size(self): # T(n)
 refRecord=self._head # Θ(1)
 the=0 # Θ(1)
 while refRecord!=None: # n*Θ(1)+Θ(1)
 refRecord=refRecord.getNext() # Θ(1)
 the+=1 # Θ(1)
 return the # Θ(1)
 
 
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
 
