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




# ALGORITMI DI ORDINAMENTO - COUNTING SORT

'''
COUNTING SORT 

L'algoritmo Counting Sort e' un classico esempio di algoritmo di ordinamento
lineare, diversamente dagli algoritmi di ordinamento basati sul confronto visti
fino ad ora (Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, Quick
Sort e Heap Sort). Il fatto che si basi su un approccio diverso, gli consente
di aver un costo computazionale ancora piu' basso rispetto al limite inferiore
valido per gli algoritmi basati sul confronto. Esso, infatti, ha costo Θ(n) 
anziche' Θ(nlogn).'

* Caratteristiche Principali *
Le caratteristiche principali dell'algoritmo COUNTING SORT sono le seguenti:
    - ITERATIVE Algorithm (NON RICORSIVO!!)
    - Presenta 2 formulazioni leggermente differenti a seconda che sia o meno
      accettabile che gli elementi del vettore da ordinare siano sovrascritti
      (presenza di dati satellite/metadata)
    - Processo di ordinamento IN LOCO (versione Classica) e NON IN LOCO 
      (versione Avanzata)
    - Funziona solo per valori interi positivi 
        - in caso non siano interi e/o positivi, e' necessario renderli 
          tali prima di eseguire l'algoritmo e poi ritrasformarli nel loro
          valore originale'
    
- Computational Cost: Θ(n)

'''


'VERSIONE CLASSICA - No Dati Satellite'

def countingSortv1(A):                                        # T(n)
    '1. Ricerca valore intero massimo k'
    imax=0                                                    # Θ(1)
    for i in range(0,len(A),1):                               # n*Θ(1)+Θ(1)
        if A[imax]<A[i]:                                      # Θ(1)
            imax=i                                            # Θ(1)
    k=A[imax]                                                 # Θ(1)
    '2. Inizializzazione vettore ausiliario C'
    C=[0]*(k+1)                                               # Θ(1)
    '3. Conteggio istanze valori uguali presenti in A'
    for i in range(0,len(A),1):                               # n*Θ(1)+Θ(1)
        C[A[i]]=C[A[i]]+1                                     # Θ(1)
    '4. Sostituzione valori ordinati nel vettore A'
    j=0                                                       # Θ(1)
    for i in range(0,len(C),1):                               # k*Θ(1)+Θ(1)
        while C[i]>0:                                         # tk**Θ(1)+Θ(1)
            A[j]=i                                            # Θ(1)
            j+=1                                              # Θ(1)
            C[i]-=1                                           # Θ(1)
    return                                                    # Θ(1)


'VERSIONE AVANZATA - Dati Satellite'

def countingSortv2(A):                                        # T(n)
    '1. Ricerca valore intero massimo k'
    imax=0                                                    # Θ(1)
    for i in range(0,len(A),1):                               # n*Θ(1)+Θ(1)
        if A[imax]<A[i]:                                      # Θ(1)
            imax=i                                            # Θ(1)
    k=A[imax]                                                 # Θ(1)
    '2. Inizializzazione vettore ausiliario C'
    C=[0]*(k+1)                                               # Θ(1)
    '3. Conteggio istanze valori uguali presenti in A'
    for i in range(0,len(A),1):                               # n*Θ(1)+Θ(1)
        C[A[i]]=C[A[i]]+1                                     # Θ(1)
    '4. Conteggio numero valori minori o uguali a i'    
    for i in range(1,len(C),1):                               # k*Θ(1)+Θ(1)
        C[i]=C[i]+C[i-1]                                      # Θ(1) 
    '5. Sostituzione valori ordinati nel vettore B'
    B=[0]*len(A)                                              # Θ(1)
    for i in range(0,len(A),1):                               # n*Θ(1)+Θ(1)
        B[C[A[i]]-1]=A[i]                                     # Θ(1)
        C[A[i]]-=1                                            # Θ(1)
    '6. Copia valori vettore B in vettore A'
    for i in range (0,len(A),1):                              # n*Θ(1)+Θ(1)
        A[i]=B[i]                                             # Θ(1) 
    return                                                    # Θ(1)    



# Input size: numero n di elementi nell'array A
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
    countingSortv1(Alist)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(5,100,1):
    Blist=list(range(0,i,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    countingSortv1(Blist)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Counting Sort","Caso Peggiore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Counting Sort","Caso Migliore")

