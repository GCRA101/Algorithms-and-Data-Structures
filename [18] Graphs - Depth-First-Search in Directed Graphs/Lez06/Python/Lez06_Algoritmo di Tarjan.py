# -*- coding: utf-8 -*-
"""
LEZIONE 06 - DFS IN GRAFI DIRETTI - ALGORITMO DI TARJAN

Algoritmi di utilita' tramite uso di DFS
    - Ricerca Componenti Fortemente Connesse in Grafi Diretti
        - Algoritmo di Tarjan
        
"""


" ALGORITMI *****************************************************************"


class Nodo:
    
    def __init__(self,valore):
        self.valore=valore
    
    

class GrafoDiretto:
    
    visitati=[]                 # Vettore dei Nodi Visitati        
    CC=[]                       # Vettore Indici Componenti Fortemente Connesse
    S=[]                        # Pila di Tarjan
    listaAdiacenza=[]           # Lista di Adiacenza
    c=0                         # Contatore Tempo di Visita
    nc=0                        # Contatore Numero Componenti    
    
    
    def __init__(self,listaAdiacenza):
        self.listaAdiacenza=listaAdiacenza
    
    
    # RICERCA delle COMPONENTI FORTEMENTE CONNESSE [Grafi Diretti]

    def __DFS_cfc(self,u):                                       # S(n,m)
        self.c+=1                                                # Θ(1)
        self.visitati[u]=self.c                                  # Θ(1)
        back=self.visitati[u]                                    # Θ(1)
        keys=list(self.listaAdiacenza.keys())                    # Θ(n)
        uKey=keys[u]                                             # Θ(1)
        self.S.append(uKey)                                      # Θ(1)
        for v in self.listaAdiacenza[uKey]:
            if self.visitati[keys.index(v)]==0:                  # Θ(1)
                x=self.__DFS_cfc(keys.index(v))                  # S(n-1,v)
                back=min(back,x)                                 # Θ(1)
            else:
                if self.CC[v]==0:                                # Θ(1)
                    back=min(back, self.visitati[keys.index(v)]) # Θ(1)
        if back==self.visitati[u]:                               # Θ(1)
            self.nc+=1                                           # Θ(1)
            while True:                                          # k*Θ(1)+Θ(1) 
                w=self.S.pop()                                   # Θ(1)
                self.CC[w]=self.nc                               # Θ(1)
                if w==uKey:                                      # Θ(1)
                    break                                        # Θ(1)
        return back                                              # Θ(1)


    def ricercaCompFortConnesse(self):                           # T(n,m)
        self.visitati=[0 for v in self.listaAdiacenza]           # Θ(n)
        self.CC={key: 0 for key in self.listaAdiacenza.keys()}   # Θ(n)
        for u in range(0, len(self.listaAdiacenza)):             # n*Θ(1)+Θ(1)
            if self.visitati[u]==0:                              # Θ(1)
                self.__DFS_cfc(u)                                # S(n,m)
        return self.CC                                           # Θ(1)
            
    # Costo Computazionale: Θ(n+m)   - CASO PEGGIORE/MIGLIORE   



" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...

"""

# LISTE DI ADIACENZA

'Grafo Diretto Ciclico con Componenti Fortemente Connesse'
L01= {'a': ['e'],
      'b': ['p','d'],
      'c': ['p'],
      'd': ['c'],
      'e': ['r','h'],
      'f': ['g','q'],
      'g': ['b'],
      'h': ['a','e'],
      'i': [],
      'l': ['n'], 
      'm': ['i','o'], 
      'n': ['q'], 
      'o': ['m'], 
      'p': ['r'], 
      'q': ['l','m'], 
      'r': ['g'] 
      }

'Grafo Diretto Ciclico con Componenti Fortemente Connesse'
L02= {'Aternum': ['Larinum'],
      'Ariminum': ['Castrum Truentum'],
      'Barium': ['Canusium'],
      'Beneventum': ['Tarentum'],
      'Brindisium': ['Barium'],
      'Canusium': ['Beneventum','Capua'],
      'Capua': ['Beneventum'],
      'Castrum Truentum': ['Aternum', 'Spoletum'],
      'Corfinium': ['Aternum'],
      'Larinum': ['Barium'], 
      'Roma': ['Spoletum','Tarracina','Tibur'], 
      'Spoletum': ['Ariminum'], 
      'Tarracina': ['Capua'], 
      'Tarentum': ['Brindisium'], 
      'Tibur': ['Corfinium']
      }


# MATRICE DI ADIACENZA

'Grafo Diretto Ciclico con Componenti Fortemente Connesse'
M01= [[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo A
      [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0], # Riga di adiacenza del nodo B
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], # Riga di adiacenza del nodo C
      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo D
      [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1], # Riga di adiacenza del nodo E      
      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0], # Riga di adiacenza del nodo F      
      [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo G     
      [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo H
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo I
      [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], # Riga di adiacenza del nodo L
      [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0], # Riga di adiacenza del nodo M
      [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo N
      [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], # Riga di adiacenza del nodo O      
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], # Riga di adiacenza del nodo P      
      [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0], # Riga di adiacenza del nodo Q     
      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]] # Riga di adiacenza del nodo R

'Grafo Diretto Ciclico con Componenti Fortemente Connesse'
M02= [[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], # Riga di adiacenza del nodo Aternum
      [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Ariminum
      [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Barium
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], # Riga di adiacenza del nodo Beneventum
      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Brindisium
      [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Canusium
      [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Capua
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0], # Riga di adiacenza del nodo Castr Tru
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Corfinium
      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Larinum
      [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1], # Riga di adiacenza del nodo Roma
      [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Spoletum
      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Tarracina      
      [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo Tarentum         
      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]] # Riga di adiacenza del nodo Tibur
   


# INSTANZIAZIONE GRAFI
gi01=GrafoDiretto(L01)
gi02=GrafoDiretto(L02)


# RICERCA delle COMPONENTI FORTEMENTE CONNESSE [Grafi Diretti]
print("\n")
cfc01=gi01.ricercaCompFortConnesse()
print("Grafo 01 - Componenti Fortemente Connesse: " + str(cfc01))
print("\n")
print("\n")
cfc02=gi02.ricercaCompFortConnesse()
print("Grafo 02 - Componenti Fortemente Connesse: " + str(cfc02))


