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
from SingleRecord import RecordSingolo


# OPERAZIONI SU LISTE

'''
LISTE SEMPLICI 
- Search - Cost: O(n)
- Inserimento (in testa) - Cost: Θ(1)
- Inserimento (in mezzo) - Cost: Θ(1)
- Eliminazione - Cost: O(n)
'''


'Creazione list with istanze of the user-defined class Record.py'

keys=[1,32,54,2,5,3,7,6,4,11,23,26]
pointers=[118612,198612,210618,211668,225432,238112,
 289093,300132,313220,345100,366332,399320]
listA=list()

for k in range(0,len(keys)-1,1):
 listA.append(RecordSingolo(keys[k],pointers[k+1],pointers[k]))
listA.append(RecordSingolo(keys[k+1],None,pointers[k+1])) 
 
'Creazione Record aggiuntivo'

addRecord=RecordSingolo(15,None,544312)


'Search'

def search(p,k): # T(n)
 p_corr=p # Θ(1)
 p_corr_key=listA[0].getKey() # Θ(1)
 the=0 # Θ(1)
 while p_corr!=None and p_corr_key!=k: # n*Θ(1)+Θ(1)
 p_corr=listA[the].getPointer() # Θ(1)
 p_corr_key=listA[the].getKey() # Θ(1)
 the+=1 # Θ(1)
 return p_corr # Θ(1)

# Computational Cost: 
# Worst case - T(n)=Θ(1)+n*Θ(1)+Θ(1)=O(n) -the key not c'e' 
# Best case - T(n)=Θ(1)+1*Θ(1)+Θ(1)=O(1) -the key is in first position

pSearch=search(118612,3)



'Inserimento - In Testa'

def insertHead(p,k): # T(n)
 if k!=None: # Θ(1)
 k.setNext(p) # Θ(1)
 p=k.getPointer() # Θ(1)
 return p # Θ(1)

# Computational Cost: 
# T(n)=Θ(1) (for best case and for worst case)

pInsertHead=insertHead(118612,addRecord)


'Inserimento - In Mezzo'

def insertInside(p,k,d): # T(n)
 if d!=None: # Θ(1)
 k.setNext(d.getNext()) # Θ(1)
 d.setNext(k.getPointer()) # Θ(1)
 return p # Θ(1)
 else: # Θ(1)
 return None # Θ(1)

# Computational Cost: 
# T(n)=Θ(1) (for best case and for worst case)

pInsertInside=insertInside(544312,listA[5],addRecord)


'Eliminazione'

def delete (p,k): # T(n)
 if k!=None: # Θ(1)
 if k==p: # Θ(1)
 p=listA[0].getNext() # Θ(1)
 listA[0].delete() # Θ(1)
 return p # Θ(1)
 p_corr=p # Θ(1)
 the=0 # Θ(1)
 while listA[the].getNext()!=k: # n*Θ(1)+Θ(1)
 p_corr=listA[the].getNext() # Θ(1)
 the+=1 # Θ(1)
 listA[the-1].setNext(listA[the+1].getPointer()) # Θ(1)
 listA[the].delete() # Θ(1)
 return p # Θ(1)

# Computational Cost: 
# T(n)=O(n) - Worst case (element from eliminare not esiste)
# T(n)=Ω(1) - Best case (element from eliminare is the first of the list)

pDelete=delete(544312,366332)


