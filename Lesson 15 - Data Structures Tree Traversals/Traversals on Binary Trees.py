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


# IMPORT CLASSI DEL PACKAGE
from BinaryNode import Nodo
from BinaryTree import AlberoBinario
from Coda_Modificata import Coda

'''
PREPARAZIONE ALBERO
'''

'COSTRUZIONE ARRAY DI RECORDS DOPPI'
valoriNodi=[3,1,5,8,4,3,2,8,0,8,5]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,(len(nodi)-2)//2+1,1):
        nodi[i].setFiglioSx(nodi[2*i+1])
        nodi[i].setFiglioDx(nodi[2*i+2])
        
'COSTRUZIONE ALBERO BINARIO'     
radice=nodi[0]
albero=AlberoBinario(radice)



'''
VISITE *********************************************************************
'''

'VISITA in PREORDINE'
# Ciascun nodo viene visitato prima di visitare i suoi sottoalberi destro e 
# sinistro.

def visitaPreordine(p):                    # T(n)
    if p!=None:                            # Θ(1)
        'OPERAZIONE SUL NODO'
        print(str(p.getValore()),end=" ")  # Θ(1)
        'PASSO RICORSIVO 1 (SX)'
        visitaPreordine(p.getFiglioSx())   # T(k)
        'PASSO RICORSIVO 2 (DX)'
        visitaPreordine(p.getFiglioDx())   # T(n-k-1)
    'CASO BASE'
    return                                 # Θ(1)

# Costo Computazionale
# Dimensioni input: numero nodi dell'albero (incognito a priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2]
print("VISITA in PREORDINE")
visitaPreordine(albero.getRoot())


'VISITA in INORDINE'
# Ciascun nodo viene visitato dopo aver visitato il suo sottoalbero sinistro
# ma prima di visitare il suo sottoalbero destro.

def visitaInordine(p):                      # T(n)
    if p!=None:                             # Θ(1)
        'PASSI RICORSIVO 1 (SX)'
        visitaInordine(p.getFiglioSx())    # T(k)
        'OPERAZIONE SUL NODO'
        print(str(p.getValore()),end=" ")   # Θ(1)
        'PASSI RICORSIVO 2 (DX)'
        visitaInordine(p.getFiglioDx())    # T(n-k-1)
    'CASO BASE'
    return                                  # Θ(1)

# Costo Computazionale
# Dimensioni input: numero nodi dell'albero (incognito a priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [8,8,0,1,8,4,5,3,3,5,2]
print()
print("VISITA in INORDINE")
visitaInordine(albero.getRoot())


'VISITA in POSTORDINE'
# Ciascun nodo viene visitato solo dopo aver visitato entrambi i suoi sotto
# alberi destro e sinistro

def visitaPostordine(p):                    # T(n)
    if p!=None:                             # Θ(1)
        'PASSI RICORSIVO 1 (SX)'
        visitaPostordine(p.getFiglioSx())   # T(k)
        'PASSI RICORSIVO 2 (DX)'
        visitaPostordine(p.getFiglioDx())   # T(n-k-1)
        'OPERAZIONE SUL NODO'
        print(str(p.getValore()),end=" ")   # Θ(1)
    'CASO BASE'
    return                                  # Θ(1)

# Costo Computazionale
# Dimensioni input: numero nodi dell'albero (incognito a priori)
# Cost: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n) [METODO DI SOSTITUZIONE]

'Test'
# Risultato atteso: [8,0,8,8,5,4,1,3,2,5,3]
print()
print("VISITA in POSTORDINE")
visitaPostordine(albero.getRoot())


'VISITA per LIVELLI'
# Per visitare un albero per livelli, l'approccio ricorsivo non puo' funzionare
# La soluzione e' usare un approccio iterativo che faccia uso di una coda di 
# appoggio per scorrere tutti i nodi un livello dopo l'altro.
# IMPORTANTE!
# 1.Volendo salvare tutti i nodi in un array mano a mano che li si visitano, 
#   otteniamo esattamente il VETTORE POSIZIONALE dell'albero A MENO DEGLI SPAZI
#   VUOTI per i nodi mancanti.
# 2.La Coda, per poter funzionare, deve essere implementata in modo diverso 
#   dal metodo classico. Ciascuno dei Record Singoli da cui e' costituita, 
#   dovra' contenere come VALORE il riferimento al nodo corrispondente dell'
#   albero e come PUNTATORE il riferimento al Record Singolo successivo della
#   Coda (che conterra', come VALORE, il riferimento al nodo successivo dell'
#   albero binario).
# >>>> VEDI CODICE PYTHON "Coda_Modificata.py" <<<<<


'Funzione Ausiliaria Controllo Riempimento Coda'
def codaVuota(coda):
    if coda.size()==0:
        return True
    return False

'FUNZIONE ITERATIVA per Visita per Livelli'
def visitaPerLivelli(p):                       # T(n)
    # Controllo esistenza albero in input
    if p==None:                                # Θ(1)
        return                                 # Θ(1)
    # Inizializzazione coda di supporto
    coda=Coda()                                # Θ(1)                                                     
    # Incodamento radice albero nella coda
    coda.enqueue(p)                            # Θ(1)                           
    # Scorrimento nodi albero tramite coda
    while(not codaVuota(coda)):                # n*Θ(1)+Θ(1) 
        # 1. Scoda e stampa nodo
        p=coda.dequeue()                       # Θ(1)
        print(str(p),end=" ")                  # Θ(1)         
        # Incoda figlioSx
        if p.getFiglioSx()!=None:              # Θ(1)
            coda.enqueue(p.getFiglioSx())      # Θ(1)
        # Incoda figlio Dx
        if p.getFiglioDx()!=None:              # Θ(1)
            coda.enqueue(p.getFiglioDx())      # Θ(1)
    return                                     # Θ(1)
    

# Costo Computazionale
# Dimensioni input: numero nodi dell'albero (incognito a priori)
# Cost: T(n)=Θ(1)+Θ(n)+Θ(1)  -> T(n)=Θ(n) 

'Test'
# Risultato atteso: [3,1,5,8,4,3,2,8,0,8,5]
print("VISITA per LIVELLI")
visitaPerLivelli(albero.getRoot())
