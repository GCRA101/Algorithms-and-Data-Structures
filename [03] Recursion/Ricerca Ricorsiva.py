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
ALGORITMI di RICERCA RICORSIVA
Sia la ricerca SEQUENZIALE sia la ricerca BINARIA possono essere definite
tramite algoritmi RICORSIVI'''

# Algoritmo RICORSIVO di RICERCA SEQUENZIALE

def ricercaSequenzialeRicorsiva(A,v,i):
    if A[i]==v:                                    # Θ(1)   'Caso Base 1
        return i                                   # Θ(1) 
    elif i>=len(A):                                # Θ(1)   'Caso Base 2 
        return -1                                  # Θ(1) 
    else:                                          # Θ(1) 
        i+=1                                       # Θ(1) 
        return ricercaSequenzialeRicorsiva(A,v,i)  # T(n-1) 'Passo Ricorsivo
    

# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore variano a seconda che l'elemento cercato v
# si trovi nella prima cella dell'array A o non esista affatto.
# Costo Computazionale: T(n)=Θ(1)+T(n-1)


# Alternativamente...si possono utilizzare due funzioni, una interna all'altra
# di cui solo quella interna e' ricorsiva

def ricercaSequenziale(A,v):
    'Chiamata di lancio della Ricorsione'
    return ricercaSequenzialeRicorsiva(A,v,len(A)-1) #T(n)
    
def ricercaSequenzialeRicorsiva(A,v,n):
    if A[n]==v:                                     # Θ(1)   'Caso Base 1
        return True                                 # Θ(1) 
    elif n==0:                                      # Θ(1)   'Caso Base 2 
        return False                                # Θ(1) 
    else:                                           # Θ(1) 
        return ricercaSequenzialeRicorsiva(A,v,n-1) # T(n-1) 'Passo Ricorsivo





# Algoritmo RICORSIVO di RICERCA BINARIA

def ricercaBinaria(A,v):
    a,b=0,len(A)-1                                   # Θ(1)
    return ricercaBinariaRicorsiva(A,v,a,b)          # T(n)
    
def ricercaBinariaRicorsiva(A,v,a,b):
    m=(a+b)//2                                       # Θ(1)
    if a>b:                                          # Θ(1)   'Caso Base 1
        return False                                 # Θ(1)
    if A[m]==v:                                      # Θ(1)   'Caso Base 2
        return True                                  # Θ(1)
    if A[m]<v:                                       # Θ(1)
        return ricercaBinariaRicorsiva(A, v, m+1, b) # T(n/2) 'Passo Ricorsivo
    if A[m]>v:                                       # Θ(1)
        return ricercaBinariaRicorsiva(A, v, a, m-1) # T(n/2)


# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore variano a seconda che il valore cercato
# sia a meta' dell'array ordinato A (Ω(1)) o non sia affatto presente
# all'interno dell'array A (O(logn))
# Costo Computazionale: T(n)=Θ(1)+T(n/2) -> Equazioni di Ricorrenza



v=1
A=range(1,1000)

tic=time.perf_counter_ns()
found=ricercaSequenziale(A,v)
toc=time.perf_counter_ns()
seqRicTime=round(toc-tic,6)

tic=time.perf_counter_ns()
found=ricercaBinaria(A,v)
toc=time.perf_counter_ns()
binRicTime=round(toc-tic,6)

print('Algoritmo di Ricerca Sequenziale Ricorsivo : ',seqRicTime,' [nanosecs]')
print('Algoritmo di Ricerca Binaria Ricorsivo : ',binRicTime,' [nanosecs]')



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
for i in range(5,1000):
    A=list(range(1,i))
    v=i
    tic=time.perf_counter_ns()
    found=ricercaSequenziale(A,v)
    toc=time.perf_counter_ns()
    stepsA.append(round(toc-tic,6))


stepsB=[]
for i in range(5,1000):
    B=list(range(1,i))
    v=i
    tic=time.perf_counter_ns()
    found=ricercaBinaria(B,v)
    toc=time.perf_counter_ns()
    stepsB.append(round(toc-tic,6))

    
rappresentazioneGrafica(range(5,1000),stepsA,1000,"Algoritmi di Ricerca "  
                        "Sequenziale/Binaria Ricorsiva","Sequenziale")

rappresentazioneGrafica(range(5,1000),stepsB,1000,"Algoritmi di Ricerca "  
                        "Sequenziale/Binaria Ricorsiva","Binaria")



