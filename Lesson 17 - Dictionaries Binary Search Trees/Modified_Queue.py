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
from SingleRecord import RecordSingolo

'''
CLASSE CODA (QUEUE)
Costruita servendosi della Struttura Dati di LISTA PUNTATA SINGOLA e modificata
nel suo funzionamento per essere usata per la VISITA PER LIVELLI di un ALBERO
BINARIO.
La Coda si serve di Record Singoli mentre l'albero binario di Record Doppi. 
Il segreto consiste nell'immagazzinare il riferimento a ciascun nodo dell'albero
nel campo Data e il riferimento al record singolo successivo nel campo Next.
La Coda e' quindi costituita da una successione di record singoli che si puntano
a vicenda in sequenza e in cui ciascuno di essi contiene il riferimento a 
ciascun nodo corrispondente dell'Albero Binario.
Quindi...
    - Campo DATA : Riferimento a Nodo Albero Binario
    - Campo NEXT : Riferimento a Record Singolo Successivo nella Coda

'''

class Coda:
    
    # ATTRIBUTI
    _head=None
    _tail=None
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,_head=None,_tail=None):
        self._head=_head
        self._tail=_tail
   
        
    # METODI
    

    'ENQUEUE'
    def enqueue(self,el):                       # T(n)
        if self._tail==None:                    # Θ(1)
            # Creiamo un nuovo Record Singolo che contiene il riferimento 
            # al nodo dell'albero binario nel suo campo Data.
            self._tail=RecordSingolo()          # Θ(1)
            self._tail.setData(el)              # Θ(1)
            self._tail.setNext(None)            # Θ(1) 
            self._head=self._tail               # Θ(1) 
        else:                                   # Θ(1)
            # Creiamo un nuovo Record Singolo che contiene il riferimento 
            # al nodo dell'albero binario nel suo campo Data.
            nuovoRecord=RecordSingolo(el,None)  # Θ(1)
            self._tail.setNext(nuovoRecord)     # Θ(1)
            self._tail=self._tail.getNext()     # Θ(1)
        return                                  # Θ(1)


    'DEQUEUE'    
    def dequeue(self):                          # T(n)
        if self._head==None:                    # Θ(1)
            return None                         # Θ(1)
        else:                                   # Θ(1)
            # Si scoda il record singolo di testa (head) e si ritorna 
            # all'utente il dato contenuto nel suo campo Data...ovvero 
            # il riferimento al corrispondente Nodo dell'albero binario.
            e=self._head.getData()              # Θ(1)
            self._head=self._head.getNext()     # Θ(1)
        if self._head==None:                    # Θ(1)
            self._tail=None                     # Θ(1)
        return e                                # Θ(1)
    
    
    'SIZE'
    def size(self):                             # T(n)
        refRecord=self._head                    # Θ(1)
        i=0                                     # Θ(1)
        while refRecord!=None:                  # n*Θ(1)+Θ(1)
            refRecord=refRecord.getNext()       # Θ(1)
            i+=1                                # Θ(1)
        return i                                # Θ(1)
            
        
    'ToString'
    def __str__(self):
        p_corr=self._head
        output=""
        while p_corr!=None:
            if p_corr.getNext()!=None:
                output+="["+str(p_corr)+"]" + " - "
            else:
                output+="["+str(p_corr)+"]"
            p_corr=p_corr.getNext()
        return output
        
