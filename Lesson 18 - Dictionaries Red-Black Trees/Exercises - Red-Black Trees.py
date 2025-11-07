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
Scrivere lo pseudocodice di una funzione che ordina un vettore A:
    - inserendo i suoi elementi in un ABR
    - ricopiando su A gli elementi incontrati eseguendo la visita inorder
      sull'ABR
Valutarne il costo computazionale. Se l'ABR fosse un Albero RossoNero, 
cambierebbe qualcosa? se si, cosa?
'''


'INSERIMENTO'

# Dato l'albero p e dato il nodo z in input, la funzione ritorna l'albero con
# il nodo aggiuntivo inserito nella posizione appropriata.

def ABR_insert(albero,z):                         # T(h)
    'ESTRAZIONE RADICE ALBERO'
    p=albero.getRoot()
    '1. INIZIALIZZAZIONE Puntatori ausiliari'
    # Padre Nodo Corrente
    y=None                                       # Θ(1)
    # Nodo corrente
    x=p                                          # Θ(1)
    '2. DISCESA fino a Nodo con Figlio Nullo'
    while x!=None:                               # h*Θ(1)+Θ(1)
        # Aggiorna y eguagliandolo a x...
        y=x                                      # Θ(1)
        # Aggiorna x facendolo scendere a dx/sx in base alla sua chiave...
        if z.getKey()<x.getKey():                # Θ(1)
            x=x.getLeft()                        # Θ(1)
        else:                                    # Θ(1)
            x=x.getRight()                       # Θ(1)
    '3. AGGIUNTA Nuovo Nodo'
    # Se l'Albero e' Nullo, usa Nuovo Nodo come Radice dell'Albero...
    if y==None:                                  # Θ(1)
        albero.root=z                            # Θ(1)
        p=albero.root                            # Θ(1)
    # Se l'Albero non e' nullo, aggiungi il Nuovo Nodo a dx/sx dell'ultimo...
    else:                                        # Θ(1)
        if z.getKey()<y.getKey():                # Θ(1)
            y.left=z                             # Θ(1)
        else:                                    # Θ(1)
            y.right=z                            # Θ(1)
    # Aggiorna il campo Padre del nuovo nodo aggiunto all'albero...
    z.setParent(y)                               # Θ(1)
    # Restituisci l'albero modificato...
    return p                                     # Θ(1)

# Computational Cost
# Dimensione dell'input: Altezza h dell'albero
# Costo: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)


'VISITA IN INORDINE'

# Dato l'albero e l'array in input, la funzione effettua una visita inordine
# dell'albero e ne ricopia le chiavi dei nodi all'interno dell'array uno ad
# uno.

# Funzione Ricorsiva 
def visitaInOrdine(p,array=[],i=-1):             # T(n)
    if p!=None:                                  # Θ(1)
        i+=1                                     # Θ(1)
        'PASSI RICORSIVO 1 (SX)'
        visitaInOrdine(p.getLeft(),array)        # T(k)
        'OPERAZIONE SUL NODO'      
        array.append(p.getKey())                 # Θ(1)     
        'PASSI RICORSIVO 2 (DX)'
        visitaInOrdine(p.getRight(),array)       # T(n-k-1)
    'CASO BASE'
    return array                                 # Θ(1)

# Computational Cost
# Dimensioni input: numero nodi dell'albero (incognito a priori)
# CoTto: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]


'ESERCIZIO'

# Array delle Chiavi
arrayChiavi=[18,11,33,7,15,22,80,13,16,50,91,42,64]    # Θ(1)
# Albero Binario di Ricerca
albero=AlberoBinarioDiRicerca()                        # Θ(1)
    
# Inserimento chiavi array in Albero di Ricerca Binaria
for i in range(0,len(arrayChiavi),1):                  # n*Θ(1)+Θ(1)
    z=Nodo(arrayChiavi[i])                             # Θ(1)
    ABR_insert(albero, z)                              # R(n)
# Riordinamento chiavi nell'array tramite Visita In Ordine
# dell'albero di ricerca binaria
arrayChiavi=visitaInOrdine(albero.getRoot())           # S(n)


# Computational Cost
# Dimensioni input: numero elementi/chiavi all'interno dell'array
# Costo: T(n)=sommatoria_1_n(Θ(logi))+S(n)
#        T(n)=Θ(log(n*(n+1)/2))+Θ(n)=Θ(log(n^2))+Θ(log(n))+Θ(n)
#            =Θ(log(n))+Θ(n)=Θ(n)


