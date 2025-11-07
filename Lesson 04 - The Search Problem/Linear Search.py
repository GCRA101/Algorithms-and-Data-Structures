# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:41:52 2023

@author: galbieri
"""


from matplotlib import pyplot as plt
import numpy as np
import math
import time


# LINEAR SEARCH

# Dimensione input: numero elementi contenuti nell'array A

# CASO PEGGIORE: L'elemento ricercato v non e' presente nell'array A

def linearSearch(A,v):
    i=0                              # Θ(1)
    while((i<len(A))and(A[i]!=v)):   # n*Θ(1)+Θ(1)
        i+=1                         # Θ(1)
    if (i<len(A)):                   # Θ(1)
        return i
    else:                            # Θ(1)
        return -1                    # Θ(1)
        

# Costo computazionale
# T(n)=Θ(1)+n*Θ(1)+Θ(1)+Θ(1)
# Dato che le costanti si trascurano (a meno che siano all'esponente...),
# si tiene solo il valore di ordine massimo per valori sufficientemente 
# grandi di n e per la commutativita' del prodotto...
# T(n)=Θ(n)
# Costo computazionale: Θ(n)
        
        
        
# CASO MIGLIORE: L'elemento ricercato v e' presente nella prima 
# cella dell'array A   

def linearSearch(A,v):
    i=0                              # Θ(1)
    while((i<len(A))and(A[i]!=v)):   # Θ(1)
        i+=1
    if (i<len(A)):                   # Θ(1)
        return i                     # Θ(1)
    else:       
        return -1                    # Θ(1)

# (*): La condizione del ciclo while non si verifica mai!        
        
# Costo computazionale
# T(n)=Θ(1)
# Costo computazionale: Θ(1)
        
    
# CONCLUSIONE
# L'algoritmo e' un O(n) e un Ω(1)


# RAPPRESENTAZIONE GRAFICA

A=list(range(1,1000))

v=1
stepsA=[]
for i in range(1,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    linearSearch(A,v)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))


v=2321
stepsB=[]
for i in range(1,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    linearSearch(A,v)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,7))

    
    
bestCase=plt.plot(range(1,1000),stepsA,label="Best Case Ω(1)")
worstCase=plt.plot(range(1,1000),stepsB,label="Worst Case O(n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Linear Search Algorithm - Best & Worst Case")

plt.show()