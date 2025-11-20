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




# SORTING ALGORITHMS - COUNTING SORT

'''
COUNTING SORT 

The algorithm Counting Sort is a classico esempio of algorithm of sorting
lineare, diversamente dagli sorting algorithms basati on the comparison visti
fino ad ora (Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, Quick
Sort and Heap Sort). The fatto that si basi on a approccio diverso, the consente
of having an even lower computational cost compared to the lower bound
valido for the algorithms basati on the comparison. Esso, indeed, ha cost Θ(n) 
anziche' Θ(nlogn).'

* Caratteristiche Principali *
The caratteristiche principali than the algorithm COUNTING SORT are the following:
    - ITERATIVE Algorithm (NON RICORSIVO!!)
    - Presenta 2 formulazioni leggermente different to second that sia o less
      accettabile that the elements del vector to be sorted siano sovrascritti
      (presenza of data satellite/metadata)
    - Processo of sorting IN LOCO (versione Classica) and NON IN LOCO 
      (versione Avanzata)
    - Funziona only for valori interi positivi 
        - if not siano interi e/o positivi, it is necessary to make them 
          such first of eseguire the algorithm and poi ritrasformarli nel loro
          value originale'
    
- Computational Cost: Θ(n)

'''


'VERSIONE CLASSICA - No Data Satellite'

def countingSortv1(To):                                        # T(n)
    '1. Search value intero massimo k'
    imax=0                                                    # Θ(1)
    for the in range(0,len(To),1):                               # n*Θ(1)+Θ(1)
        if To[imax]<To[the]:                                      # Θ(1)
            imax=the                                            # Θ(1)
    k=To[imax]                                                 # Θ(1)
    '2. Inizializzazione auxiliary vector C'
    C=[0]*(k+1)                                               # Θ(1)
    '3. Conteggio istanze valori uguali presenti in To'
    for the in range(0,len(To),1):                               # n*Θ(1)+Θ(1)
        C[To[the]]=C[To[the]]+1                                     # Θ(1)
    '4. Sostituzione valori ordinati nel vector To'
    j=0                                                       # Θ(1)
    for the in range(0,len(C),1):                               # k*Θ(1)+Θ(1)
        while C[the]>0:                                         # tk**Θ(1)+Θ(1)
            To[j]=the                                            # Θ(1)
            j+=1                                              # Θ(1)
            C[the]-=1                                           # Θ(1)
    return                                                    # Θ(1)


'VERSIONE AVANZATA - Data Satellite'

def countingSortv2(To):                                        # T(n)
    '1. Search value intero massimo k'
    imax=0                                                    # Θ(1)
    for the in range(0,len(To),1):                               # n*Θ(1)+Θ(1)
        if To[imax]<To[the]:                                      # Θ(1)
            imax=the                                            # Θ(1)
    k=To[imax]                                                 # Θ(1)
    '2. Inizializzazione auxiliary vector C'
    C=[0]*(k+1)                                               # Θ(1)
    '3. Conteggio istanze valori uguali presenti in To'
    for the in range(0,len(To),1):                               # n*Θ(1)+Θ(1)
        C[To[the]]=C[To[the]]+1                                     # Θ(1)
    '4. Conteggio number values minori o uguali to the'    
    for the in range(1,len(C),1):                               # k*Θ(1)+Θ(1)
        C[the]=C[the]+C[the-1]                                      # Θ(1) 
    '5. Sostituzione valori ordinati nel vector B'
    B=[0]*len(To)                                              # Θ(1)
    for the in range(0,len(To),1):                               # n*Θ(1)+Θ(1)
        B[C[To[the]]-1]=To[the]                                     # Θ(1)
        C[To[the]]-=1                                            # Θ(1)
    '6. Copia valori vector B in vector To'
    for the in range (0,len(To),1):                              # n*Θ(1)+Θ(1)
        To[the]=B[the]                                             # Θ(1) 
    return                                                    # Θ(1)    



# Input size: number n of elements in array To
# Best case and worst case coincide.
# Computational Cost: T(n)=+Θ(1)+n*Θ(1)+n*Θ(1)+k*Θ(1)+n*Θ(1)+n*Θ(1)+Θ(1)
# T(n)=Θ(5n)=Θ(n)


'Counting Sort - Versione Classica'

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

countingSortv1(A1)   
countingSortv1(A2) 
countingSortv1(A3) 
countingSortv1(Aworst)
countingSortv1(Abest)


'Counting Sort - Versione Avanzata'

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

countingSortv2(A1)   
countingSortv2(A2) 
countingSortv2(A3) 
countingSortv2(Aworst)
countingSortv2(Abest)



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
    countingSortv1(Alist)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(5,100,1):
    Blist=list(range(0,the,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    countingSortv1(Blist)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms "  
                        "- Counting Sort","worst case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms "  
                        "- Counting Sort","best case")

