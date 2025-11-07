# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
NODO per ALBERO BINARIO di RICERCA
Il Nodo dell'Albero Binario di Ricerca viene implementato come un record triplo
ovvero una classe contenente il valore del nodo (chiave), il puntatore al 
figlio sinistro, il puntatore al figlio destro e il puntatore al padre.
Quest'ultimo e' fondamentale per poter effettuare le salite attraverso l'albero
(per esempio per trovare i Nodi Predecessori e i Nodi Successori.'
In un Albero Binario Ordinato, il figlio Sx viene prima del figlio Dx.
'''


class Nodo:
    
    # ATTRIBUTI
    key=None
    left=None
    right=None
    parent=None
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,key=None, parent=None, left=None, right=None):
        self.key=key
        self.parent=parent
        self.left=left
        self.right=right
        
        
    # METODI
    
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
    