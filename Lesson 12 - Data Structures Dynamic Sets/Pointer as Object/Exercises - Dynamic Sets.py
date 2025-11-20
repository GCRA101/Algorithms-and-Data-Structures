

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

from SinglyLinkedList import ListaPuntataSingola
from DoublyLinkedList import ListaPuntataDoppia
from SingleRecord import RecordSingolo
from DoubleRecord import RecordDoppio



'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Given in input a list through the pointer al first element, restituire the 
pointer all'last element.
'''




# ESERCIZIO 2 ################################################################

'''
Given in input a list through the pointer al first element, restituire the 
pointer al penultimo element.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 3 ################################################################

'''
Given in input a list through the pointer al first element, restituire the 
pointer to the same list from which the last element has been removed.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 4 ################################################################

'''
Given in input a list through the pointer al first element, restituire the 
pointer of a list that contenga the stessi record of the list of partenza
ma in ordine inverso (N.B. not deve essere creato alcun record, ma bisogna 
smontare and rimontare opportunamente the record iniziali)
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 5 ################################################################

'''
Given in input a list through the pointer al first element, restituire the 
puntatori to two lists, a with the elements of posto pari in the list of 
partenza, ed a with the elements of posto dispari (also qui, not bisogna 
creare nuovi record)
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 6 ################################################################

'''
Given in input a list of interi through the pointer al first element, 
print all the values that compaiono almeno two times in the list.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 7 ################################################################

'''
Given in input a list sorted of interi through the pointer al first 
element, ed a element from inserire, add tale element to the list in
way from rispettare l'sorting.
'''

' VEDI RISOLUZIONE SU CARTA '


# ESERCIZIO 8 ################################################################

'''
Given in input a list of interi through the pointer al first element, 
restituire the list ordinata (senza creare nuovi record).
'''


'CREAZIONE LISTA PUNTATA DOPPIA'

# Creazione dei Records
keys=[1,32,54,2,5,3,7,6,4,11,23,26]
records=[]
# Concatenamento dei Records
for the in range(0,len(keys),1):
 records.append(RecordDoppio(keys[the]))
for the in range(0,len(records),1):
 if the>0:
 records[the].setPrev(records[the-1])
 if the<len(records)-1:
 records[the].setNext(records[the+1])
 
# Creazione list puntata (contiene the riferimento al record of testa)
listaPuntataDopp=ListaPuntataDoppia(records[0])


def ordinaListaDoppia(list):
 
 'Inizializzazione Records of supporto'
 p_corr,p_prev=RecordDoppio(),RecordDoppio()
 p_next,p_forward=RecordDoppio(),RecordDoppio()
 'Salva second record of the list in p_corr'
 p_corr=list.getPrimoRecord().getNext()
 'Salva first record of the list in p_prev'
 p_prev=list.getPrimoRecord()
 
 'Fino to that not si raggiunge the fine of the list...'
 while p_corr!=None:
 'If p_corr punta to a record, stora quel record in p_forward'
 if p_corr.getNext()!=None:
 p_forward=p_corr.getNext()
 else: 
 p_forward=None
 
 'Fino to that not si raggiunge l''inizio of the list...'
 while p_corr.getPrev()!=None:
 'Aggiorna the record precedente p_corr'
 p_prev=p_corr.getPrev()
 '''If the key of p_corr is minore of that of p_prev...scambia 
 'the two record of position...'''
 if p_corr.getData()<p_prev.getData():
 'Memorizza the record successivo in p_next, if esso esiste...'
 if p_corr.getNext()!=None:
 p_next=p_corr.getNext()
 else: 
 p_next=None 
 'Aggiorna the record precedente p_corr'
 p_prev=p_corr.getPrev()
 'Scambia the puntatori dei records p_next and (p_prev->prev)'
 if (p_prev.getPrev()!=None):
 p_prev.getPrev().setNext(p_corr)
 if (p_next!=None):
 p_next.setPrev(p_prev)
 
 'Memorizza campi next and prev of p_corr and p_prev '
 'in variables supporto.'
 p1=p_prev.getPrev()
 p2=p_prev.getNext()
 p3=p_corr.getPrev()
 p4=p_corr.getNext()
 
 'Scambio campi next and prev of p_corr and p_prev'
 p_corr.setPrev(p1)
 p_corr.setNext(p3)
 p_prev.setPrev(p2)
 p_prev.setNext(p4)
 else:
 break
 'Aggiorna p_corr spostandolo of a position in avanti in the list.'
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

