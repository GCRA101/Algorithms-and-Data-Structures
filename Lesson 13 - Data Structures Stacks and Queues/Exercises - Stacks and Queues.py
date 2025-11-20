

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
Scrivere lo pseudocodice (e script python) delle funzioni Enqueue e Dequeue
quando la coda sia implementata su un array
'''

# Considerazioni
'''L'array e' una struttura dati inerentemente statica. Cio' significa che
la sua dimensione non puo' cambiare una volta che e' stato creato. 
L'array su cui costruire la coda deve quindi avere una dimensione la piu' 
grande possibile e lo slittamento degli elementi dovuto alle operazioni di 
enqueing e dequeuing dev'essere gestito in senso circolare.
Per essere certi che l'head e la tail non si invertano di ordine basta 
verificare che l'array non sia pieno (prima di ogni operazione di enqueueing)
o che non sia vuoto (prima di ogni operazione di dequeueing).
Ogni volta che la head o la tail raggiungono l'indice ultimo dell'array, 
allo step successivo li si fanno ripartire dall'indice zero.'
''' 

'''
CLASSE CODA (QUEUE)
Costruita servendosi della Struttura Dati di ARRAY
'''

class Coda:
    
    # ATTRIBUTI
    _head=0
    _tail=-1
    nElem=0
    array=[]
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METODI

    'ENQUEUE'
    def enqueue(self,el):                       # T(n)
        'Se l''array e'' pieno, non si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''indice di tail'
        if 0<=self._tail<len(self.array)-1:
            self._tail+=1
        else:
            self._tail=0
        'Si aggiunge l''elemento nella nuova tail'
        self.array[self._tail]=el
        'Si aggiorna il contatore degli elementi (cresce di un unita)'
        self.nElem+=1
        return
    

    'DEQUEUE'    
    def dequeue(self):
        'Se l''array e'' vuoto, non si fa nulla'
        if self.nElem==0:
            return
        'Si rimuove l''elemento contenuto nella head corrente'
        el=self.array[self._head]
        self.array[self._head]=None
        'Incremento dell''indice di head'
        if self._head<len(self.array)-1:
            self._head+=1
        else:
            self._head=0
        'Si aggiorna il contatore degli elementi (decresce di un unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrQueue=Coda(10)

'Enqueuing'
for i in range(3,40,2):
    arrQueue.enqueue(i)   
    print(arrQueue)
'Dequeuing'
for i in range(0,12,1):
    n=arrQueue.dequeue()
    print(arrQueue)
'Enqueing again'
for i in range(3,40,2):
    arrQueue.enqueue(i)   
    print(arrQueue)
    
    
    
    
# ESERCIZIO 2 ################################################################

'''
Scrivere lo pseudocodice (e script python) delle funzioni Push e Pop
quando la pila sia implementata su un array
'''

# Considerazioni
'''L'array e' una struttura dati inerentemente statica. Cio' significa che
la sua dimensione non puo' cambiare una volta che e' stato creato. 
L'array su cui costruire la pila deve quindi avere una dimensione la piu' 
grande possibile. Una volta che l'array e' stato completamente riempito,
infatti, non si potra' pushare alcun elemento.
Analogamente una volta che l'array fosse vuoto, non si potra poppare alcun 
elemento.
Per ottenere cio' bastera' tenere il conto degli elementi contenuti nell'array
tramite un opportuno contatore.'
''' 

'''
CLASSE PILA (STACK)
Costruita servendosi della Struttura Dati di ARRAY
'''

class Pila:
    
    # ATTRIBUTI
    _top=-1
    nElem=0
    array=[]
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,maxDim):
        self.array=[None]*maxDim
        
    # METODI

    'PUSH'
    def push(self,el):                       # T(n)
        'Se l''array e'' pieno, non si fa nulla'
        if self.nElem==len(self.array):
            return
        'Incremento dell''indice di top'
        self._top+=1
        'Si aggiunge l''elemento in cima'
        self.array[self._top]=el
        'Si aggiorna il contatore degli elementi (cresce di un unita)'
        self.nElem+=1
        return
    

    'POP'    
    def pop(self):
        'Se l''array e'' vuoto, non si fa nulla'
        if self.nElem==0:
            return
        'Si rimuove l''elemento in cima'
        el=self.array[self._top]
        self.array[self._top]=None
        'Decremento dell''indice di top'
        self._top-=1
        'Si aggiorna il contatore degli elementi (decresce di un unita)'
        self.nElem-=1
        return el
    
    'ToString'
    def __str__(self):
        return str(self.array)
        

'TEST'

arrStack=Pila(10)

'Pushing'
for i in range(3,40,2):
    arrStack.push(i)   
    print(arrStack)
'Popping'
for i in range(0,12,1):
    n=arrStack.pop()
    print(arrStack)
'Pushing again'
for i in range(3,40,2):
    arrStack.push(i)   
    print(arrStack)