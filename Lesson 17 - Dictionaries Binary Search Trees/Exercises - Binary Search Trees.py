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


# IMPORT CLASSI DEL PACKAGE
from BinarySearchNode import Nodo
from BinarySearchTree import AlberoBinarioDiRicerca




'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


'''
PREPARAZIONE ALBERO
'''

valoriNodi=[18,11,33,7,15,22,80,13,16,50,91,42,64]
indiciPadri=[None,0,0,1,1,2,2,4,4,6,6,9,9]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,len(nodi),1):
    if indiciPadri[i]==None:
        nodi[i].setParent(None)
    else:
        nodi[i].setParent(nodi[indiciPadri[i]])
    k=0
    for j in range(0,len(indiciPadri),1):
        if indiciPadri[j]==i:
            if k==0:
                nodi[i].setLeft(nodi[j])
                k+=1
            else:
                nodi[i].setRight(nodi[j])
                break
         
radice=nodi[0]
albero=AlberoBinarioDiRicerca(radice)


'''
FUNZIONE DI RICERCA
'''

# Data una chiave k e un albero p in input, la funzione ritorna il nodo
# dell'albero avente chiave con valore uguale a k.

def ABR_searchRic(p,k):                         # T(h)
    if (p==None or p.getKey()==k):              # Θ(1)
        return p                                # Θ(1)
    if (k<p.getKey()):                          # Θ(1)
        return ABR_searchRic(p.getLeft(),k)     # T(h-1)
    else:                                       # Θ(1)
        return ABR_searchRic(p.getRight(),k)    # T(h-1)

# Costo Computazionale
# Dimensione dell'input: Altezza h dell'albero
# Si esegue la funzione h volte con operazioni ogni volta di costo costante
# Θ(1). Quindi il costo totale equivale a h volte Θ(1).
# Costo: T(h)= T(h-1)+Θ(1) -> T(h)=Θ(h)





# ESERCIZIO 1 ################################################################

'''
Scrivere lo pseudocodice (sia iterativo che ricorsivo) della funzione che 
calcola il MINIMO in un ABR.
'''

# Ricorsivo
def minimoRecurs(p):                             # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    if p.getLeft()==None:                        # Θ(1)
        return p                                 # Θ(1)
    return minimoRecurs(p.getLeft())             # T(h-1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def minimoIter(p):                               # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getLeft()                            # Θ(1)
    return p                                     # Θ(1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'TEST'
# Risultato atteso: 7
print("Minimo: " +str(minimoRecurs(albero.getRoot()))+ " [Ricorsivo]")
print("Minimo: " + str(minimoIter(albero.getRoot())) + " [Iterativo]")




    
# ESERCIZIO 2 ################################################################

'''
Scrivere lo pseudocodice (sia iterativo che ricorsivo) della funzione che
calcola il massimo in un ABR.
'''

# Ricorsivo
def massimoRecurs(p):                             # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    if p.getRight()==None:                        # Θ(1)
        return p                                  # Θ(1)
    return massimoRecurs(p.getRight())            # T(h-1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def massimoIter(p):                               # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getRight()                            # Θ(1)
    return p                                      # Θ(1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'TEST'
# Risultato atteso: 91
print("Massimo: " +str(massimoRecurs(albero.getRoot()))+ " [Ricorsivo]")
print("Massimo: " + str(massimoIter(albero.getRoot())) + " [Iterativo]")





# ESERCIZIO 3 ################################################################

'''
Scrivere lo pseudocodice (sia ITERATIVO sia RICORSIVO) della funzione che
calcola il PREDECESSORE di un valore dato in un Albero Binario di Ricerca.
'''

# Restituisce il nodo avente chiave il cui valore sarebbe immediatamente 
# precedente a quello passato in input se i nodi dell'albero venissero ordinati
# in ordine crescente in base al valore della loro chiave.

# Iterativo
def predecessoreIter(p,k):                        # T(h)
    # 1. Ricava il nodo avente chiave uguale a k
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. Se il nodo ha figlio Sx cerca il massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoIter(nodo.getLeft())   # Ω(1) o O(h)
    else:                                         # Θ(1)
    # 4. Se il nodo NON ha figlio Sx, risali l'albero     
    #    tramite ITERAZIONE    
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getLeft()):  # Θ(1)
            nodo=nodo.getParent()                 # Θ(1)
        predecessor=nodo.getParent()              # Θ(1)
    return predecessor                            # Θ(1)

# Ricorsivo
def predecessoreRecurs(p,k):                      # T(h)
    # 1. Ricava il nodo avente chiave uguale a k    
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. Se il nodo ha figlio Sx cerca il massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoRecurs(nodo.getLeft()) # Ω(1) o O(h)     
    else:                                         # Θ(1)
    # 4. Se il nodo NON ha figlio Sx, risali l'albero
    #    tramite RICORSIONE
        return predecRecurs(nodo)                 # S(h)
    return predecessor                            # Θ(1)

def predecRecurs(nodo):                           # S(h)
    # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
    #    quindi ritorna la radice.
    if nodo.getParent()==None:                    # Θ(1)
        return nodo                               # Θ(1)
    # 2. Se il nodo non coincide con il figlio Sx di suo padre,
    #    restituisci il nodo...
    if nodo!=nodo.getParent().getLeft():          # Θ(1)
        return nodo.getParent()                   # Θ(1)
    # 3. Se il nodo coincide con il figlio Sx di suo padre, 
    #    continua la risalita passando il nodo padre nella nuova 
    #    chiamata ricorsiva.
    return predecRecurs(nodo.getParent())         # S(h-1)   

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  


'TEST'
k1=80
k2=13
predIter1=predecessoreIter(albero.getRoot(),k1)  # Iterativo -Caso 1- Discesa
predIter2=predecessoreIter(albero.getRoot(),k2)  # Iterativo -Caso 2- Risalita
predRec1=predecessoreRecurs(albero.getRoot(),k1) # Ricorsivo -Caso 1- Discesa
predRec2=predecessoreRecurs(albero.getRoot(),k2) # Ricorsivo -Caso 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))






# ESERCIZIO 4 ################################################################

'''
Scrivere lo pseudocodice (sia ITERATIVO sia RICORSIVO) della funzione che
calcola il SUCCESSORE di un valore dato in un Albero Binario di Ricerca.
'''


# Restituisce il nodo avente chiave il cui valore sarebbe immediatamente 
# successivo a quello passato in input se i nodi dell'albero venissero ordinati
# in ordine crescente in base al valore della loro chiave.

# Iterativo
def successoreIter(p, k):                          # T(h)
    # 1. Ricava il nodo avente chiave uguale a k
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. Se il nodo ha figlio Dx cerca il minimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoIter(nodo.getRight())      # Ω(1) o O(h)
    else:        
    # 4. Se il nodo NON ha figlio Dx, risali l'albero     
    #    tramite ITERAZIONE
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getRight()):  # Θ(1)
            nodo=nodo.getParent()                  # Θ(1)
        successor=nodo.getParent()                 # Θ(1)
    return successor                               # Θ(1)

# Ricorsivo
def successoreRecurs(p,k):                         # T(h)
    # 1. Ricava il nodo avente chiave uguale a k    
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. Se il nodo ha figlio Dx cerca il massimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoRecurs(nodo.getRight())    # Ω(1) o O(h)
    else:                                          # Θ(1)
    # 4. Se il nodo NON ha figlio Dx, risali l'albero
    #    tramite RICORSIONE
        return succesRecurs(nodo)                  # S(h)
    return successor                               # Θ(1)

def succesRecurs(nodo):                            # S(h)
    # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
    #    quindi ritorna la radice.
    if nodo.getParent()==None:                     # Θ(1)
        return nodo                                # Θ(1) 
    # 2. Se il nodo non coincide con il figlio Dx di suo padre,
    #    restituisci il nodo...
    if nodo!=nodo.getParent().getRight():          # Θ(1)
        return nodo.getParent()                    # Θ(1)
    # 3. Se il nodo coincide con il figlio Dx di suo padre, 
    #    continua la risalita passando il nodo padre nella nuova 
    #    chiamata ricorsiva.
    return succesRecurs(nodo.getParent())          # S(h-1)     

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  


'TEST'
k1=11
k2=16
succIter1=successoreIter(albero.getRoot(),k1)  # Iterativo -Caso 1- Discesa
succIter2=successoreIter(albero.getRoot(),k2)  # Iterativo -Caso 2- Risalita
succRec1=successoreRecurs(albero.getRoot(),k1) # Ricorsivo -Caso 1- Discesa
succRec2=successoreRecurs(albero.getRoot(),k2) # Ricorsivo -Caso 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))


