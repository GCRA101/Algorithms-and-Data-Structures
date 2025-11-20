# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 16:44:46 2023

@author: giorg
"""


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
 
 'ToString'
 def __str__(self):
 return (str(self._data))
 