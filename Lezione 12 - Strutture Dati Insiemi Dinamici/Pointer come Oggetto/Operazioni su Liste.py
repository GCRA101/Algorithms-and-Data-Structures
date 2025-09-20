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
from RecordSingolo import RecordSingolo
from RecordDoppio import RecordDoppio
from ListaPuntataSingola import ListaPuntataSingola
from ListaPuntataDoppia import ListaPuntataDoppia


# OPERAZIONI SU LISTE

'''
LISTE PUNTATE  
- Lettura                       - Costo: O(n)
- Ricerca                       - Costo: O(n)
- Inserimento (in testa)        - Costo: Θ(1)
- Inserimento (in mezzo)        - Costo: Θ(1)
- Eliminazione                  - Costo: O(n)
'''



# LISTE PUNTATE SINGOLE ######################################################


'CREAZIONE LISTA PUNTATA SINGOLA'

# Creazione dei Records
keys=[1,32,54,2,5,3,7,6,4,11,23,26]
records=[]
# Concatenamento dei Records
for i in range(0,len(keys),1):
    records.append(RecordSingolo(keys[i]))
for i in range(0,len(records)-1,1):
    records[i].setNext(records[i+1])
# Creazione lista puntata (contiene il riferimento al record di testa)
listaPuntataSing=ListaPuntataSingola(records[0])

# Creazione lista puntata (contiene il riferimento al record di testa)
listaPuntataSing=ListaPuntataSingola(records[0])

    
'Creazione Record aggiuntivo'

addRecord=RecordSingolo(15,None)


'LETTURA - Reading'

print(str(listaPuntataSing) + "\n")

data1=listaPuntataSing.read(0)
data2=listaPuntataSing.read(4)
data3=listaPuntataSing.read(1333)


'RICERCA - Search'

index1=listaPuntataSing.search(3)
index2=listaPuntataSing.search(26)
index3=listaPuntataSing.search(129321)


'INSERIMENTO - Insertion'

listaPuntataSing.insert(-2, 230)
listaPuntataSing.insert(5, 230)
listaPuntataSing.insert(1000, 230)

print(str(listaPuntataSing) + "\n")

'ELIMINAZIONE - Deletion'

listaPuntataSing.delete(-3)
listaPuntataSing.delete(0)
listaPuntataSing.delete(3)
listaPuntataSing.delete(1000)

print(str(listaPuntataSing) + "\n")






# LISTE PUNTATE DOPPIE ########################################################


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


'Creazione Record aggiuntivo'

addRecord=RecordDoppio(15,None,None)


'LETTURA - Reading'

print(str(listaPuntataDopp) + "\n")

data1=listaPuntataDopp.read(0)
data2=listaPuntataDopp.read(4)
data3=listaPuntataDopp.read(1333)


'RICERCA - Search'

index1=listaPuntataDopp.search(3)
index2=listaPuntataDopp.search(26)
index3=listaPuntataDopp.search(129321)


'INSERIMENTO - Insertion'

listaPuntataDopp.insert(-2, 230)
listaPuntataDopp.insert(5, 230)
listaPuntataDopp.insert(1000, 230)

print(str(listaPuntataDopp) + "\n")

'ELIMINAZIONE - Deletion'

listaPuntataDopp.delete(-3)
listaPuntataDopp.delete(0)
listaPuntataDopp.delete(3)
listaPuntataDopp.delete(1000)

print(str(listaPuntataDopp) + "\n")