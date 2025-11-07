# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:10:30 2023

@author: giorg
"""

'Import main libraries'
import math as math
import numpy as np
import time
import matplotlib.pyplot as plt




'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Mostrare che il Counting Sort e' un algoritmo di ordinamento stabile.
'''




# ESERCIZI0 2 ################################################################

'''
Qual'e' il tempo di esecuzione del Bucket Sort nel caso peggiore?
Quale semplice modifica dell'algoritmo consente di conservare tempo medio 
lineare e costo Θ(nlogn) nel caso peggiore?'
'''

# Considerazioni
'''
Basta usare per i buckets, un algoritmo di ordinamento avente costo 
computazionale peggiore pari a O(nlogn): MergeSort/QuickSort/HeapSort'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''

# Algoritmo

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

'Funzione Heap Sort'

# HEAPIFY Function

def heapify(A,n,i):                             # T(n)               '--(A)--'
    left=2*i+1                                  # Θ(1)               '--(B)--'
    right=2*i+2                                 # Θ(1)
    if (left<n)and(A[left]>A[i]):               # Θ(1)
        iMax=left                               # Θ(1)
    else:                                       # Θ(1)
        iMax=i                                  # Θ(1)
    if (right<n)and(A[right]>A[iMax]):          # Θ(1)
        iMax=right                              # Θ(1)
    if iMax!=i:                                 # Θ(1)
        temp=A[i]                               # Θ(1)
        A[i]=A[iMax]                            # Θ(1)
        A[iMax]=temp                            # Θ(1)
        heapify(A,n,iMax)                       # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeap(A):                               # T(n)
    m=len(A)                                    # Θ(1)               '--(C)--'
    for i in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(A,m,i)                            
    return                                      # Θ(1)
    

# HEAPSORT Function

def heapSort(A):                            # T(n)
    buildHeap(A)                            # O(n)
    for heapSize in range(len(A)-1,-1,-1):   # (n-1) + Θ(1)        
        temp=A[heapSize]                    # Θ(1)
        A[heapSize]=A[0]                    # Θ(1)
        A[0]=temp                           # Θ(1)
        heapify(A,heapSize,0)               # O(logn)                '--(D)--'
    return                                  # Θ(1)


'BUCKET SORT'

def bucketSortHeap(A):                                     # T(n)
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
    '4. Ordinamento elementi buckets usando HEAPSORT'
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        if len(B[i])>0:                      '(**)'        # Θ(1)
            heapSort(B[i])                                 # vlogv*Θ(1)+Θ(1)                               
    '5. Concatenzazione liste B[i] nel vettore A'    
    k=0                                                    # Θ(1)
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
       for j in range(0,len(B[i]),1):                      # v*Θ(1)+Θ(1)   
           A[k]=B[i][j]                                    # Θ(1)
           k+=1                                            # Θ(1)
    return                                                 # Θ(1)


# NOTE IMPORTANTI
'''(**): IMPORTANTE! Per evitare il lancio di Exceptions bisogna evitare di 
lanciare l'algoritmo di ordinamento se il bucket non contiene nessun elemento'''


# Computational Cost
# T(n)=Θ(nlogn)


bucketSortHeap(A1)   
bucketSortHeap(A2) 
bucketSortHeap(A3) 
bucketSortHeap(Aworst)
bucketSortHeap(Abest)





# ESERCIZI0 3 ################################################################

'''
Il Bucket Sort puo' essere modficato in mdo che l'ordinamento all'interno 
delle liste sia eseguito tramite counting sort.
Affinche' il costo dell'algoritmo sia lineare anche nel caso peggiore, 
quale ipotesi bisogna fare su k?
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# Considerazioni
'''
Basta che k<n dove k valore massimo contenuto nell'array da ordinare e n 
numero totale degli elementi in esso contenuti'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''

# Algoritmo

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

'Funzione Counting Sort'

'VERSIONE AVANZATA - Dati Satellite'

def countingSort(A):                                          # T(n)
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


'BUCKET SORT'

def bucketSortCounting(A):                                 # T(n)
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
    '4. Ordinamento elementi buckets usando HEAPSORT'
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        if len(B[i])>0:                      '(**)'        # Θ(1)
            countingSort(B[i])                             # v*Θ(1)+Θ(1)                               
    '5. Concatenzazione liste B[i] nel vettore A'    
    k=0                                                    # Θ(1)
    for i in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
       for j in range(0,len(B[i]),1):                      # v*Θ(1)+Θ(1)   
           A[k]=B[i][j]                                    # Θ(1)
           k+=1                                            # Θ(1)
    return                                                 # Θ(1)


# Computational Cost
# T(n)=Θ(n)


bucketSortCounting(A1)   
bucketSortCounting(A2) 
bucketSortCounting(A3) 
bucketSortCounting(Aworst)
bucketSortCounting(Abest)