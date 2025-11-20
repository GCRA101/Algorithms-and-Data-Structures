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




# SORTING ALGORITHMS - BUCKET SORT

'''
BUCKET SORT 

The algorithm Bucking Sort is a classico esempio of algorithm of sorting
lineare, diversamente dagli sorting algorithms basati on the comparison visti
fino ad ora (Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, Quick
Sort and Heap Sort). The fatto that si basi on a approccio diverso, the consente
of having an even lower computational cost compared to the lower bound
valido for the algorithms basati on the comparison. Esso, indeed, ha cost Θ(n) 
instead of Θ(nlogn).
The vantaggio that ha rispetto al suo simile algorithm of COUNTING SORT sta nel 
fatto that esso not ha bisogno of alcun limite/condizione on the value of k (
that is, the value massimo contained in the vector not deve essere minore del 
number of elements contained in the vector medesimo)

* Caratteristiche Principali *
The caratteristiche principali than the algorithm BUCKET SORT are the following:
 - ITERATIVE Algorithm (NON RICORSIVO!!)
 - NOT IN-PLACE sorting process
 - Works only for positive integer values 
 - if not siano interi e/o positivi, it is necessary to make them 
 such first of eseguire the algorithm and poi ritrasformarli nel loro
 original value'
 - I values nel vector in input devono essere distribuiti in a way 
 uniforme
 
- Computational Cost: Θ(n) (Best case - values unif distribuiti)
 Θ(n^2) (Worst case - values all uguali)

'''


'function Insertion Sort'

def insertionSort(To): # T(n)
 for j in range(1,len(To)): # (n-1)Θ(1)+Θ(1)
 x=To[j] # Θ(1)
 the=j-1 # Θ(1)
 while (the>=0)and(To[the]>x): # tjΘ(1)+Θ(1) where tj=(n-1) or 1
 To[the+1]=To[the] # Θ(1)
 the-=1 # Θ(1)
 To[the+1]=x # Θ(1)
 return To


'BUCKET SORT'

def bucketSort(To): # T(n)
 '1. Search value intero massimo k'
 imax=0 # Θ(1)
 for the in range(0,len(To),1): # n*Θ(1)+Θ(1)
 if To[imax]<To[the]: # Θ(1)
 imax=the # Θ(1)
 k=To[imax] # Θ(1)
 '2. Inizializzazione vector multidimensionale ausiliario B'
 n=len(To) # Θ(1)
 delta=k//n # Θ(1)
 B=[0]*(k//delta) # Θ(1)
 for the in range(0,len(B),1): # k//delta*Θ(1)+Θ(1)
 B[the]=[] # Θ(1)
 '3. Copy values of A to corresponding buckets in B'
 for the in range(0,len(To),1): # n*Θ(1)+Θ(1)
 B[To[the]//(delta+1)].append(To[the]) # Θ(1)
 '4. sorting elements buckets usando selection sort'
 for the in range(0,len(B),1): # k//delta*Θ(1)+Θ(1)
 B[the]=insertionSort(B[the]) # v*Θ(1)+Θ(1) 
 '5. Concatenzazione lists B[the] nel vector To' 
 k=0 # Θ(1)
 for the in range(0,len(B),1): # k//delta*Θ(1)+Θ(1)
 for j in range(0,len(B[the]),1): # v*Θ(1)+Θ(1) 
 To[k]=B[the][j] # Θ(1)
 k+=1 # Θ(1)
 return # Θ(1)


# Input size: number n of elements in array To
# Best case and worst case differiscono.
# Best case-> values uniformemente distribuiti - Θ(n)
# Worst case-> values all DIVERSI ma very vicini such
# end up all in the same bucket, sorted 
# in ORDINE INVERSO and facendo uso dell'INSERTION SORT - Θ(n^2)
# Computational Cost: T(n)=+Θ(1)+n*Θ(1)+k//delta*Θ(1)+n*Θ(1)+n*Θ(1)+n*Θ(1)
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
 bucketSort(Alist)
 toc=time.perf_counter_ns()
 stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(5,100,1):
 Blist=list(range(0,the,1))
 'RANDOMIZZAZIONE DATI IN INPUT!'
 random.shuffle(Blist) # DATI IN INPUT DISORDINATI
 tic=time.perf_counter_ns()
 bucketSort(Blist)
 toc=time.perf_counter_ns()
 stepsB.append(abs(round(toc-tic,8)))

 
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms " 
 "- Bucket Sort","worst case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms " 
 "- Bucket Sort","best case")

