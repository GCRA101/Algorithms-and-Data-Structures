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
'Nodo with 3 puntatori: Padre (parent), FiglioSx (left) e FiglioDx (right)'
from BinarySearchNode import Nodo
'Coda Modificata for ospitare the nodi dellalbero nel campo value dei'
'suoi record singoli.'
from Modified_Queue import Coda

'''
CLASSE ALBERO (TREE)
Costruita servendosi of Record e Puntatori
Since ciascun nodo e' rappresentato in memoria through a record,
ciascun nodo dell'albero e' sparso nella memoria del computer e puo' essere 
acceduto through the puntatori destro, sinistro e padre of ciascun nodo to partire
dalla radice dell'albero.'
The classe albero, quindi deve only contenere the record della radice.
'''


class AlberoBinarioDiRicerca:
    
    
    # ATTRIBUTES
    root=None
    
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,root=None):
        self.root=root
        
        
    # METHODS
    
    'GET ROOT'
    def getRoot(self):                                  # T(n)
        return self.root                                # Θ(1)  
    
    # Computational Cost: T(n)=Θ(1)



    'VISITA IN PREORDINE'
    
    # function Privata recursive    
    def _visitaPreOrdine(self,p):                    # S(n)
        if p!=None:                                  # Θ(1)
            'OPERAZIONE SUL NODO'
            print(str(p.getKey()),end=" ")           # Θ(1)
            'PASSO RICORSIVO 1 (SX)'
            self._visitaPreOrdine(p.getLeft())       # S(k)
            'PASSO RICORSIVO 2 (DX)'
            self._visitaPreOrdine(p.getRight())      # S(n-k-1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Pubblica Wrapper of lancio della function recursive
    def visitaPreOrdine(self):                       # T(n)
        p=self.root                                  # Θ(1)
        self._visitaPreOrdine(p)                     # S(n)
        return                                       # Θ(1)

    # Computational Cost
    # Dimensioni input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA IN INORDINE'
    
    # function Privata recursive 
    def _visitaInOrdine(self,p):                     # S(n)
        if p!=None:                                  # Θ(1)
            'PASSI RICORSIVO 1 (SX)'
            self._visitaInOrdine(p.getLeft())        # S(k)
            'OPERAZIONE SUL NODO'
            print(str(p.getKey()),end=" ")           # Θ(1)
            'PASSI RICORSIVO 2 (DX)'
            self._visitaInOrdine(p.getRight())       # S(n-k-1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Pubblica Wrapper of lancio della function recursive
    def visitaInOrdine(self):                        # T(n)
        p=self.root                                  # Θ(1)
        self._visitaInOrdine(p)                      # S(n)

    # Computational Cost
    # Dimensioni input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA IN POSTORDINE'
    
    # function Privata recursive
    def _visitaPostOrdine(self,p):                   # S(n)
        if p!=None:                                  # Θ(1)
            'PASSI RICORSIVO 1 (SX)'
            self._visitaPostOrdine(p.getLeft())      # S(k)
            'PASSI RICORSIVO 2 (DX)'
            self._visitaPostOrdine(p.getRight())     # S(n-k-1)
            'OPERAZIONE SUL NODO'
            print(str(p.getKey()),end=" ")           # Θ(1)
        'CASO BASE'
        return                                       # Θ(1)

    # function Publica Wrapper of lancio della function recursive
    def visitaPostOrdine(self):                      # T(n)
        p=self.root                                  # Θ(1)
        self._visitaPostOrdine(p)                    # S(n)

    # Computational Cost
    # Dimensioni input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA PER LIVELLI'

    'Controllo Riempimento Coda'
    def _codaVuota(self,coda):                     # T(n)
        if coda.size()==0:                         # Θ(1)
            return True                            # Θ(1)
        return False                               # Θ(1)

    # Cost: T(n)=Θ(1)


    'Visita For Livelli'

    def visitaPerLivelli(self):                    # T(n)
        # Inizializzazione alla radice dell'albero
        p=self.root                                # Θ(1)
        # Controllo esistenza albero
        if p==None:                                # Θ(1)
            return                                 # Θ(1)
        # Inizializzazione coda of supporto
        coda=Coda()                                # Θ(1)                                                     
        # Incodamento radice albero nella coda
        coda.enqueue(p)                            # Θ(1)                           
        # Scorrimento nodi albero through coda
        while(not self._codaVuota(coda)):          # n*Θ(1)+Θ(1) 
            # 1. Scoda e prints nodo
            p=coda.dequeue()                       # Θ(1)
            print(str(p),end=" ")                  # Θ(1)         
            # Incoda Left
            if p.getLeft()!=None:                  # Θ(1)
                coda.enqueue(p.getLeft())          # Θ(1)
            # Incoda figlio Dx
            if p.getRight()!=None:                 # Θ(1)
                coda.enqueue(p.getRight())         # Θ(1)
        return                                     # Θ(1)
        
    # Computational Cost
    # Dimensioni input: number nodi dell'albero (incognito to priori)
    # Cost: T(n)=Θ(1)+Θ(n)+Θ(1)  -> T(n)=Θ(n) 

     

    'CONTEGGIO number NODI'
    
    # function Privata recursive
    def _calcola_n(self,p):                          # S(n)
        if p!=None:                                  # Θ(1)
            # 1. Recursive Step SottoAlbero Sx
            num_l=self._calcola_n(p.getLeft())       # S(k)
            # 2. Recursive Step SottoAlbero Dx
            num_r=self._calcola_n(p.getRight())      # S(n-k-1)
            # 3. Operazione sul Nodo
            num=num_l+num_r+1                        # Θ(1)     
            return num                               # Θ(1)  
        return 0                                     # Θ(1)  
    
    # function Pubblica Wrapper of lancio della function recursive
    def calcola_n(self):                             # T(n)
        p=self.root                                  # Θ(1)
        return self._calcola_n(p)                    # S(n)
    
    # Computational Cost
    # Dimensione Input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   
    


    'CALCOLO ALTEZZA'
    
    # function Privata recursive
    def _calcola_h(self,p):                                  # S(n)
        if p==None:                                          # Θ(1) 
            return -1                                        # Θ(1)
        if p.getLeft()==None and p.getRight()==None:         # Θ(1)
            return 0                                         # Θ(1)
        # 1. 2. Recursive Step SottoAlbero Sx e Dx
        h=max(self._calcola_h(p.getLeft()),                  # S(k)
              self._calcola_h(p.getRight()))                 # S(n-k-1)
        # 3. Operazione sul Nodo
        return h+1                                           # Θ(1)                       

    # function Pubblica Wrapper for the lancio della function recursive
    def calcola_h(self):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self._calcola_h(p)                            # S(n)

    # Computational Cost
    # Dimensione Input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)



    'CONTEGGIO NODI al LIVELLO K'
    
    # function Privata recursive
    def _conta_k(self,k,the,p):                                # S(n)
        if p==None:                                          # Θ(1)
            return 0                                         # Θ(1)
        if k==the:                                             # Θ(1)
            return 1                                         # Θ(1)
        # 1. Recursive Step SottoAlbero Sx
        k_left=self._conta_k(k,the+1,p.getLeft())              # S(k)
        # 2. Recursive Step SottoAlbero Dx
        k_right=self._conta_k(k,the+1,p.getRight())            # S(n-k-1)
        # 3. Operazione sul Nodo
        return k_left+k_right                                # Θ(1)

    # function Pubblica Wrapper for the lancio della function recursive
    def conta_k(self,k):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self._conta_k(k, 0, p)                        # S(n)

    # Computational Cost
    # Dimensione Input: number nodi dell'albero (incognito to priori)
    # Cost: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



    'RICERCA'
    
    # function Privata recursive
    def _cerca(self,p,k):                           # S(h)
        if (p==None or p.getKey()==k):              # Θ(1)
            return p                                # Θ(1)
        if (k<p.getKey()):                          # Θ(1)
            return self._cerca(p.getLeft(),k)       # S(h-1)
        else:                                       # Θ(1)
            return self._cerca(p.getRight(),k)      # S(h-1)
        
    # function Pubblica Wrapper for the lancio della function recursive
    def cerca(self,k):                              # T(h)
        p=self.getRoot()                            # Θ(1)
        return self._cerca(p,k)                     # Θ(h)
    
    # Computational Cost
    # Dimensione dell'input: Altezza h dell'albero
    # Si esegue the function h volte with operazioni each volta of costo costante
    # Θ(1). Quindi the costo totale equivale to h volte Θ(1).
    # Cost: T(h)= Θ(1)+Θ(h) -> T(h)=Θ(h)



    'INSERIMENTO'
    
    def inserisci(self,z):                           # T(h)
        '1. INIZIALIZZAZIONE Puntatori ausiliari'
        # Padre Nodo Corrente
        y=None                                       # Θ(1)
        # Nodo corrente
        p=self.getRoot()                             # Θ(1)
        x=p                                          # Θ(1)
        '2. DISCESA fino to Nodo with Figlio Nullo'
        while x!=None:                               # h*Θ(1)+Θ(1)
            # Aggiorna y eguagliandolo to x...
            y=x                                      # Θ(1)
            # Aggiorna x facendolo scendere to dx/sx in base alla sua key...
            if z.getKey()<x.getKey():                # Θ(1)
                x=x.getLeft()                        # Θ(1)
            else:                                    # Θ(1)
                x=x.getRight()                       # Θ(1)
        '3. AGGIUNTA Nuovo Nodo'
        # If l'Albero e' Nullo, usa Nuovo Nodo as Radice dell'Albero...
        if y==None:                                  # Θ(1)
            p=z                                      # Θ(1)
        # If l'Albero not e' nullo, aggiungi the Nuovo Nodo to dx/sx dell'last...
        else:                                        # Θ(1)
            if z.getKey()<y.getKey():                # Θ(1)
                y.left=z                             # Θ(1)
            else:                                    # Θ(1)
                y.right=z                            # Θ(1)
        # Aggiorna the campo Padre del nuovo nodo aggiunto all'albero...
        z.setParent(y)                               # Θ(1)
        # Restituisci l'albero modificato...
        return p                                     # Θ(1)
    
    # Computational Cost
    # Dimensione dell'input: Altezza h dell'albero
    # Cost: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)



    'MINIMO'
    
    # RICORSIVO
    
    # function Privata recursive
    def _minimoRecurs(self,p):                       # S(h)
        'Controllo Input'
        if p==None:                                  # Θ(1)
            return                                   # Θ(1)
        'CASO BASE'
        if p.getLeft()==None:                        # Θ(1)
            return p                                 # Θ(1)
        'PASSO RICORSIVO'
        return self._minimoRecurs(p.getLeft())       # S(h-1)
    
    # function Pubblica Wrapper for the lancio della function recursive
    def minimoRecurs(self):                          # T(h)
        'Inizializzazione Nodo of partenza'
        p=self.getRoot()                             # Θ(1)
        'Chiamata to function recursive privata'
        return self._minimoRecurs(p)                 # S(h)
    
    # Computational Cost
    # Input size: altezza dell'albero h
    # Cost: T(h)=Θ(1)+S(h)=Θ(1)+Θ(h) -> T(h)=Θ(h)
    
    
    # ITERATIVO
    
    # function Privata recursive
    def _minimoIter(self,p):                         # S(h)
        'Controllo Input'
        if p==None:                                  # Θ(1)
            return                                   # Θ(1)
        'ITERAZIONE'
        while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
            p=p.getLeft()                            # Θ(1)
        return p                                     # Θ(1)
    
    # function Pubblica Wrapper for the lancio della function recursive
    def minimoIter(self):                            # T(h)
        'Inizializzazione Nodo of partenza'
        p=self.getRoot()                             # Θ(1)                            
        'Chiamata to function iterative privata'
        return self._minimoIter(p)                   # Θ(h)
    
    # Computational Cost
    # Input size: altezza dell'albero h
    # Cost: T(h)=Θ(1)+S(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)
    
    
    
    'MASSIMO'
    
    # RICORSIVO
    
    # function Privata recursive
    def _massimoRecurs(self,p):                       # S(h)
        'Controllo Input'
        if p==None:                                   # Θ(1)
            return                                    # Θ(1)
        'CASO BASE'
        if p.getRight()==None:                        # Θ(1)
            return p                                  # Θ(1)
        'PASSO RICORSIVO'
        return self._massimoRecurs(p.getRight())      # S(h-1)
    
    # function Pubblica Wrapper for the lancio della function recursive
    def massimoRecurs(self):                          # T(h)
        'Inizializzazione Nodo of partenza'
        p=self.getRoot()                              # Θ(1) 
        'Chiamata to function recursive privata'
        return self._massimoRecurs(p)                 # Θ(h) 
    
    # Computational Cost
    # Input size: altezza dell'albero h
    # Cost: T(h)=Θ(1)+S(h)=Θ(1)+Θ(h) -> T(h)=Θ(h)
    
    
    # ITERATIVO
    
    # function Privata recursive
    def _massimoIter(self,p):                         # T(h)
        'Controllo Input'
        if p==None:                                   # Θ(1)
            return                                    # Θ(1)
        'ITERAZIONE'
        while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
            p=p.getRight()                            # Θ(1)
        return p                                      # Θ(1)
    
    # function Pubblica Wrapper for the lancio della function recursive
    def massimoIter(self):                            # T(h)
        'Inizializzazione Nodo of partenza'
        p=self.getRoot()                              # Θ(1)
        'Chiamata to function iterative privata'
        return self._massimoIter(p)                   # Θ(h) 
    
    # Computational Cost
    # Input size: altezza dell'albero h
    # Cost: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



    'PREDECESSORE'

    # ITERATIVO
    
    def predecessoreIter(self,k):                     # T(h)
        # 1. Ricava the nodo avente key uguale to k
        nodo=self.cerca(k)                            # Θ(h)
        # 2. If the nodo not esiste, restituisci value nullo
        if nodo==None:                                # Θ(1)
            return None                               # Θ(1)
        # 3. If the nodo ha figlio Sx cerca the massimo nel
        #    suo sottoalbero Sx
        if nodo.getLeft()!=None:                      # Θ(1)
            predecessor=self._massimoIter(nodo.getLeft())   # Ω(1) o O(h)
        else:                                         # Θ(1)
        # 4. If the nodo NON ha figlio Sx, risali l'albero     
        #    through ITERAZIONE    
            while(nodo.getParent()!=None and 
                  nodo==nodo.getParent().getLeft()):  # Θ(1)
                nodo=nodo.getParent()                 # Θ(1)
            predecessor=nodo.getParent()              # Θ(1)
        return predecessor                            # Θ(1)
    
    # RICORSIVO
    
    # function Privata recursive
    def _predecRecurs(self,nodo):                     # S(h)
        # 1. If the nodo not ha padre, esso e' the radice dell'albero...
        #    quindi ritorna the radice.
        if nodo.getParent()==None:                    # Θ(1)
            return nodo                               # Θ(1)
        # 2. If the nodo not coincide with the figlio Sx of suo padre,
        #    restituisci the nodo...
        if nodo!=nodo.getParent().getLeft():          # Θ(1)
            return nodo.getParent()                   # Θ(1)
        # 3. If the nodo coincide with the figlio Sx of suo padre, 
        #    continua the risalita passando the nodo padre nella nuova 
        #    chiamata ricorsiva.
        return self._predecRecurs(nodo.getParent())   # S(h-1)   
    
    # function Pubblica Wrapper for the lancio della function recursive
    def predecessoreRecurs(self,k):                   # T(h)
        # 1. Ricava the nodo avente key uguale to k    
        nodo=self.cerca(k)                            # Θ(h)
        # 2. If the nodo not esiste, restituisci value nullo
        if nodo==None:                                # Θ(1)
            return None                               # Θ(1)
        # 3. If the nodo ha figlio Sx cerca the massimo nel
        #    suo sottoalbero Sx
        if nodo.getLeft()!=None:                      # Θ(1)
            predecessor=self._massimoRecurs(nodo.getLeft()) # Ω(1) o O(h)     
        else:                                         # Θ(1)
        # 4. If the nodo NON ha figlio Sx, risali l'albero
        #    through RICORSIONE
            return self._predecRecurs(nodo)           # S(h)
        return predecessor                            # Θ(1)
    
    # Computational Cost
    # Input size: altezza dell'albero h
    # Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
    # Costo Ricorsiva: T(h)=Θ(h) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  
    
    
    
    'SUCCESSORE'

    # ITERATIVO
    
    def successoreIter(self, k):                       # T(h)
        # 1. Ricava the nodo avente key uguale to k
        nodo=self.cerca(k)                             # Θ(h)
        # 2. If the nodo not esiste, restituisci value nullo
        if nodo==None:                                 # Θ(1)
            return None                                # Θ(1)
        # 3. If the nodo ha figlio Dx cerca the minimo nel
        #    suo sottoalbero Dx
        if nodo.getRight()!=None:                      # Θ(1)
            successor=self._minimoIter(nodo.getRight()) # Ω(1) o O(h)
        else:        
        # 4. If the nodo NON ha figlio Dx, risali l'albero     
        #    through ITERAZIONE
            while(nodo.getParent()!=None and 
                  nodo==nodo.getParent().getRight()):  # Θ(1)
                nodo=nodo.getParent()                  # Θ(1)
            successor=nodo.getParent()                 # Θ(1)
        return successor                               # Θ(1)
    
    # RICORSIVO
    
    # function Privata recursive
    def _succesRecurs(self,nodo):                      # S(h)
        # 1. If the nodo not ha padre, esso e' the radice dell'albero...
        #    quindi ritorna the radice.
        if nodo.getParent()==None:                     # Θ(1)
            return nodo                                # Θ(1) 
        # 2. If the nodo not coincide with the figlio Dx of suo padre,
        #    restituisci the nodo...
        if nodo!=nodo.getParent().getRight():          # Θ(1)
            return nodo.getParent()                    # Θ(1)
        # 3. If the nodo coincide with the figlio Dx of suo padre, 
        #    continua the risalita passando the nodo padre nella nuova 
        #    chiamata ricorsiva.
        return self._succesRecurs(nodo.getParent())    # S(h-1)   
    
    # function Pubblica Wrapper for the lancio della function recursive
    def successoreRecurs(self,k):                      # T(h)
        # 1. Ricava the nodo avente key uguale to k    
        nodo=self.cerca(k)                             # Θ(h)
        # 2. If the nodo not esiste, restituisci value nullo
        if nodo==None:                                 # Θ(1)
            return None                                # Θ(1)
        # 3. If the nodo ha figlio Dx cerca the massimo nel
        #    suo sottoalbero Dx
        if nodo.getRight()!=None:                      # Θ(1)
            successor=self._minimoRecurs(nodo.getRight()) # Ω(1) o O(h)
        else:                                          # Θ(1)
        # 4. If the nodo NON ha figlio Dx, risali l'albero
        #    through RICORSIONE
            return self._succesRecurs(nodo)            # S(h)
        return successor                               # Θ(1)

    # Computational Cost
    # Input size: altezza dell'albero h
    # Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) ->T(h)=Ω(1) o O(h)  
    # Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) ->T(h)=Ω(1) o O(h) 
    
    
    
    'CANCELLAZIONE'

    # function Ausiliaria for the cancellazione of a singola foglia
    def cancellaFoglia(self,p,nodo):                                 # T(h)
        # Aggiorna the campo figlio (Dx/Sx) del padre 
        # corrispondente alla foglia from cancellare.
        if (nodo==nodo.getParent().getLeft()):                       # Θ(1)
            nodo.getParent().setLeft(None)                           # Θ(1)
        else:                                                        # Θ(1)
            nodo.getParent().setRight(None)                          # Θ(1)
        return                                                       # Θ(1)
    


    def cancella(self,k):                                            # T(h)
        # Estrai nodo avente value key uguale to k
        nodo=self.cerca(k)                                    # Ω(1) o O(h)
        # If the nodo not esiste chiudi the function
        if nodo==None:                                               # Θ(1)
            return                                                   # Θ(1)
        # CASO 1 - The Nodo NON HA FIGLI
        # Cancella the nodo aggiornando the corrispondente campo figlio
        # del nodo padre.
        if (nodo.getLeft()==None and nodo.getRight()==None):         # Θ(1)
           self.cancellaFoglia(self.getRoot(),nodo)                  # Θ(1)
        # CASO 2 - The Nodo HA 1 FIGLIO
        # Cortocircuita the padre with the figlio del nodo from eliminare
        # If l'unico figlio e' that Sx...
        if (nodo.getLeft()!=None and nodo.getRight()==None):         # Θ(1)
            # Assegna the padre del nodo al figlio Sx
            nodo.getLeft().setParent(nodo.getParent())               # Θ(1)
            # Assegna the figlio Sx al padre del nodo
            if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
                nodo.getParent().setLeft(nodo.getLeft())             # Θ(1)
            else:                                                    # Θ(1)
                nodo.getParent().setRight(nodo.getLeft())            # Θ(1)
        # If l'unico figlio e' that Dx...
        if (nodo.getLeft()==None and nodo.getRight()!=None):         # Θ(1)
            # Assegna the padre del nodo al figlio Dx
            nodo.getRight().setParent(nodo.getParent())              # Θ(1)
            # Assegna the figlio Dx al padre del nodo
            if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
                nodo.getParent().setLeft(nodo.getRight())            # Θ(1)
            else:                                                    # Θ(1)
                nodo.getParent().setRight(nodo.getRight())           # Θ(1)
        
        # CASO 3 - The Nodo HA 2 FIGLI
        # Trova the predecessore/successore del nodo from cancellare, 
        # copia the suo contained in the nodo from cancellare e, infine, 
        # cancella the nodo predecessore/successore.
        if (nodo.getLeft()!=None and nodo.getRight()!=None):         # Θ(1)
            # Ricava the nodi predecessore e successore
            pred=self.predecessoreIter(nodo.getKey())       # Ω(1) o O(h) 
            succes=self.successoreRecurs(nodo.getKey())     # Ω(1) o O(h) 
            # Sostituisci key del nodo e cancella 
            # predecessore/successore
            if pred!=None:                                           # Θ(1)
                nodo.setKey(pred.getKey())                           # Θ(1)
                self.cancellaFoglia(self.getRoot(),pred)             # Θ(1)
            else:                                                    # Θ(1)
                nodo.setKey(succes.getKey())                         # Θ(1)
                self.cancellaFoglia(self.getRoot(),succes)           # Θ(1)

        # Computational Cost
        # Input size: altezza dell'albero h
        # Iterative cost: T_case1(h)=O(h)+Θ(1)=O(h)
        #                  T_case2(h)=O(h)+Θ(1)=O(h)
        #                  T_case3(h)=O(h)+O(h)+Θ(1)=O(h)
        # Cost: T(h)=max{T_case1;T_case2;T_case3}=O(h)


'''

'TEST'

# 1. CREAZIONE ALBERO PER I TEST

valoriNodi=[18,11,33,7,15,22,80,13,16,50,91,42,64]
indiciPadri=[None,0,0,1,1,2,2,4,4,6,6,9,9]
nodi=[]
vettorePosizionale=[]

for the in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[the])) 
    
for the in range(0,len(nodi),1):
    if indiciPadri[the]==None:
        nodi[the].setParent(None)
    else:
        nodi[the].setParent(nodi[indiciPadri[the]])
    k=0
    for j in range(0,len(indiciPadri),1):
        if indiciPadri[j]==the:
            if k==0:
                nodi[the].setLeft(nodi[j])
                k+=1
            else:
                nodi[the].setRight(nodi[j])
                break
         
radice=nodi[0]
albero=AlberoBinarioDiRicerca(radice)


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

'Visita For Livelli'
print("\nVisita for Livelli:")
albero.visitaPerLivelli()

'Conteggio number nodi'
print("\nConteggio number Nodi: " + str(albero.calcola_n()))

'Calcolo Altezza'
print("Calcolo Altezza dell'albero: " + str(albero.calcola_h()))

'Conteggio Nodi al Livello k'
print("Conteggio number nodi al livello 2: " + str(albero.conta_k(2)))

'Ricerca'
nodoRicercato=albero.cerca(22)
print("\nRICERCA\nIl nodo ricercato e' : " + str(nodoRicercato))

'Inserimento'
z=Nodo(47)
print("\nINSERIMENTO\nAlbero first dell'inserimento del nodo " + str(z))
albero.visitaPerLivelli()
albero.inserisci(z)
print("\nAlbero dopo l'inserimento del nodo " + str(z))
albero.visitaPerLivelli()
print()

'Minimo'
minRec=albero.minimoRecurs()
minIter=albero.minimoIter()
print("\nMINIMO\nChiave minima nell'albero [RICORSIONE]: " + str(minRec))
print("Chiave minima nell'albero [ITERAZIONE]: " + str(minIter))

'Massimo'
maxRec=albero.massimoRecurs()
maxIter=albero.massimoIter()
print("\nMASSIMO\nChiave massima nell'albero [RICORSIONE]: " + str(maxRec))
print("Chiave massima nell'albero [ITERAZIONE]: " + str(maxIter))

'Predecessore'
k1=80
k2=13
predIter1=albero.predecessoreIter(k1)      # iterative -Case 1- Discesa
predIter2=albero.predecessoreIter(k2)      # iterative -Case 2- Risalita
predRec1=albero.predecessoreRecurs(k1)     # recursive -Case 1- Discesa
predRec2=albero.predecessoreRecurs(k2)     # recursive -Case 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))

'Successore'
k1=11
k2=16
succIter1=albero.successoreIter(k1)     # iterative -Case 1- Discesa
succIter2=albero.successoreIter(k2)     # iterative -Case 2- Risalita
succRec1=albero.successoreRecurs(k1)    # recursive -Case 1- Discesa
succRec2=albero.successoreRecurs(k2)    # recursive -Case 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))

'Cancellazione'
k_case1=7
k_case3=33
print("\nDELETION - Case 1 - key " + str(k_case1) + "\nBefore...")
albero.visitaPerLivelli()
print("\nAfter...")
albero.cancella(k_case1)
albero.visitaPerLivelli()
print("\n\nDELETION - Case 3 - key " + str(k_case3) + "\nBefore...")
albero.visitaPerLivelli()
print("\nAfter...")
albero.cancella(k_case3)
albero.visitaPerLivelli()

'''
