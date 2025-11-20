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


# ESERCIZIO 4 ################################################################

'''
Write to function that, given to vector of n elements ed a index j, trovi
the minimo del sottovettore To[j..n]. Riscrivere the SelectionSort sfruttando 
this function.
'''

# algorithm

def ricercaMinimo(To,j):                 # T(n)
    min=To[j]                            # Θ(1)
    for the in range(j,len(To),1):         # tj*Θ(1)+Θ(1) with tj=n or tj=1
        if To[the]<min: min=To[the]           # Θ(1)
    return min                          # Θ(1)

# Computational Cost: T(n)=O(n) o Ω(1)     

def selectionSort(To):                     # T(n)
    for the in range(0,len(To),1):           # n*Θ(1)+Θ(1)
        min=ricercaMinimo(To,the)            # (n-the)*Θ(1)+Θ(1)             
        To.remove(min)                     # Θ(1)
        To.insert(the,min)                   # Θ(1)
    return To

# Computational Cost: T(n)=Θ(n^2)     
        

To=[23,41,1,5,2,9,7,8,4,3,51,34,25,11,78]


ticSs=time.perf_counter_ns()
selectionSort(To)
tocSs=time.perf_counter_ns()
SsTime=tocSs-ticSs



# ESERCIZIO 5 ################################################################

'''
Given to vector of n elements, design an algorithm that verifichi if ci
are occorrenze ripetute of one stesso value (e, ad esempio, restituisca 1 if
ve ne are e 0 altrimenti)
'''

def trovaValoriUnici(To):                 # T(n)
    for the in range(0,len(To)-1,1):        # n*Θ(1)+Θ(1)
         for j in range(the+1,len(To),1):   # tj*Θ(1)+Θ(1) with tj=1 or n-1
            if To[the]==To[j]: return 1
    return 0

# Worst case: Not ci are values identici -> tj=n-1
# Best case: I primi two values are identici -> tj=1
# Computational cost: O(n), Ω(1)'


To=[3,26,34,73,44,77,11,2,3,4]
B=[1,2,3,4]

n1=trovaValoriUnici(To)
n2=trovaValoriUnici(B)

