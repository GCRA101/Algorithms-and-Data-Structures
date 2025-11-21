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




# ALGORITMI DI ORDINAMENTO - BUCKET SORT

'''
BUCKET SORT 

L'algoritmo Bucking Sort e' un classico esempio di algoritmo di ordinamento
lineare, diversamente dagli algoritmi di ordinamento basati sul confronto visti
fino ad ora (Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, Quick
Sort e Heap Sort). Il fatto che si basi su un approccio diverso, gli consente
di aver un costo computazionale ancora piu' basso rispetto al limite inferiore
valido per gli algoritmi basati sul confronto. Esso, infatti, ha costo Θ(n) 
anziche' Θ(nlogn).
Il vantaggio che ha rispetto al suo simile algoritmo di COUNTING SORT sta nel 
fatto che esso non ha bisogno di alcun limite/condizione sul valore di k (
ovvero, il valore massimo contenuto nel vettore non deve essere minore del 
numero di elementi contenuti nel vettore medesimo)

* Caratteristiche Principali *
Le caratteristiche principali dell'algoritmo BUCKET SORT sono le seguenti:
    - Algoritmo ITERATIVO (NON RICORSIVO!!)
    - Processo di ordinamento NON IN LOCO
    - Funziona solo per valori interi positivi 
        - in caso non siano interi e/o positivi, e' necessario renderli 
          tali prima di eseguire l'algoritmo e poi ritrasformarli nel loro
          valore originale'
    - I valori nel vettore in input devono essere distribuiti in modo 
      uniforme
    
- Costo Computazionale: Θ(n)   (Caso migliore - valori unif distribuiti)
                        Θ(n^2) (Caso peggiore - valori tutti uguali)

'''


'Funzione Insertion Sort'

def insertionSort(A):               # T(n)
    for j in range(1,len(A)):       # (n-1)Θ(1)+Θ(1)
        x=A[j]                      # Θ(1)
        i=j-1                       # Θ(1)
        while (i>=0)and(A[i]>x):    # tjΘ(1)+Θ(1) dove tj=(n-1) oppure 1
            A[i+1]=A[i]             # Θ(1)
            i-=1                    # Θ(1)
        A[i+1]=x                    # Θ(1)
    return A


'BUCKET SORT'

def bucketSort(A):                                         # T(n)
    '1. Ricerca valore intero massimo k'
    imax=0                                                 # Θ(1)
    for i in range(0,len(A),1):                            # n*Θ(1)+Θ(1)
        if A[imax]<A[i]:                                   # Θ(1)
            imax=i                                         # Θ(1)
    k=A[imax]                                              # Θ(1)
    '2. Inizializzazione vettore multidimensionale ausiliario B'
    n=len(A)                                               # Θ(1)
    delta=k//n                                             # Θ(1)
    B=[0]*(k//delta)                                       # Θ(1)
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        B[i]=[]                                            # Θ(1)
    '3. Copia valori di A in corrispondenti buckets in B'
    for i in range(0,len(A),1):                            # n*Θ(1)+Θ(1)
        B[A[i]//(delta+1)].append(A[i])                    # Θ(1)
    '4. Ordinamento elementi buckets usando selection sort'
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        B[i]=insertionSort(B[i])                           # v*Θ(1)+Θ(1)                               
    '5. Concatenzazione liste B[i] nel vettore A'    
    k=0                                                    # Θ(1)
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
       for j in range(0,len(B[i]),1):                      # v*Θ(1)+Θ(1)   
           A[k]=B[i][j]                                    # Θ(1)
           k+=1                                            # Θ(1)
    return                                                 # Θ(1)


# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore differiscono.
# Caso migliore-> valori uniformemente distribuiti - Θ(n)
# Caso peggiore-> valori tutti DIVERSI ma molto vicini tali
#                 da finire tutti nello stesso bucket, ordinati 
#                 in ORDINE INVERSO e facendo uso dell'INSERTION SORT - Θ(n^2)
# Costo Computazionale: T(n)=+Θ(1)+n*Θ(1)+k//delta*Θ(1)+n*Θ(1)+n*Θ(1)+n*Θ(1)
# T(n)=Θ(n)


'Bucket Sort'

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

bucketSort(A1)   
bucketSort(A2) 
bucketSort(A3) 
bucketSort(Aworst)
bucketSort(Abest)




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
    Alist=list(range(0,i,1))    # DATI  IN INPUT ORDINATI
    tic=time.perf_counter_ns()
    bucketSort(Alist)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(5,100,1):
    Blist=list(range(0,i,1))
    'RANDOMIZZAZIONE DATI IN INPUT!'
    random.shuffle(Blist)       # DATI IN INPUT DISORDINATI
    tic=time.perf_counter_ns()
    bucketSort(Blist)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Bucket Sort","Caso Peggiore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Bucket Sort","Caso Migliore")

