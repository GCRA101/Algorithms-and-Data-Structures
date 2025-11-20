# -*- coding: utf-8 -*-
"""
Created on Thu Jun 1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# SORTING ALGORITHMS - BUBBLE SORT OPTIMIZED

'''
BUBBLE SORT 
The algorithm bubble Sort is one of the algorithms simplest for performing
l'sorting a series/record of data along with INSERTION SORT and al 
bubble SORT'
The algorithm BUBBLE SORT, SE OTTIMIZZATO CON UN PARAMETRO DI CONTROLLO CHE NE
BLOCCHI L'ESECUZIONE NEL CASO IN CUI IL VETTORE SIA sorted, presenta 
DIVERSO computational cost for the worst case (serie given sorted in 
ordine inverso) and the best case (data series already sorted)
Computational Cost: T(n)=O(n^2) - Worst case
 T(n)=Ω(n) - Best case
'''

To=[56,1,5,3,7,8,2,11,4]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]

def bubbleSortOptimized(To): # T(n)
 for the in range(0,len(To)): # n*Θ(1)+Θ(1)
 sortedArray=True # Θ(1)
 for j in range(len(To)-1,the,-1): # tjΘ(1)+Θ(1) where tj=(n-1) o tj=1
 if To[j]<To[j-1]:
 x=To[j] # Θ(1)
 To[j]=To[j-1] # Θ(1)
 To[j-1]=x # Θ(1)
 sortedArray=False # Θ(1)
 if sortedArray==True: break # Θ(1)
 return To
 

# Input size: number n of elements in array To
# Best case and worst case coincide for any large value of n 
# since the internal for loop will always scan all elements
# for trovare the minimi parziali
# Computational Cost: T(n)=Θ(n^2) - Worst case/migliore


Asorted1=bubbleSortOptimized(To)
Asorted2=bubbleSortOptimized(Aworst)
Asorted3=bubbleSortOptimized(Abest)



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
 To=list(range(0,the,1))
 tic=time.perf_counter_ns()
 bubbleSortOptimized(To)
 toc=time.perf_counter_ns()
 stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for the in range(100,5,-1):
 B=list(range(the,0,-1))
 tic=time.perf_counter_ns()
 bubbleSortOptimized(B)
 toc=time.perf_counter_ns()
 stepsB.append(abs(round(toc-tic,8)))

 
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Sorting Algorithms " 
 "- Bubble Sort","best case")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Sorting Algorithms " 
 "- Bubble Sort","worst case")



