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
Sia dato un vettore di lunghezza n contenente solo valori 0 e 2. Si progetti
un algoritmo con costo computazionale lineare che modifichi il vettore in modo
che tutte le occorrenze di 0 si trovino piu' a sinistra di tutte le occorrenze
di 2.
'''

# Considerazioni
'''
Per risolvere il problema basta usare l'algoritmo di Partizione del QuickSort
considerando, come pivot, il valore 1.
'''

# Algoritmo


A1=[2,2,0,0,2,0,2,0,0,0,2,0,2,2,0,2,2,2,0,0]
A2=[2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,]
A3=[0,0,0,0,0,0,2,2,2,2,2,]



def partition(A,indStart,indEnd):         # T(n)
    pivot=1                               # Θ(1)
    i=indStart                            # Θ(1)
    j=indEnd                              # Θ(1)
    while True:                           # Θ(1)
        while A[i]<pivot:                 # (n-k)*Θ(1)+Θ(1)
            i+=1                          # Θ(1)
        while A[j]>pivot:                 # k*Θ(1)+Θ(1)
            j-=1                          # Θ(1)
        if i<j:                           # Θ(1)
            temp=A[j]                     # Θ(1)
            A[j]=A[i]                     # Θ(1)
            A[i]=temp                     # Θ(1)
            i,j=i+1,j-1                   # Θ(1)
        else:                             # Θ(1)
            return                        # Θ(1)


# Input size: numero n di elementi nell'array A
# Computational Cost: T(n)=(n-k)*Θ(n)+k*Θ(1)+Θ(1)=Θ(n)

partition(A1,0,len(A1)-1)
partition(A2,0,len(A2)-1)
partition(A3,0,len(A3)-1)





# ESERCIZI 2 E 3 #############################################################

'''VEDI RISOLUZIONE SU CARTA'''



# ESERCIZI0 4 ################################################################

'''
Si progetti un algoritmo il piu' efficiente possibile per il seguente problema.
  - Data una matrice mxn, si vogliono rimescolare i suoi elementi in modo che 
    tutti i vettori riga e tutti i vettori colonna siano ordinati in senso 
    non decrescente.'
'''
# Algoritmo


''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# QuickSort Algorithm

def partition(A,indStart,indEnd):                  # S(n)
    pivot=A[indStart]                              # Θ(1)
    i=indStart                                     # Θ(1)
    j=indEnd                                       # Θ(1)
    while True:                                    # n*Θ(1)+Θ(1) 
        while A[i]<pivot:                          # Θ(1)
            i=i+1                                  # Θ(1)
        while A[j]>pivot:                          # Θ(1)
            j=j-1                                  # Θ(1)
        if i<j:                                    # Θ(1)
            temp=A[i]                              # Θ(1)
            A[i]=A[j]                              # Θ(1)
            A[j]=temp                              # Θ(1)
            i,j=i+1,j-1                            # Θ(1) 
        else:                                      # Θ(1)
            return j                               # Θ(1)


def quickSort(A,indStart,indEnd):                  # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=partition(A,indStart,indEnd)        # S(n)
        quickSort(A,indStart,indMid)               # T(n/2)
        quickSort(A,indMid+1,indEnd)               # T(n/2)
    return 


# Sort Matrix Algorithm

def sortMatrix(M):
    m=len(M)                        # Θ(1)
    n=len(M[0,:])                   # Θ(1)
    for i in range(0,m,1):          # m*Θ(1)+Θ(1)
        quickSort(M[i,:],0,n-1)     # Θ(n*logn)
    for j in range(0,n,1):          # n*Θ(1)+Θ(1)
        quickSort(M[:,j],0,m-1)     # Θ(m*logm)
        
# Input size: n,m ovvero numero righe/colonne matrice M
# Computational Cost:
# T(n,m)=Θ(1)+m*Θ(n*logn)+n*Θ(m*logm)=Θ(n*m*logn)+Θ(m*n*logm)
# Assumendo n==m avremo... T(n)=Θ((n^2)*logn)
        

# Test

M1=np.array([[3,2,6,11],[16,2,5,1],[61,6,6,6],[0,29,7,14]])
M2=np.array([[0,0,0,11,1],[3,1,16,83,84],[44,31,22,34,11]])   
M3=np.array([[1,6,3],[6,11,23],[0,0,82],[6,3,1],[65,33,12]])           
        
sortMatrix(M1)
sortMatrix(M2)
sortMatrix(M3)