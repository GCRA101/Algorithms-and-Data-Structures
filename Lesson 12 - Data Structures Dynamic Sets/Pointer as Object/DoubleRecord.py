# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
RECORD DOPPIO with POINTER OBJECT
In this implementazione del record/nodo singolo, the puntatore agli elementi
successivo e precedente nella list are implementati as riferimenti
agli oggetti.
Invece of usare a stringa with l'id ipotetico dell'indirizzo of memoria, 
usiamo direttamente the riferimento alla corrispondente variabile.
A'implementazione piu' robusta e semplice from usare ed also piu' pratica.
'''


class RecordDoppio:
    
    # ATTRIBUTES
    _data=None
    _prev=None
    _next=None
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,_data=None,_prev=None,_next=None):
        self._data=_data
        self._prev=_prev
        self._next=_next
        
        
    # METHODS
    
    'Setters'
    def setData(self,_data):
        self._data=_data
    def setPrev(self,_prev):
        self._prev=_prev
    def setNext(self,_next):
        self._next=_next
    
    'Getters'
    def getData(self):
        return self._data
    def getPrev(self):
        return self._prev
    def getNext(self):
        return self._next
    
    'Overridden ToString()'
    def __str__(self):
        return (str(self._data))
    