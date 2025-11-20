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

# Input size: number of elements contained in array To

# WORST CASE: The searched element v is not present in array To

def linearSearch(To,v):
    the=0                              # Θ(1)
    while((the<len(To))and(To[the]!=v)):   # n*Θ(1)+Θ(1)
        the+=1                         # Θ(1)
    if (the<len(To)):                   # Θ(1)
        return the
    else:                            # Θ(1)
        return -1                    # Θ(1)
        

# Computational cost
# T(n)=Θ(1)+n*Θ(1)+Θ(1)+Θ(1)
# Since constants are neglected (unless they are in the exponent...),
# only the maximum order value is kept for sufficiently 
# large values of n and for the commutativity of the product...
# T(n)=Θ(n)
# Computational cost: Θ(n)
        
        
        
# BEST CASE: The searched element v is present in the first 
# cella dell'array To   

def linearSearch(To,v):
    the=0                              # Θ(1)
    while((the<len(To))and(To[the]!=v)):   # Θ(1)
        the+=1
    if (the<len(To)):                   # Θ(1)
        return the                     # Θ(1)
    else:       
        return -1                    # Θ(1)

# (*): The while loop condition never occurs!        
        
# Computational cost
# T(n)=Θ(1)
# Computational cost: Θ(1)
        
    
# CONCLUSION
# The algorithm is O(n) and a Ω(1)


# GRAPHICAL REPRESENTATION

To=list(range(1,1000))

v=1
stepsA=[]
for the in range(1,1000):
    To=list(range(1,the))
    tic=time.perf_counter()
    linearSearch(To,v)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))


v=2321
stepsB=[]
for the in range(1,1000):
    To=list(range(1,the))
    tic=time.perf_counter()
    linearSearch(To,v)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,7))

    
    
bestCase=plt.plot(range(1,1000),stepsA,label="Best Case Ω(1)")
worstCase=plt.plot(range(1,1000),stepsB,label="Worst Case O(n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Linear Search Algorithm - Best & Worst Case")

plt.show()