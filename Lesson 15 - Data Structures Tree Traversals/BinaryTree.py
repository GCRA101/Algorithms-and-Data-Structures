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
from Modified_Queue import Coda

'''
CLASSE ALBERO (TREE)
Costruita servendosi di Record e Puntatori
Dato che ciascun nodo e' rappresentato in memoria tramite un record doppio,
ciascun nodo dell'albero e' sparso nella memoria del computer e puo' essere 
acceduto solo tramite i puntatori destro e sinistro di ciascun record a partire
dal nodo radice dell'albero.
La classe albero, quindi deve solo contenere il record della radice.
'''

class AlberoBinario:
    
    # ATTRIBUTES
    root=None
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,root=None):
        self.root=root
        
    # METHODS
    
    'GetRoot'
    def getRoot(self):                                  # T(n)
        return self.root                                # Θ(1)  
    
    # Computational Cost: T(n)=Θ(1)



    'Visita in Preordine'
    
    # Funzione Privata Ricorsiva    
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

    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def visitaPreOrdine(self):                       # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaPreOrdine(p)                    # S(n)
        return

    # Computational Cost
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Visita in Inordine'
    
    # Funzione Privata Ricorsiva 
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

    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def visitaInOrdine(self):                        # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaInOrdine(p)                     # S(n)

    # Computational Cost
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Visita in Postordine'
    
    # Funzione Privata Ricorsiva
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

    # Funzione Publica Wrapper di lancio della Funzione Ricorsiva
    def visitaPostOrdine(self):                      # T(n)
        p=self.root                                  # Θ(1)
        self.__visitaPostOrdine(p)                   # S(n)

    # Computational Cost
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'Controllo Riempimento Coda'
    def codaVuota(self,coda):                      # T(n)
        if coda.size()==0:                         # Θ(1)
            return True                            # Θ(1)
        return False                               # Θ(1)

    # Costo: T(n)=Θ(1)


    'Visita Per Livelli'

    def visitaPerLivelli(self):                    # T(n)
        # Inizializzazione alla radice dell'albero
        p=self.root                                # Θ(1)
        # Controllo esistenza albero
        if p==None:                                # Θ(1)
            return                                 # Θ(1)
        # Inizializzazione coda di supporto
        coda=Coda()                                # Θ(1)                                                     
        # Incodamento radice albero nella coda
        coda.enqueue(p)                            # Θ(1)                           
        # Scorrimento nodi albero tramite coda
        while(not self.codaVuota(coda)):           # n*Θ(1)+Θ(1) 
            # 1. Scoda e stampa nodo
            p=coda.dequeue()                       # Θ(1)
            print(str(p),end=" ")                  # Θ(1)         
            # Incoda figlioSx
            if p.getFiglioSx()!=None:              # Θ(1)
                coda.enqueue(p.getFiglioSx())      # Θ(1)
            # Incoda figlio Dx
            if p.getFiglioDx()!=None:              # Θ(1)
                coda.enqueue(p.getFiglioDx())      # Θ(1)
        return                                     # Θ(1)
        
    # Computational Cost
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: T(n)=Θ(1)+Θ(n)+Θ(1)  -> T(n)=Θ(n) 

     

    'Conteggio numero nodi'
    
    # Funzione Privata Ricorsiva
    def __calcola_n(self,p):                         # S(n)
        if p!=None:                                  # Θ(1)
            # 1. Recursive Step SottoAlbero Sx
            num_l=self.__calcola_n(p.getFiglioSx())  # S(k)
            # 2. Recursive Step SottoAlbero Dx
            num_r=self.__calcola_n(p.getFiglioDx())  # S(n-k-1)
            # 3. Operazione sul Nodo
            num=num_l+num_r+1                        # Θ(1)     
            return num                               # Θ(1)  
        return 0                                     # Θ(1)  
    
    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def calcola_n(self):                             # T(n)
        p=self.root                                  # Θ(1)
        return self.__calcola_n(p)                   # S(n)
    
    # Computational Cost
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



    'Ricerca Nodo'
    
    # Funzione Privata Ricorsiva
    def __cerca(self,k,p):                               # S(n)
        if p!=None:                                      # Θ(1) 
          # 1. Operazione sul Nodo
          if p.getValore()==k.getValore():               # Θ(1)              
              return True                                # Θ(1) 
          # 2. Recursive Step SottoAlbero Sx
          elif self.__cerca(k,p.getFiglioSx())==True:    # S(k)
              return True                                # Θ(1) 
          else:                                          # Θ(1) 
          # 3. Recursive Step SottoAlbero Dx
              return self.__cerca(k,p.getFiglioDx())     # S(n-k-1)
        return False                                     # Θ(1) 
    
    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def cerca(self,k):                                   # T(n)
        p=self.root                                      # Θ(1) 
        return self.__cerca(k, p)                        # S(n)
    
    # Computational Cost
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)
    


    'Calcolo Altezza'
    
    # Funzione Privata Ricorsiva
    def __calcola_h(self,p):                                 # S(n)
        if p==None:                                          # Θ(1) 
            return -1                                        # Θ(1)
        if p.getFiglioSx()==None and p.getFiglioDx()==None:  # Θ(1)
            return 0                                         # Θ(1)
        # 1. 2. Recursive Step SottoAlbero Sx e Dx
        h=max(self.__calcola_h(p.getFiglioSx()),             # S(k)
              self.__calcola_h(p.getFiglioDx()))             # S(n-k-1)
        # 3. Operazione sul Nodo
        return h+1                                           # Θ(1)                       

    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def calcola_h(self):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self.__calcola_h(p)                           # S(n)

    # Computational Cost
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)



    'Conteggio Nodi al Livello k'
    
    # Funzione Privata Ricorsiva
    def __conta_k(self,k,i,p):                               # S(n)
        if p==None:                                          # Θ(1)
            return 0                                         # Θ(1)
        if k==i:                                             # Θ(1)
            return 1                                         # Θ(1)
        # 1. Recursive Step SottoAlbero Sx
        k_left=self.__conta_k(k,i+1,p.getFiglioSx())         # S(k)
        # 2. Recursive Step SottoAlbero Dx
        k_right=self.__conta_k(k,i+1,p.getFiglioDx())        # S(n-k-1)
        # 3. Operazione sul Nodo
        return k_left+k_right                                # Θ(1)

    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def conta_k(self,k):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self.__conta_k(k, 0, p)                       # S(n)

    # Computational Cost
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



'TEST'

# 1. CREAZIONE ALBERO PER I TEST

valoriNodi=[3,1,5,8,4,3,2,8,0,8,5]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,(len(nodi)-2)//2+1,1):
        nodi[i].setFiglioSx(nodi[2*i+1])
        nodi[i].setFiglioDx(nodi[2*i+2])
        
radice=nodi[0]
albero=AlberoBinario(radice)


# 2. TEST METODI

'GetRoot'
print("\nGetRoot(): " + str(albero.getRoot()))

'Visita in Preordine'  
print("Visita in Preordine:")
albero.visitaPreOrdine()

'Visita in Inordine' 
print("\nVisita in Inordine:")
albero.visitaInOrdine()

'Visita in Postordine'   
print("\nVisita in Postordine:")
albero.visitaPostOrdine()

'Visita Per Livelli'
print("\nVisita per Livelli:")
albero.visitaPerLivelli()

'Conteggio numero nodi'
print("\nConteggio Numero Nodi: " + str(albero.calcola_n()))

'Ricerca Nodo'
k=nodi[3]
print("Ricerca Nodo " + str(k) + " : " + str(albero.cerca(k)))

'Calcolo Altezza'
print("Calcolo Altezza dell'albero: " + str(albero.calcola_h()))

'Conteggio Nodi al Livello k'
print("Conteggio numero nodi al livello 2: " + str(albero.conta_k(2)))
