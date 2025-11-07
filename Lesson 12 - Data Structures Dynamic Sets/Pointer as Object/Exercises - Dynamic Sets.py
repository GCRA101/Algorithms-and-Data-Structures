

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

from SinglyLinkedList import ListaPuntataSingola
from DoublyLinkedList import ListaPuntataDoppia
from SingleRecord import RecordSingolo
from DoubleRecord import RecordDoppio



'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Data in input una lista tramite il puntatore al primo elemento, restituire il 
puntatore all'ultimo elemento.
'''




# ESERCIZIO 2 ################################################################

'''
Data in input una lista tramite il puntatore al primo elemento, restituire il 
puntatore al penultimo elemento.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 3 ################################################################

'''
Data in input una lista tramite il puntatore al primo elemento, restituire il 
puntatore alla stessa lista da cui sia stato eliminato l'ultimo elemento.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 4 ################################################################

'''
Data in input una lista tramite il puntatore al primo elemento, restituire il 
puntatore di una lista che contenga gli stessi record della lista di partenza
ma in ordine inverso (N.B. non deve essere creato alcun record, ma bisogna 
smontare e rimontare opportunamente i record iniziali)
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 5 ################################################################

'''
Data in input una lista tramite il puntatore al primo elemento, restituire i 
puntatori a due liste, una con gli elementi di posto pari nella lista di 
partenza, ed una con gli elementi di posto dispari (anche qui, non bisogna 
creare nuovi record)
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 6 ################################################################

'''
Data in input una lista di interi tramite il puntatore al primo elemento, 
stampare tutti i valori che compaiono almeno due volte nella lista.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 7 ################################################################

'''
Data in input una lista ordinata di interi tramite il puntatore al primo 
elemento, ed un elemento da inserire, aggiungere tale elemento alla lista in
modo da rispettare l'ordinamento.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 8 ################################################################

'''
Data in input una lista di interi tramite il puntatore al primo elemento, 
restituire la lista ordinata (senza creare nuovi record).
'''


'CREAZIONE LISTA PUNTATA DOPPIA'

# Creazione dei Records
keys=[1,32,54,2,5,3,7,6,4,11,23,26]
records=[]
# Concatenamento dei Records
for i in range(0,len(keys),1):
    records.append(RecordDoppio(keys[i]))
for i in range(0,len(records),1):
    if i>0:
        records[i].setPrev(records[i-1])
    if i<len(records)-1:
        records[i].setNext(records[i+1])
    
# Creazione lista puntata (contiene il riferimento al record di testa)
listaPuntataDopp=ListaPuntataDoppia(records[0])


def ordinaListaDoppia(lista):
    
    'Inizializzazione Records di supporto'
    p_corr,p_prev=RecordDoppio(),RecordDoppio()
    p_next,p_forward=RecordDoppio(),RecordDoppio()
    'Salva secondo record della lista in p_corr'
    p_corr=lista.getPrimoRecord().getNext()
    'Salva primo record della lista in p_prev'
    p_prev=lista.getPrimoRecord()
    
    'Fino a che non si raggiunge la fine della lista...'
    while p_corr!=None:
        'Se p_corr punta a un record, memorizza quel record in p_forward'
        if p_corr.getNext()!=None:
            p_forward=p_corr.getNext()
        else: 
            p_forward=None
        
        'Fino a che non si raggiunge l''inizio della lista...'
        while p_corr.getPrev()!=None:
            'Aggiorna il record precedente p_corr'
            p_prev=p_corr.getPrev()
            '''Se la key di p_corr e' minore di quella di p_prev...scambia 
            'i due record di posizione...'''
            if p_corr.getData()<p_prev.getData():
               'Memorizza il record successivo in p_next, se esso esiste...'
               if p_corr.getNext()!=None:
                    p_next=p_corr.getNext()
               else: 
                    p_next=None    
               'Aggiorna il record precedente p_corr'
               p_prev=p_corr.getPrev()
               'Scambia i puntatori dei records p_next e (p_prev->prev)'
               if (p_prev.getPrev()!=None):
                    p_prev.getPrev().setNext(p_corr)
               if (p_next!=None):
                    p_next.setPrev(p_prev)
                    
               'Memorizza campi next e prev di p_corr e p_prev '
               'in variabili supporto.'
               p1=p_prev.getPrev()
               p2=p_prev.getNext()
               p3=p_corr.getPrev()
               p4=p_corr.getNext()
                
               'Scambio campi next e prev di p_corr e p_prev'
               p_corr.setPrev(p1)
               p_corr.setNext(p3)
               p_prev.setPrev(p2)
               p_prev.setNext(p4)
            else:
                break
        'Aggiorna p_corr spostandolo di una posizione in avanti nella lista.'
        p_corr=p_forward
        'Aggiorna p_prev.'
        if p_corr!=None:
            p_prev=p_corr.getPrev()

    
    
p=records[0]

print("\n\nLista DISORDINATA\n")
print(listaPuntataDopp)
    

ordinaListaDoppia(listaPuntataDopp)


print("\n\nLista ORDINATA\n")
print(listaPuntataDopp)

