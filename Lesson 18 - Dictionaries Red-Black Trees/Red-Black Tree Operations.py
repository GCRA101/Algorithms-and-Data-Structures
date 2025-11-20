# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import math as math
import time
import matplotlib.pyplot as plt
import random


# IMPORT PACKAGE CLASSES
from BinarySearchNode import Nodo
from BinarySearchTree import AlberoBinarioDiRicerca


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
         
radice=nodi[0]
albero=AlberoBinarioDiRicerca(radice)



'''
OPERAZIONI ******************************************************************
'''


'RICERCA'

# Given aa key k e a albero p in input, the function returns the nodo
# dell'albero avente key with value uguale to k.

def ABR_searchRic(p,k):                         # T(h)
    if (p==None or p.getKey()==k):              # Θ(1)
        return p                                # Θ(1)
    if (k<p.getKey()):                          # Θ(1)
        return ABR_searchRic(p.getLeft(),k)     # T(h-1)
    else:                                       # Θ(1)
        return ABR_searchRic(p.getRight(),k)    # T(h-1)

# Computational Cost
# Dimensione dell'input: Altezza h dell'albero
# Si esegue the function h volte with operazioni each volta of costo costante
# Θ(1). Quindi the costo totale equivale to h volte Θ(1).
# Cost: T(h)= T(h-1)+Θ(1) -> T(h)=Θ(h)



'INSERIMENTO'

# Given l'albero p e given the nodo z in input, the function returns l'albero with
# the nodo aggiuntivo inserito nella posizione appropriata.

def ABR_insert(p,z):                             # T(h)
    '1. INIZIALIZZAZIONE Puntatori ausiliari'
    # Padre Nodo Corrente
    y=None                                       # Θ(1)
    # Nodo corrente
    x=p                                          # Θ(1)
    '2. DISCESA fino to Nodo with Figlio Nullo'
    while x!=None:                               # h*Θ(1)+Θ(1)
        # Aggiorna y eguagliandolo to x...
        y=x                                      # Θ(1)
        # Aggiorna x facendolo scendere to dx/sx in base alla sua key...
        if z.getKey()<x.getKey():                # Θ(1)
            x=x.getLeft()                        # Θ(1)
        else:                                    # Θ(1)
            x=x.getRight()                       # Θ(1)
    '3. AGGIUNTA Nuovo Nodo'
    # If l'Albero e' Nullo, usa Nuovo Nodo as Radice dell'Albero...
    if y==None:                                  # Θ(1)
        p=z                                      # Θ(1)
    # If l'Albero not e' nullo, aggiungi the Nuovo Nodo to dx/sx dell'last...
    else:                                        # Θ(1)
        if z.getKey()<y.getKey():                # Θ(1)
            y.left=z                             # Θ(1)
        else:                                    # Θ(1)
            y.right=z                            # Θ(1)
    # Aggiorna the campo Padre del nuovo nodo aggiunto all'albero...
    z.setParent(y)                               # Θ(1)
    # Restituisci l'albero modificato...
    return p                                     # Θ(1)

# Computational Cost
# Dimensione dell'input: Altezza h dell'albero
# Cost: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'MINIMO'

# returns the nodo avente key of value minimo all'interno 
# dell'albero passato in input.

# Ricorsivo
def minimoRecurs(p):                             # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    if p.getLeft()==None:                        # Θ(1)
        return p                                 # Θ(1)
    return minimoRecurs(p.getLeft())             # T(h-1)

# Computational Cost
# Input size: altezza dell'albero h
# Cost: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def minimoIter(p):                               # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getLeft()                            # Θ(1)
    return p                                     # Θ(1)

# Computational Cost
# Input size: altezza dell'albero h
# Cost: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'MASSIMO'

# returns the nodo avente key of value massimo all'interno 
# dell'albero passato in input.

# Ricorsivo
def massimoRecurs(p):                             # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    if p.getRight()==None:                        # Θ(1)
        return p                                  # Θ(1)
    return massimoRecurs(p.getRight())            # T(h-1)

# Computational Cost
# Input size: altezza dell'albero h
# Cost: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def massimoIter(p):                               # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getRight()                            # Θ(1)
    return p                                      # Θ(1)

# Computational Cost
# Input size: altezza dell'albero h
# Cost: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'PREDECESSORE'

# returns the nodo avente key the cui value sarebbe immediatamente 
# precedente to that passato in input if the nodi dell'albero venissero ordinati
# in ordine crescente in base al value della loro key.

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
    # 4. If the nodo NON ha figlio Sx, risali l'albero     
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
    # 4. If the nodo NON ha figlio Sx, risali l'albero
    #    through RICORSIONE
        return predecRecurs(nodo)                 # S(h)
    return predecessor                            # Θ(1)

def predecRecurs(nodo):                           # S(h)
    # 1. If the nodo not ha padre, esso e' the radice dell'albero...
    #    quindi ritorna the radice.
    if nodo.getParent()==None:                    # Θ(1)
        return nodo                               # Θ(1)
    # 2. If the nodo not coincide with the figlio Sx of suo padre,
    #    restituisci the nodo...
    if nodo!=nodo.getParent().getLeft():          # Θ(1)
        return nodo.getParent()                   # Θ(1)
    # 3. If the nodo coincide with the figlio Sx of suo padre, 
    #    continua the risalita passando the nodo padre nella nuova 
    #    chiamata ricorsiva.
    return predecRecurs(nodo.getParent())         # S(h-1)   

# Computational Cost
# Input size: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  



'SUCCESSORE'

# returns the nodo avente key the cui value sarebbe immediatamente 
# successivo to that passato in input if the nodi dell'albero venissero ordinati
# in ordine crescente in base al value della loro key.

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
    # 4. If the nodo NON ha figlio Dx, risali l'albero     
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
    # 4. If the nodo NON ha figlio Dx, risali l'albero
    #    through RICORSIONE
        return succesRecurs(nodo)                  # S(h)
    return successor                               # Θ(1)

def succesRecurs(nodo):                            # S(h)
    # 1. If the nodo not ha padre, esso e' the radice dell'albero...
    #    quindi ritorna the radice.
    if nodo.getParent()==None:                     # Θ(1)
        return nodo                                # Θ(1) 
    # 2. If the nodo not coincide with the figlio Dx of suo padre,
    #    restituisci the nodo...
    if nodo!=nodo.getParent().getRight():          # Θ(1)
        return nodo.getParent()                    # Θ(1)
    # 3. If the nodo coincide with the figlio Dx of suo padre, 
    #    continua the risalita passando the nodo padre nella nuova 
    #    chiamata ricorsiva.
    return succesRecurs(nodo.getParent())          # S(h-1)     

# Computational Cost
# Input size: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  



'CANCELLAZIONE'

# Elimina the nodo dell'albero avente the key del value passato in input.
# The nodo eliminato viene sostituito with the suo predecessore o successore (
# one o l'altro e' the stesso..the risultato e' the medesimo) in modo from evitare
# the disknnessione dell'albero in two sottoalberi separati.
# For ottenere cio' ci are 3 cases different:
# Case 1) The nodo from eliminare NON HA FIGLI
#           - Si assegna value nullo al campo figlio dx/sx corrispondente del
#             nodo padre.
# Case 2) The nodo from eliminare HA 1 SOLO FIGLIO
#            - Si collega the padre del nodo with the suo unico figlio, 
#              indipendentemente that this sia destro o sinistro.
# Case 3) The nodo from eliminare HA 2 FIGLI
#            - Si sostituisce nel nodo from elimninare the key del suo 
#              successore/predecessore e si cancella quindi questultimo.


def cancellaFoglia(p,nodo):                                      # T(h)
    # Aggiorna the campo figlio (Dx/Sx) del padre 
    # corrispondente alla foglia from cancellare.
    if (nodo==nodo.getParent().getLeft()):                       # Θ(1)
        nodo.getParent().setLeft(None)                           # Θ(1)
    else:                                                        # Θ(1)
        nodo.getParent().setRight(None)                          # Θ(1)
    return                                                       # Θ(1)
    


def cancella(p,k):                                               # T(h)
    # Estrai nodo avente value key uguale to k
    nodo=ABR_searchRic(p, k)                                     # Ω(1) o O(h)
    # If the nodo not esiste chiudi the function
    if nodo==None:                                               # Θ(1)
        return                                                   # Θ(1)
    # CASO 1 - The Nodo NON HA FIGLI
    # Cancella the nodo aggiornando the corrispondente campo figlio
    # del nodo padre.
    if (nodo.getLeft()==None and nodo.getRight()==None):         # Θ(1)
       cancellaFoglia(p,nodo)                                    # Θ(1)
       
    # CASO 2 - The Nodo HA 1 FIGLIO
    # Cortocircuita the padre with the figlio del nodo from eliminare
    # If l'unico figlio e' that Sx...
    if (nodo.getLeft()!=None and nodo.getRight()==None):         # Θ(1)
        # Assegna the padre del nodo al figlio Sx
        nodo.getLeft().setParent(nodo.getParent())               # Θ(1)
        # Assegna the figlio Sx al padre del nodo
        if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
            nodo.getParent().setLeft(nodo.getLeft())             # Θ(1)
        else:                                                    # Θ(1)
            nodo.getParent().setRight(nodo.getLeft())            # Θ(1)
    # If l'unico figlio e' that Dx...
    if (nodo.getLeft()==None and nodo.getRight()!=None):         # Θ(1)
        # Assegna the padre del nodo al figlio Dx
        nodo.getRight().setParent(nodo.getParent())              # Θ(1)
        # Assegna the figlio Dx al padre del nodo
        if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
            nodo.getParent().setLeft(nodo.getRight())            # Θ(1)
        else:                                                    # Θ(1)
            nodo.getParent().setRight(nodo.getRight())           # Θ(1)
    
    # CASO 3 - The Nodo HA 2 FIGLI
    # Trova the predecessore/successore del nodo from cancellare, 
    # copia the suo contained in the nodo from cancellare e, infine, 
    # cancella the nodo predecessore/successore.
    if (nodo.getLeft()!=None and nodo.getRight()!=None):         # Θ(1)
        # Ricava the nodi predecessore e successore
        pred=predecessoreIter(p,nodo.getKey())                   # Ω(1) o O(h) 
        succes=successoreRecurs(p,nodo.getKey())                 # Ω(1) o O(h) 
        # Sostituisci key del nodo e cancella 
        # predecessore/successore
        if pred!=None:                                           # Θ(1)
            nodo.setKey(pred.getKey())                           # Θ(1)
            cancellaFoglia(p,pred)                               # Θ(1)
        else:                                                    # Θ(1)
            nodo.setKey(succes.getKey())                         # Θ(1)
            cancellaFoglia(p,succes)                             # Θ(1)

# Computational Cost
# Input size: altezza dell'albero h
# Iterative cost: T_case1(h)=O(h)+Θ(1)=O(h)
#                  T_case2(h)=O(h)+Θ(1)=O(h)
#                  T_case3(h)=O(h)+O(h)+Θ(1)=O(h)
# Cost: T(h)=max{T_case1;T_case2;T_case3}=O(h)


# TESTS

'Ricerca'
nodoRicercato=ABR_searchRic(albero.getRoot(),22)
print("RICERCA - The nodo ricercato e' : " + str(nodoRicercato))

'Inserimento'
z=Nodo(47)
print("\nINSERIMENTO\nAlbero first dell'inserimento del nodo " + str(z))
albero.visitaPreOrdine()
ABR_insert(albero.getRoot(), z)
print("\nAlbero dopo l'inserimento del nodo " + str(z))
albero.visitaPreOrdine()
print()

'Minimo'
minRec=minimoRecurs(albero.getRoot())
minIter=minimoIter(albero.getRoot())
print("\nMINIMO\nChiave minima nell'albero [RICORSIONE]: " + str(minRec))
print("Chiave minima nell'albero [ITERAZIONE]: " + str(minIter))

'Massimo'
maxRec=massimoRecurs(albero.getRoot())
maxIter=massimoIter(albero.getRoot())
print("\nMASSIMO\nChiave massima nell'albero [RICORSIONE]: " + str(maxRec))
print("Chiave massima nell'albero [ITERAZIONE]: " + str(maxIter))

'Predecessore'
k1=80
k2=13
predIter1=predecessoreIter(albero.getRoot(),k1)  # iterative -Case 1- Discesa
predIter2=predecessoreIter(albero.getRoot(),k2)  # iterative -Case 2- Risalita
predRec1=predecessoreRecurs(albero.getRoot(),k1) # recursive -Case 1- Discesa
predRec2=predecessoreRecurs(albero.getRoot(),k2) # recursive -Case 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))

'Successore'
k1=11
k2=16
succIter1=successoreIter(albero.getRoot(),k1)  # iterative -Case 1- Discesa
succIter2=successoreIter(albero.getRoot(),k2)  # iterative -Case 2- Risalita
succRec1=successoreRecurs(albero.getRoot(),k1) # recursive -Case 1- Discesa
succRec2=successoreRecurs(albero.getRoot(),k2) # recursive -Case 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))


'Cancellazione'
k_case1=7
k_case3=33
print("\nDELETION - Case 1 - key " + str(k_case1) + "\nBefore...")
albero.visitaPerLivelli()
print("\nAfter...")
cancella(albero.getRoot(), k_case1)
albero.visitaPerLivelli()
print("\n\nDELETION - Case 3 - key " + str(k_case3) + "\nBefore...")
albero.visitaPerLivelli()
print("\nAfter...")
cancella(albero.getRoot(),k_case3)
albero.visitaPerLivelli()

