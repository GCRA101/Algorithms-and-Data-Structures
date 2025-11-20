# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:44:46 2023

@author: giorg
"""


'''
RECORD SINGOLO with POINTER OBJECT
In this implementazione del record/nodo singolo, the pointer all'element
successivo in the list is implementato as a riferimento all'oggetto.
Instead of usare a stringa with l'id ipotetico dell'indirizzo of memoria, 
usiamo direttamente the riferimento to the corrispondente variable.
A'implementazione piu' robusta and semplice from usare ed also piu' pratica.
'''

class RecordSingolo:
    
    
    # ATTRIBUTES
    _data=None
    _next=None

    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,_data=None,_next=None):
        self._data=_data
        self._next=_next
    
    # METHODS
    
    'Setters'
    def setData(self,_data):
        self._data=_data
    def setNext(self,_next):
        self._next=_next
    
    'Getters'
    def getData(self):
        return self._data
    def getNext(self):
        return self._next
    
    'Overridden ToString'
    def __str__(self):
        return str(self._data)

    