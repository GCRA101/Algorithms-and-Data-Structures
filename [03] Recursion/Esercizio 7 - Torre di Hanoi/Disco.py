# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:48:40 2023

@author: giorg
"""

class Disco:
    
    # ATTRIBUTI
    diametro=0
    
    # COSTRUTTORE
    def __init__(self,diametro):
        self.diametro=diametro
    
    # METODI
    
    # Metodo di Utilita
    def minoreDi(self,disco):
        return self.diametro<disco.diametro
    # Metodo Getter
    def getDiametro(self):
        return self.diametro