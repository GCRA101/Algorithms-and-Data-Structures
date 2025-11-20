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
Design an algorithm that, given as input a vector that rappresenta a heap,
restituisca the value minimo. Fare the opportune considerazioni sul costo 
computazionale.
'''

# Considerazioni
'''
In a Heap the value minimo sara' always from ricercare between the foglie dell'albero
(that is between the elementi/valori that not presentano figli). Quando l'albero e'
completo the foglie saranno all concentrate all'last livello, mentre quando
l'albero e' incompleto vi saranno also foglie al livello immediatamente 
precedente l'last.
Scorrendo the elements dell'Heap, l'index del first element the that presenti the 
figlio destro e sinistro inesistenti (2i+1>=len(To) and 2i+2>=len(To)) sara' the
first from cui partire nella ricerca del value minimo' 
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# algorithm

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,22,3,8,5,32,33,81,12,18,54,42,38,101,9]
A3=[101,23,84,33,61,41,32,73,92,111,41,9]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


# HEAPIFY Function

def heapify(To,n,the):                             # T(n)=O(logn)            
    left=2*the+1                                  # Θ(1)             
    right=2*the+2                                 # Θ(1)
    if (left<n)and(To[left]>To[the]):               # Θ(1)
        iMax=left                               # Θ(1)
    else:                                       # Θ(1)
        iMax=the                                  # Θ(1)
    if (right<n)and(To[right]>To[iMax]):          # Θ(1)
        iMax=right                              # Θ(1)
    if iMax!=the:                                 # Θ(1)
        temp=To[the]                               # Θ(1)
        To[the]=To[iMax]                            # Θ(1)
        To[iMax]=temp                            # Θ(1)
        heapify(To,n,iMax)                       # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeap(To):                               # T(n)=O(n)
    m=len(To)                                    # Θ(1)           
    for the in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(To,m,the)                            
    return                                      # Θ(1)

# HEAPMINIMUM Function

def heapMinimum(To):                             # T(n)
    buildHeap(To)                                # O(n)
    iStart=(len(To)-1)//2                        # Θ(1)
    iMin=iStart                                 # Θ(1)
    for the in range(iStart,len(To)-1,1):          # log(n+1)*Θ(1)+Θ(1)
        if To[the+1]<To[the]:                         # Θ(1)
            iMin=the+1                            # Θ(1)
    return To[iMin]                              # Θ(1)
        

# Input size: number n of elements in array To
# Computational Cost: T(n)=O(n)+Θ(1)+Θ(logn)+Θ(1)=O(n)

minA1=heapMinimum(A1)
minA2=heapMinimum(A2)
minA3=heapMinimum(A3)
minAworst=heapMinimum(Aworst)
minAbest=heapMinimum(Abest)



# ESERCIZI0 2 ################################################################

'''
A Heap minimo e' a albero binario completo o quasi completo with the proprieta' 
that the key on each nodo e' minore o uguale alla key dei suoi figli. Si
modifichi the algorithm of Heap Sort in modo that the struttura given of rirerimento 
sia a heap minimo e not a heap.'
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# algorithm

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


'FUNZIONI AUSILIARIE'

# HEAPIFY Function

def heapifyMin(To,n,the):                      # T(n)           
    left=2*the+1                              # Θ(1)         
    right=2*the+2                             # Θ(1)
    if (left<n)and(To[left]<To[the]):           # Θ(1)             ** != heapify 
        iMin=left                           # Θ(1)             ** != heapify
    else:                                   # Θ(1)
        iMin=the                              # Θ(1)             ** != heapify
    if (right<n)and(To[right]<To[iMin]):      # Θ(1)             ** != heapify
        iMin=right                          # Θ(1)             ** != heapify
    if iMin!=the:                             # Θ(1)             ** != heapify
        temp=To[the]                           # Θ(1)
        To[the]=To[iMin]                        # Θ(1)
        To[iMin]=temp                        # Θ(1)
        heapifyMin(To,n,iMin)                # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeapMin(To):                        # T(n)
    m=len(To)                                # Θ(1)       
    for the in range(m//2-1,-1,-1):           # n/2*O(logn)+Θ(1)
        heapifyMin(To,m,the)                            
    return                                  # Θ(1)
    

' function HEAPSORT'

def heapSortMin(To):                         # T(n)
    buildHeapMin(To)                         # O(n)
    for heapSize in range(len(To)-1,-1,-1):  # (n-1) + Θ(1)      
        temp=To[heapSize]                    # Θ(1)
        To[heapSize]=To[0]                    # Θ(1)
        To[0]=temp                           # Θ(1)
        heapifyMin(To,heapSize,0)            # O(logn)
    return                                  # Θ(1)


# Input size: number n of elements in array To
# Best case and worst case coincide.
# The costo computazionale dei 3 algoritmi Heapify, BuildHeap e HeapSort e' 
# as segue:
# - Heapify:   T(n)=T(2/3n)+Θ(1)  -> T(n)=O(logn)
# - BuildHeap: T(n)=O(n)          -> T(n)=O(n)
# - HeapSort:  T(n)=O(nlogn)      -> T(n)=O(nlogn)


heapSortMin(A1)   
heapSortMin(A2) 
heapSortMin(A3) 
heapSortMin(Aworst)
heapSortMin(Abest)
