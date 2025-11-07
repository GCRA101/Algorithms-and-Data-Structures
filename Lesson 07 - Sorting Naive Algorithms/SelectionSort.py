# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# ALGORITMI DI ORDINAMENTO - SELECTION SORT

'''
SELECTION SORT 
L'algoritmo Selection Sort e' uno degli algoritmi piu' semplici per effettuare
l'ordinamento di una serie/record di dati insieme al INSERTION SORT e al 
BUBBLE SORT'
L'algoritmo SELECTION SORT presenta lo stesso costo computazionale per il caso
peggiore (serie dati ordinata in ordine inverso) e il caso migliore (serie dati
gia' ordinata)
- Costo Computazionale: Θ(n^2)
'''

A=[1,5,3,7,8,11,1,56,2,4]
Aworst=[87,31,25,23,21,11,8,5,3,1]
Abest=[1,5,6,31,44,53,98,101]

def selectionSort(A):                 # T(n)
    for i in range(0,len(A)):         # n*Θ(1)+Θ(1)
        #min=A[i]                      # Θ(1)
        jmin=i
        for j in range(i+1,len(A)):   # tjΘ(1)+Θ(1) dove tj=(n-1) sempre
            #if A[j]<min:
             if A[j]<A[jmin]:
                #min=A[j]              # Θ(1)
                jmin=j
        #A.pop(jmin)
        A.insert(i,A.pop(jmin))               # Θ(1)
        
    return A
    

# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore coincidono per qualsiasi valore grande di n 
# dato che il ciclo for interno passsera' in rassegna sempre tutti gli elementi
# per trovare i minimi parziali
# Costo Computazionale: T(n)=Θ(n^2) - Caso peggiore/migliore


Asorted1=selectionSort(A)
Asorted2=selectionSort(Aworst)
Asorted3=selectionSort(Abest)



# RAPPRESENTAZIONE GRAFICA


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
for i in range(5,100,1):
    A=list(range(0,i,1))
    tic=time.perf_counter_ns()
    selectionSort(A)
    toc=time.perf_counter_ns()
    stepsA.append(abs(round(toc-tic,8)))


stepsB=[]
for i in range(100,5,-1):
    B=list(range(i,0,-1))
    tic=time.perf_counter_ns()
    selectionSort(B)
    toc=time.perf_counter_ns()
    stepsB.append(abs(round(toc-tic,8)))

    
rappresentazioneGrafica(range(5,100,1),stepsA,1,"Algoritmi di Ordinamento "  
                        "- Selection Sort","Caso Migliore")

rappresentazioneGrafica(range(5,100,1),stepsB,1,"Algoritmi di Ordinamento "  
                        "- Selection Sort","Caso Peggiore")



