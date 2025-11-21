# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:44:46 2023

@author: giorg
"""


class RecordSingolo:
    
    
    # ATTRIBUTI
    _key=None
    _next=None
    _pointer=None

    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,_key=None,_next=None,_pointer=None):
        self._key=_key
        self._next=_next
        self._pointer=_pointer
    
    # METODI
    
    'Setters'
    def setKey(self,_key):
        self._key=_key
    def setNext(self,_next):
        self._next=_next
    def setPointer(self,_pointer):
        self._pointer=_pointer
    
    'Getters'
    def getKey(self):
        return self._key
    def getNext(self):
        return self._next
    def getPointer(self):
        return self._pointer
    