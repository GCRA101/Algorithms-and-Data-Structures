# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023

@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# LA RICORSIONE

'''
CALCOLO del FATTORIALE
Il calcolo del fattoriale puo' essere eseguito tramite un algoritmo ITERATIVO
ma anche tramite un algoritmo RICORSIVO'''

# Algoritmo ITERATIVO

def fattorialeIterativo(n):
    fatt=1                      #Θ(1)
    for i in range(1,n+1):      #n*Θ(1)+Θ(1)
        fatt=fatt*i             #Θ(1)
    return fatt                 #Θ(1)

# Dimensione input: valore intero n
# Caso migliore e caso peggiore coincidono per qualsiasi valore grande
# di n dato che l'algoritmo scorre sempre e cmq tutti i valori da 1 a n.
# Costo Computazionale: T(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)

# Algoritmo RICORSIVO

def fattorialeRicorsivo(n):
    if n==1:                              #Θ(1)     'Caso Base'
        return 1                          #Θ(1)     
    else:                                 #Θ(1)
        return n*fattorialeRicorsivo(n-1) # T(n-1)  'Passo Ricorsivo'

# Dimensione input: valore intero n
# Costo Computazionale: T(n)=Θ(1)+T(n-1) -> Equazioni di Ricorrenza


n=61

tic=time.perf_counter()
fattIter=fattorialeIterativo(n)
toc=time.perf_counter()
fattIterTime=round(toc-tic,6)

tic=time.perf_counter()
fattRicors=fattorialeRicorsivo(n)
toc=time.perf_counter()
fattRicorsTime=round(toc-tic,6)

print('Algoritmo Iterativo : ',fattIterTime, ' [secs]')
print('Algoritmo Ricorsivo : ',fattRicorsTime, ' [secs]')




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
for i in range(5,2000):
    tic=time.perf_counter()
    fattorialeIterativo(i)
    toc=time.perf_counter()
    stepsA.append(round(abs(toc-tic),12))


stepsB=[]
for i in range(5,2000):
    tic=time.perf_counter()
    fattorialeRicorsivo(i)
    toc=time.perf_counter()
    stepsB.append(round(abs(toc-tic),12))

    
rappresentazioneGrafica(range(5,2000),stepsA,0.0001,"Algoritmi di Calcolo "  
                        "del Fattoriale Iterat/Ricors","Iterativo")

rappresentazioneGrafica(range(5,2000),stepsB,0.0001,"Algoritmi di Calcolo " 
                       "del Fattoriale Iterat/Ricors","Ricorsivo")












