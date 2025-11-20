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
'Nodo with 3 puntatori: Padre (parent), FiglioSx (left) e FiglioDx (right) e '
'e 2 campi: Chiave (key) e Colore (color).'
from RedBlackNode import Nodo
'Colore Enumeration'
from Color import Colore
'Coda Modificata for ospitare the nodi dellalbero nel campo value dei'
'suoi record singoli.'
from Modified_Queue import Coda

'''
CLASSE ALBERO BINARIO DI RICERCA ROSSONERO (TREE)

Costruita servendosi of Record e Puntatori
Since ciascun nodo e' rappresentato in memoria through a record,
ciascun nodo dell'albero e' sparso nella memoria del computer e puo' essere 
acceduto through the puntatori destro, sinistro e padre of ciascun nodo to partire
dalla radice dell'albero.'
The classe albero, quindi deve only contenere the record della radice.

A Albero RossoNero e' a sottotipo specifico of Binary Search Tree that,
for consentire the riaggiustamento della sua struttura to seguito of a'
operazione of modifica (e.g. Inserimento e Cancellazione), si serve of a campo
aggiuntivo of nome "Colore" assegnato ai suoi nodi.
This campo puo' assumere only two values: Rosso o Nero.'
'''


class AlberoRossoNero:
    
    
    # ATTRIBUTES
    root=None
    
    
    # CONSTRUCTOR
    'Default e Overloaded'
    def __init__(self,root=None):
        self.root=root
        
        
    # METHODS
    
    'GET ROOT'
    def getRoot(self):                               # T(n)
        return self.root                             # Θ(1)  
    
    # Computational Cost: T(n)=Θ(1)
    
    
    'SET ROOT'
    def setRoot(self,root):                          # T(n)
        self.root=root                               # Θ(1) 

    # Computational Cost: T(n)=Θ(1)
    

    'VISITA IN PREORDINE'
    
    # function Privata recursive    
    def _visitaPreOrdine(self,p):                    # S(n)
        if p!=None:                                  # Θ(1)
            'OPERAZIONE SUL NODO'
            print(str(p.getKey())+"_"+               # Θ(1)
                  str(p.getColor()).split('.')[1][0],end=" ")
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
            print(str(p.getKey())+"_"+               # Θ(1)
                  str(p.getColor()).split('.')[1][0],end=" ")
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
            print(str(p.getKey())+"_"+               # Θ(1)
                  str(p.getColor()).split('.')[1][0],end=" ")
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
        # Verifica specifica for Alberi RossoNeri 
        # value key foglie fittizie
        if (p.getKey()==None):                      # Θ(1)
            return None                             # Θ(1)
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



    'MINIMO'
    
    # RICORSIVO
    
    # function Privata recursive
    def _minimoRecurs(self,p):                       # S(h)
        'Controllo Input'
        if p==None:                                  # Θ(1)
            return                                   # Θ(1)
        'CASO BASE'
        if p.getLeft().getKey()==None:               # Θ(1)
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
        while p.getLeft().getKey()!=None:            # h*Θ(1)+Θ(1)
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
        if p.getRight().getKey()==None:               # Θ(1)
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
        while p.getRight().getKey()!=None:            # h*Θ(1)+Θ(1)
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
        if nodo.getLeft().getKey()!=None:             # Θ(1)
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
        if nodo.getLeft().getKey()!=None:             # Θ(1)
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
        if nodo.getRight().getKey()!=None:              # Θ(1)
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
        if nodo.getRight().getKey()!=None:             # Θ(1)
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
    
    
    
    'ROTAZIONI'
    
    # Rotazione SX
    def rotazioneSx(self,pivot):                        # T(n)
        'INIZIALIZZAZIONE NODI DI RIFERIMENTO'
        # 1.1 Estrai radice dell'albero
        p=self.getRoot()                                # Θ(1)
        # 1.2 Inizializza the puntatori ausiliari
        to=pivot                                         # Θ(1)
        b=to.getRight()                                  # Θ(1)
        'SCAMBIO FIGLIO β DA B AD To'
        # 2.1 Transfer figlio Sx of b (β) to figlio Dx of "to"
        to.setRight(b.getLeft())                         # Θ(1)
        # 2.2 Aggiornamento campo parent del nodo β (from "b" ad "to")
        if to.getRight()!=None:                          # Θ(1)
            to.getRight().setParent(to)                   # Θ(1)
        'SCAMBIO NODI To E B'
        # 3.1 Aggiornamento figlio Sx of b (from β ad "to")
        b.setLeft(to)                                    # Θ(1)
        # 3.2 Aggiornamento padre of b (from "to" to padre of "to")
        b.setParent(to.getParent())                      # Θ(1)
        # 3.3 If to e' the radice dell'albero (padre nullo) aggiorna
        #     the radice dell'albero assegnandogli "b"
        if to.getParent()==None:                         # Θ(1)
            self.root=b                                 # Θ(1)
        # ... If "to" e' the figlio Sx of suo padre, aggiorna the campo
        #     figlio Sx del padre with the nodo "b"
        elif to==to.getParent().getLeft():                # Θ(1)
            to.getParent().setLeft(b)                    # Θ(1)
        # ... Altrimenti aggiorna with "b" the campo figlio Dx del padre of "to"
        else:                                           # Θ(1)
            to.getParent().setRight(b)                   # Θ(1)
        # 3.4 Assegna "b" al campo parent of "to"
        to.setParent(b)                                  # Θ(1)

        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: T(h)=Θ(1)
        
    # Rotazione DX
    def rotazioneDx(self,pivot):                        # T(n)
        'INIZIALIZZAZIONE NODI DI RIFERIMENTO'
        # 1.1 Estrai radice dell'albero
        p=self.getRoot()                                # Θ(1)
        # 1.2 Inizializza the puntatori ausiliari
        to=pivot                                         # Θ(1)
        b=to.getLeft()                                   # Θ(1)
        'SCAMBIO FIGLIO β DA B AD To'
        # 2.1 Transfer figlio Sx of b (β) to figlio Dx of "to"
        to.setLeft(b.getRight())                         # Θ(1)
        # 2.2 Aggiornamento campo parent del nodo β (from "b" ad "to")
        if to.getLeft()!=None:                           # Θ(1)
            to.getLeft().setParent(to)                    # Θ(1)
        'SCAMBIO NODI To E B'
        # 3.1 Aggiornamento figlio Dx of b (from β ad "to")
        b.setRight(to)                                   # Θ(1)
        # 3.2 Aggiornamento padre of b (from "to" to padre of "to")
        b.setParent(to.getParent())                      # Θ(1)
        # 3.3 If to e' the radice dell'albero (padre nullo) aggiorna
        #     the radice dell'albero assegnandogli "b"
        if to.getParent()==None:                         # Θ(1)
            self.root=b                                 # Θ(1)
        # ... If "to" e' the figlio Sx of suo padre, aggiorna the campo
        #     figlio Sx del padre with the nodo "b"
        elif to==to.getParent().getLeft():                # Θ(1)
            to.getParent().setLeft(b)                    # Θ(1)
        # ... Altrimenti aggiorna with "b" the campo figlio Dx del padre of "to"
        else:                                           # Θ(1)
            to.getParent().setRight(b)                   # Θ(1)
        # 3.4 Assegna "b" al campo parent of "to"
        to.setParent(b)                                  # Θ(1)
        
        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: T(h)=Θ(1)
    
    
    'INSERIMENTO'
    
    # PASSO PRELIMINARE
    'function Ausiliaria'
    
    def _passoPreliminare(self,z):                      # T(h)
        '1. INIZIALIZZAZIONE Puntatori ausiliari'
        # Padre Nodo Corrente
        y=None                                          # Θ(1)
        # Nodo corrente
        p=self.getRoot()                                # Θ(1)
        x=p                                             # Θ(1)
        '2. DISCESA fino to Nodo with Figlio Nullo'
        while x.getKey()!=None:                         # h*Θ(1)+Θ(1)
            # Aggiorna y eguagliandolo to x...
            y=x                                         # Θ(1)
            # Aggiorna x facendolo scendere to dx/sx in base alla sua key..
            if z.getKey()<x.getKey():                   # Θ(1)
                x=x.getLeft()                           # Θ(1)
            else:                                       # Θ(1)
                x=x.getRight()                          # Θ(1)
        '3. AGGIUNTA Nuovo Nodo'
        # If l'Albero e' Nullo, usa Nuovo Nodo as Radice dell'Albero...
        if y==None:                                     # Θ(1)
            p=z                                         # Θ(1)
        # If l'Albero not e' nullo, aggiungi the Nuovo Nodo to dx/sx dell'last...
        else:                                           # Θ(1)
            if z.getKey()<y.getKey():                   # Θ(1)
                y.left=z                                # Θ(1)
            else:                                       # Θ(1)
                y.right=z                               # Θ(1)
        # Aggiorna the campo Padre del nuovo nodo aggiunto all'albero...
        z.setParent(y)                                  # Θ(1)
        '4. AGGIUNTA Figli Fittizi'
        # Si aggiungono two foglie fittizie nere as figli del nodo inserito..
        z.setLeft(Nodo(None,Colore.NERO))               # Θ(1)               
        z.getLeft().setParent(z)                        # Θ(1)
        z.setRight(Nodo(None,Colore.NERO))              # Θ(1)
        z.getRight().setParent(z)                       # Θ(1)
        '5. RITORNA the nodo inserito'
        # Ritorna the nodo inserito 
        return z                                        # Θ(1)

        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: T(h)=Θ(h)+Θ(1)=Θ(h)


    # PASSO DI AGGIUSTAMENTO
    'function Ausiliaria'
    
    # function Privata recursive
    def __passoDiAggiustamento(self,p,z):                        # S(h)
    
        '** CASO BASE **'
        # If the nodo coincide with the radice dell'albero, basta cambiare
        # the suo colore from ROSSO to NERO e l'aggiustamento dell'albero e'
        # finalmente concluso.
        # This implica also that l'albero avra' adesso a b-altezza
        # of a'unita' superiore rispetto to that that aveva first dell'
        # inserimento.
        if z==p:                                                 # Θ(1)                                    
            'CASO 0'
            # If the nodo inserito e' the radice, cambia the 
            # colore from ROSSO to NERO.
            p.setColor(Colore.NERO)                              # Θ(1)
            return  

        '** CASI SPECIFICI **'
        # If the nodo NON coincide with the radice dell'albero, the manovre of 
        # aggiustamento dell'albero saranno necessarie only if esso viola
        # the regola for cui each nodo ROSSO puo' avere only figli NERI.
        # Quindi si procede with the seguenti operazioni of aggiustamento 
        # SOLO SE IL NODO E' ROSSO E SUO PADRE E' ANCH'ESSO ROSSO!
        if z.getColor()==Colore.ROSSO and \
            z.getParent().getColor()==Colore.ROSSO:              # Θ(1)                   
            
            'PREPARATIVI'
            'Estrazione Nodi PADRE, ZIO e NONNO del nodo inserito'
            # Nodo PADRE
            parent=z.getParent()                                 # Θ(1)
            # Nodo NONNO
            grandParent=parent.getParent()                       # Θ(1)
            # Nodo ZIO
            uncle=Nodo()                                         # Θ(1)
            if grandParent!=None:                                # Θ(1)
                if parent==grandParent.getLeft():                # Θ(1)
                    uncle=grandParent.getRight()                 # Θ(1)
                else:                                            # Θ(1)
                    uncle=grandParent.getLeft()                  # Θ(1)      
            
            'CASI DI AGGIUSTAMENTO'
            # CASO 1 #####################################################
            if  uncle.getColor()==Colore.ROSSO:                  # Θ(1)
                    # If the nodo inserito ha zio ROSSO e padre ROSSO,   
                    # cambia the colori dei seguenti nodi nel modo seguente:
                    #   - Padre e Zio -> Colore NERO
                    #   - Nonno       -> Colore ROSSO
                    parent.setColor(Colore.NERO)                 # Θ(1)
                    uncle.setColor(Colore.NERO)                  # Θ(1)
                    grandParent.setColor(Colore.ROSSO)           # Θ(1)
                    # ...e vai to controllare that the violazione dell'albero
                    # RossoNero not si sia spostata sul nodo NONNO.
                    # In that case, esegui l'aggiustamento on of esso 
                    # applicando ricorsivamente the Case 1,2 or 3.
                    '** PASSO RICORSIVO **'
                    self.__passoDiAggiustamento(p,grandParent)   # S(h-1)
            
            # CASO 2 #####################################################
            elif uncle.getColor()==Colore.NERO and \
                z==parent.getRight():                            # Θ(1)
                    # If the nodo inserito ha zio NERO ed e' figlio DX
                    # of a nodo ROSSO, si effettuano the seguenti operazioni:
                    #   1. Rotazione SX with PERNO SUL PADRE del nodo inserito
                    #   2. Aggiustamento on Nodo Padre (sappiamo for certo
                    #      from teoria that the padre violera' l'albero RossoNero
                    #      second the Case 3 e that this portera' alla 
                    #      risoluzione definitiva della violazione)
                    self.rotazioneSx(parent)                     # Θ(1)
                    '** PASSO RICORSIVO **'
                    self.__passoDiAggiustamento(p,parent)        # S(h-1)
            
            # CASO 3 #####################################################
            elif uncle.getColor()==Colore.NERO and \
                z==parent.getLeft():                             # Θ(1)
                    # If the nodo inserito ha zio NERO ed e' figlio SX of
                    # a nodo ROSSO, si effettuano the seguenti operazioni:
                    #   1. Cambiamento Colori as of seguito:
                    #       - Padre -> Colore NERO
                    #       - Nonno -> Colore ROSSO
                    #   2. Rotazione with PERNO SUL PADRE del nodo inserito
                    # Nessun bisogno of effettuare ulteriori aggiustamenti
                    # sui livelli piu' alti dell'albero. As from teoria,
                    # indeed, the Case 3 risolve always the violazione.
                    parent.setColor(Colore.NERO)                 # Θ(1)
                    grandParent.setColor(Colore.ROSSO)           # Θ(1)
                    self.rotazioneDx(grandParent)                # Θ(1)
        return
            
        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: S(h)=Θ(1)+S(h-1)=Ω(1) o O(h)=O(logn)      
        
    
    # function Pubblica Wrapper for the lancio della function privata ricors
    def _passoDiAggiustamento(self,z):               # T(h)
        # Estrai Radice dell'Albero RossoNero
        p=self.getRoot()                             # Θ(1)
        # Chiama function Privata recursive
        self.__passoDiAggiustamento(p,z)             # S(h)
    
        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: T(h)=O(h)=O(logn)     
    
     # INSERIMENTO
    'function Principale'
    def inserisci(self,z):                           # T(h)
        zz=self._passoPreliminare(z)                 # Θ(h)
        self._passoDiAggiustamento(zz)               # O(h) 
    
        # Computational Cost
        # Input size: altezza dell'albero h
        # Computational Cost: T(h)=O(h)=O(logn)           
  
    
  
    'DELETION ----- WIP ----- '
    
    '''
    # function Ausiliaria for the cancellazione of a singola foglia
    def cancellaFoglia(self,p,nodo):                                 # T(h)
        # Aggiorna the campo figlio (Dx/Sx) del padre 
        # corrispondente alla foglia from cancellare.
        if (nodo==nodo.getParent().getLeft()):                       # Θ(1)
            nodo.getParent().setLeft(None)                           # Θ(1)
        else:                                                        # Θ(1)
            nodo.getParent().setRight(None)                          # Θ(1)
        return                                                       # Θ(1)
    
    # function Principale for the cancellazione del nodo of key =k
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

numTest=1

# 1. CREAZIONE ALBERO BINARIO DI RICERCA ROSSONERO PER I TEST

r=Colore.ROSSO
n=Colore.NERO

match numTest:
    case 1:
        valoriNodi=[11,2,14,1,7,None,15,None,None,5,8,None,None,None,
                    None,None,None]
        coloriNodi=[n,r,n,n,n,n,r,n,n,r,r,n,n,n,n,n,n]
        indiciPadri=[None,0,0,1,1,2,2,3,3,4,4,6,6,9,9,10,10]
        keyNodoAggiuntivo=4
    case 2:
        valoriNodi=[18,11,33,7,15,22,80,None,None,13,16,None,None,50,
                    91,None,None,None,None,None,None,None,None]
        coloriNodi=[n,r,r,n,n,n,n,n,n,r,r,n,n,r,r,n,n,n,n,n,n,n,n]
        indiciPadri=[None,0,0,1,1,2,2,3,3,4,4,5,5,6,6,9,9,10,10,13,13,14,14]
        keyNodoAggiuntivo=47
        
nodi=[]
vettorePosizionale=[]

for the in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[the],coloriNodi[the])) 
    
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
albero=AlberoRossoNero(radice)


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
print("Conteggio number nodi al livello 4: " + str(albero.conta_k(4)))

'Ricerca'
nodoRicercato=albero.cerca(22)
print("\nRICERCA\nIl nodo ricercato e' : " + str(nodoRicercato))

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


'Inserimento'
z=Nodo(keyNodoAggiuntivo,Colore.ROSSO)
print("\nINSERIMENTO\nAlbero first dell'inserimento del nodo " + str(z))
albero.visitaPerLivelli()
albero.inserisci(z)
print("\nAlbero dopo l'inserimento del nodo " + str(z))
albero.visitaPerLivelli()
print()

'''

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