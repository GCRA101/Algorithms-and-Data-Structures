

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:10:30 2023

@author: giorg
"""

'Import main libraries'
import math as math
import numpy as np
import time

import matplotlib.pyplot as plt





'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Scrivere the pseudocodice (e script python) of the funzioni Enqueue and Dequeue
when the queue sia implementata on a array
'''

# Considerazioni
'''L'array is a struttura data inerentemente statica. Cio' significa that
the sua dimension not puo' cambiare a time that is stato creato. 
The array on which to build the queue must therefore have a dimension as 
grande possibile and the slittamento of the elements dovuto to the operazioni of 
enqueing and dequeuing dev'essere gestito in senso circolare.
For essere certi that l'head and the tail not si invertano of ordine enough 
verify that l'array not sia pieno (first of each operazione of enqueueing)
o that not sia vuoto (first of each operazione of dequeueing).
Each time that the head o the tail raggiungono l'index last dell'array, 
to the step successivo li si fanno ripartire dall'index zero.'
''' 

'''
CLASSE CODA (QUEUE)
Costruita servendosi of the Struttura Data of ARRAY
'''

class Queue:
    
    # ATTRIBUTES
    _head=0
    _tail=-1
    nElem=0
    array=[]
    
    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METHODS

    'ENQUEUE'
    def enqueue(self,el):                       # T(n)
        'If l''array e'' pieno, not si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''index of tail'
        if 0<=self._tail<len(self.array)-1:
            self._tail+=1
        else:
            self._tail=0
        'Si aggiunge l''element in the nuova tail'
        self.array[self._tail]=el
        'Si aggiorna the contatore of the elements (cresce of a unita)'
        self.nElem+=1
        return
    

    'DEQUEUE'    
    def dequeue(self):
        'If l''array e'' vuoto, not si fa nulla'
        if self.nElem==0:
            return
        'Si rimuove l''element contained in thela head corrente'
        el=self.array[self._head]
        self.array[self._head]=None
        'Incremento dell''index of head'
        if self._head<len(self.array)-1:
            self._head+=1
        else:
            self._head=0
        'Si aggiorna the contatore of the elements (decresce of a unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrQueue=Queue(10)

'Enqueuing'
for the in range(3,40,2):
    arrQueue.enqueue(the)   
    print(arrQueue)
'Dequeuing'
for the in range(0,12,1):
    n=arrQueue.dequeue()
    print(arrQueue)
'Enqueing again'
for the in range(3,40,2):
    arrQueue.enqueue(the)   
    print(arrQueue)
    
    
    
    
# ESERCIZIO 2 ################################################################

'''
Scrivere the pseudocodice (e script python) of the funzioni Push and Pop
when the stack sia implementata on a array
'''

# Considerazioni
'''L'array is a struttura data inerentemente statica. Cio' significa that
the sua dimension not puo' cambiare a time that is stato creato. 
The array on which to build the stack must therefore have a dimension as 
grande possibile. A time that l'array is stato completamente riempito,
indeed, not si potra' pushare alcun element.
Analogamente a time that l'array were vuoto, not si potra poppare alcun 
element.
For ottenere what' bastera' tenere the conto of the elements contained in thel'array
through a opportuno contatore.'
''' 

'''
CLASSE PILA (STACK)
Costruita servendosi of the Struttura Data of ARRAY
'''

class Stack:
    
    # ATTRIBUTES
    _top=-1
    nElem=0
    array=[]
    
    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METHODS

    'PUSH'
    def push(self,el):                       # T(n)
        'If l''array e'' pieno, not si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''index of top'
        self._top+=1
        'Si aggiunge l''element in cima'
        self.array[self._top]=el
        'Si aggiorna the contatore of the elements (cresce of a unita)'
        self.nElem+=1
        return
    

    'POP'    
    def pop(self):
        'If l''array e'' vuoto, not si fa nulla'
        if self.nElem==0:
            return
        'Si rimuove l''element in cima'
        el=self.array[self._top]
        self.array[self._top]=None
        'Decremento dell''index of top'
        self._top-=1
        'Si aggiorna the contatore of the elements (decresce of a unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrStack=Stack(10)

'Pushing'
for the in range(3,40,2):
    arrStack.push(the)   
    print(arrStack)
'Popping'
for the in range(0,12,1):
    n=arrStack.pop()
    print(arrStack)
'Pushing again'
for the in range(3,40,2):
    arrStack.push(the)   
    print(arrStack)