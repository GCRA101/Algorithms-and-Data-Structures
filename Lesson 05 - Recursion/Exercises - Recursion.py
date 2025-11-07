# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:10:30 2023

@author: giorg
"""

'Import main libraries'
import math as math
import numpy as np
import time
import matplotlib.pyplot as plt




# ESERCIZIO 1 ################################################################

'''
Dati in input due interi n e k, calcolare la potenza k-esima di n tramite 
algoritmo recursive method
'''

# Considerazioni
''' 
n^k=n*n*n*n*n... k volte
Caso base: per k=1->n=n
'''

# Algoritmo

def es1(n,k):                     # T(k)
    if k==1: return n             # Θ(1)      ' Base Case
    return n*es1(n,k-1)           # T(k-1)    ' Recursive Step

# Input size: valore del coefficiente intero k
# Il caso peggiore e il caso migliore coincidono. Infatti, anche se per k=0,
# il costo computazionale sarebbe = Θ(1), la notazione asintotica si calcola
# solo per valori grandi dell'input (i.e. k->∞) per cui il costo computazionale
# e' maggiore di Θ(1) e cresce al crescere del valore di k.
# Computational Cost: T(k)=Θ(1)+T(k-1) -> Recurrence Equations





# ESERCIZIO 2 ################################################################

'''
Dato in input un array di n interi, calcolare la somma dei suoi elementi
tramite un algoritmo recursive method
'''

# Considerazioni
'''
L'azione da eseguire ripetutamente consiste nel sommare il numero corrente
alla somma dei precedenti. 
Il caso base che interrompe la ricorsione si ha quando si raggiunge l'indice
dell'ultimo elemento
'''


# Algoritmo SBAGLIATO

def es2a(A,sum=0,i=0):             # T(n)
    if i==len(A) : return sum      # Θ(1)
    sum+=A[i]                      # Θ(1)
    return es2a(A,sum,i+1)         # T(n-1)

# Input size: numero n di valori contenuti nell'array A
# Il caso peggiore e il caso migliore coincidono. Infatti, per qualunque valore
# GRANDE di n, l'algoritmo scorrera' sempre tutti gli elementi dell'array A
# dal primo all'ultimo.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations

'''
ATTENZIONE!!!
L'algoritmo sopra NON E' PROPRIAMENTE RICORSIVO in quanto il valore totale
della somma viene ritornato proprio una volta raggiunto il caso base 
(i==len(A)-1)...mentre dovrebbe essere ritornato dalla chiusura di chiamata
della prima funzione della catena ricorsiva...
Vediamo come riscrivere la funzione ricorsiva in modo corretto.
'''


# Algoritmo CORRETTO

def es2b(A,i=0):                   # T(n)
    if i==len(A)-1: return A[i]    # Θ(1)      ' Base Case 
    return (A[i]+es2b(A,i+1))      # T(n-1)    ' Recursive Step

# Input size: numero n di valori contenuti nell'array A
# Il caso peggiore e il caso migliore coincidono. Infatti, per qualunque valore
# GRANDE di n, l'algoritmo scorrera' sempre tutti gli elementi dell'array A
# dal primo all'ultimo.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations


A=[1,2,3,4,5,6,7,8,9,10]
sommaAlgA=es2a(A)
sommaAlgB=es2b(A)





# ESERCIZIO 3 ################################################################

'''
Dato in input un array di n interi, trovare il minimo.
'''

# Considerazioni
'''
Assumendo che l'array non sia un array ordinato, l'algoritmo dovra' scorrere
tutti gli elementi dell'array dal primo all'ultimo per trovare il minimo.
l'operazione che viene ripetuta e' il confronto tra due elementi consecutivi.
Il caso base si ha quando si raggiunge l'ultimo elemento nell'array'''

# Algoritmo

A=[31,22,7,83,101,71,27,52,3,21,15,98,88,17]

def es3(A,i=len(A)-1):                   # T(n)
    if i==0: return A[i]                 # Θ(1)      ' Base Case 
    return min(A[i],es3(A,i-1))          # T(n-1)    ' Recursive Step
    
minVal=es3(A)

# Input size: numero n di valori contenuti nell'array A
# Il caso peggiore e il caso migliore coincidono. Infatti, per qualunque valore
# GRANDE di n, l'algoritmo scorrera' sempre tutti gli elementi dell'array A
# dal primo all'ultimo.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations





# ESERCIZIO 4 ################################################################
    
'''
Dato in input un array di n interi, verificare se e' palindromo.'''

# Considerazioni
'''
L'algoritmo deve ritornare un output di tipo boolean a seconda che l'array in 
input sia palindromo o meno.
Casi base: 1) differenza indici estremi subArray <=1 
           2) valori negli indici estremi sono differenti
Passo recursive method: confronto valori indici estremi per indici che si avvicinano
                 verso il punto medio dell'array'''

'Best Case'
# A=[31,22,7,83,101,71,27,52,3,21,15,98,88,17]
'Worst Case'
A=[38,12,71,4,22,9,32,9,22,4,71,12,38] 
                 
def es4(A,i=0,j=len(A)-1):        # T(n)
    if i>=j: return True          # Θ(1)    ' Base Case
    if A[i]!=A[j]: return False   # Θ(1)    ' Base Case
    return es4(A,i+1,j-1)         # T(n-2)  ' Recursive Step

bool=es4(A)

# Input size: numero n di valori contenuti nell'array A

# Computational Cost
# Il caso migliore e' il caso in cui gia' i due valori estremi dell'array sono
# differenti (in tal caso, e' possibile uscire dalla ricorsione gia' alla prima
# iterazione).
# Il caso peggiore e' il caso in cui l'array e' palindromo.
# Caso Migliore: T(n)=Θ(1)
# Caso Peggiore: T(n)=Θ(1)+T(n-2) -> Recurrence Equations





# ESERCIZIO 5 ################################################################
    
'''
Dato in input un array di n interi, stampare le chiavi dall'ultima alla 
prima, ossia nell'ordine: V[n-1] V[n-2] V[n-3] V[n-4]...V[1] V[0]'''

# Considerazioni
'''
L'algoritmo deve arrivare a stampare l'ultimo elemento nel caso base e poi
stampare tutti i restanti fino al primo nella sequenza di chiusura delle 
chiamate di funzione.
Caso base: 1) indice elemento = indice finale
Passo recursive method: stampa elemento V[n] in console'''

'Best/Worst Case'
A=[12,51,22,61,32,81,9,43,78,101,2] 
                 
def es5a(A,i=0):                                    # T(n)
    if (i==len(A)-1):                               # Θ(1)
        return A[i]                                 # Θ(1)
    return str(es5a(A,i+1)) + " " + str(A[i])+ " "  # T(n-1)

print("Soluzione Mia")
print(es5a(A))

def es5b(A,i=len(A)-1):
    print(A[i], end= "  ")
    if i>0:
        return es5b(A,i-1)

print("Soluzione Prof")
es5b(A)

# Input size: numero n di valori contenuti nell'array A

# Computational Cost
# Per valori grandi di n, il caso migliore e il caso peggiore coincidono.
# Infatti l'algoritmo deve sempre e comunque scorrere tutti gli elementi dell'
# array.
# Caso Migliore/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations




# ESERCIZIO 6 ################################################################
    
'''
Dato in input un array di n interi, stampare le chiavi dalla prima all'
ultima, ossia nell'ordine: V[0] V[1] V[2]...V[n-2] V[n-1]'''

# Considerazioni
'''
L'algoritmo deve arrivare a stampare il primo elemento nel caso base e poi
stampare tutti i restanti fino all'ultimo nella sequenza di chiusura delle 
chiamate di funzione.
Caso base: 1) indice elemento = indice iniziale
Passo recursive method: stampa elemento V[n] in console'''

'Best/Worst Case'
A=[12,51,22,61,32,81,9,43,78,101,2] 
                 
def es6a(A,i=len(A)-1):                             # T(n)
    if (i==0):                                      # Θ(1)
        return A[i]                                 # Θ(1)
    return str(es6a(A,i-1)) + " " + str(A[i])+ " "  # T(n-1)

print("")
print("Soluzione Mia")
print(es6a(A))

def es6b(A,i=0):
    print(A[i], end= "  ")
    if i<len(A)-1:
        return es6b(A,i+1)

print("Soluzione Prof")
es6b(A)

# Input size: numero n di valori contenuti nell'array A

# Computational Cost
# Per valori grandi di n, il caso migliore e il caso peggiore coincidono.
# Infatti l'algoritmo deve sempre e comunque scorrere tutti gli elementi dell'
# array.
# Caso Migliore/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations




# ESERCIZIO 7 ################################################################
    
'''
VEDI IL FOLDER TORRE HANOI '''



# ESERCIZI per CASA ##########################################################

'Esercizio B'
'''Progettare un algoritmo recursive method che, dati due numeri interi x e y, x>y>0,
ne calcoli il massimo comun divisore utilizzando il seguente procedimento (di
Euclide): 
    - se y=0 allora MCD(x,y)=x
    - altrimenti MCD(x,y)=MCD(y,x%y)
        - dove x%y rappresenta il resto della divisione tra x e y '''
        
def MCD(x,y):
    if y==0: 
        return x
    return MCD(y,x%y)

x=73
y=41
print("\n\nMCD di ",x," e ",y, " e' ",MCD(x,y))

# Input size: numero n di valori contenuti nell'array A

# Computational Cost
# Per valori grandi di n, il caso migliore e il caso peggiore coincidono.
# Infatti l'algoritmo deve sempre e comunque scorrere tutti gli elementi dell'
# array.
# Caso Migliore/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations
