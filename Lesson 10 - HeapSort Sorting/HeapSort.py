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




# SORTING ALGORITHMS - HEAP SORT

'''
HEAP SORT 

The algorithm Heap Sort is an algorithm for sorting piu' avanzato and complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) and consente of ottenere the miglior computational cost possibile
for an algorithm for sorting based on comparisons: O(nlogn) sia nel case 
peggiore sia nel best case. Inoltre consente l'sorting in loco (al 
contrario del MergeSort). 
Unico limite consiste nel fatto that esso puo' lavorare only with strutture data
of tipo Heap.'

* Caratteristiche Principali *
The caratteristiche principali than the algorithm HEAP SORT are the following:
 - RECURSIVE Algorithm
 - Si serve of two funzioni ausiliarie: Heapify and BuildHeap
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

def heapify(To,n,the): # T(n) '--(To)--'
 left=2*the+1 # Θ(1) '--(B)--'
 right=2*the+2 # Θ(1)
 if (left<n)and(To[left]>To[the]): # Θ(1)
 iMax=left # Θ(1)
 else: # Θ(1)
 iMax=the # Θ(1)
 if (right<n)and(To[right]>To[iMax]): # Θ(1)
 iMax=right # Θ(1)
 if iMax!=the: # Θ(1)
 temp=To[the] # Θ(1)
 To[the]=To[iMax] # Θ(1)
 To[iMax]=temp # Θ(1)
 heapify(To,n,iMax) # T(2/3n)
 return
 
# BUILDHEAP Function

def buildHeap(To): # T(n)
 m=len(To) # Θ(1) '--(C)--'
 for the in range(m//2-1,-1,-1): # n/2*O(logn)+Θ(1)
 heapify(To,m,the) 
 return # Θ(1)
 

' function HEAPSORT'

def heapSort(To): # T(n)
 buildHeap(To) # O(n)
 for heapSize in range(len(To)-1,-1,-1): # (n-1) + Θ(1) 
 temp=To[heapSize] # Θ(1)
 To[heapSize]=To[0] # Θ(1)
 To[0]=temp # Θ(1)
 heapify(To,heapSize,0) # O(logn) '--(D)--'
 return # Θ(1)

 
'''
Important Notes
(A): Passing the variable parameter n to the heapify function is what
 allows considering a progressively smaller portion of vector A (
 1 element less at each cycle in the heapSort function) without having to 
 pass the corresponding sub-vector of A. A always remains the same 
 length so that it can be modified and sorted in place while the 
 portion of it to be considered is comprised between 0 and n.
(B): left=2*i and right=2*i+1 would be correct only if the first index of the array
 were 1! Since the first index is always =0, we must add 1
 to the above expressions so that, when i=0 -> left=1 and right=2.
 We therefore have left=2*i+1 and right=2*i+2!
(C): We call the heapify function on vector A, with constant dimension m
 and element of variable index i from the middle of the vector to the initial
 position (index 0)
(D): We call the heapify function passing it always the same vector A,
 the same root index 0 but with maximum index that decreases by 1 
 at each cycle.

'''

# Input size: number n of elements in array A
# Best case and worst case coincide.
# The computational cost of the 3 algorithms Heapify, BuildHeap and HeapSort is 
# as follows:
# - Heapify: T(n)=T(2/3n)+Θ(1) -> T(n)=O(logn)
# - BuildHeap: T(n)=O(n) -> T(n)=O(n)
# - HeapSort: T(n)=O(nlogn) -> T(n)=O(nlogn)


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
 data_cor.append(data_y[0]) # we append two first points
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
 Alist=list(range(0,the,1)) # DATI IN INPUT ORDINATI
 tic=time.perf_counter_ns()
 heapSort(Alist)
 toc=time.perf_counter_ns()
 stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(5,100,1):
 Blist=list(range(0,the,1))
 'RANDOMIZZAZIONE DATI IN INPUT!'
 random.shuffle(Blist) # DATI IN INPUT DISORDINATI
 tic=time.perf_counter_ns()
 heapSort(Blist)
 toc=time.perf_counter_ns()
 stepsB.append(abs(round(toc-tic,8)))

 
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms " 
 "- Heap Sort","worst case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms " 
 "- Heap Sort","best case")

