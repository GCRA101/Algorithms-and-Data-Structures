# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:43:13 2023

@author: giorg
"""

# IMPORT LIBRARIES
import copy

# IMPORT PACKAGE CLASSES
from Disk import Disco


# CLASSE PIOLO

class Piolo:
    
    # ATTRIBUTI
    dischi=list()
    
    # COSTRUTTORI
    'Default and Overloaded'
    def __init__(self,n=None):
        self.dischi=list()
        if n!=None:
            for i in range(n,0,-1):
                self.dischi.append(Disco(i))
            
            
    # METODI
    'Rimuovi disco in cima alla pila'
    def rimuoviDisco(self):
        if len(self.dischi)!=0:
            return self.dischi.pop()
    
    'Aggiungi disco in cima alla pila'
    def aggiungiDisco(self,disco):
        '''Se la pila e vuota o il disco da aggiungere ha diametro minore
         del disco in cima alla pila...aggiungi il disco'''
        if len(self.dischi)==0 or disco.minoreDi(self.dischi[-1]):
            self.dischi.append(disco)

    def getCopiaDischi(self):
        return copy.copy(self.dischi)
        