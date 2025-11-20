# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# SORTING ALGORITHMS - INSERTION SORT

'''
INSERTION SORT 
The algorithm Insertion Sort e' one dethe algorithms piu' semplici for effettuare
l'sorting to series/record of given along with SELECTION SORT e al 
BUBBLE SORT'
The algorithm INSERTION SORT has two different computational costs between case
peggiore (given series sorted in reverse order) e best case (serie given
already' ordinata)
- worst case: O(n^2)
- best case: Ω(n)
'''

To=[1,5,3,7,8,11,56,2,4]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]

def insertionSort(To):               # T(n)
    for j in range(1,len(To)):       # (n-1)Θ(1)+Θ(1)
        x=To[j]                      # Θ(1)
        the=j-1                       # Θ(1)
        while (the>=0)and(To[the]>x):    # tjΘ(1)+Θ(1) where tj=(n-1) or 1
            To[the+1]=To[the]             # Θ(1)
            the-=1                    # Θ(1)
        To[the+1]=x                    # Θ(1)
    return To
    

# Input size: number n of elements in array To
# Best case e worst case variano depending on whether the array sia already' sorted
# o, viceversa, sia ordinato in ordine inverso
# Computational Cost: T(n)=O(n^2) - Worst case
#                       T(n)=Ω(n)   - Best case


Asorted1=insertionSort(To)
Asorted2=insertionSort(Aworst)
Asorted3=insertionSort(Abest)



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
for the in range(5,1000,1):
    To=list(range(0,the,1))
    tic=time.perf_counter_ns()
    insertionSort(To)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,6)))


stepsB=[]
for the in range(1000,5,-1):
    B=list(range(the,0,-1))
    tic=time.perf_counter_ns()
    insertionSort(B)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,6)))

    
rappresentazioneGrafica(range(5,1000,1),stepsA,1,"Sorting Algorithms "  
                        "- Insertion Sort","best case")

rappresentazioneGrafica(range(5,1000,1),stepsB,1,"Sorting Algorithms "  
                        "- Insertion Sort","worst case")



