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

# Input size: number of elements contained in array A

# WORST CASE: The searched element v is not present in array A

def linearSearch(A,v):
    i=0                              # Θ(1)
    while((i<len(A))and(A[i]!=v)):   # n*Θ(1)+Θ(1)
        i+=1                         # Θ(1)
    if (i<len(A)):                   # Θ(1)
        return i
    else:                            # Θ(1)
        return -1                    # Θ(1)
        

# Computational cost
# T(n)=Θ(1)+n*Θ(1)+Θ(1)+Θ(1)
# Since constants are neglected (unless they are in the exponent...),
# only the maximum order value is kept for sufficiently 
# large values of n and for the commutativity of the product...
# T(n)=Θ(n)
# Computational cost: Θ(n)
        
        
        
# BEST CASE: L'elemento ricercato v e' presente nella prima 
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
        
# Computational cost
# T(n)=Θ(1)
# Computational cost: Θ(1)
        
    
# CONCLUSION
# The algorithm is O(n) e un Ω(1)


# GRAPHICAL REPRESENTATION

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