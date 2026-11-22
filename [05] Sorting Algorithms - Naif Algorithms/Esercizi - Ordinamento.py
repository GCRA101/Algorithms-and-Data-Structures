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
Scrivere una funzione che, dato un vettore di n elementi ed un indice j, trovi
il minimo del sottovettore A[j..n]. Riscrivere il SelectionSort sfruttando 
questa funzione.
'''

# Algoritmo

def ricercaMinimo(A,j):                 # T(n)
    min=A[j]                            # Θ(1)
    for i in range(j,len(A),1):         # tj*Θ(1)+Θ(1) con tj=n oppure tj=1
        if A[i]<min: min=A[i]           # Θ(1)
    return min                          # Θ(1)

# Costo Computazionale: T(n)=O(n) o Ω(1)     

def selectionSort(A):                     # T(n)
    for i in range(0,len(A),1):           # n*Θ(1)+Θ(1)
        min=ricercaMinimo(A,i)            # (n-i)*Θ(1)+Θ(1)             
        A.remove(min)                     # Θ(1)
        A.insert(i,min)                   # Θ(1)
    return A

# Costo Computazionale: T(n)=Θ(n^2)     
        

A=[23,41,1,5,2,9,7,8,4,3,51,34,25,11,78]


ticSs=time.perf_counter_ns()
selectionSort(A)
tocSs=time.perf_counter_ns()
SsTime=tocSs-ticSs



# ESERCIZIO 5 ################################################################

'''
Dato un vettore di n elementi, si progetti un algoritmo che verifichi se ci
sono occorrenze ripetute di uno stesso valore (e, ad esempio, restituisca 1 se
ve ne sono e 0 altrimenti)
'''

def trovaValoriUnici(A):                 # T(n)
    for i in range(0,len(A)-1,1):        # n*Θ(1)+Θ(1)
         for j in range(i+1,len(A),1):   # tj*Θ(1)+Θ(1) con tj=1 oppure n-1
            if A[i]==A[j]: return 1
    return 0

# Caso peggiore: Non ci sono valori identici -> tj=n-1
# Caso migliore: I primi due valori sono identici -> tj=1
# Costo computazionale: O(n), Ω(1)'


A=[3,26,34,73,44,77,11,2,3,4]
B=[1,2,3,4]

n1=trovaValoriUnici(A)
n2=trovaValoriUnici(B)

