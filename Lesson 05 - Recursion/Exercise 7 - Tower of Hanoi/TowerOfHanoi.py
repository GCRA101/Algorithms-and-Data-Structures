# -*- coding: utf-8 -*-
"""
Created on Fri Jun 9 18:01:26 2023

@author: giorg
"""

# IMPORT LIBRARIES
import time

# IMPORT PACKAGE CLASSES
from Peg import Piolo
from Disk import Disco


class TorreHanoi:
 
 # ATTRIBUTES
 nDischi=0
 millisecs=0
 peg1=Piolo()
 peg2=Piolo()
 peg3=Piolo()
 
 
 # CONSTRUCTOR
 'Overloaded'
 def __init__(self,nDischi,millisecs):
 self.nDischi=nDischi
 self.millisecs=millisecs
 self.peg1=Piolo(self.nDischi)
 self.peg2=Piolo()
 self.peg3=Piolo()
 
 
 
 # METHODS

 'MUOVI - Privato Ricorsivo'
 def _muovi(self,n,origine,temp,target):
 'While there are disks to move...'
 if n>0:
 '1) Move n-1 disks from source peg to temporary peg'
 self._muovi(n-1,origine,target, temp)
 '2) Move the last remaining disk from source peg to target peg'
 target.aggiungiDisco(origine.rimuoviDisco())
 ' Print to Console'
 self.printStep()
 '3) Move disks from temp peg to target peg'
 self._muovi(n-1,temp,origine,target)
 
 'MUOVI - Pubblico'
 '''Public method that makes the first call to the private 
 recursive method'''
 def muovi(self):
 self.printStep()
 self._muovi(self.nDischi,self.peg1,self.peg2,self.peg3)


 'GETLEVELSTRING - Disk Representation on Peg'
 def getLevelString(self,diametroDisco):
 res=""
 spazi=" "*(self.nDischi-diametroDisco)
 res+=spazi
 res +="-"*((diametroDisco-1)*2 + 1)
 res+=spazi
 return res

 '__STR___ - ToString()'
 '''Returns the graphical visualization of the 3 towers'''
 def __str__(self):
 res=""
 '1) Create copies of disk stacks on the three pegs'
 disks1=self.peg1.getCopiaDischi()
 disks2=self.peg2.getCopiaDischi()
 disks3=self.peg3.getCopiaDischi()
 '2) Extract the size of each disk'
 size1=len(disks1)
 size2=len(disks2)
 size3=len(disks3)
 '3) Draw the 3 towers by calling the function getLevelString'
 emptyRow=" "*(self.nDischi*2-1)
 
 for the in range(self.nDischi,0,-1):
 if size1<the :
 res+=emptyRow
 else:
 res+=self.getLevelString(disks1.pop().getDiametro())
 res+=" | "
 if size2<the :
 res+=emptyRow
 else:
 res+=self.getLevelString(disks2.pop().getDiametro())
 res+=" | "
 if size3<the :
 res+=emptyRow
 else:
 res+=self.getLevelString(disks3.pop().getDiametro())
 res+="\n" 
 
 return res
 
 
 
 'PRINTSTEP - Visualization Method'
 def printStep(self):
 'Clear the Console Window'
 for the in range(0,30,1): print("\n")
 'Print current state of towers'
 print(self.__str__())
 'Wait for milliseconds before next step'
 time.sleep(self.millisecs/1000) 

