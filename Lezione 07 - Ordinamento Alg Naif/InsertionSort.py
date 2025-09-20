# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# ALGORITMI DI ORDINAMENTO - INSERTION SORT

'''
INSERTION SORT 
L'algoritmo Insertion Sort e' uno degli algoritmi piu' semplici per effettuare
l'ordinamento di una serie/record di dati insieme al SELECTION SORT e al 
BUBBLE SORT'
L'algoritmo INSERTION SORT presenta due costi computazionali diversi tra caso
peggiore (serie dati ordinata in ordine inverso) e caso migliore (serie dati
gia' ordinata)
- Caso Peggiore: O(n^2)
- Caso Migliore: Ω(n)
'''

A=[1,5,3,7,8,11,56,2,4]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]

def insertionSort(A):               # T(n)
    for j in range(1,len(A)):       # (n-1)Θ(1)+Θ(1)
        x=A[j]                      # Θ(1)
        i=j-1                       # Θ(1)
        while (i>=0)and(A[i]>x):    # tjΘ(1)+Θ(1) dove tj=(n-1) oppure 1
            A[i+1]=A[i]             # Θ(1)
            i-=1                    # Θ(1)
        A[i+1]=x                    # Θ(1)
    return A
    

# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore variano a seconda che l'array sia gia' ordinato
# o, viceversa, sia ordinato in ordine inverso
# Costo Computazionale: T(n)=O(n^2) - Caso peggiore
#                       T(n)=Ω(n)   - Caso migliore


Asorted1=insertionSort(A)
Asorted2=insertionSort(Aworst)
Asorted3=insertionSort(Abest)



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
for i in range(5,1000,1):
    A=list(range(0,i,1))
    tic=time.perf_counter_ns()
    insertionSort(A)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,6)))


stepsB=[]
for i in range(1000,5,-1):
    B=list(range(i,0,-1))
    tic=time.perf_counter_ns()
    insertionSort(B)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,6)))

    
rappresentazioneGrafica(range(5,1000,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Insertion Sort","Caso Migliore")

rappresentazioneGrafica(range(5,1000,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Insertion Sort","Caso Peggiore")



