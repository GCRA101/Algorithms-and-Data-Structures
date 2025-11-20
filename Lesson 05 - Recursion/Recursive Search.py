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
ALGORITMI of RICERCA RICORSIVA
Sia the ricerca SEQUENZIALE sia the ricerca BINARIA possono essere definite
through algorithms RICORSIVI'''

# RECURSIVE Algorithm of RICERCA SEQUENZIALE

def ricercaSequenzialeRicorsiva(To,v,the):
    if To[the]==v:                                    # Θ(1)   'Base Case 1
        return the                                   # Θ(1) 
    elif the>=len(To):                                # Θ(1)   'Base Case 2 
        return -1                                  # Θ(1) 
    else:                                          # Θ(1) 
        the+=1                                       # Θ(1) 
        return ricercaSequenzialeRicorsiva(To,v,the)  # T(n-1) 'Recursive Step
    

# Input size: number n of elements in array To
# Best case e worst case variano to second that l'element cercato v
# si trovi nella first cella dell'array To o not esista affatto.
# Computational Cost: T(n)=Θ(1)+T(n-1)


# Alternativamente...si possono utilizzare two funzioni, a interna all'altra
# of cui only that interna e' recursive

def ricercaSequenziale(To,v):
    'Chiamata of lancio della Ricorsione'
    return ricercaSequenzialeRicorsiva(To,v,len(To)-1) #T(n)
    
def ricercaSequenzialeRicorsiva(To,v,n):
    if To[n]==v:                                     # Θ(1)   'Base Case 1
        return True                                 # Θ(1) 
    elif n==0:                                      # Θ(1)   'Base Case 2 
        return False                                # Θ(1) 
    else:                                           # Θ(1) 
        return ricercaSequenzialeRicorsiva(To,v,n-1) # T(n-1) 'Recursive Step





# RECURSIVE Algorithm of RICERCA BINARIA

def ricercaBinaria(To,v):
    to,b=0,len(To)-1                                   # Θ(1)
    return ricercaBinariaRicorsiva(To,v,to,b)          # T(n)
    
def ricercaBinariaRicorsiva(To,v,to,b):
    m=(to+b)//2                                       # Θ(1)
    if to>b:                                          # Θ(1)   'Base Case 1
        return False                                 # Θ(1)
    if To[m]==v:                                      # Θ(1)   'Base Case 2
        return True                                  # Θ(1)
    if To[m]<v:                                       # Θ(1)
        return ricercaBinariaRicorsiva(To, v, m+1, b) # T(n/2) 'Recursive Step
    if To[m]>v:                                       # Θ(1)
        return ricercaBinariaRicorsiva(To, v, to, m-1) # T(n/2)


# Input size: number n of elements in array To
# Best case e worst case variano to second that the value cercato
# sia to meta' dell'array ordinato To (Ω(1)) o not sia affatto presente
# all'interno dell'array To (O(logn))
# Computational Cost: T(n)=Θ(1)+T(n/2) -> Recurrence Equations



v=1
To=range(1,1000)

tic=time.perf_counter_ns()
found=ricercaSequenziale(To,v)
toc=time.perf_counter_ns()
seqRicTime=round(toc-tic,6)

tic=time.perf_counter_ns()
found=ricercaBinaria(To,v)
toc=time.perf_counter_ns()
binRicTime=round(toc-tic,6)

print('algorithm of Ricerca Sequenziale recursive : ',seqRicTime,' [nanosecs]')
print('algorithm of Ricerca Binaria recursive : ',binRicTime,' [nanosecs]')



# GRAPHICAL REPRESENTATION


def rappresentazioneGrafica(data_x,data_y,tolerance,title,legendLabel):
    
    delta_max = tolerance # maximum difference in y between two points
    delta = 0 # running correction value
    data_cor = [] # corrected array
    data_cor.append(data_y[0])   # we append two first points
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
for the in range(5,1000):
    To=list(range(1,the))
    v=the
    tic=time.perf_counter_ns()
    found=ricercaSequenziale(To,v)
    toc=time.perf_counter_ns()
    stepsA.append(round(toc-tic,6))


stepsB=[]
for the in range(5,1000):
    B=list(range(1,the))
    v=the
    tic=time.perf_counter_ns()
    found=ricercaBinaria(B,v)
    toc=time.perf_counter_ns()
    stepsB.append(round(toc-tic,6))

    
rappresentazioneGrafica(range(5,1000),stepsA,1000,"Algoritmi of Ricerca "  
                        "Sequenziale/Binaria Ricorsiva","Sequenziale")

rappresentazioneGrafica(range(5,1000),stepsB,1000,"Algoritmi of Ricerca "  
                        "Sequenziale/Binaria Ricorsiva","Binaria")



