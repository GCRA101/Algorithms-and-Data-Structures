# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""




class RecordDoppio:
    
    # ATTRIBUTES
    _key=None
    _prev=None
    _next=None
    _pointer=None
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,_key=None,_prev=None,_next=None,_pointer=None):
        self._key=_key
        self._prev=_prev
        self._next=_next
        self._pointer=_pointer
        
        
    # METHODS
    
    'Setters'
    def setKey(self,_key):
        self._key=_key
    def setPrev(self,_prev):
        self._prev=_prev
    def setNext(self,_next):
        self._next=_next
    def setPointer(self, _pointer):
        self._pointer=_pointer
    
    'Getters'
    def getKey(self):
        return self._key
    def getPrev(self):
        return self._prev
    def getNext(self):
        return self._next
    def getPointer(self):
        return self._pointer
    
    
    def __str__(self):
        return (str(self._key) + "-" + str(self._prev) + "-" 
                + str(self._pointer) + "-" + str(self._next))
    