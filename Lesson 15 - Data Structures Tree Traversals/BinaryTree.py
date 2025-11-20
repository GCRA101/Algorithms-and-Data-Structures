# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import math as math
import time
import matplotlib.pyplot as plt
import random


# IMPORT PACKAGE CLASSES
from BinaryNode import Nodo
from Modified_Queue import Queue

'''
CLASSE ALBERO (TREE)
Costruita servendosi of Record and Puntatori
Since ciascun nodo is rappresentato in memoria through a record doppio,
ciascun nodo dell'tree is sparso in the memoria del computer and puo' essere 
acceduto only through the puntatori destro and sinistro of ciascun record to partire
dal nodo root dell'tree.
The classe tree, therefore deve only contenere the record of the root.
'''

class AlberoBinario:
    
    # ATTRIBUTES
    root=None
    
    # CONSTRUCTOR
    'Default and Overloaded'
    def __init__(self,root=None):
        self.root=root
        
    # METHODS
    
    'GetRoot'
    def getRoot(self):                                  # T(n)
        return self.root                                # Θ(1)  
    
    # Computational Cost: T(n)=Θ(1)



    'Visita in Preordine'
    
    # function Privata recursive    
    def __visitaPreOrdine(self,p):                   # S(n)
        if p!=None:                                  # Θ(1)
            'OPERAZIONE SUL NODO'
            print(str(p.getValore()),end=" ")        # Θ(1)
            'PASSO RICORSIVO 1 (SX)'
            self.__visitaPreOrdine(p.getFiglioSx())  # S(k)
            'PASSO RICORSIVO 2 (DX)'
            self.__visitaPreOrdine(p.getFiglioDx())  # S(n-k-1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Pubblica Wrapper launch of the function recursive
    def visitaPreOrdine(self):                       # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaPreOrdine(p)                    # S(n)
        return

    # Computational Cost
    # Dimensions input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Visita in Inordine'
    
    # function Privata recursive 
    def __visitaInOrdine(self,p):                    # S(n)
        if p!=None:                                  # Θ(1)
            'PASSI RICORSIVO 1 (SX)'
            self.__visitaInOrdine(p.getFiglioSx())   # S(k)
            'OPERAZIONE SUL NODO'
            print(str(p.getValore()),end=" ")        # Θ(1)
            'PASSI RICORSIVO 2 (DX)'
            self.__visitaInOrdine(p.getFiglioDx())   # S(n-k-1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Pubblica Wrapper launch of the function recursive
    def visitaInOrdine(self):                        # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaInOrdine(p)                     # S(n)

    # Computational Cost
    # Dimensions input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Visita in Postordine'
    
    # function Privata recursive
    def __visitaPostOrdine(self,p):                  # S(n)
        if p!=None:                                  # Θ(1)
            'PASSI RICORSIVO 1 (SX)'
            self.__visitaPostOrdine(p.getFiglioSx()) # S(k)
            'PASSI RICORSIVO 2 (DX)'
            self.__visitaPostOrdine(p.getFiglioDx()) # S(n-k-1)
            'OPERAZIONE SUL NODO'
            print(str(p.getValore()),end=" ")        # Θ(1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Publica Wrapper launch of the function recursive
    def visitaPostOrdine(self):                      # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaPostOrdine(p)                   # S(n)

    # Computational Cost
    # Dimensions input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Controllo Riempimento Queue'
    def codaVuota(self,queue):                      # T(n)
        if queue.size()==0:                         # Θ(1)
            return True                            # Θ(1)
        return False                               # Θ(1)

    # Cost: T(n)=Θ(1)


    'Visita For Livelli'

    def visitaPerLivelli(self):                    # T(n)
        # Inizializzazione to the root dell'tree
        p=self.root                                # Θ(1)
        # Controllo esistenza tree
        if p==None:                                # Θ(1)
            return                                 # Θ(1)
        # Inizializzazione queue of supporto
        queue=Queue()                                # Θ(1)                                                     
        # Incodamento root tree in the queue
        queue.enqueue(p)                            # Θ(1)                           
        # Scorrimento nodi tree through queue
        while(not self.codaVuota(queue)):           # n*Θ(1)+Θ(1) 
            # 1. Scoda and prints nodo
            p=queue.dequeue()                       # Θ(1)
            print(str(p),end=" ")                  # Θ(1)         
            # Incoda figlioSx
            if p.getFiglioSx()!=None:              # Θ(1)
                queue.enqueue(p.getFiglioSx())      # Θ(1)
            # Incoda figlio Dx
            if p.getFiglioDx()!=None:              # Θ(1)
                queue.enqueue(p.getFiglioDx())      # Θ(1)
        return                                     # Θ(1)
        
    # Computational Cost
    # Dimensions input: number nodi dell'tree (incognito to priori)
    # Cost: T(n)=Θ(1)+Θ(n)+Θ(1)  -> T(n)=Θ(n) 

     

    'Conteggio number nodi'
    
    # function Privata recursive
    def __calcola_n(self,p):                         # S(n)
        if p!=None:                                  # Θ(1)
            # 1. Recursive Step SottoAlbero Sx
            num_l=self.__calcola_n(p.getFiglioSx())  # S(k)
            # 2. Recursive Step SottoAlbero Dx
            num_r=self.__calcola_n(p.getFiglioDx())  # S(n-k-1)
            # 3. Operazione on the Nodo
            num=num_l+num_r+1                        # Θ(1)     
            return num                               # Θ(1)  
        return 0                                     # Θ(1)  
    
    # function Pubblica Wrapper launch of the function recursive
    def calcola_n(self):                             # T(n)
        p=self.root                                  # Θ(1)
        return self.__calcola_n(p)                   # S(n)
    
    # Computational Cost
    # Dimension Input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



    'Search Nodo'
    
    # function Privata recursive
    def __cerca(self,k,p):                               # S(n)
        if p!=None:                                      # Θ(1) 
          # 1. Operazione on the Nodo
          if p.getValore()==k.getValore():               # Θ(1)              
              return True                                # Θ(1) 
          # 2. Recursive Step SottoAlbero Sx
          elif self.__cerca(k,p.getFiglioSx())==True:    # S(k)
              return True                                # Θ(1) 
          else:                                          # Θ(1) 
          # 3. Recursive Step SottoAlbero Dx
              return self.__cerca(k,p.getFiglioDx())     # S(n-k-1)
        return False                                     # Θ(1) 
    
    # function Pubblica Wrapper launch of the function recursive
    def cerca(self,k):                                   # T(n)
        p=self.root                                      # Θ(1) 
        return self.__cerca(k, p)                        # S(n)
    
    # Computational Cost
    # Dimension Input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)
    


    'Calcolo Altezza'
    
    # function Privata recursive
    def __calcola_h(self,p):                                 # S(n)
        if p==None:                                          # Θ(1) 
            return -1                                        # Θ(1)
        if p.getFiglioSx()==None and p.getFiglioDx()==None:  # Θ(1)
            return 0                                         # Θ(1)
        # 1. 2. Recursive Step SottoAlbero Sx and Dx
        h=max(self.__calcola_h(p.getFiglioSx()),             # S(k)
              self.__calcola_h(p.getFiglioDx()))             # S(n-k-1)
        # 3. Operazione on the Nodo
        return h+1                                           # Θ(1)                       

    # function Pubblica Wrapper for the lancio of the function recursive
    def calcola_h(self):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self.__calcola_h(p)                           # S(n)

    # Computational Cost
    # Dimension Input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)



    'Conteggio Nodi al Level k'
    
    # function Privata recursive
    def __conta_k(self,k,the,p):                               # S(n)
        if p==None:                                          # Θ(1)
            return 0                                         # Θ(1)
        if k==the:                                             # Θ(1)
            return 1                                         # Θ(1)
        # 1. Recursive Step SottoAlbero Sx
        k_left=self.__conta_k(k,the+1,p.getFiglioSx())         # S(k)
        # 2. Recursive Step SottoAlbero Dx
        k_right=self.__conta_k(k,the+1,p.getFiglioDx())        # S(n-k-1)
        # 3. Operazione on the Nodo
        return k_left+k_right                                # Θ(1)

    # function Pubblica Wrapper for the lancio of the function recursive
    def conta_k(self,k):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self.__conta_k(k, 0, p)                       # S(n)

    # Computational Cost
    # Dimension Input: number nodi dell'tree (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



'TEST'

# 1. CREAZIONE ALBERO PER I TEST

valoriNodi=[3,1,5,8,4,3,2,8,0,8,5]
nodi=[]
vettorePosizionale=[]

for the in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[the])) 
    
for the in range(0,(len(nodi)-2)//2+1,1):
        nodi[the].setFiglioSx(nodi[2*the+1])
        nodi[the].setFiglioDx(nodi[2*the+2])
        
root=nodi[0]
tree=AlberoBinario(root)


# 2. TEST METODI

'GetRoot'
print("\nGetRoot(): " + str(tree.getRoot()))

'Visita in Preordine'  
print("Visita in Preordine:")
tree.visitaPreOrdine()

'Visita in Inordine' 
print("\nVisita in Inordine:")
tree.visitaInOrdine()

'Visita in Postordine'   
print("\nVisita in Postordine:")
tree.visitaPostOrdine()

'Visita For Livelli'
print("\nVisita for Livelli:")
tree.visitaPerLivelli()

'Conteggio number nodi'
print("\nConteggio number Nodi: " + str(tree.calcola_n()))

'Search Nodo'
k=nodi[3]
print("Search Nodo " + str(k) + " : " + str(tree.cerca(k)))

'Calcolo Altezza'
print("Calcolo Altezza dell'tree: " + str(tree.calcola_h()))

'Conteggio Nodi al Level k'
print("Conteggio number nodi al level 2: " + str(tree.conta_k(2)))
