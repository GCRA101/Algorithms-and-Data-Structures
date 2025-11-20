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


# IMPORT PACKAGE CLASSES
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

for the in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[the])) 
    
for the in range(0,len(nodi),1):
    if indiciPadri[the]==None:
        nodi[the].setParent(None)
    else:
        nodi[the].setParent(nodi[indiciPadri[the]])
    k=0
    for j in range(0,len(indiciPadri),1):
        if indiciPadri[j]==the:
            if k==0:
                nodi[the].setLeft(nodi[j])
                k+=1
            else:
                nodi[the].setRight(nodi[j])
                break
         
root=nodi[0]
tree=AlberoBinarioDiRicerca(root)


'''
function DI RICERCA
'''

# Given aa key k and a tree p in input, the function returns the nodo
# dell'tree avente key with value uguale to k.

def ABR_searchRic(p,k):                         # T(h)
    if (p==None or p.getKey()==k):              # Θ(1)
        return p                                # Θ(1)
    if (k<p.getKey()):                          # Θ(1)
        return ABR_searchRic(p.getLeft(),k)     # T(h-1)
    else:                                       # Θ(1)
        return ABR_searchRic(p.getRight(),k)    # T(h-1)

# Computational Cost
# Dimension dell'input: Altezza h dell'tree
# Si esegue the function h times with operazioni each time of cost constant
# Θ(1). Therefore the cost totale equivale to h times Θ(1).
# Cost: T(h)= T(h-1)+Θ(1) -> T(h)=Θ(h)





# ESERCIZIO 1 ################################################################

'''
Scrivere the pseudocodice (sia iterative that recursive method) of the function that 
calculates the MINIMO in a ABR.
'''

# Ricorsivo
def minimoRecurs(p):                             # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    if p.getLeft()==None:                        # Θ(1)
        return p                                 # Θ(1)
    return minimoRecurs(p.getLeft())             # T(h-1)

# Computational Cost
# Input size: altezza dell'tree h
# Cost: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def minimoIter(p):                               # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getLeft()                            # Θ(1)
    return p                                     # Θ(1)

# Computational Cost
# Input size: altezza dell'tree h
# Cost: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'TEST'
# Risultato atteso: 7
print("Minimo: " +str(minimoRecurs(tree.getRoot()))+ " [Ricorsivo]")
print("Minimo: " + str(minimoIter(tree.getRoot())) + " [Iterativo]")




    
# ESERCIZIO 2 ################################################################

'''
Scrivere the pseudocodice (sia iterative that recursive method) of the function that
calculates the massimo in a ABR.
'''

# Ricorsivo
def massimoRecurs(p):                             # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    if p.getRight()==None:                        # Θ(1)
        return p                                  # Θ(1)
    return massimoRecurs(p.getRight())            # T(h-1)

# Computational Cost
# Input size: altezza dell'tree h
# Cost: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def massimoIter(p):                               # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getRight()                            # Θ(1)
    return p                                      # Θ(1)

# Computational Cost
# Input size: altezza dell'tree h
# Cost: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'TEST'
# Risultato atteso: 91
print("Massimo: " +str(massimoRecurs(tree.getRoot()))+ " [Ricorsivo]")
print("Massimo: " + str(massimoIter(tree.getRoot())) + " [Iterativo]")





# ESERCIZIO 3 ################################################################

'''
Scrivere the pseudocodice (sia iterative sia recursive) of the function that
calculates the PREDECESSOR of to value given in a Binary Search Tree.
'''

# returns the nodo avente key the which value sarebbe immediatamente 
# precedente to that passato in input if the nodi dell'tree venissero ordinati
# in ordine crescente in base al value of the loro key.

# Iterativo
def predecessoreIter(p,k):                        # T(h)
    # 1. Ricava the nodo avente key uguale to k
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. If the nodo not esiste, restituisci value nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. If the nodo ha figlio Sx cerca the massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoIter(nodo.getLeft())   # Ω(1) o O(h)
    else:                                         # Θ(1)
    # 4. If the nodo NON ha figlio Sx, risali l'tree     
    #    through ITERAZIONE    
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getLeft()):  # Θ(1)
            nodo=nodo.getParent()                 # Θ(1)
        predecessor=nodo.getParent()              # Θ(1)
    return predecessor                            # Θ(1)

# Ricorsivo
def predecessoreRecurs(p,k):                      # T(h)
    # 1. Ricava the nodo avente key uguale to k    
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. If the nodo not esiste, restituisci value nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. If the nodo ha figlio Sx cerca the massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoRecurs(nodo.getLeft()) # Ω(1) o O(h)     
    else:                                         # Θ(1)
    # 4. If the nodo NON ha figlio Sx, risali l'tree
    #    through RICORSIONE
        return predecRecurs(nodo)                 # S(h)
    return predecessor                            # Θ(1)

def predecRecurs(nodo):                           # S(h)
    # 1. If the nodo not ha padre, esso is the root dell'tree...
    #    therefore ritorna the root.
    if nodo.getParent()==None:                    # Θ(1)
        return nodo                               # Θ(1)
    # 2. If the nodo not coincide with the figlio Sx of suo padre,
    #    restituisci the nodo...
    if nodo!=nodo.getParent().getLeft():          # Θ(1)
        return nodo.getParent()                   # Θ(1)
    # 3. If the nodo coincide with the figlio Sx of suo padre, 
    #    continua the risalita passando the nodo padre in the nuova 
    #    chiamata ricorsiva.
    return predecRecurs(nodo.getParent())         # S(h-1)   

# Computational Cost
# Input size: altezza dell'tree h
# Costo Iterativa: T(h)=Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  


'TEST'
k1=80
k2=13
predIter1=predecessoreIter(tree.getRoot(),k1)  # iterative -Case 1- Discesa
predIter2=predecessoreIter(tree.getRoot(),k2)  # iterative -Case 2- Risalita
predRec1=predecessoreRecurs(tree.getRoot(),k1) # recursive -Case 1- Discesa
predRec2=predecessoreRecurs(tree.getRoot(),k2) # recursive -Case 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))






# ESERCIZIO 4 ################################################################

'''
Scrivere the pseudocodice (sia iterative sia recursive) of the function that
calculates the SUCCESSORE of to value given in a Binary Search Tree.
'''


# returns the nodo avente key the which value sarebbe immediatamente 
# successivo to that passato in input if the nodi dell'tree venissero ordinati
# in ordine crescente in base al value of the loro key.

# Iterativo
def successoreIter(p, k):                          # T(h)
    # 1. Ricava the nodo avente key uguale to k
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. If the nodo not esiste, restituisci value nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. If the nodo ha figlio Dx cerca the minimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoIter(nodo.getRight())      # Ω(1) o O(h)
    else:        
    # 4. If the nodo NON ha figlio Dx, risali l'tree     
    #    through ITERAZIONE
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getRight()):  # Θ(1)
            nodo=nodo.getParent()                  # Θ(1)
        successor=nodo.getParent()                 # Θ(1)
    return successor                               # Θ(1)

# Ricorsivo
def successoreRecurs(p,k):                         # T(h)
    # 1. Ricava the nodo avente key uguale to k    
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. If the nodo not esiste, restituisci value nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. If the nodo ha figlio Dx cerca the massimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoRecurs(nodo.getRight())    # Ω(1) o O(h)
    else:                                          # Θ(1)
    # 4. If the nodo NON ha figlio Dx, risali l'tree
    #    through RICORSIONE
        return succesRecurs(nodo)                  # S(h)
    return successor                               # Θ(1)

def succesRecurs(nodo):                            # S(h)
    # 1. If the nodo not ha padre, esso is the root dell'tree...
    #    therefore ritorna the root.
    if nodo.getParent()==None:                     # Θ(1)
        return nodo                                # Θ(1) 
    # 2. If the nodo not coincide with the figlio Dx of suo padre,
    #    restituisci the nodo...
    if nodo!=nodo.getParent().getRight():          # Θ(1)
        return nodo.getParent()                    # Θ(1)
    # 3. If the nodo coincide with the figlio Dx of suo padre, 
    #    continua the risalita passando the nodo padre in the nuova 
    #    chiamata ricorsiva.
    return succesRecurs(nodo.getParent())          # S(h-1)     

# Computational Cost
# Input size: altezza dell'tree h
# Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  


'TEST'
k1=11
k2=16
succIter1=successoreIter(tree.getRoot(),k1)  # iterative -Case 1- Discesa
succIter2=successoreIter(tree.getRoot(),k2)  # iterative -Case 2- Risalita
succRec1=successoreRecurs(tree.getRoot(),k1) # recursive -Case 1- Discesa
succRec2=successoreRecurs(tree.getRoot(),k2) # recursive -Case 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))


