

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
Scrivere the pseudocodice (e script python) delle funzioni Enqueue e Dequeue
quando the coda sia implementata on a array
'''

# Considerazioni
'''L'array e' a struttura data inerentemente statica. Cio' significa that
the sua dimensione not puo' cambiare a volta that e' stato creato. 
L'array on cui costruire the coda deve quindi avere a dimensione the piu' 
grande possibile e the slittamento degli elementi dovuto alle operazioni of 
enqueing e dequeuing dev'essere gestito in senso circolare.
For essere certi that l'head e the tail not si invertano of ordine basta 
verificare that l'array not sia pieno (first of each operazione of enqueueing)
o that not sia vuoto (first of each operazione of dequeueing).
Each volta that the head o the tail raggiungono l'index last dell'array, 
allo step successivo li si fanno ripartire dall'indice zero.'
''' 

'''
CLASSE CODA (QUEUE)
Costruita servendosi della Struttura Data of ARRAY
'''

class Coda:
    
    # ATTRIBUTES
    _head=0
    _tail=-1
    nElem=0
    array=[]
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METHODS

    'ENQUEUE'
    def enqueue(self,el):                       # T(n)
        'If l''array e'' pieno, not si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''indice of tail'
        if 0<=self._tail<len(self.array)-1:
            self._tail+=1
        else:
            self._tail=0
        'Si aggiunge l''element nella nuova tail'
        self.array[self._tail]=el
        'Si aggiorna the contatore degli elementi (cresce of a unita)'
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
        'Incremento dell''indice of head'
        if self._head<len(self.array)-1:
            self._head+=1
        else:
            self._head=0
        'Si aggiorna the contatore degli elementi (decresce of a unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrQueue=Coda(10)

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
Scrivere the pseudocodice (e script python) delle funzioni Push e Pop
quando the pila sia implementata on a array
'''

# Considerazioni
'''L'array e' a struttura data inerentemente statica. Cio' significa that
the sua dimensione not puo' cambiare a volta that e' stato creato. 
L'array on cui costruire the pila deve quindi avere a dimensione the piu' 
grande possibile. A volta that l'array e' stato completamente riempito,
indeed, not si potra' pushare alcun element.
Analogamente a volta that l'array fosse vuoto, not si potra poppare alcun 
element.
For ottenere cio' bastera' tenere the conto degli elementi contained in thel'array
through a opportuno contatore.'
''' 

'''
CLASSE PILA (STACK)
Costruita servendosi della Struttura Data of ARRAY
'''

class Pila:
    
    # ATTRIBUTES
    _top=-1
    nElem=0
    array=[]
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METHODS

    'PUSH'
    def push(self,el):                       # T(n)
        'If l''array e'' pieno, not si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''indice of top'
        self._top+=1
        'Si aggiunge l''element in cima'
        self.array[self._top]=el
        'Si aggiorna the contatore degli elementi (cresce of a unita)'
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
        'Decremento dell''indice of top'
        self._top-=1
        'Si aggiorna the contatore degli elementi (decresce of a unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrStack=Pila(10)

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