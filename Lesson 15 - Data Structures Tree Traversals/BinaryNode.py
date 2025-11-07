# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
NODO per ALBERO
Il Nodo dell'Albero Binario viene implementato come un record doppio, ovvero
una classe contenente il valore del nodo, il puntatore al figlio sinistro e 
il puntatore al figlio destro.
In un Albero Binario Ordinato, il figlio Sx viene prima del figlio Dx.
'''


class Nodo:
    
    # ATTRIBUTI
    valore=None
    figlioSx=None
    figlioDx=None
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,valore=None, figlioSx=None, figlioDx=None):
        self.valore=valore
        self.figlioSx=figlioSx
        self.figlioDx=figlioDx
        
        
    # METODI
    
    'Setters'
    def setValore(self, valore):
        self.valore=valore
    def setFiglioSx(self, figlioSx):
        self.figlioSx=figlioSx
    def setFiglioDx(self, figlioDx):
        self.figlioDx=figlioDx
    
    'Getters'
    def getValore(self):
        return self.valore
    def getFiglioSx(self):
        return self.figlioSx
    def getFiglioDx(self):
        return self.figlioDx
    
    'Overridden ToString()'
    def __str__(self):
        return (str(self.valore))
    