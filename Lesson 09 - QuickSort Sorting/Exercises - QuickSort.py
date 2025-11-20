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
Sia given to vector of length n containing only values 0 e 2. Design
an algorithm with computational cost lineare that modifichi the vector in modo
that all the occorrenze of 0 si trovino piu' to sinistra of all the occorrenze
of 2.
'''

# Considerazioni
'''
For risolvere the problema basta usare the algorithm of Partizione del QuickSort
considerando, as pivot, the value 1.
'''

# algorithm


A1=[2,2,0,0,2,0,2,0,0,0,2,0,2,2,0,2,2,2,0,0]
A2=[2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,]
A3=[0,0,0,0,0,0,2,2,2,2,2,]



def partition(To,indStart,indEnd):         # T(n)
    pivot=1                               # Θ(1)
    the=indStart                            # Θ(1)
    j=indEnd                              # Θ(1)
    while True:                           # Θ(1)
        while To[the]<pivot:                 # (n-k)*Θ(1)+Θ(1)
            the+=1                          # Θ(1)
        while To[j]>pivot:                 # k*Θ(1)+Θ(1)
            j-=1                          # Θ(1)
        if the<j:                           # Θ(1)
            temp=To[j]                     # Θ(1)
            To[j]=To[the]                     # Θ(1)
            To[the]=temp                     # Θ(1)
            the,j=the+1,j-1                   # Θ(1)
        else:                             # Θ(1)
            return                        # Θ(1)


# Input size: number n of elements in array To
# Computational Cost: T(n)=(n-k)*Θ(n)+k*Θ(1)+Θ(1)=Θ(n)

partition(A1,0,len(A1)-1)
partition(A2,0,len(A2)-1)
partition(A3,0,len(A3)-1)





# ESERCIZI 2 E 3 #############################################################

'''VEDI RISOLUZIONE SU CARTA'''



# ESERCIZI0 4 ################################################################

'''
Design an algorithm the piu' efficiente possibile for the seguente problema.
  - Given aa matrice mxn, si vogliono rimescolare the suoi elementi in modo that 
    all the vettori riga e all the vettori colonna siano sorted in senso 
    not decrescente.'
'''
# algorithm


''' VEDI ANCHE CONSIDERAZIONI E PSEUDOCODICE SU CARTA '''


# QuickSort Algorithm

def partition(To,indStart,indEnd):                  # S(n)
    pivot=To[indStart]                              # Θ(1)
    the=indStart                                     # Θ(1)
    j=indEnd                                       # Θ(1)
    while True:                                    # n*Θ(1)+Θ(1) 
        while To[the]<pivot:                          # Θ(1)
            the=the+1                                  # Θ(1)
        while To[j]>pivot:                          # Θ(1)
            j=j-1                                  # Θ(1)
        if the<j:                                    # Θ(1)
            temp=To[the]                              # Θ(1)
            To[the]=To[j]                              # Θ(1)
            To[j]=temp                              # Θ(1)
            the,j=the+1,j-1                            # Θ(1) 
        else:                                      # Θ(1)
            return j                               # Θ(1)


def quickSort(To,indStart,indEnd):                  # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=partition(To,indStart,indEnd)        # S(n)
        quickSort(To,indStart,indMid)               # T(n/2)
        quickSort(To,indMid+1,indEnd)               # T(n/2)
    return 


# Sort Matrix Algorithm

def sortMatrix(M):
    m=len(M)                        # Θ(1)
    n=len(M[0,:])                   # Θ(1)
    for the in range(0,m,1):          # m*Θ(1)+Θ(1)
        quickSort(M[the,:],0,n-1)     # Θ(n*logn)
    for j in range(0,n,1):          # n*Θ(1)+Θ(1)
        quickSort(M[:,j],0,m-1)     # Θ(m*logm)
        
# Input size: n,m that is number righe/colonne matrice M
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