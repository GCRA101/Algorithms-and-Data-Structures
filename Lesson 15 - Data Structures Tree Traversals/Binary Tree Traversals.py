# -*- coding: utf-8 -*-
"""
Created on Thu Jun 1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import math as math
import time
import matplotlib.pyplot as plt
import random


# IMPORT PACKAGE CLASSES
from BinaryNode import Nodo
from BinaryTree import AlberoBinario
from Modified_Queue import Queue

'''
PREPARAZIONE ALBERO
'''

'COSTRUZIONE ARRAY DI RECORDS DOPPI'
valoriNodi=[3,1,5,8,4,3,2,8,0,8,5]
nodi=[]
vettorePosizionale=[]

for the in range(0,len(valoriNodi),1):
 nodi.append(Nodo(valoriNodi[the])) 
 
for the in range(0,(len(nodi)-2)//2+1,1):
 nodi[the].setFiglioSx(nodi[2*the+1])
 nodi[the].setFiglioDx(nodi[2*the+2])
 
'COSTRUZIONE ALBERO BINARIO' 
root=nodi[0]
tree=AlberoBinario(root)



'''
VISITE *********************************************************************
'''

'VISITA in PREORDINE'
# Ciascun nodo viene visitato first of visitare the suoi sottoalberi destro and 
# sinistro.

def visitaPreordine(p): # T(n)
 if p!=None: # Θ(1)
 'OPERAZIONE SUL NODO'
 print(str(p.getValore()),end=" ") # Θ(1)
 'PASSO RICORSIVO 1 (SX)'
 visitaPreordine(p.getFiglioSx()) # T(k)
 'PASSO RICORSIVO 2 (DX)'
 visitaPreordine(p.getFiglioDx()) # T(n-k-1)
 'CASO BASE'
 return # Θ(1)

# Computational Cost
# Dimensions input: number nodi dell'tree (incognito to priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1) -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2]
print("VISITA in PREORDINE")
visitaPreordine(tree.getRoot())


'VISITA in INORDINE'
# Ciascun nodo viene visitato after aver visitato the suo sottoalbero sinistro
# ma first of visitare the suo sottoalbero destro.

def visitaInordine(p): # T(n)
 if p!=None: # Θ(1)
 'PASSI RICORSIVO 1 (SX)'
 visitaInordine(p.getFiglioSx()) # T(k)
 'OPERAZIONE SUL NODO'
 print(str(p.getValore()),end=" ") # Θ(1)
 'PASSI RICORSIVO 2 (DX)'
 visitaInordine(p.getFiglioDx()) # T(n-k-1)
 'CASO BASE'
 return # Θ(1)

# Computational Cost
# Dimensions input: number nodi dell'tree (incognito to priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1) -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [8,8,0,1,8,4,5,3,3,5,2]
print()
print("VISITA in INORDINE")
visitaInordine(tree.getRoot())


'VISITA in POSTORDINE'
# Ciascun nodo viene visitato only after aver visitato both the suoi sotto
# alberi destro and sinistro

def visitaPostordine(p): # T(n)
 if p!=None: # Θ(1)
 'PASSI RICORSIVO 1 (SX)'
 visitaPostordine(p.getFiglioSx()) # T(k)
 'PASSI RICORSIVO 2 (DX)'
 visitaPostordine(p.getFiglioDx()) # T(n-k-1)
 'OPERAZIONE SUL NODO'
 print(str(p.getValore()),end=" ") # Θ(1)
 'CASO BASE'
 return # Θ(1)

# Computational Cost
# Dimensions input: number nodi dell'tree (incognito to priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1) -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [8,0,8,8,5,4,1,3,2,5,3]
print()
print("VISITA in POSTORDINE")
visitaPostordine(tree.getRoot())


'VISITA for LIVELLI'
# For visitare a tree for livelli, l'approccio recursive method not puo' funzionare
# The soluzione is usare a approccio iterativo that faccia uso of a queue of 
# appoggio for scorrere all the nodi a level after l'other.
# IMPORTANTE!
# 1.Volendo salvare all the nodi in a array mano to mano that li si visitano, 
# otteniamo esattamente the VETTORE POSIZIONALE dell'tree To MENO DEGLI SPAZI
# VUOTI for the nodi mancanti.
# 2.The Queue, for poter funzionare, deve essere implementata in a way diverso 
# dal metodo classico. Ciascuno dei Record Singoli from which is costituita, 
# dovra' contenere as value the riferimento al nodo corrispondente dell'
# tree and as PUNTATORE the riferimento al Record Singolo successivo of the
# Queue (that conterra', as value, the riferimento al nodo successivo dell'
# tree binario).
# >>>> VEDI CODICE PYTHON "Coda_Modificata.py" <<<<<


'function Ausiliaria Controllo Riempimento Queue'
def codaVuota(queue):
 if queue.size()==0:
 return True
 return False

'function iterative for Visita for Livelli'
def visitaPerLivelli(p): # T(n)
 # Controllo esistenza tree in input
 if p==None: # Θ(1)
 return # Θ(1)
 # Inizializzazione queue of supporto
 queue=Queue() # Θ(1) 
 # Incodamento root tree in the queue
 queue.enqueue(p) # Θ(1) 
 # Scorrimento nodi tree through queue
 while(not codaVuota(queue)): # n*Θ(1)+Θ(1) 
 # 1. Scoda and prints nodo
 p=queue.dequeue() # Θ(1)
 print(str(p),end=" ") # Θ(1) 
 # Incoda figlioSx
 if p.getFiglioSx()!=None: # Θ(1)
 queue.enqueue(p.getFiglioSx()) # Θ(1)
 # Incoda figlio Dx
 if p.getFiglioDx()!=None: # Θ(1)
 queue.enqueue(p.getFiglioDx()) # Θ(1)
 return # Θ(1)
 

# Computational Cost
# Dimensions input: number nodi dell'tree (incognito to priori)
# Cost: T(n)=Θ(1)+Θ(n)+Θ(1) -> T(n)=Θ(n) 

'Test'
# Risultato atteso: [3,1,5,8,4,3,2,8,0,8,5]
print("VISITA for LIVELLI")
visitaPerLivelli(tree.getRoot())
