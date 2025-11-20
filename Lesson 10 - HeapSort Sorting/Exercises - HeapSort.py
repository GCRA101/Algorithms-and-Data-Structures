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
Progettare un algoritmo che, dato in input un vettore che rappresenta un heap,
restituisca il valore minimo. Fare le opportune considerazioni sul costo 
computazionale.
'''

# Considerazioni
'''
In un Heap il valore minimo sara' sempre da ricercare fra le foglie dell'albero
(ovvero tra gli elementi/valori che non presentano figli). Quando l'albero e'
completo le foglie saranno tutte concentrate all'ultimo livello, mentre quando
l'albero e' incompleto vi saranno anche foglie al livello immediatamente 
precedente l'ultimo.
Scorrendo gli elementi dell'Heap, l'indice del primo elemento i che presenti il 
figlio destro e sinistro inesistenti (2i+1>=len(A) and 2i+2>=len(A)) sara' il
primo da cui partire nella ricerca del valore minimo' 
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# Algoritmo

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,22,3,8,5,32,33,81,12,18,54,42,38,101,9]
A3=[101,23,84,33,61,41,32,73,92,111,41,9]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


# HEAPIFY Function

def heapify(A,n,i):                             # T(n)=O(logn)            
    left=2*i+1                                  # Θ(1)             
    right=2*i+2                                 # Θ(1)
    if (left<n)and(A[left]>A[i]):               # Θ(1)
        iMax=left                               # Θ(1)
    else:                                       # Θ(1)
        iMax=i                                  # Θ(1)
    if (right<n)and(A[right]>A[iMax]):          # Θ(1)
        iMax=right                              # Θ(1)
    if iMax!=i:                                 # Θ(1)
        temp=A[i]                               # Θ(1)
        A[i]=A[iMax]                            # Θ(1)
        A[iMax]=temp                            # Θ(1)
        heapify(A,n,iMax)                       # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeap(A):                               # T(n)=O(n)
    m=len(A)                                    # Θ(1)           
    for i in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(A,m,i)                            
    return                                      # Θ(1)

# HEAPMINIMUM Function

def heapMinimum(A):                             # T(n)
    buildHeap(A)                                # O(n)
    iStart=(len(A)-1)//2                        # Θ(1)
    iMin=iStart                                 # Θ(1)
    for i in range(iStart,len(A)-1,1):          # log(n+1)*Θ(1)+Θ(1)
        if A[i+1]<A[i]:                         # Θ(1)
            iMin=i+1                            # Θ(1)
    return A[iMin]                              # Θ(1)
        

# Dimensione input: numero n di elementi nell'array A
# Costo Computazionale: T(n)=O(n)+Θ(1)+Θ(logn)+Θ(1)=O(n)

minA1=heapMinimum(A1)
minA2=heapMinimum(A2)
minA3=heapMinimum(A3)
minAworst=heapMinimum(Aworst)
minAbest=heapMinimum(Abest)



# ESERCIZI0 2 ################################################################

'''
Un Heap minimo e' un albero binario completo o quasi completo con la proprieta' 
che la chiave su ogni nodo e' minore o uguale alla chiave dei suoi figli. Si
modifichi l'algoritmo di Heap Sort in modo che la struttura dati di rirerimento 
sia un heap minimo e non un heap.'
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# Algoritmo

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


'FUNZIONI AUSILIARIE'

# HEAPIFY Function

def heapifyMin(A,n,i):                      # T(n)           
    left=2*i+1                              # Θ(1)         
    right=2*i+2                             # Θ(1)
    if (left<n)and(A[left]<A[i]):           # Θ(1)             ** != heapify 
        iMin=left                           # Θ(1)             ** != heapify
    else:                                   # Θ(1)
        iMin=i                              # Θ(1)             ** != heapify
    if (right<n)and(A[right]<A[iMin]):      # Θ(1)             ** != heapify
        iMin=right                          # Θ(1)             ** != heapify
    if iMin!=i:                             # Θ(1)             ** != heapify
        temp=A[i]                           # Θ(1)
        A[i]=A[iMin]                        # Θ(1)
        A[iMin]=temp                        # Θ(1)
        heapifyMin(A,n,iMin)                # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeapMin(A):                        # T(n)
    m=len(A)                                # Θ(1)       
    for i in range(m//2-1,-1,-1):           # n/2*O(logn)+Θ(1)
        heapifyMin(A,m,i)                            
    return                                  # Θ(1)
    

' FUNZIONE HEAPSORT'

def heapSortMin(A):                         # T(n)
    buildHeapMin(A)                         # O(n)
    for heapSize in range(len(A)-1,-1,-1):  # (n-1) + Θ(1)      
        temp=A[heapSize]                    # Θ(1)
        A[heapSize]=A[0]                    # Θ(1)
        A[0]=temp                           # Θ(1)
        heapifyMin(A,heapSize,0)            # O(logn)
    return                                  # Θ(1)


# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore coincidono.
# Il costo computazionale dei 3 algoritmi Heapify, BuildHeap e HeapSort e' 
# come segue:
# - Heapify:   T(n)=T(2/3n)+Θ(1)  -> T(n)=O(logn)
# - BuildHeap: T(n)=O(n)          -> T(n)=O(n)
# - HeapSort:  T(n)=O(nlogn)      -> T(n)=O(nlogn)


heapSortMin(A1)   
heapSortMin(A2) 
heapSortMin(A3) 
heapSortMin(Aworst)
heapSortMin(Abest)
