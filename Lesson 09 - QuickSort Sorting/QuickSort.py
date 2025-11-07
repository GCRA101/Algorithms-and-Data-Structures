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




# ALGORITMI DI ORDINAMENTO - QUICK SORT

'''
QUICK SORT 
L'algoritmo Quick Sort e' un algoritmo di ordinamento piu' avanzato e complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) e consente di ottenere il miglior costo computazionale possibile
per un algoritmo di ordinamento basato su confronti: O(nlogn).

* Confronto con MergeSort *
Esso si differenzia rispetto all'algoritmo di MergeSort nei seguenti punti:
    - Vantaggio: Riordinamento IN LOCO
            - Gli elementi del vettore vengono riordinati IN LOCO e cio'
              consente di aver una MIGLIORE COMPLESSITA' SPAZIALE
    - Svantaggio: Alto Computational Cost nel Caso Peggiore
            - Nel Caso Peggiore, il costo computazionale e' O(n^2) anziche' 
              O(nlogn). Il Caso Peggiore, in ogni caso, puo' essere facilmente
              evitato andando a RANDOMIZZARE/DISORDINARE i dati in input'
Conclusione: il QuickSort e' MEGLIO del MergeSort
Infatti, il QuickSort e' l'algoritmo di Ordinamento che viene in genere usato
nelle funzioni dei principali linguaggi di programmazione.

* Caratteristiche Principali *
Le caratteristiche principali dell'algoritmo MERGE SORT sono le seguenti:
    - RECURSIVE Algorithm
    - Tecnica Algoritmica del DIVIDE ET IMPERA
    - Equazione di Ricorrenza risolubile tramite Metodo Principale (Teorema
      Master)
    - Processo di ordinamento IN LOCO
    - Lavora meglio con sequenze di dati DISORDINATE
    
- Computational Cost: O(n^2)   (Caso Peggiore)
                        Ω(nlogn) (Caso Migliore)                    
'''

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]


def partition(A,indStart,indEnd):                  # S(n)
    pivot=A[indStart]                              # Θ(1)
    i=indStart                                     # Θ(1)
    j=indEnd                                       # Θ(1)
    while True:                                    # n*Θ(1)+Θ(1) 
        while A[i]<pivot:                          # Θ(1)
            i=i+1                                  # Θ(1)
        while A[j]>pivot:                          # Θ(1)
            j=j-1                                  # Θ(1)
        if i<j:                                    # Θ(1)
            temp=A[i]                              # Θ(1)
            A[i]=A[j]                              # Θ(1)
            A[j]=temp                              # Θ(1)
            i,j=i+1,j-1                            # Θ(1) 
        else:                                      # Θ(1)
            return j                               # Θ(1)


def quickSort(A,indStart,indEnd):                  # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=partition(A,indStart,indEnd)        # S(n)
        quickSort(A,indStart,indMid)               # T(n/2)
        quickSort(A,indMid+1,indEnd)               # T(n/2)
    return 


# Input size: numero n di elementi nell'array A
# Caso migliore e caso peggiore differiscono in base al livello di disordine
# dei dati in input.
# Se i dati in input sono gia' abbastanza ordinati, il pivot, se scelto sempre
# come il primo elemento del subarray, risultera' essere sovente lontano dalla
# mezzeria. Al contrario sara' sovente in prossimita' della mezzeria.
# Le equazioni di ricorrenza corrispondenti ai casi peggiore e migliore sopra
# illustrati sono come segue:
# - Caso Migliore: T(n)=2*T(n/2)+Θ(n)   -> T(n)=Ω(nlogn)
# - Caso Peggiore: T(n)=T(n-1)+Θ(n)     -> T(n)=O(n^2)
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
    quickSort(Alist,0,len(Alist)-1)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(5,100,1):
    Blist=list(range(0,i,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    quickSort(Blist,0,len(Blist)-1)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Quick Sort","Caso Peggiore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Quick Sort","Caso Migliore")

