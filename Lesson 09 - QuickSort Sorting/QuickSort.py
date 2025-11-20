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




# SORTING ALGORITHMS - QUICK SORT

'''
QUICK SORT 
The algorithm Quick Sort is an algorithm for sorting piu' avanzato and complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) and consente of ottenere the miglior computational cost possibile
for an algorithm for sorting based on comparisons: O(nlogn).

* Confronto with MergeSort *
Esso si differenzia rispetto althe algorithm of MergeSort nei seguenti punti:
    - Advantage: IN-PLACE reordering
            - The elements del vector vengono riordinati IN LOCO and what'
              consente of aver a MIGLIORE complexity' SPAZIALE
    - Sadvantage: Alto Computational Cost nel worst case
            - Nel worst case, the computational cost is O(n^2) anziche' 
              O(nlogn). The worst case, in any case, can be easily
              evitato andando to RANDOMIZZARE/DISORDINARE the given as input'
Conclusione: the QuickSort is MEGLIO del MergeSort
Indeed, the QuickSort is the algorithm of sorting that viene in genere usato
in the funzioni dei principali linguaggi of programmazione.

* Caratteristiche Principali *
The caratteristiche principali than the algorithm MERGE SORT are the following:
    - RECURSIVE Algorithm
    - Tecnica Algoritmica del DIVIDE ET IMPERA
    - Recurrence Equation solvable through the Master Method (Teorema
      Master)
    - Processo of sorting IN LOCO
    - Lavora meglio with sequenze of data DISORDINATE
    
- Computational Cost: O(n^2)   (worst case)
                        Ω(nlogn) (best case)                    
'''

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


def partition(To,indStart,indEnd):                  # S(n)
    pivot=To[indStart]                              # Θ(1)
    the=indStart                                     # Θ(1)
    j=indEnd                                       # Θ(1)
    while True:                                    # n*Θ(1)+Θ(1) 
        while To[the]<pivot:                          # Θ(1)
            the=the+1                                  # Θ(1)
        while To[j]>pivot:                          # Θ(1)
            j=j-1                                  # Θ(1)
        if the<j:                                    # Θ(1)
            temp=To[the]                              # Θ(1)
            To[the]=To[j]                              # Θ(1)
            To[j]=temp                              # Θ(1)
            the,j=the+1,j-1                            # Θ(1) 
        else:                                      # Θ(1)
            return j                               # Θ(1)


def quickSort(To,indStart,indEnd):                  # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=partition(To,indStart,indEnd)        # S(n)
        quickSort(To,indStart,indMid)               # T(n/2)
        quickSort(To,indMid+1,indEnd)               # T(n/2)
    return 


# Input size: number n of elements in array To
# Best case and worst case differiscono in base al level of disordine
# dei given as input.
# If the data given as input are already fairly sorted, the pivot, if always chosen
# as the first element of the subarray, will often be far from the
# middle. On the contrary it will often be in proximity to the middle.
# The recurrence equations corresponding to the worst and best cases above
# illustrated are as follows:
# - best case: T(n)=2*T(n/2)+Θ(n)   -> T(n)=Ω(nlogn)
# - worst case: T(n)=T(n-1)+Θ(n)     -> T(n)=O(n^2)
#


quickSort(A1,0,len(A1)-1)   
quickSort(A2,0,len(A2)-1) 
quickSort(A3,0,len(A3)-1) 
quickSort(Aworst,0,len(Aworst)-1)
quickSort(Abest,0,len(Abest)-1)





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
    quickSort(Alist,0,len(Alist)-1)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(5,100,1):
    Blist=list(range(0,the,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    quickSort(Blist,0,len(Blist)-1)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms "  
                        "- Quick Sort","worst case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms "  
                        "- Quick Sort","best case")

