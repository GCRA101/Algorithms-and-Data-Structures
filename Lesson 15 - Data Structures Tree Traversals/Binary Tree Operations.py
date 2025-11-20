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
from BinaryNode import Nodo
from BinaryTree import AlberoBinario


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
radice=nodi[0]
albero=AlberoBinario(radice)



'''
OPERAZIONI ******************************************************************
'''

'CONTEGGIO DEL number DEI NODI'
def calcola_n(p):
    if p!=None:
        num_l=calcola_n(p.getFiglioSx()) # Recursive Step 1 (SottoAlbero Sx)
        num_r=calcola_n(p.getFiglioDx()) # Recursive Step 2 (SottoAlbero Dx)
        num=num_l+num_r+1                # Operazione sul Nodo
        return num
    return 0


'RICERCA IN UN ALBERO'
def cerca(p,k):
    if p!=None:
      if p.getValore()==k:                 # Operazione sul Nodo
          return True
      elif cerca(p.getFiglioSx(),k)==True: # Recursive Step 1 (SottoAlbero Sx)
          return True
      else:
          return cerca(p.getFiglioDx(),k)  # Recursive Step 2 (SottoAlbero Dx)
    return False


'CALCOLO ALTEZZA DELL ALBERO'
def calcola_h(p):
    if p==None:
        return -1
    if p.getFiglioSx()==None and p.getFiglioDx()==None:
        return 0
    h=max(calcola_h(p.getFiglioSx()),      # Recursive Step 1 (SottoAlbero Sx)
          calcola_h(p.getFiglioDx()))      # Recursive Step 2 (SottoAlbero Dx)
    return h+1                             # Operazione sul Nodo


'CONTEGGIO NODI AL LIVELLO K'
def conta_k(p,k,the):
    if p==None:
        return 0
    if k==the:
        return 1
    k_left=conta_k(p.getFiglioSx(),k,the+1)  # Recursive Step 1 (SottoAlbero Sx)
    k_right=conta_k(p.getFiglioDx(),k,the+1) # Recursive Step 2 (SottoAlbero Dx)
    return k_left+k_right                  # Operazione sul Nodo
        


'Test'
numNodi=calcola_n(albero.getRoot())
cercaNodo=cerca(albero.getRoot(), 8)
altezza=calcola_h(albero.getRoot())

