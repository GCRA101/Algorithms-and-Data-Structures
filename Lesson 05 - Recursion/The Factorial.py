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
FACTORIAL CALCULATION
The factorial calculation can be performed using an ITERATIVE algorithm
but also using to RECURSIVE algorithm'''

# ITERATIVE Algorithm

def fattorialeIterativo(n):
 fatt=1 #Θ(1)
 for the in range(1,n+1): #n*Θ(1)+Θ(1)
 fatt=fatt*the #Θ(1)
 return fatt #Θ(1)

# Input size: integer value n
# Best case and worst case coincide for any large value
# of n since the algorithm always iterates through all values from 1 to n.
# Computational Cost: T(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)

# RECURSIVE Algorithm

def fattorialeRicorsivo(n):
 if n==1: #Θ(1) 'Base Case'
 return 1 #Θ(1) 
 else: #Θ(1)
 return n*fattorialeRicorsivo(n-1) # T(n-1) 'Recursive Step'

# Input size: integer value n
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations


n=61

tic=time.perf_counter()
fattIter=fattorialeIterativo(n)
toc=time.perf_counter()
fattIterTime=round(toc-tic,6)

tic=time.perf_counter()
fattRicors=fattorialeRicorsivo(n)
toc=time.perf_counter()
fattRicorsTime=round(toc-tic,6)

print('Iterative Algorithm : ',fattIterTime, ' [secs]')
print('Recursive Algorithm : ',fattRicorsTime, ' [secs]')




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
for the in range(5,2000):
 tic=time.perf_counter()
 fattorialeIterativo(the)
 toc=time.perf_counter()
 stepsA.append(round(abs(toc-tic),12))


stepsB=[]
for the in range(5,2000):
 tic=time.perf_counter()
 fattorialeRicorsivo(the)
 toc=time.perf_counter()
 stepsB.append(round(abs(toc-tic),12))

 
rappresentazioneGrafica(range(5,2000),stepsA,0.0001,"Factorial Calculation " 
 "Algorithms Iterat/Recurs","Iterativo")

rappresentazioneGrafica(range(5,2000),stepsB,0.0001,"Factorial Calculation " 
 "Algorithms Iterat/Recurs","Ricorsivo")












