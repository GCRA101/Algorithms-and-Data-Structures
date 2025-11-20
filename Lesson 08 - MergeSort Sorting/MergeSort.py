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




# SORTING ALGORITHMS - MERGE SORT

'''
MERGE SORT 
The Merge Sort algorithm is a more advanced and complex sorting algorithm
compared to the naive algorithms studied so far (Insertion Sort, Selection Sort and
Bubble Sort) and allows achieving the best possible computational cost
for a comparison-based sorting algorithm: O(nlogn).
The main characteristics of the MERGE SORT algorithm are the following:
 - RECURSIVE Algorithm
 - DIVIDE AND CONQUER Algorithmic Technique
 - Recurrence Equation solvable through the Master Method (Master
 Theorem)
 - NOT IN-PLACE sorting process
 
- Computational Cost: Θ(nlogn)
'''

To=[56,1,5,3,7,8,2,11,32]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]


def merge(To,indStart,indMid,indEnd): # S(n)
 B=[None]*(indEnd+1-indStart) # Θ(1)
 the=indStart # Θ(1)
 j=indMid+1 # Θ(1)
 k=0 # Θ(1)
 while ((the<=indMid) and (j<=indEnd)): # tij*Θ(1)+Θ(1) 
 if (To[the]<To[j]): # Θ(1)
 B[k]=To[the] # Θ(1)
 the+=1 # Θ(1)
 else: # Θ(1)
 B[k]=To[j] # Θ(1)
 j+=1 # Θ(1)
 k+=1 # Θ(1)
 while(the<=indMid): # si*Θ(1)+Θ(1)
 B[k]=To[the] # Θ(1)
 the,k=the+1,k+1 # Θ(1)
 while(j<=indEnd): # vj*Θ(1)+Θ(1)
 B[k]=To[j] # Θ(1)
 j,k=j+1,k+1 # Θ(1)
 To[indStart:indEnd+1]=B # Θ(1)


def mergeSort(To,indStart,indEnd): # T(n)
 if (indStart<indEnd): # Θ(1)
 indMid=(indStart+indEnd)//2 # Θ(1)
 mergeSort(To,indStart,indMid) # T(n/2)
 mergeSort(To,indMid+1,indEnd) # T(n/2)
 merge(To,indStart,indMid,indEnd) # S(n)
 return 


# Input size: number n of elements in array To
# Best case and worst case coincide for any large value of n 
# Computational Cost
# - merge function
# - S(n)=Θ(1)+tij*Θ(1)+Θ(1)+si*Θ(1)+Θ(1)+vj*Θ(1)+Θ(1)+Θ(1)
# - where tij_max=n and tij_min=n/2
# si_max=n/2 and si_min=0
# vj_max=n/2 and vj_min=0
# - S(n)=n*Θ(1)+Θ(1) or n/2*Θ(1)+n/2*Θ(1) -> S(n)=Θ(n)
# - merge Sort
# -T(n)=Θ(1)+2*T(n/2)+Θ(n)
# -T(n)=2*T(n/2)+Θ(n) -> Θ(nlogn)
# T(1)=Θ(1)
#
# T(n)=Θ(nlogn)


mergeSort(To,0,len(To)-1) 
mergeSort(Aworst,0,len(Aworst)-1)
mergeSort(Abest,0,len(Abest)-1)





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
 Alist=list(range(0,the,1))
 tic=time.perf_counter_ns()
 mergeSort(Alist,0,len(Alist)-1)
 toc=time.perf_counter_ns()
 stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(100,5,-1):
 Blist=list(range(the,0,-1))
 tic=time.perf_counter_ns()
 mergeSort(Blist,0,len(Blist)-1)
 toc=time.perf_counter_ns()
 stepsB.append(abs(round(toc-tic,8)))

 
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms " 
 "- Merge Sort","Best Case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms " 
 "- Merge Sort","Worst Case")

