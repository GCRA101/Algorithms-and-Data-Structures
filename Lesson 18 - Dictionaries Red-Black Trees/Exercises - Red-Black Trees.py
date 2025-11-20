# -*- coding: utf-8 -*-
"""
Created on Fri Jun 2 22:10:30 2023

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
 - inserendo the suoi elements in a ABR
 - ricopiando on To the elements incontrati eseguendo the visita inorder
 sull'ABR
Valutarne the computational cost. If l'ABR were a Tree RossoNero, 
cambierebbe qualcosa? if si, cosa?
'''


'INSERIMENTO'

# Given l'tree p and given the nodo z in input, the function returns l'tree with
# the nodo aggiuntivo inserito in the position appropriata.

def ABR_insert(tree,z): # T(h)
 'ESTRAZIONE RADICE ALBERO'
 p=tree.getRoot()
 '1. INIZIALIZZAZIONE Puntatori ausiliari'
 # Padre Nodo Corrente
 y=None # Θ(1)
 # Nodo corrente
 x=p # Θ(1)
 '2. DISCESA fino to Nodo with Figlio Nullo'
 while x!=None: # h*Θ(1)+Θ(1)
 # Aggiorna y eguagliandolo to x...
 y=x # Θ(1)
 # Aggiorna x facendolo scendere to dx/sx in base to the sua key...
 if z.getKey()<x.getKey(): # Θ(1)
 x=x.getLeft() # Θ(1)
 else: # Θ(1)
 x=x.getRight() # Θ(1)
 '3. AGGIUNTA Nuovo Nodo'
 # If l'Tree is Nullo, usa Nuovo Nodo as Radice dell'Tree...
 if y==None: # Θ(1)
 tree.root=z # Θ(1)
 p=tree.root # Θ(1)
 # If l'Tree not is nullo, aggiungi the Nuovo Nodo to dx/sx dell'last...
 else: # Θ(1)
 if z.getKey()<y.getKey(): # Θ(1)
 y.left=z # Θ(1)
 else: # Θ(1)
 y.right=z # Θ(1)
 # Aggiorna the campo Padre del nuovo nodo aggiunto all'tree...
 z.setParent(y) # Θ(1)
 # Restituisci l'tree modificato...
 return p # Θ(1)

# Computational Cost
# Dimension dell'input: Altezza h dell'tree
# Cost: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'VISITA IN INORDINE'

# Given l'tree and l'array in input, the function effettua a visita inordine
# dell'tree and ne ricopia the keys dei nodi inside the array one ad
# one.

# function recursive 
def visitaInOrdine(p,array=[],the=-1): # T(n)
 if p!=None: # Θ(1)
 the+=1 # Θ(1)
 'PASSI RICORSIVO 1 (SX)'
 visitaInOrdine(p.getLeft(),array) # T(k)
 'OPERAZIONE SUL NODO' 
 array.append(p.getKey()) # Θ(1) 
 'PASSI RICORSIVO 2 (DX)'
 visitaInOrdine(p.getRight(),array) # T(n-k-1)
 'CASO BASE'
 return array # Θ(1)

# Computational Cost
# Dimensions input: number nodi dell'tree (incognito to priori)
# CoTto: T(n)=T(k)+T(n-k-1)+Θ(1) -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]


'ESERCIZIO'

# Array of the Keys
arrayChiavi=[18,11,33,7,15,22,80,13,16,50,91,42,64] # Θ(1)
# Binary Search Tree
tree=AlberoBinarioDiRicerca() # Θ(1)
 
# Insertion of array keys in Binary Search Tree
for the in range(0,len(arrayChiavi),1): # n*Θ(1)+Θ(1)
 z=Nodo(arrayChiavi[the]) # Θ(1)
 ABR_insert(tree, z) # R(n)
# Reordering keys in the array through In-Order Traversal
# of the binary search tree
arrayChiavi=visitaInOrdine(tree.getRoot()) # S(n)


# Computational Cost
# Dimensions input: number elements/keys inside the array
# Cost: T(n)=sommatoria_1_n(Θ(logi))+S(n)
# T(n)=Θ(log(n*(n+1)/2))+Θ(n)=Θ(log(n^2))+Θ(log(n))+Θ(n)
# =Θ(log(n))+Θ(n)=Θ(n)


