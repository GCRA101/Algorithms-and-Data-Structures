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


# IMPORT CLASSI DEL PACKAGE
'Nodo con 3 puntatori: Padre (parent), FiglioSx (left) e FiglioDx (right)'
from BinarySearchNode import Nodo
'Coda Modificata per ospitare i nodi dellalbero nel campo valore dei'
'suoi record singoli.'
from Modified_Queue import Coda

'''
CLASSE ALBERO (TREE)
Costruita servendosi di Record e Puntatori
Dato che ciascun nodo e' rappresentato in memoria tramite un record,
ciascun nodo dell'albero e' sparso nella memoria del computer e puo' essere 
acceduto tramite i puntatori destro, sinistro e padre di ciascun nodo a partire
dalla radice dell'albero.'
La classe albero, quindi deve solo contenere il record della radice.
'''


class AlberoBinarioDiRicerca:
    
    
    # ATTRIBUTI
    root=None
    
    
    # COSTRUTTORE
    'Default e Overloaded'
    def __init__(self,root=None):
        self.root=root
        
        
    # METODI
    
    'GET ROOT'
    def getRoot(self):                                  # T(n)
        return self.root                                # Θ(1)  
    
    # Costo Computazionale: T(n)=Θ(1)



    'VISITA IN PREORDINE'
    
    # Funzione Privata Ricorsiva    
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

    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def visitaPreOrdine(self):                       # T(n)
        p=self.root                                  # Θ(1)
        self._visitaPreOrdine(p)                     # S(n)
        return                                       # Θ(1)

    # Costo Computazionale
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA IN INORDINE'
    
    # Funzione Privata Ricorsiva 
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

    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def visitaInOrdine(self):                        # T(n)
        p=self.root                                  # Θ(1)
        self._visitaInOrdine(p)                      # S(n)

    # Costo Computazionale
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA IN POSTORDINE'
    
    # Funzione Privata Ricorsiva
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

    # Funzione Publica Wrapper di lancio della Funzione Ricorsiva
    def visitaPostOrdine(self):                      # T(n)
        p=self.root                                  # Θ(1)
        self._visitaPostOrdine(p)                    # S(n)

    # Costo Computazionale
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1)  -> S(n)=Θ(n) [METODO DI SOSTITUZIONE]
    #        T(n)=Θ(1)+S(n)=Θ(1)+Θ(n) -> T(n)=Θ(n)



    'VISITA PER LIVELLI'

    'Controllo Riempimento Coda'
    def _codaVuota(self,coda):                     # T(n)
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
        while(not self._codaVuota(coda)):          # n*Θ(1)+Θ(1) 
            # 1. Scoda e stampa nodo
            p=coda.dequeue()                       # Θ(1)
            print(str(p),end=" ")                  # Θ(1)         
            # Incoda Left
            if p.getLeft()!=None:                  # Θ(1)
                coda.enqueue(p.getLeft())          # Θ(1)
            # Incoda figlio Dx
            if p.getRight()!=None:                 # Θ(1)
                coda.enqueue(p.getRight())         # Θ(1)
        return                                     # Θ(1)
        
    # Costo Computazionale
    # Dimensioni input: numero nodi dell'albero (incognito a priori)
    # Costo: T(n)=Θ(1)+Θ(n)+Θ(1)  -> T(n)=Θ(n) 

     

    'CONTEGGIO NUMERO NODI'
    
    # Funzione Privata Ricorsiva
    def _calcola_n(self,p):                          # S(n)
        if p!=None:                                  # Θ(1)
            # 1. Passo Ricorsivo SottoAlbero Sx
            num_l=self._calcola_n(p.getLeft())       # S(k)
            # 2. Passo Ricorsivo SottoAlbero Dx
            num_r=self._calcola_n(p.getRight())      # S(n-k-1)
            # 3. Operazione sul Nodo
            num=num_l+num_r+1                        # Θ(1)     
            return num                               # Θ(1)  
        return 0                                     # Θ(1)  
    
    # Funzione Pubblica Wrapper di lancio della Funzione Ricorsiva
    def calcola_n(self):                             # T(n)
        p=self.root                                  # Θ(1)
        return self._calcola_n(p)                    # S(n)
    
    # Costo Computazionale
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   
    


    'CALCOLO ALTEZZA'
    
    # Funzione Privata Ricorsiva
    def _calcola_h(self,p):                                  # S(n)
        if p==None:                                          # Θ(1) 
            return -1                                        # Θ(1)
        if p.getLeft()==None and p.getRight()==None:         # Θ(1)
            return 0                                         # Θ(1)
        # 1. 2. Passo Ricorsivo SottoAlbero Sx e Dx
        h=max(self._calcola_h(p.getLeft()),                  # S(k)
              self._calcola_h(p.getRight()))                 # S(n-k-1)
        # 3. Operazione sul Nodo
        return h+1                                           # Θ(1)                       

    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def calcola_h(self):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self._calcola_h(p)                            # S(n)

    # Costo Computazionale
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)   
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)



    'CONTEGGIO NODI al LIVELLO K'
    
    # Funzione Privata Ricorsiva
    def _conta_k(self,k,i,p):                                # S(n)
        if p==None:                                          # Θ(1)
            return 0                                         # Θ(1)
        if k==i:                                             # Θ(1)
            return 1                                         # Θ(1)
        # 1. Passo Ricorsivo SottoAlbero Sx
        k_left=self._conta_k(k,i+1,p.getLeft())              # S(k)
        # 2. Passo Ricorsivo SottoAlbero Dx
        k_right=self._conta_k(k,i+1,p.getRight())            # S(n-k-1)
        # 3. Operazione sul Nodo
        return k_left+k_right                                # Θ(1)

    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def conta_k(self,k):                                     # T(n)
        p=self.root                                          # Θ(1)
        return self._conta_k(k, 0, p)                        # S(n)

    # Costo Computazionale
    # Dimensione Input: numero nodi dell'albero (incognito a priori)
    # Costo: S(n)=S(k)+S(n-k-1)+Θ(1) -> S(n)=Θ(n)
    #        T(n)=Θ(1)+S(n)          -> T(n)=Θ(n)   



    'RICERCA'
    
    # Funzione Privata Ricorsiva
    def _cerca(self,p,k):                           # S(h)
        if (p==None or p.getKey()==k):              # Θ(1)
            return p                                # Θ(1)
        if (k<p.getKey()):                          # Θ(1)
            return self._cerca(p.getLeft(),k)       # S(h-1)
        else:                                       # Θ(1)
            return self._cerca(p.getRight(),k)      # S(h-1)
        
    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def cerca(self,k):                              # T(h)
        p=self.getRoot()                            # Θ(1)
        return self._cerca(p,k)                     # Θ(h)
    
    # Costo Computazionale
    # Dimensione dell'input: Altezza h dell'albero
    # Si esegue la funzione h volte con operazioni ogni volta di costo costante
    # Θ(1). Quindi il costo totale equivale a h volte Θ(1).
    # Costo: T(h)= Θ(1)+Θ(h) -> T(h)=Θ(h)



    'INSERIMENTO'
    
    def inserisci(self,z):                           # T(h)
        '1. INIZIALIZZAZIONE Puntatori ausiliari'
        # Padre Nodo Corrente
        y=None                                       # Θ(1)
        # Nodo corrente
        p=self.getRoot()                             # Θ(1)
        x=p                                          # Θ(1)
        '2. DISCESA fino a Nodo con Figlio Nullo'
        while x!=None:                               # h*Θ(1)+Θ(1)
            # Aggiorna y eguagliandolo a x...
            y=x                                      # Θ(1)
            # Aggiorna x facendolo scendere a dx/sx in base alla sua chiave...
            if z.getKey()<x.getKey():                # Θ(1)
                x=x.getLeft()                        # Θ(1)
            else:                                    # Θ(1)
                x=x.getRight()                       # Θ(1)
        '3. AGGIUNTA Nuovo Nodo'
        # Se l'Albero e' Nullo, usa Nuovo Nodo come Radice dell'Albero...
        if y==None:                                  # Θ(1)
            p=z                                      # Θ(1)
        # Se l'Albero non e' nullo, aggiungi il Nuovo Nodo a dx/sx dell'ultimo...
        else:                                        # Θ(1)
            if z.getKey()<y.getKey():                # Θ(1)
                y.left=z                             # Θ(1)
            else:                                    # Θ(1)
                y.right=z                            # Θ(1)
        # Aggiorna il campo Padre del nuovo nodo aggiunto all'albero...
        z.setParent(y)                               # Θ(1)
        # Restituisci l'albero modificato...
        return p                                     # Θ(1)
    
    # Costo Computazionale
    # Dimensione dell'input: Altezza h dell'albero
    # Costo: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)



    'MINIMO'
    
    # RICORSIVO
    
    # Funzione Privata Ricorsiva
    def _minimoRecurs(self,p):                       # S(h)
        'Controllo Input'
        if p==None:                                  # Θ(1)
            return                                   # Θ(1)
        'CASO BASE'
        if p.getLeft()==None:                        # Θ(1)
            return p                                 # Θ(1)
        'PASSO RICORSIVO'
        return self._minimoRecurs(p.getLeft())       # S(h-1)
    
    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def minimoRecurs(self):                          # T(h)
        'Inizializzazione Nodo di partenza'
        p=self.getRoot()                             # Θ(1)
        'Chiamata a funzione ricorsiva privata'
        return self._minimoRecurs(p)                 # S(h)
    
    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo: T(h)=Θ(1)+S(h)=Θ(1)+Θ(h) -> T(h)=Θ(h)
    
    
    # ITERATIVO
    
    # Funzione Privata Ricorsiva
    def _minimoIter(self,p):                         # S(h)
        'Controllo Input'
        if p==None:                                  # Θ(1)
            return                                   # Θ(1)
        'ITERAZIONE'
        while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
            p=p.getLeft()                            # Θ(1)
        return p                                     # Θ(1)
    
    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def minimoIter(self):                            # T(h)
        'Inizializzazione Nodo di partenza'
        p=self.getRoot()                             # Θ(1)                            
        'Chiamata a funzione iterativa privata'
        return self._minimoIter(p)                   # Θ(h)
    
    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo: T(h)=Θ(1)+S(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)
    
    
    
    'MASSIMO'
    
    # RICORSIVO
    
    # Funzione Privata Ricorsiva
    def _massimoRecurs(self,p):                       # S(h)
        'Controllo Input'
        if p==None:                                   # Θ(1)
            return                                    # Θ(1)
        'CASO BASE'
        if p.getRight()==None:                        # Θ(1)
            return p                                  # Θ(1)
        'PASSO RICORSIVO'
        return self._massimoRecurs(p.getRight())      # S(h-1)
    
    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def massimoRecurs(self):                          # T(h)
        'Inizializzazione Nodo di partenza'
        p=self.getRoot()                              # Θ(1) 
        'Chiamata a funzione ricorsiva privata'
        return self._massimoRecurs(p)                 # Θ(h) 
    
    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo: T(h)=Θ(1)+S(h)=Θ(1)+Θ(h) -> T(h)=Θ(h)
    
    
    # ITERATIVO
    
    # Funzione Privata Ricorsiva
    def _massimoIter(self,p):                         # T(h)
        'Controllo Input'
        if p==None:                                   # Θ(1)
            return                                    # Θ(1)
        'ITERAZIONE'
        while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
            p=p.getRight()                            # Θ(1)
        return p                                      # Θ(1)
    
    # Funzione Pubblica Wrapper per il lancio della Funzione Ricorsiva
    def massimoIter(self):                            # T(h)
        'Inizializzazione Nodo di partenza'
        p=self.getRoot()                              # Θ(1)
        'Chiamata a funzione iterativa privata'
        return self._massimoIter(p)                   # Θ(h) 
    
    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



    'PREDECESSORE'

    # ITERATIVO
    
    def predecessoreIter(self,k):                     # T(h)
        # 1. Ricava il nodo avente chiave uguale a k
        nodo=self.cerca(k)                            # Θ(h)
        # 2. Se il nodo non esiste, restituisci valore nullo
        if nodo==None:                                # Θ(1)
            return None                               # Θ(1)
        # 3. Se il nodo ha figlio Sx cerca il massimo nel
        #    suo sottoalbero Sx
        if nodo.getLeft()!=None:                      # Θ(1)
            predecessor=self._massimoIter(nodo.getLeft())   # Ω(1) o O(h)
        else:                                         # Θ(1)
        # 4. Se il nodo NON ha figlio Sx, risali l'albero     
        #    tramite ITERAZIONE    
            while(nodo.getParent()!=None and 
                  nodo==nodo.getParent().getLeft()):  # Θ(1)
                nodo=nodo.getParent()                 # Θ(1)
            predecessor=nodo.getParent()              # Θ(1)
        return predecessor                            # Θ(1)
    
    # RICORSIVO
    
    # Funzione Privata Ricorsiva
    def _predecRecurs(self,nodo):                     # S(h)
        # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
        #    quindi ritorna la radice.
        if nodo.getParent()==None:                    # Θ(1)
            return nodo                               # Θ(1)
        # 2. Se il nodo non coincide con il figlio Sx di suo padre,
        #    restituisci il nodo...
        if nodo!=nodo.getParent().getLeft():          # Θ(1)
            return nodo.getParent()                   # Θ(1)
        # 3. Se il nodo coincide con il figlio Sx di suo padre, 
        #    continua la risalita passando il nodo padre nella nuova 
        #    chiamata ricorsiva.
        return self._predecRecurs(nodo.getParent())   # S(h-1)   
    
    # Funzione Pubblica Wrapper per il lancio della funzione ricorsiva
    def predecessoreRecurs(self,k):                   # T(h)
        # 1. Ricava il nodo avente chiave uguale a k    
        nodo=self.cerca(k)                            # Θ(h)
        # 2. Se il nodo non esiste, restituisci valore nullo
        if nodo==None:                                # Θ(1)
            return None                               # Θ(1)
        # 3. Se il nodo ha figlio Sx cerca il massimo nel
        #    suo sottoalbero Sx
        if nodo.getLeft()!=None:                      # Θ(1)
            predecessor=self._massimoRecurs(nodo.getLeft()) # Ω(1) o O(h)     
        else:                                         # Θ(1)
        # 4. Se il nodo NON ha figlio Sx, risali l'albero
        #    tramite RICORSIONE
            return self._predecRecurs(nodo)           # S(h)
        return predecessor                            # Θ(1)
    
    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
    # Costo Ricorsiva: T(h)=Θ(h) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  
    
    
    
    'SUCCESSORE'

    # ITERATIVO
    
    def successoreIter(self, k):                       # T(h)
        # 1. Ricava il nodo avente chiave uguale a k
        nodo=self.cerca(k)                             # Θ(h)
        # 2. Se il nodo non esiste, restituisci valore nullo
        if nodo==None:                                 # Θ(1)
            return None                                # Θ(1)
        # 3. Se il nodo ha figlio Dx cerca il minimo nel
        #    suo sottoalbero Dx
        if nodo.getRight()!=None:                      # Θ(1)
            successor=self._minimoIter(nodo.getRight()) # Ω(1) o O(h)
        else:        
        # 4. Se il nodo NON ha figlio Dx, risali l'albero     
        #    tramite ITERAZIONE
            while(nodo.getParent()!=None and 
                  nodo==nodo.getParent().getRight()):  # Θ(1)
                nodo=nodo.getParent()                  # Θ(1)
            successor=nodo.getParent()                 # Θ(1)
        return successor                               # Θ(1)
    
    # RICORSIVO
    
    # Funzione Privata Ricorsiva
    def _succesRecurs(self,nodo):                      # S(h)
        # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
        #    quindi ritorna la radice.
        if nodo.getParent()==None:                     # Θ(1)
            return nodo                                # Θ(1) 
        # 2. Se il nodo non coincide con il figlio Dx di suo padre,
        #    restituisci il nodo...
        if nodo!=nodo.getParent().getRight():          # Θ(1)
            return nodo.getParent()                    # Θ(1)
        # 3. Se il nodo coincide con il figlio Dx di suo padre, 
        #    continua la risalita passando il nodo padre nella nuova 
        #    chiamata ricorsiva.
        return self._succesRecurs(nodo.getParent())    # S(h-1)   
    
    # Funzione Pubblica Wrapper per il lancio della funzione ricorsiva
    def successoreRecurs(self,k):                      # T(h)
        # 1. Ricava il nodo avente chiave uguale a k    
        nodo=self.cerca(k)                             # Θ(h)
        # 2. Se il nodo non esiste, restituisci valore nullo
        if nodo==None:                                 # Θ(1)
            return None                                # Θ(1)
        # 3. Se il nodo ha figlio Dx cerca il massimo nel
        #    suo sottoalbero Dx
        if nodo.getRight()!=None:                      # Θ(1)
            successor=self._minimoRecurs(nodo.getRight()) # Ω(1) o O(h)
        else:                                          # Θ(1)
        # 4. Se il nodo NON ha figlio Dx, risali l'albero
        #    tramite RICORSIONE
            return self._succesRecurs(nodo)            # S(h)
        return successor                               # Θ(1)

    # Costo Computazionale
    # Dimensione input: altezza dell'albero h
    # Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) ->T(h)=Ω(1) o O(h)  
    # Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) ->T(h)=Ω(1) o O(h) 
    
    
    
    'CANCELLAZIONE'

    # Funzione Ausiliaria per la cancellazione di una singola foglia
    def cancellaFoglia(self,p,nodo):                                 # T(h)
        # Aggiorna il campo figlio (Dx/Sx) del padre 
        # corrispondente alla foglia da cancellare.
        if (nodo==nodo.getParent().getLeft()):                       # Θ(1)
            nodo.getParent().setLeft(None)                           # Θ(1)
        else:                                                        # Θ(1)
            nodo.getParent().setRight(None)                          # Θ(1)
        return                                                       # Θ(1)
    


    def cancella(self,k):                                            # T(h)
        # Estrai nodo avente valore chiave uguale a k
        nodo=self.cerca(k)                                    # Ω(1) o O(h)
        # Se il nodo non esiste chiudi la funzione
        if nodo==None:                                               # Θ(1)
            return                                                   # Θ(1)
        # CASO 1 - Il Nodo NON HA FIGLI
        # Cancella il nodo aggiornando il corrispondente campo figlio
        # del nodo padre.
        if (nodo.getLeft()==None and nodo.getRight()==None):         # Θ(1)
           self.cancellaFoglia(self.getRoot(),nodo)                  # Θ(1)
        # CASO 2 - Il Nodo HA 1 FIGLIO
        # Cortocircuita il padre con il figlio del nodo da eliminare
        # Se l'unico figlio e' quello Sx...
        if (nodo.getLeft()!=None and nodo.getRight()==None):         # Θ(1)
            # Assegna il padre del nodo al figlio Sx
            nodo.getLeft().setParent(nodo.getParent())               # Θ(1)
            # Assegna il figlio Sx al padre del nodo
            if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
                nodo.getParent().setLeft(nodo.getLeft())             # Θ(1)
            else:                                                    # Θ(1)
                nodo.getParent().setRight(nodo.getLeft())            # Θ(1)
        # Se l'unico figlio e' quello Dx...
        if (nodo.getLeft()==None and nodo.getRight()!=None):         # Θ(1)
            # Assegna il padre del nodo al figlio Dx
            nodo.getRight().setParent(nodo.getParent())              # Θ(1)
            # Assegna il figlio Dx al padre del nodo
            if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
                nodo.getParent().setLeft(nodo.getRight())            # Θ(1)
            else:                                                    # Θ(1)
                nodo.getParent().setRight(nodo.getRight())           # Θ(1)
        
        # CASO 3 - Il Nodo HA 2 FIGLI
        # Trova il predecessore/successore del nodo da cancellare, 
        # copia il suo contenuto nel nodo da cancellare e, infine, 
        # cancella il nodo predecessore/successore.
        if (nodo.getLeft()!=None and nodo.getRight()!=None):         # Θ(1)
            # Ricava i nodi predecessore e successore
            pred=self.predecessoreIter(nodo.getKey())       # Ω(1) o O(h) 
            succes=self.successoreRecurs(nodo.getKey())     # Ω(1) o O(h) 
            # Sostituisci chiave del nodo e cancella 
            # predecessore/successore
            if pred!=None:                                           # Θ(1)
                nodo.setKey(pred.getKey())                           # Θ(1)
                self.cancellaFoglia(self.getRoot(),pred)             # Θ(1)
            else:                                                    # Θ(1)
                nodo.setKey(succes.getKey())                         # Θ(1)
                self.cancellaFoglia(self.getRoot(),succes)           # Θ(1)

        # Costo Computazionale
        # Dimensione input: altezza dell'albero h
        # Costo Iterativa: T_caso1(h)=O(h)+Θ(1)=O(h)
        #                  T_caso2(h)=O(h)+Θ(1)=O(h)
        #                  T_caso3(h)=O(h)+O(h)+Θ(1)=O(h)
        # Costo: T(h)=max{T_caso1;T_caso2;T_caso3}=O(h)


'''

'TEST'

# 1. CREAZIONE ALBERO PER I TEST

valoriNodi=[18,11,33,7,15,22,80,13,16,50,91,42,64]
indiciPadri=[None,0,0,1,1,2,2,4,4,6,6,9,9]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,len(nodi),1):
    if indiciPadri[i]==None:
        nodi[i].setParent(None)
    else:
        nodi[i].setParent(nodi[indiciPadri[i]])
    k=0
    for j in range(0,len(indiciPadri),1):
        if indiciPadri[j]==i:
            if k==0:
                nodi[i].setLeft(nodi[j])
                k+=1
            else:
                nodi[i].setRight(nodi[j])
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

'Visita Per Livelli'
print("\nVisita per Livelli:")
albero.visitaPerLivelli()

'Conteggio numero nodi'
print("\nConteggio Numero Nodi: " + str(albero.calcola_n()))

'Calcolo Altezza'
print("Calcolo Altezza dell'albero: " + str(albero.calcola_h()))

'Conteggio Nodi al Livello k'
print("Conteggio numero nodi al livello 2: " + str(albero.conta_k(2)))

'Ricerca'
nodoRicercato=albero.cerca(22)
print("\nRICERCA\nIl nodo ricercato e' : " + str(nodoRicercato))

'Inserimento'
z=Nodo(47)
print("\nINSERIMENTO\nAlbero prima dell'inserimento del nodo " + str(z))
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
predIter1=albero.predecessoreIter(k1)      # Iterativo -Caso 1- Discesa
predIter2=albero.predecessoreIter(k2)      # Iterativo -Caso 2- Risalita
predRec1=albero.predecessoreRecurs(k1)     # Ricorsivo -Caso 1- Discesa
predRec2=albero.predecessoreRecurs(k2)     # Ricorsivo -Caso 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))

'Successore'
k1=11
k2=16
succIter1=albero.successoreIter(k1)     # Iterativo -Caso 1- Discesa
succIter2=albero.successoreIter(k2)     # Iterativo -Caso 2- Risalita
succRec1=albero.successoreRecurs(k1)    # Ricorsivo -Caso 1- Discesa
succRec2=albero.successoreRecurs(k2)    # Ricorsivo -Caso 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))

'Cancellazione'
k_caso1=7
k_caso3=33
print("\nCANCELLAZIONE - Caso 1 - chiave " + str(k_caso1) + "\nPrima...")
albero.visitaPerLivelli()
print("\nDopo...")
albero.cancella(k_caso1)
albero.visitaPerLivelli()
print("\n\nCANCELLAZIONE - Caso 3 - chiave " + str(k_caso3) + "\nPrima...")
albero.visitaPerLivelli()
print("\nDopo...")
albero.cancella(k_caso3)
albero.visitaPerLivelli()

'''
