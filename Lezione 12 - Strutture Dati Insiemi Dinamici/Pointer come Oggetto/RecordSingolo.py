# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:44:46 2023

@author: giorg
"""


'''
RECORD SINGOLO con POINTER OBJECT
In questa implementazione del record/nodo singolo, il puntatore all'elemento
successivo nella lista e' implementato come un riferimento all'oggetto.
Invece di usare una stringa con l'id ipotetico dell'indirizzo di memoria, 
usiamo direttamente il riferimento alla corrispondente variabile.
Un'implementazione piu' robusta e semplice da usare ed anche piu' pratica.
'''

class RecordSingolo:
    
    
    # ATTRIBUTI
    _data=None
    _next=None

    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,_data=None,_next=None):
        self._data=_data
        self._next=_next
    
    # METODI
    
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

    