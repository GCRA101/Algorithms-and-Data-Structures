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
Mostrare that the Counting Sort e' an algorithm for sorting stabile.
'''




# ESERCIZI0 2 ################################################################

'''
Qual'e' the tempo of esecuzione del Bucket Sort nel worst case?
Quale semplice modifica delthe algorithm consente of conservare tempo middle 
lineare e costo Θ(nlogn) nel worst case?'
'''

# Considerazioni
'''
Basta usare for the buckets, an algorithm for sorting avente costo 
computazionale peggiore pari to O(nlogn): MergeSort/QuickSort/HeapSort'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''

# algorithm

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

'function Heap Sort'

# HEAPIFY Function

def heapify(To,n,the):                             # T(n)               '--(To)--'
    left=2*the+1                                  # Θ(1)               '--(B)--'
    right=2*the+2                                 # Θ(1)
    if (left<n)and(To[left]>To[the]):               # Θ(1)
        iMax=left                               # Θ(1)
    else:                                       # Θ(1)
        iMax=the                                  # Θ(1)
    if (right<n)and(To[right]>To[iMax]):          # Θ(1)
        iMax=right                              # Θ(1)
    if iMax!=the:                                 # Θ(1)
        temp=To[the]                               # Θ(1)
        To[the]=To[iMax]                            # Θ(1)
        To[iMax]=temp                            # Θ(1)
        heapify(To,n,iMax)                       # T(2/3n)
    return
    
# BUILDHEAP Function

def buildHeap(To):                               # T(n)
    m=len(To)                                    # Θ(1)               '--(C)--'
    for the in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapify(To,m,the)                            
    return                                      # Θ(1)
    

# HEAPSORT Function

def heapSort(To):                            # T(n)
    buildHeap(To)                            # O(n)
    for heapSize in range(len(To)-1,-1,-1):   # (n-1) + Θ(1)        
        temp=To[heapSize]                    # Θ(1)
        To[heapSize]=To[0]                    # Θ(1)
        To[0]=temp                           # Θ(1)
        heapify(To,heapSize,0)               # O(logn)                '--(D)--'
    return                                  # Θ(1)


'BUCKET SORT'

def bucketSortHeap(To):                                     # T(n)
    '1. Ricerca value intero massimo k'
    imax=0                                                 # Θ(1)
    for the in range(0,len(To),1):                            # n*Θ(1)+Θ(1)
        if To[imax]<To[the]:                                   # Θ(1)
            imax=the                                         # Θ(1)
    k=To[imax]                                              # Θ(1)
    '2. Inizializzazione vector multidimensionale ausiliario B'
    n=len(To)                                               # Θ(1)
    delta=k//n                                             # Θ(1)
    B=[0]*(k//delta)                                       # Θ(1)
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        B[the]=[]                                            # Θ(1)
    '3. Copia valori of To in corrispondenti buckets in B'
    for the in range(0,len(To),1):                            # n*Θ(1)+Θ(1)
        B[To[the]//(delta+1)].append(To[the])                    # Θ(1)
    '4. sorting elements buckets usando HEAPSORT'
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        if len(B[the])>0:                      '(**)'        # Θ(1)
            heapSort(B[the])                                 # vlogv*Θ(1)+Θ(1)                               
    '5. Concatenzazione liste B[the] nel vector To'    
    k=0                                                    # Θ(1)
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
       for j in range(0,len(B[the]),1):                      # v*Θ(1)+Θ(1)   
           To[k]=B[the][j]                                    # Θ(1)
           k+=1                                            # Θ(1)
    return                                                 # Θ(1)


# NOTE IMPORTANTI
'''(**): IMPORTANTE! For evitare the lancio of Exceptions bisogna evitare of 
lanciare the algorithm of sorting if the bucket not contiene nessun element'''


# Computational Cost
# T(n)=Θ(nlogn)


bucketSortHeap(A1)   
bucketSortHeap(A2) 
bucketSortHeap(A3) 
bucketSortHeap(Aworst)
bucketSortHeap(Abest)





# ESERCIZI0 3 ################################################################

'''
The Bucket Sort puo' essere modficato in mdo that l'sorting all'interno 
delle liste sia eseguito through counting sort.
Affinche' the costo delthe algorithm sia lineare also nel worst case, 
quale ipotesi bisogna fare on k?
'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# Considerazioni
'''
Basta that k<n where k value massimo contenuto in the array from ordinare e n 
number totale degli elements in esso contenuti'''

''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''

# algorithm

A1=[56,1,5,3,7,8,2,11,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,1,25,5,21,8,11,23,3,31]
Abest=[1,5,6,31,44,53,98,101]

'function Counting Sort'

'VERSIONE AVANZATA - Data Satellite'

def countingSort(To):                                          # T(n)
    '1. Ricerca value intero massimo k'
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


'BUCKET SORT'

def bucketSortCounting(To):                                 # T(n)
    '1. Ricerca value intero massimo k'
    imax=0                                                 # Θ(1)
    for the in range(0,len(To),1):                            # n*Θ(1)+Θ(1)
        if To[imax]<To[the]:                                   # Θ(1)
            imax=the                                         # Θ(1)
    k=To[imax]                                              # Θ(1)
    '2. Inizializzazione vector multidimensionale ausiliario B'
    n=len(To)                                               # Θ(1)
    delta=k//n                                             # Θ(1)
    B=[0]*(k//delta)                                       # Θ(1)
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        B[the]=[]                                            # Θ(1)
    '3. Copia valori of To in corrispondenti buckets in B'
    for the in range(0,len(To),1):                            # n*Θ(1)+Θ(1)
        B[To[the]//(delta+1)].append(To[the])                    # Θ(1)
    '4. sorting elements buckets usando HEAPSORT'
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
        if len(B[the])>0:                      '(**)'        # Θ(1)
            countingSort(B[the])                             # v*Θ(1)+Θ(1)                               
    '5. Concatenzazione liste B[the] nel vector To'    
    k=0                                                    # Θ(1)
    for the in range(0,len(B),1):                            # k//delta*Θ(1)+Θ(1)
       for j in range(0,len(B[the]),1):                      # v*Θ(1)+Θ(1)   
           To[k]=B[the][j]                                    # Θ(1)
           k+=1                                            # Θ(1)
    return                                                 # Θ(1)


# Computational Cost
# T(n)=Θ(n)


bucketSortCounting(A1)   
bucketSortCounting(A2) 
bucketSortCounting(A3) 
bucketSortCounting(Aworst)
bucketSortCounting(Abest)