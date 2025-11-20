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



# ESERCIZIO 1 ################################################################

'''
Scrivere the pseudocodice of a function that ordina a vector To:
    - inserendo the suoi elementi in a ABR
    - ricopiando on To the elementi incontrati eseguendo the visita inorder
      sull'ABR
Valutarne the costo computazionale. If l'ABR fosse a Albero RossoNero, 
cambierebbe qualcosa? if si, cosa?
'''


'INSERIMENTO'

# Given l'albero p e given the nodo z in input, the function returns l'albero with
# the nodo aggiuntivo inserito nella posizione appropriata.

def ABR_insert(albero,z):                         # T(h)
    'ESTRAZIONE RADICE ALBERO'
    p=albero.getRoot()
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
        albero.root=z                            # Θ(1)
        p=albero.root                            # Θ(1)
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


'VISITA IN INORDINE'

# Given l'albero e l'array in input, the function effettua a visita inordine
# dell'albero e ne ricopia the chiavi dei nodi all'interno dell'array one ad
# one.

# function recursive 
def visitaInOrdine(p,array=[],the=-1):             # T(n)
    if p!=None:                                  # Θ(1)
        the+=1                                     # Θ(1)
        'PASSI RICORSIVO 1 (SX)'
        visitaInOrdine(p.getLeft(),array)        # T(k)
        'OPERAZIONE SUL NODO'      
        array.append(p.getKey())                 # Θ(1)     
        'PASSI RICORSIVO 2 (DX)'
        visitaInOrdine(p.getRight(),array)       # T(n-k-1)
    'CASO BASE'
    return array                                 # Θ(1)

# Computational Cost
# Dimensioni input: number nodi dell'albero (incognito to priori)
# CoTto: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]


'ESERCIZIO'

# Array delle Chiavi
arrayChiavi=[18,11,33,7,15,22,80,13,16,50,91,42,64]    # Θ(1)
# Binary Search Tree
albero=AlberoBinarioDiRicerca()                        # Θ(1)
    
# Inserimento chiavi array in Albero of Ricerca Binaria
for the in range(0,len(arrayChiavi),1):                  # n*Θ(1)+Θ(1)
    z=Nodo(arrayChiavi[the])                             # Θ(1)
    ABR_insert(albero, z)                              # R(n)
# Riordinamento chiavi in the array through Visita In Ordine
# dell'albero of ricerca binaria
arrayChiavi=visitaInOrdine(albero.getRoot())           # S(n)


# Computational Cost
# Dimensioni input: number elements/chiavi all'interno dell'array
# Cost: T(n)=sommatoria_1_n(Θ(logi))+S(n)
#        T(n)=Θ(log(n*(n+1)/2))+Θ(n)=Θ(log(n^2))+Θ(log(n))+Θ(n)
#            =Θ(log(n))+Θ(n)=Θ(n)


