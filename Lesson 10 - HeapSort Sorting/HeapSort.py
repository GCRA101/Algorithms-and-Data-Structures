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




# SORTING ALGORITHMS - HEAP SORT

'''
HEAP SORT 

The algorithm Heap Sort e' an algorithm for sorting piu' avanzato e complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) e consente of ottenere the miglior costo computazionale possibile
for an algorithm for sorting based on comparisons: O(nlogn) sia nel case 
peggiore sia nel best case. Inoltre consente l'sorting in loco (al 
contrario del MergeSort). 
Unico limite consiste nel fatto that esso puo' lavorare only with strutture data
of tipo Heap.'

* Caratteristiche Principali *
The caratteristiche principali delthe algorithm HEAP SORT are the following:
    - RECURSIVE Algorithm
    - Si serve of two funzioni ausiliarie: Heapify e BuildHeap
    - Recurrence Equation solvable through the Master Method (Teorema
      Master)
    - Processo of sorting IN LOCO
    - Lavora only with strutture data of tipo Heap
    
- Computational Cost: Θ(nlogn)

'''

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


'FUNZIONI AUSILIARIE'

# HEAPIFY Function

def heapify(To,n,the):                             # T(n)               '--(To)--'
    left=2*the+1                                  # Θ(1)               '--(B)--'
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

def buildHeap(To):                               # T(n)
    m=len(To)                                    # Θ(1)               '--(C)--'
    for the in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(To,m,the)                            
    return                                      # Θ(1)
    

' function HEAPSORT'

def heapSort(To):                            # T(n)
    buildHeap(To)                            # O(n)
    for heapSize in range(len(To)-1,-1,-1):   # (n-1) + Θ(1)        
        temp=To[heapSize]                    # Θ(1)
        To[heapSize]=To[0]                    # Θ(1)
        To[0]=temp                           # Θ(1)
        heapify(To,heapSize,0)               # O(logn)                '--(D)--'
    return                                  # Θ(1)

    
'''
Note Importanti
(To): Passare the parametro variabile n nella function heapify e' cio' that
     consente of considerare a porzione of vector To always piu' piccola (
     1 element less at each cycle nella function heapSort) without having to 
     passare the corrispondente sotto-vector of To. To rimane always della stessa 
     lunghezza cosi from poter essere modificato e sorted in loco mentre the 
     porzione of esso that si va via via to considerare e' compresa between 0 e n.
(B): left=2*the e right=2*the+1 sarebbero corretti only if the first indice dell'array
     fosse 1! Since the first index e' always =0, dobbiamo aggiungere a 1
     alle espressioni sopra in modo that, quando the=0 -> left=1 e right=2.
     Abbiamo quindi left=2*the+1 e right=2*the+2!
(C): Chiamiamo the function heapify sul vector To, with dimensione costante m
     e element of index variabile the dalla mezzeria del vector alla posizione
     iniziale (indice 0)
(D): Richiamiamo the function heapify passandole always the stesso vector To,
     the stesso index of radice 0 ma with index massimo that si riduce of 1 
     ad each ciclo.

'''

# Input size: number n of elements in array To
# Best case and worst case coincide.
# The costo computazionale dei 3 algoritmi Heapify, BuildHeap e HeapSort e' 
# as segue:
# - Heapify:   T(n)=T(2/3n)+Θ(1)  -> T(n)=O(logn)
# - BuildHeap: T(n)=O(n)          -> T(n)=O(n)
# - HeapSort:  T(n)=O(nlogn)      -> T(n)=O(nlogn)


heapSort(A1)   
heapSort(A2) 
heapSort(A3) 
heapSort(Aworst)
heapSort(Abest)





# GRAPHICAL REPRESENTATION


def rappresentazioneGrafica(data_x,data_y,tolerance,title,legendLabel):
    
    delta_max = tolerance # maximum difference in y between two points
    delta = 0 # running correction value
    data_cor = [] # corrected array
    data_cor.append(data_y[0])   # we append two first points
    data_cor.append(data_y[1])
    the=0
    
    for the in range(0,len(data_x)-2): # two first points are allready appended
        the += 2
        delta_i = data_y[the] - data_y[the-1]
        if np.abs(delta_i) > delta_max:
            delta += (delta_i - (data_cor[the-1] - data_cor[the-2]))
            data_cor.append(data_y[the]-delta)
        else:
            data_cor.append(data_y[the]-delta)
    
    
    plt.plot(data_x, data_cor,label=legendLabel)
    
    plt.xlabel('Inputs')
    plt.ylabel('Time [secs]')
    plt.legend()
    plt.title(title)



stepsA=[]
for the in range(5,100,1):
    Alist=list(range(0,the,1))    # DATI  IN INPUT ORDINATI
    tic=time.perf_counter_ns()
    heapSort(Alist)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(5,100,1):
    Blist=list(range(0,the,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    heapSort(Blist)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms "  
                        "- Heap Sort","worst case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms "  
                        "- Heap Sort","best case")

