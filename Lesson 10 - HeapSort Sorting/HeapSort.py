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




# ALGORITMI DI ORDINAMENTO - HEAP SORT

'''
HEAP SORT 

L'algoritmo Heap Sort e' un algoritmo di ordinamento piu' avanzato e complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) e consente di ottenere il miglior costo computazionale possibile
per un algoritmo di ordinamento basato su confronti: O(nlogn) sia nel caso 
peggiore sia nel caso migliore. Inoltre consente l'ordinamento in loco (al 
contrario del MergeSort). 
Unico limite consiste nel fatto che esso puo' lavorare solo con strutture dati
di tipo Heap.'

* Caratteristiche Principali *
Le caratteristiche principali dell'algoritmo HEAP SORT sono le seguenti:
    - RECURSIVE Algorithm
    - Si serve di due funzioni ausiliarie: Heapify e BuildHeap
    - Equazione di Ricorrenza risolubile tramite Metodo Principale (Teorema
      Master)
    - Processo di ordinamento IN LOCO
    - Lavora solo con strutture dati di tipo Heap
    
- Computational Cost: Θ(nlogn)

'''

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


'FUNZIONI AUSILIARIE'

# HEAPIFY Function

def heapify(A,n,i):                             # T(n)               '--(A)--'
    left=2*i+1                                  # Θ(1)               '--(B)--'
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

def buildHeap(A):                               # T(n)
    m=len(A)                                    # Θ(1)               '--(C)--'
    for i in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(A,m,i)                            
    return                                      # Θ(1)
    

' FUNZIONE HEAPSORT'

def heapSort(A):                            # T(n)
    buildHeap(A)                            # O(n)
    for heapSize in range(len(A)-1,-1,-1):   # (n-1) + Θ(1)        
        temp=A[heapSize]                    # Θ(1)
        A[heapSize]=A[0]                    # Θ(1)
        A[0]=temp                           # Θ(1)
        heapify(A,heapSize,0)               # O(logn)                '--(D)--'
    return                                  # Θ(1)

    
'''
Note Importanti
(A): Passare il parametro variabile n nella funzione heapify e' cio' che
     consente di considerare una porzione di vettore A sempre piu' piccola (
     1 elemento in meno ad ogni ciclo nella funzione heapSort) senza dover 
     passare il corrispondente sotto-vettore di A. A rimane sempre della stessa 
     lunghezza cosi da poter essere modificato e ordinato in loco mentre la 
     porzione di esso che si va via via a considerare e' compresa tra 0 e n.
(B): left=2*i e right=2*i+1 sarebbero corretti solo se il primo indice dell'array
     fosse 1! Dato che il primo indice e' sempre =0, dobbiamo aggiungere un 1
     alle espressioni sopra in modo che, quando i=0 -> left=1 e right=2.
     Abbiamo quindi left=2*i+1 e right=2*i+2!
(C): Chiamiamo la funzione heapify sul vettore A, con dimensione costante m
     e elemento di indice variabile i dalla mezzeria del vettore alla posizione
     iniziale (indice 0)
(D): Richiamiamo la funzione heapify passandole sempre lo stesso vettore A,
     lo stesso indice di radice 0 ma con indice massimo che si riduce di 1 
     ad ogni ciclo.

'''

# Input size: numero n di elementi nell'array A
# Best case and worst case coincide.
# Il costo computazionale dei 3 algoritmi Heapify, BuildHeap e HeapSort e' 
# come segue:
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
    i=0
    
    for i in range(0,len(data_x)-2): # two first points are allready appended
        i += 2
        delta_i = data_y[i] - data_y[i-1]
        if np.abs(delta_i) > delta_max:
            delta += (delta_i - (data_cor[i-1] - data_cor[i-2]))
            data_cor.append(data_y[i]-delta)
        else:
            data_cor.append(data_y[i]-delta)
    
    
    plt.plot(data_x, data_cor,label=legendLabel)
    
    plt.xlabel('Inputs')
    plt.ylabel('Time [secs]')
    plt.legend()
    plt.title(title)



stepsA=[]
for i in range(5,100,1):
    Alist=list(range(0,i,1))    # DATI  IN INPUT ORDINATI
    tic=time.perf_counter_ns()
    heapSort(Alist)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(5,100,1):
    Blist=list(range(0,i,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    heapSort(Blist)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Heap Sort","Caso Peggiore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Heap Sort","Caso Migliore")

