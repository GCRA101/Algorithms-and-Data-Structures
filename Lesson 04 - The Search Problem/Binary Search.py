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

# Input size: number of elements contained in array A

# WORST CASE: The searched element v is not present in array A

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
        

# Computational cost
# T(n)=Θ(1)+logn*Θ(1)+Θ(1)
# Since constants are neglected (unless they are in the exponent...),
# only the maximum order value is kept for sufficiently 
# large values of n and for the commutativity of the product...
# T(n)=Θ(logn)
# Computational cost: Θ(logn)
        
        
        
# BEST CASE: The searched element v is present in the middle cell 
# of array A   

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
        
# Computational cost
# T(n)=Θ(1)
# Computational cost: Θ(1)
        
    
# CONCLUSION
# The algorithm is O(logn) e un Ω(1)


# GRAPHICAL REPRESENTATION

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