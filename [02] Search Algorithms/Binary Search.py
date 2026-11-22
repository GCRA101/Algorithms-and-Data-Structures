# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:41:52 2023

@author: galbieri
"""


from matplotlib import pyplot as plt
import numpy as np
import math
import time


# BINARY SEARCH

# Dimensione input: numero elementi contenuti nell'array A

# CASO PEGGIORE: L'elemento ricercato v non e' presente nell'array A

def binarySearch(A,v):
    a=0                              # Θ(1)
    b=len(A)-1                       # Θ(1)
    m=(a+b)//2                       # Θ(1)
    while ((A[m]!=v)and(a<b)):       # logn*Θ(1)+Θ(1)
        if (v<A[m]):                 # Θ(1)
            b=m-1                    # Θ(1)
        else:                        # Θ(1)
            a=m+1                    # Θ(1)
        m=(a+b)//2                   # Θ(1)
    if (A[m]==v):                    # Θ(1)
        return m
    else:                            # Θ(1)
        return -1                    # Θ(1)
        

# Costo computazionale
# T(n)=Θ(1)+logn*Θ(1)+Θ(1)
# Dato che le costanti si trascurano (a meno che siano all'esponente...),
# si tiene solo il valore di ordine massimo per valori sufficientemente 
# grandi di n e per la commutativita' del prodotto...
# T(n)=Θ(logn)
# Costo computazionale: Θ(logn)
        
        
        
# CASO MIGLIORE: L'elemento ricercato v e' presente nella cella in mezzo 
# all'array A   

def binarySearch(A,v):
    a=0                              # Θ(1)
    b=len(A)-1                       # Θ(1)
    m=(a+b)//2                       # Θ(1)
    while ((A[m]!=v)and(a<b)):       # Θ(1)
        if (v<A[m]):                
            b=m-1              
        else:             
            a=m+1        
        m=(a+b)//2 
    if (A[m]==v):                    # Θ(1)
        return m                     # Θ(1)
    else:          
        return -1              

# (*): La condizione del ciclo while non si verifica mai!        
        
# Costo computazionale
# T(n)=Θ(1)
# Costo computazionale: Θ(1)
        
    
# CONCLUSIONE
# L'algoritmo e' un O(logn) e un Ω(1)


# RAPPRESENTAZIONE GRAFICA

A=list(range(1,1000))


stepsA=[]
for i in range(5,1000):
    A=list(range(1,i))
    v=(i+1)//2
    tic=time.perf_counter_ns()
    binarySearch(A,v)
    toc=time.perf_counter_ns()
    stepsA.append(toc-tic)


v=2321
stepsB=[]
for i in range(5,1000):
    A=list(range(1,i))
    tic=time.perf_counter_ns()
    binarySearch(A,v)
    toc=time.perf_counter_ns()
    stepsB.append(toc-tic)

    
    
bestCase=plt.plot(range(5,1000),stepsA,label="Best Case Ω(1)")
worstCase=plt.plot(range(5,1000),stepsB,label="Worst Case O(logn)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Binary Search Algorithm - Best & Worst Case")

plt.show()