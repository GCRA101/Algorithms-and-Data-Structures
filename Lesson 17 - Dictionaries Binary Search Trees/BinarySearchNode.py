# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
NODO for ALBERO BINARIO of RICERCA
The Nodo dell'Binary Search Tree viene implementato as a record triplo
that is a classe containing the value del nodo (key), the puntatore al 
figlio sinistro, the puntatore al figlio destro e the puntatore al padre.
Quest'last e' fondamentale for poter effettuare the salite through l'albero
(for esempio for trovare the Nodi Predecessori e the Nodi Successori.'
In a Albero Binario sorted, the figlio Sx viene first del figlio Dx.
'''


class Nodo:
    
    # ATTRIBUTES
    key=None
    left=None
    right=None
    parent=None
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,key=None, parent=None, left=None, right=None):
        self.key=key
        self.parent=parent
        self.left=left
        self.right=right
        
        
    # METHODS
    
    'Setters'
    def setKey(self,key):
        self.key=key
    def setParent(self, parent):
        self.parent=parent
    def setLeft(self, left):
        self.left=left
    def setRight(self, right):
        self.right=right
    
    'Getters'
    def getKey(self):
        return self.key
    def getParent(self):
        return self.parent
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    
    'Overridden ToString()'
    
    def __str__(self):
        return (str(self.key))
    
    'Overridden CompareTo'
    def __le__(self,o):
        if isinstance(o, Nodo):
            return self.key<=o.key
        return False
    
    def __lt__(self,o):
        if isinstance(o,Nodo):
            return self.key<o.key
        return False
    
    def __ge__(self,o):
        if isinstance(o,Nodo):
            return self.key>=o.key
        return False
    
    def __gt__(self,o):
        if isinstance(o,Nodo):
            return self.key>o.key
        return False
    
    def __eq__(self, o):
        if isinstance(o, Nodo):
            return self.key == o.key
        return False
    
    def __neg__(self,o):
        if isinstance(o,Nodo):
            return not self.__eq__(o)
        return False
    