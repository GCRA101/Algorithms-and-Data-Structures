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
Scrivere the versione iterative delthe algorithm of Merge Sort
'''

# algorithm


A1=[56,1,5,3,7,8,2,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]  



def merge(To,indStart,indMid,indEnd):               # S(n)
    B=[None]*(indEnd+1-indStart)                   # Θ(1)
    the=indStart                                     # Θ(1)
    j=indMid+1                                     # Θ(1)
    k=0                                            # Θ(1)
    while ((the<=indMid) and (j<=indEnd)):           # tij*Θ(1)+Θ(1) 
        if (To[the]<To[j]):                            # Θ(1)
            B[k]=To[the]                              # Θ(1)
            the+=1                                   # Θ(1)
        else:                                      # Θ(1)
            B[k]=To[j]                              # Θ(1)
            j+=1                                   # Θ(1)
        k+=1                                       # Θ(1)
    while(the<=indMid):                              # si*Θ(1)+Θ(1)
        B[k]=To[the]                                  # Θ(1)
        the,k=the+1,k+1                                # Θ(1)
    while(j<=indEnd):                              # vj*Θ(1)+Θ(1)
        B[k]=To[j]                                  # Θ(1)
        j,k=j+1,k+1                                # Θ(1)
    To[indStart:indEnd+1]=B                         # Θ(1)


        
def mergeSortIter(To,indStart,indEnd):          # T(n)
    length=1                                   # Θ(1)
    while(length<=len(To)):                     # logn*Θ(1)+Θ(1)
        the=0                                    # Θ(1)
        while the<len(To)-length:                 # tij*Θ(1)+Θ(1) tij=n/2 or 1
            indS=the                             # Θ(1)
            indE=min(the+2*length-1,len(To)-1)    # Θ(1)
            indM=the+length-1                    # Θ(1)
            merge(To,indS,indM,indE)            # Θ(n)
            the+=2*length                        # Θ(1)
        length=2*length                        # Θ(1)


# Input size: number n of elements in array To
# Computational Cost: T(n)=Θ(n*log(n))


mergeSortIter(A1,0,len(A1)-1)
mergeSortIter(A2,0,len(A2)-1)
mergeSortIter(A3,0,len(A3)-1)
mergeSortIter(Aworst,0,len(Aworst)-1)
mergeSortIter(Abest,0,len(Abest)-1)




# ESERCIZIO 2 ################################################################

'''
Scrivere the versione recursive delthe algorithm of Merge
'''
# algorithm


A1=[56,1,5,3,7,8,2,32]
A2=[11,2,3,8,5,32,33,81,12,18,54,42,38,1,9]
A3=[101,23,84,33,61,41,32,1,2,3,4,6,5]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]  



def mergeRecurs(To,indStart,indMid,indEnd):
    B=[None]*(indEnd-indStart+1)
    the=indStart
    j=indMid+1
    k=0
    To[indStart:indEnd+1]=mergeRecursInner(To,B,the,j,k,indMid,indEnd)
    
def mergeRecursInner(To,B,the,j,k,indMid,indEnd):
	if (the > indMid) and (j > indEnd):
		return B
	if (j > indEnd) or ((the <= indMid) and (To[the] <= To[j])):
		B[k] = To[the]
		return mergeRecursInner(To, B, the+1, j, k+1, indMid, indEnd)
	else:
		B[k] = To[j]
		return mergeRecursInner(To, B, the, j+1, k+1, indMid, indEnd)


def mergeSortRecurs(To,indStart,indEnd):            # T(n)
    if (indStart<indEnd):                          # Θ(1)
        indMid=(indStart+indEnd)//2                # Θ(1)
        mergeSortRecurs(To,indStart,indMid)         # T(n/2)
        mergeSortRecurs(To,indMid+1,indEnd)         # T(n/2)
        mergeRecurs(To,indStart,indMid,indEnd)      # S(n)
    return 


# Input size: number n of elements in array To
#  T(n)=Θ(nlogn)


mergeSortRecurs(A1,0,len(A1)-1)
mergeSortRecurs(A2,0,len(A2)-1)
mergeSortRecurs(A3,0,len(A3)-1)
mergeSortRecurs(Aworst,0,len(Aworst)-1)
mergeSortRecurs(Abest,0,len(Abest)-1)




# ESERCIZI 3,4,5 ##############################################################

'''
Si supponga of scrivere a variante del Merge Sort, chiamata 4_MergeSort that,
invece of suddividere the vector from ordinare in 2 parti (e ordinarle 
separatamente), the suddivide in 4 parti, the ordina ognuna riapplicando 
4_MergeSort, e the riunifica usando a'opportuna variante 4_Merge of Merge (that
fa the fusione on 4 sottovettori invece that on 2.
'''
# algorithm


''' VEDI RISOLUZIONE SU CARTA - SOLO LO PSEUCODICE E' RICHIESTO PER 
    QUESTO ESERCIZIO '''