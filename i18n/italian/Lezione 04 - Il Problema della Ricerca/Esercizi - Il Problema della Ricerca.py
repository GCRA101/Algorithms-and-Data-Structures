# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023

@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# ESERCIZIO 1

'''
Dato un array A di n valori numerici e due valori estremi a e b, tale che 
a<b, creare due algoritmi per il conteggio dei valori contenuti nell'array
che siano compresi tra a e b.
Un algoritmo deve basarsi sulla ricerca sequenziale (Linear Search) mentre
l'altro sulla ricerca binaria (Binary Search)
'''

# Algoritmo di RICERCA SEQUENZIALE

''' Caso PEGGIORE/MIGLIORE
I due casi coincidono dato che, per qualsiasi array A in input
l'algoritmo dovra' scorrere sempre tutti i suoi elementi'''

def ricercaSequenziale(A,a,b):
    i=0                             # Θ(1)
    n=0                             # Θ(1)
    while(i<len(A)):                # n*Θ(1)+Θ(1)
       if (A[i]>=a and A[i]<=b):    # Θ(1)
           n+=1                     # Θ(1)
       i+=1                         # Θ(1)
    return n                        # Θ(1)

# Dimensione input: n elementi in array A
# Costo Computazionale: T(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)


# Algoritmo di RICERCA BINARIA

''' Caso PEGGIORE
Gli estremi a e b non vengono incontrati se non alla ultima
iterazione, nel caso in cui siano presenti - alla k-esima 
iterazione k=logn'''

def ricercaBinaria(A,a,b):
    aa=ab=0                         # Θ(1)
    ba=bb=len(A)-1                  # Θ(1)    
    af=bf=0                         # Θ(1) 
    ma=mb=(ba-aa)//2                # Θ(1)
    
    while(A[mb]!=b and ab<bb):      # logn*Θ(1)+Θ(1)
        if A[mb]<b:                 # Θ(1)
            ab=mb+1                 # Θ(1)
        else:                       # Θ(1)
            bb=mb-1                 # Θ(1)
        mb=(ab+bb)//2               # Θ(1)
    if ab>bb:                       # Θ(1)
        return -1                   # Θ(1)
    if A[mb]<=b:                    # Θ(1)
        max=A[mb]                   # Θ(1)
        bf=mb                       # Θ(1)
    else:                           # Θ(1)
        max=A[mb-1]                 # Θ(1)
        bf=mb-1                     # Θ(1)
        
    while(A[ma]!=a and aa<ba):      # logn*Θ(1)+Θ(1)
        if A[ma]<a:                 # Θ(1)
            aa=ma+1                 # Θ(1)
        else:                       # Θ(1)
            ba=ma-1                 # Θ(1)
        ma=(aa+ba)//2               # Θ(1)
    if aa>ba:                       # Θ(1)
        return -1                   # Θ(1)
    if A[ma]>=a:                    # Θ(1)
        min=A[ma]                   # Θ(1)
        af=ma                       # Θ(1)
    else:                           # Θ(1)
        min=A[ma+1]                 # Θ(1)
        af=ma+1                    # Θ(1)

    return bf-af+1                  # Θ(1)


# Dimensione input: n elementi in array A
# Costo Computazionale: T(n)=Θ(1)+2*logn*Θ(1)+Θ(1)=Θ(logn)

A=[1, 4, 8, 17, 22, 25, 31, 36, 44, 52, 55, 63, 71, 78, 92]
a=20
b=60

nSeq1=ricercaSequenziale(A, a, b)
nBin1=ricercaBinaria(A, a, b)


''' Caso MIGLIORE
Gli estremi a e b vengono incontrati alla seconda
iterazione'''

def ricercaBinaria(A,a,b):
    aa=ab=0                         # Θ(1)
    ba=bb=len(A)-1                  # Θ(1)    
    af=bf=0                         # Θ(1) 
    ma=mb=(ba-aa)//2                # Θ(1)
    
    while(A[mb]!=b and ab<bb):      # 2*Θ(1)+Θ(1)
        if A[mb]<b:                 # Θ(1)
            ab=mb+1                 # Θ(1)
        else:                       # Θ(1)
            bb=mb-1                 # Θ(1)
        mb=(ab+bb)//2               # Θ(1)
    if ab>bb:                       # Θ(1)
        return -1                   # Θ(1)
    if A[mb]<=b:                    # Θ(1)
        max=A[mb]                   # Θ(1)
        bf=mb                       # Θ(1)
    else:                           # Θ(1)
        max=A[mb-1]                 # Θ(1)
        bf=mb-1                     # Θ(1)
        
    while(A[ma]!=a and aa<ba):      # 2*Θ(1)+Θ(1)
        if A[ma]<a:                 # Θ(1)
            aa=ma+1                 # Θ(1)
        else:                       # Θ(1)
            ba=ma-1                 # Θ(1)
        ma=(aa+ba)//2               # Θ(1)
    if aa>ba:                       # Θ(1)
        return -1                   # Θ(1)
    if A[ma]>=a:                    # Θ(1)
        min=A[ma]                   # Θ(1)
        af=ma                       # Θ(1)
    else:                           # Θ(1)
        min=A[ma-1]                 # Θ(1)
        bf=mb-1                     # Θ(1)

    return bf-af+1                  # Θ(1)


        
# Dimensione input: n elementi in array A
# Costo Computazionale: T(n)=Θ(1)+2*Θ(1)+Θ(1)=Θ(1)

A=[1, 4, 8, 20, 22, 25, 31, 36, 44, 52, 55, 60, 71, 78, 92]
a=20
b=60

nSeq2=ricercaSequenziale(A, a, b)
nBin2=ricercaBinaria(A, a, b)


# Costo Computazionale Complessivo: O(logn) e Ω(1)




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
for i in range(5,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    a=i//10
    b=9*i//10
    ricercaSequenziale(A,a,b)
    toc=time.perf_counter()
    stepsA.append(round(abs(toc-tic),12))


stepsB1=[]
for i in range(5,1000):
    B1=list(range(1,i))
    tic=time.perf_counter()
    a=i//10
    b=9*i//10
    ricercaBinaria(B1,a,b)
    toc=time.perf_counter()
    stepsB1.append(round(toc-tic,12))


stepsB2=[]
for i in range(5,1000):
    B2=list(range(1,i))
    a=i//4
    b=3*i//4
    tic=time.perf_counter()
    ricercaBinaria(B2,a,b)
    toc=time.perf_counter()
    stepsB2.append(round(abs(toc-tic),12))
    
    
rappresentazioneGrafica(range(5,1000),stepsA,0.000001,"Algoritmi di " 
                        "Ricerca - Linear/Binary","Linear Search")

rappresentazioneGrafica(range(5,1000),stepsB1,0.000001,"Algoritmi di " 
                       "Ricerca - Linear/Binary","Binary Search - Worst Case")

rappresentazioneGrafica(range(5,1000),stepsB2,0.000001,"Algoritmi di " 
                       "Ricerca - Linear/Binary","Binary Search - Best Case")




# SOLUZIONI 

# Algoritmo di RICERCA SEQUENZIALE

def Conta_In_Intervallo(A,a,b):
    cont=0
    for i in range(len(A)):
        if a<=A[i]<=b:
            cont+=1
    return cont

A=[1, 4, 8, 17, 22, 25, 31, 36, 44, 52, 55, 63, 71, 78, 92]
a=20
b=60

nSeqSol=Conta_In_Intervallo(A, a, b)
