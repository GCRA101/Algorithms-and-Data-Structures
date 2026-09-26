###############################################################################
# ORDINAMENTO - MERGE SORT ####################################################
###############################################################################
'MERGESORT ___________________________________________________________________'


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




# ALGORITMI DI ORDINAMENTO - MERGE SORT

'''
MERGE SORT 
L'algoritmo Merge Sort e' un algoritmo di ordinamento piu' avanzato e complesso
rispetto agli algoritmi naif studiati finora (Insertion Sort, Selection Sort e
Bubble Sort) e consente di ottenere il miglior costo computazionale possibile
per un algoritmo di ordinamento basato su confronti: O(nlogn).
Le caratteristiche principali dell'algoritmo MERGE SORT sono le seguenti:
    - Algoritmo RICORSIVO
    - Tecnica Algoritmica del DIVIDE ET IMPERA
    - Equazione di Ricorrenza risolubile tramite Metodo Principale (Teorema
      Master)
    - Processo di ordinamento NON IN LOCO
    
- Costo Computazionale: Θ(nlogn)
'''

A=[56,1,5,3,7,8,2,11,32]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]


def merge(A,indStart,indMid,indEnd):               # S(n)
    B=[None]*(indEnd+1-indStart)                   # Θ(1)
    i=indStart                                     # Θ(1)
    j=indMid+1                                     # Θ(1)
    k=0                                            # Θ(1)
    while ((i<=indMid) and (j<=indEnd)):           # tij*Θ(1)+Θ(1) 
        if (A[i]<A[j]):                            # Θ(1)
            B[k]=A[i]                              # Θ(1)
            i+=1                                   # Θ(1)
        else:                                      # Θ(1)
            B[k]=A[j]                              # Θ(1)
            j+=1                                   # Θ(1)
        k+=1                                       # Θ(1)
    while(i<=indMid):                              # si*Θ(1)+Θ(1)
        B[k]=A[i]                                  # Θ(1)
        i,k=i+1,k+1                                # Θ(1)
    while(j<=indEnd):                              # vj*Θ(1)+Θ(1)
        B[k]=A[j]                                  # Θ(1)
        j,k=j+1,k+1                                # Θ(1)
    A[indStart:indEnd+1]=B                         # Θ(1)


def mergeSort(A,indStart,indEnd):                  # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=(indStart+indEnd)//2                # Θ(1)
        mergeSort(A,indStart,indMid)               # T(n/2)
        mergeSort(A,indMid+1,indEnd)               # T(n/2)
        merge(A,indStart,indMid,indEnd)            # S(n)
    return 


# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore coincidono per qualsiasi valore grande di n 
# Costo Computazionale
#   - merge function
#       - S(n)=Θ(1)+tij*Θ(1)+Θ(1)+si*Θ(1)+Θ(1)+vj*Θ(1)+Θ(1)+Θ(1)
#           - where tij_max=n and tij_min=n/2
#                    si_max=n/2 and si_min=0
#                    vj_max=n/2 and vj_min=0
#       - S(n)=n*Θ(1)+Θ(1) oppure n/2*Θ(1)+n/2*Θ(1) -> S(n)=Θ(n)
#   - merge Sort
#       -T(n)=Θ(1)+2*T(n/2)+Θ(n)
#       -T(n)=2*T(n/2)+Θ(n) -> Θ(nlogn)
#        T(1)=Θ(1)
#
#  T(n)=Θ(nlogn)


mergeSort(A,0,len(A)-1)    
mergeSort(Aworst,0,len(Aworst)-1)
mergeSort(Abest,0,len(Abest)-1)





# RAPPRESENTAZIONE GRAFICA


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
    Alist=list(range(0,i,1))
    tic=time.perf_counter_ns()
    mergeSort(Alist,0,len(Alist)-1)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(100,5,-1):
    Blist=list(range(i,0,-1))
    tic=time.perf_counter_ns()
    mergeSort(Blist,0,len(Blist)-1)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Merge Sort","Caso Migliore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Merge Sort","Caso Peggiore")

