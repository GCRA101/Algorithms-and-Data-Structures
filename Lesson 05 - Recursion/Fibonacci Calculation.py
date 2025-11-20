# -*- coding: utf-8 -*-
"""
Created on Thu Jun 1 20:48:46 2023

@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# RECURSION

'''
CALCOLO number DI FIBONACCI
The calculation of the number of Fibonacci is a problema inherently recursive.
E' possibile, pero', risolverlo also with a processo iterativo. 
Confrontiamo the two algoritmi'''

# RECURSIVE Algorithm of FIBONACCI

def fibRicorsivo(n):
 if n==0 or n==1: # Θ(1) 'Cases Base
 return n # Θ(1)
 else: # Θ(1) 'Recursive Step
 return fibRicorsivo(n-1)+fibRicorsivo(n-2) # T(n-1)+T(n-2)


# Input size: value del number n
# Best case and worst case coincide for large values of n (the unici
# validi for the calcolo of notazione asintotica).
# Computational Cost: T(n)=Θ(1)+T(n-1)+T(n-2) -> Recurrence Equations



# ITERATIVE Algorithm of FIBONACCI

def fibIterativo(n):
 if n<=1: # Θ(1)
 return n # Θ(1)
 fib0,fib1,fib=0,1,0 # Θ(1)
 for the in range(2,n+1): # n*Θ(1)+Θ(1)
 fib=fib0+fib1 # Θ(1)
 fib0,fib1=fib1,fib # Θ(1)
 return fib # Θ(1)

# Input size: value del number n
# Best case and worst case coincide for large values of n (the unici
# validi for the calcolo of notazione asintotica).
# Computational Cost: T(n)=Θ(1)+n*Θ(1)+Θ(1)=Θ(n) 

n=13
fibIt=fibIterativo(n)
fibRic=fibRicorsivo(n)

print("For n=",n," the number of Fibonacci is equal to ",
 "\nIterative Algorithm: ", fibIt,"\nRecursive Algorithm: ", fibRic)


n=28

tic=time.perf_counter_ns()
fibIt=fibIterativo(n)
toc=time.perf_counter_ns()
fibItTime=round(toc-tic,6)

tic=time.perf_counter_ns()
fibRic=fibRicorsivo(n)
toc=time.perf_counter_ns()
fibRicTime=round(toc-tic,6)

print('Iterative Algorithm : ',fibItTime,' [nanosecs]')
print('Recursive Algorithm : ',fibRicTime,' [nanosecs]')



# comparison algorithm recursive/iterative
'''
The algorithm recursive is much less efficient than the algorithm
ITERATIVO. Sia in termini of TIME that of SPACE COMPLEXITY!!
'''


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
for the in range(1,15):
 tic=time.perf_counter_ns()
 fibIt=fibIterativo(the)
 toc=time.perf_counter_ns()
 stepsA.append(round(toc-tic,6))


stepsB=[]
for the in range(1,15):
 tic=time.perf_counter_ns()
 fibRic=fibRicorsivo(the)
 toc=time.perf_counter_ns()
 stepsB.append(round(toc-tic,6))

 
rappresentazioneGrafica(range(1,15),stepsA,10000,"Algoritmi of Calcolo " 
 "del number of Fibonacci Iter/Ricors","iterative")

rappresentazioneGrafica(range(1,15),stepsB,10000,"Algoritmi of Calcolo " 
 "del number of Fibonacci Iter/Ricors","recursive")



