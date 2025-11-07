# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023

@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# RECURSION

'''
CALCOLO NUMERO DI FIBONACCI
Il calcolo del numero di Fibonacci e' un problema prettamente recursive method.
E' possibile, pero', risolverlo anche con un processo iterativo. 
Confrontiamo i due algoritmi'''

# RECURSIVE Algorithm di FIBONACCI

def fibRicorsivo(n):
    if n==0 or n==1:                                # Θ(1) 'Casi Base
        return n                                    # Θ(1)
    else:                                           # Θ(1) 'Recursive Step
        return fibRicorsivo(n-1)+fibRicorsivo(n-2)  # T(n-1)+T(n-2)


# Input size: valore del numero n
# Best case and worst case coincide per valori grandi di n (gli unici
# validi per il calcolo di notazione asintotica).
# Computational Cost: T(n)=Θ(1)+T(n-1)+T(n-2) -> Recurrence Equations



# ITERATIVE Algorithm di FIBONACCI

def fibIterativo(n):
    if n<=1:                             # Θ(1)
        return n                         # Θ(1)
    fib0,fib1,fib=0,1,0                  # Θ(1)
    for i in range(2,n+1):               # n*Θ(1)+Θ(1)
        fib=fib0+fib1                    # Θ(1)
        fib0,fib1=fib1,fib               # Θ(1)
    return fib                           # Θ(1)

# Input size: valore del numero n
# Best case and worst case coincide per valori grandi di n (gli unici
# validi per il calcolo di notazione asintotica).
# Computational Cost: T(n)=Θ(1)+n*Θ(1)+Θ(1)=Θ(n)    

n=13
fibIt=fibIterativo(n)
fibRic=fibRicorsivo(n)

print("Per n=",n," il numero di Fibonacci e' pari a ",
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



# CONFRONTO ALGORITMO RICORSIVO/ITERATIVO
'''
L'algoritmo RICORSIVO e' molto meno efficiente dell'algoritmo
ITERATIVO. Sia in termini di TIME che di SPACE COMPLEXITY!!
'''


# GRAPHICAL REPRESENTATION


def rappresentazioneGrafica(data_x,data_y,tolerance,title,legendLabel):
    
    delta_max = tolerance # maximum difference in y between two points
    delta = 0 # running correction value
    data_cor = [] # corrected array
    data_cor.append(data_y[0])   # we append two first points
    data_cor.append(data_y[1])
    i=0
    
    for i in range(0,len(data_x)-2): # two first points are allready appended
        i += 2
        delta_i = data_y[i] - data_y[i-1]
        if np.abs(delta_i) > delta_max:
            delta += (delta_i - (data_cor[i-1] - data_cor[i-2]))
            data_cor.append(data_y[i]-delta)
        else:
            data_cor.append(data_y[i]-delta)
    
    
    plt.plot(data_x, data_cor,label=legendLabel)
    
    plt.xlabel('Inputs')
    plt.ylabel('Time [secs]')
    plt.legend()
    plt.title(title)



stepsA=[]
for i in range(1,15):
    tic=time.perf_counter_ns()
    fibIt=fibIterativo(i)
    toc=time.perf_counter_ns()
    stepsA.append(round(toc-tic,6))


stepsB=[]
for i in range(1,15):
    tic=time.perf_counter_ns()
    fibRic=fibRicorsivo(i)
    toc=time.perf_counter_ns()
    stepsB.append(round(toc-tic,6))

    
rappresentazioneGrafica(range(1,15),stepsA,10000,"Algoritmi di Calcolo "  
                        "del numero di Fibonacci Iter/Ricors","Iterativo")

rappresentazioneGrafica(range(1,15),stepsB,10000,"Algoritmi di Calcolo "  
                        "del numero di Fibonacci Iter/Ricors","Ricorsivo")



