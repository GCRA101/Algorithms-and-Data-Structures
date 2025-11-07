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
from SingleRecord import RecordSingolo

'''
CLASSE PILA (STACK)
Costruita servendosi della Struttura Dati di LISTA PUNTATA SINGOLA e modificata
nel suo funzionamento per essere usata per la VISITA IN PREORDINE ITERATIVA 
di un ALBERO BINARIO.
La Pila si serve di Record Singoli mentre l'albero binario di Record Doppi. 
Il segreto consiste nell'immagazzinare il riferimento a ciascun nodo dell'albero
nel campo Data e il riferimento al record singolo successivo nel campo Next.
La Pila e' quindi costituita da una successione di record singoli che si puntano
a vicenda in sequenza e in cui ciascuno di essi contiene il riferimento a 
ciascun nodo corrispondente dell'Albero Binario.
Quindi...
    - Campo DATA : Riferimento a Nodo Albero Binario
    - Campo NEXT : Riferimento a Record Singolo Successivo nella Pila
'''

class Pila:
    
    # ATTRIBUTES
    _top=None
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,_top=None):
        self._top=_top
        
    # METHODS
    
    'PUSH'
    def push(self,el):                          # T(n)
        nuovoRecord=RecordSingolo(el,None)      # Θ(1)
        nuovoRecord.setNext(self._top)          # Θ(1)
        self._top=nuovoRecord                   # Θ(1)
        return                                  # Θ(1)

    'POP'    
    def pop(self):                              # T(n)
        if self._top==None:                     # Θ(1)
            return None                         # Θ(1)
        else:                                   # Θ(1)
            el=self._top.getData()              # Θ(1)
            self._top=self._top.getNext()       # Θ(1)
        return el                               # Θ(1)
    
    'LENGTH'
    def length(self):                           # T(n)
        refRecord=self._top                     # Θ(1)
        i=0                                     # Θ(1)
        while refRecord!=None:                  # n*Θ(1)+Θ(1)
            i+=1                                # Θ(1)
            refRecord=refRecord.getNext()       # Θ(1)
        return i                                # Θ(1)
    
    'ToString'
    def __str__(self):
        p_corr=self._top
        output=""
        while p_corr!=None:
            if p_corr.getNext()!=None:
                output+="["+str(p_corr)+"]" + " - "
            else:
                output+="["+str(p_corr)+"]"
            p_corr=p_corr.getNext()
        return output
        
