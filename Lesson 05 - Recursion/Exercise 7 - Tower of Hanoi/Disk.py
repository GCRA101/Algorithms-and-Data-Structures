# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:48:40 2023

@author: giorg
"""

class Disco:
    
    # ATTRIBUTES
    diametro=0
    
    # CONSTRUCTOR
    def __init__(self,diametro):
        self.diametro=diametro
    
    # METHODS
    
    # Metodo of Utilita
    def minoreDi(self,disk):
        return self.diametro<disk.diametro
    # Metodo Getter
    def getDiametro(self):
        return self.diametro