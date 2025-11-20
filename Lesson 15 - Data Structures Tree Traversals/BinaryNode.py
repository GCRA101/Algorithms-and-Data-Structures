# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
NODO for ALBERO
The Nodo dell'Tree Binario viene implementato as a record doppio, that is
a classe containing the value del nodo, the pointer al figlio sinistro and 
the pointer al figlio destro.
In a Tree Binario sorted, the figlio Sx viene first del figlio Dx.
'''


class Nodo:
    
    # ATTRIBUTES
    value=None
    figlioSx=None
    figlioDx=None
    
    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,value=None, figlioSx=None, figlioDx=None):
        self.value=value
        self.figlioSx=figlioSx
        self.figlioDx=figlioDx
        
        
    # METHODS
    
    'Setters'
    def setValore(self, value):
        self.value=value
    def setFiglioSx(self, figlioSx):
        self.figlioSx=figlioSx
    def setFiglioDx(self, figlioDx):
        self.figlioDx=figlioDx
    
    'Getters'
    def getValore(self):
        return self.value
    def getFiglioSx(self):
        return self.figlioSx
    def getFiglioDx(self):
        return self.figlioDx
    
    'Overridden ToString()'
    def __str__(self):
        return (str(self.value))
    