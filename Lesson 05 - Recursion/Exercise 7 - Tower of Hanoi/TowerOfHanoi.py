# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 18:01:26 2023

@author: giorg
"""

# IMPORT LIBRARIES
import time

# IMPORT PACKAGE CLASSES
from Peg import Piolo
from Disk import Disco


class TorreHanoi:
    
    # ATTRIBUTI
    nDischi=0
    millisecs=0
    piolo1=Piolo()
    piolo2=Piolo()
    piolo3=Piolo()
    
    
    # COSTRUTTORE
    'Overloaded'
    def __init__(self,nDischi,millisecs):
        self.nDischi=nDischi
        self.millisecs=millisecs
        self.piolo1=Piolo(self.nDischi)
        self.piolo2=Piolo()
        self.piolo3=Piolo()
        
        
        
    # METODI

    'MUOVI - Privato Ricorsivo'
    def _muovi(self,n,origine,temp,target):
        'Fino a che ci sono dischi da muovere...'
        if n>0:
            '1) Muovi n-1 dischi dal piolo origine a quello temporaneo'
            self._muovi(n-1,origine,target, temp)
            '2) Muovi lultimo disco rimasto dal piolo origine a quello target'
            target.aggiungiDisco(origine.rimuoviDisco())
            ' Stampa in Console'
            self.printStep()
            '3) Muovi i dischi del piolo temp su quello target'
            self._muovi(n-1,temp,origine,target)
    
    'MUOVI - Pubblico'
    '''Metodo pubblico che effettua la prima chiamata al metodo privato 
     ricorsivo'''
    def muovi(self):
        self.printStep()
        self._muovi(self.nDischi,self.piolo1,self.piolo2,self.piolo3)


    'GETLEVELSTRING - Rappresentazione Disco su Piolo'
    def getLevelString(self,diametroDisco):
        res=""
        spazi=" "*(self.nDischi-diametroDisco)
        res+=spazi
        res +="-"*((diametroDisco-1)*2 + 1)
        res+=spazi
        return res

    '__STR___ - ToString()'
    '''Restituisce la visualizzazione grafica delle 3 torri'''
    def __str__(self):
       res=""
       '1) Crea copie delle pile di dischi sui tre pioli'
       disks1=self.piolo1.getCopiaDischi()
       disks2=self.piolo2.getCopiaDischi()
       disks3=self.piolo3.getCopiaDischi()
       '2) Estrai la dimensione di ciascun disco'
       size1=len(disks1)
       size2=len(disks2)
       size3=len(disks3)
       '3) Disegna le 3 torri chiamando la funzione getLevelString'
       emptyRow=" "*(self.nDischi*2-1)
       
       for i in range(self.nDischi,0,-1):
           if size1<i :
               res+=emptyRow
           else:
               res+=self.getLevelString(disks1.pop().getDiametro())
           res+=" | "
           if size2<i :
               res+=emptyRow
           else:
               res+=self.getLevelString(disks2.pop().getDiametro())
           res+=" | "
           if size3<i :
               res+=emptyRow
           else:
               res+=self.getLevelString(disks3.pop().getDiametro())
           res+="\n"        
       
       return res
           
  
        
    'PRINTSTEP - Metodo di Visualizzazione'
    def printStep(self):
        'Pulisci la Console Window'
        for i in range(0,30,1): print("\n")
        'Stampa lo stato corrente delle torri'
        print(self.__str__())
        'Aspetta tot millisecondi prima del prossimo step'
        time.sleep(self.millisecs/1000)     

