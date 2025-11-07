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
Scrivere la versione iterativa dell'algoritmo di Merge Sort
'''

# Algoritmo


A1=[56,1,5,3,7,8,2,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]  



def merge(A,indStart,indMid,indEnd):               # S(n)
    B=[None]*(indEnd+1-indStart)                   # Θ(1)
    i=indStart                                     # Θ(1)
    j=indMid+1                                     # Θ(1)
    k=0                                            # Θ(1)
    while ((i<=indMid) and (j<=indEnd)):           # tij*Θ(1)+Θ(1) 
        if (A[i]<A[j]):                            # Θ(1)
            B[k]=A[i]                              # Θ(1)
            i+=1                                   # Θ(1)
        else:                                      # Θ(1)
            B[k]=A[j]                              # Θ(1)
            j+=1                                   # Θ(1)
        k+=1                                       # Θ(1)
    while(i<=indMid):                              # si*Θ(1)+Θ(1)
        B[k]=A[i]                                  # Θ(1)
        i,k=i+1,k+1                                # Θ(1)
    while(j<=indEnd):                              # vj*Θ(1)+Θ(1)
        B[k]=A[j]                                  # Θ(1)
        j,k=j+1,k+1                                # Θ(1)
    A[indStart:indEnd+1]=B                         # Θ(1)


        
def mergeSortIter(A,indStart,indEnd):          # T(n)
    length=1                                   # Θ(1)
    while(length<=len(A)):                     # logn*Θ(1)+Θ(1)
        i=0                                    # Θ(1)
        while i<len(A)-length:                 # tij*Θ(1)+Θ(1) tij=n/2 oppure 1
            indS=i                             # Θ(1)
            indE=min(i+2*length-1,len(A)-1)    # Θ(1)
            indM=i+length-1                    # Θ(1)
            merge(A,indS,indM,indE)            # Θ(n)
            i+=2*length                        # Θ(1)
        length=2*length                        # Θ(1)


# Input size: numero n di elementi nell'array A
# Computational Cost: T(n)=Θ(n*log(n))


mergeSortIter(A1,0,len(A1)-1)
mergeSortIter(A2,0,len(A2)-1)
mergeSortIter(A3,0,len(A3)-1)
mergeSortIter(Aworst,0,len(Aworst)-1)
mergeSortIter(Abest,0,len(Abest)-1)




# ESERCIZIO 2 ################################################################

'''
Scrivere la versione ricorsiva dell'algoritmo di Merge
'''
# Algoritmo


A1=[56,1,5,3,7,8,2,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]  



def mergeRecurs(A,indStart,indMid,indEnd):
    B=[None]*(indEnd-indStart+1)
    i=indStart
    j=indMid+1
    k=0
    A[indStart:indEnd+1]=mergeRecursInner(A,B,i,j,k,indMid,indEnd)
    
def mergeRecursInner(A,B,i,j,k,indMid,indEnd):
	if (i > indMid) and (j > indEnd):
		return B
	if (j > indEnd) or ((i <= indMid) and (A[i] <= A[j])):
		B[k] = A[i]
		return mergeRecursInner(A, B, i+1, j, k+1, indMid, indEnd)
	else:
		B[k] = A[j]
		return mergeRecursInner(A, B, i, j+1, k+1, indMid, indEnd)


def mergeSortRecurs(A,indStart,indEnd):            # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=(indStart+indEnd)//2                # Θ(1)
        mergeSortRecurs(A,indStart,indMid)         # T(n/2)
        mergeSortRecurs(A,indMid+1,indEnd)         # T(n/2)
        mergeRecurs(A,indStart,indMid,indEnd)      # S(n)
    return 


# Input size: numero n di elementi nell'array A
#  T(n)=Θ(nlogn)


mergeSortRecurs(A1,0,len(A1)-1)
mergeSortRecurs(A2,0,len(A2)-1)
mergeSortRecurs(A3,0,len(A3)-1)
mergeSortRecurs(Aworst,0,len(Aworst)-1)
mergeSortRecurs(Abest,0,len(Abest)-1)




# ESERCIZI 3,4,5 ##############################################################

'''
Si supponga di scrivere una variante del Merge Sort, chiamata 4_MergeSort che,
invece di suddividere il vettore da ordinare in 2 parti (e ordinarle 
separatamente), lo suddivide in 4 parti, le ordina ognuna riapplicando 
4_MergeSort, e le riunifica usando un'opportuna variante 4_Merge di Merge (che
fa la fusione su 4 sottovettori invece che su 2.
'''
# Algoritmo


''' VEDI RISOLUZIONE SU CARTA - SOLO LO PSEUCODICE E' RICHIESTO PER 
    QUESTO ESERCIZIO '''