# -*- coding: utf-8 -*-
"""
LEZIONE 12 - ALBERI MINIMI di COPERTURA e ALGORITMO di PRIM

Un albero minimo di copertura e' un albero di visita di un grafo pesato che 
consente di minimizzare il costo totale richiesto per visitare tutti i nodi a
partire da un nodo sorgente.
Tale albero minimo di copertura differisce dall'albero di visita BFS e DFS e
viene determinato utilizzando l'algoritmo di Prim

Algoritmo di Prim
    - Formulazione classica con vettore - O(n*m)
    - Formulazione avanzata con vettore - O(n^2)
    - Formulazione avanzata con heap    - O((n+m)logn)


Confronto Algoritmo di Prim vs Algoritmo di Dijkstra -------------------------

L'algoritmo di Prim e' estremamente simile all'algoritmo di Dijkstra in quanto
a struttura ma differisce sostanzialmente in quanto a scopo.

Aspetti Comuni
- Algoritmo greedy
- Struttura dati di Heap Minimo
- Costo computazionale di O(mlogn)

Aspetti Differenti
> Scopo
    - Dijkstra minimizza la distanza cumulata di ciascun nodo dal nodo sorgente
    - Prim minimizza il costo globale di estensione dell'albero di visita.
> Richiesta per Estensione della soluzione
    - Dijkstra cerca lo step che minimizza il cammino totale dal nodo sorgente
      al nodo destinazione.
    - Prim cerca lo step che minimizza il costo complessivo dell'albero di 
      ricerca.
      
Analogia Rete Stradale
> Dijkstra
    - Data una rete stradale ESISTENTE che collega le citta' italiane e data 
      la citta' di partenza (Firenze), Dijkstra determina i percorsi piu'
      brevi per raggiungere qualsiasi citta' a partire da Firenze.
    - Dikstra risponde alla domanda dell'utente:"Qual'e' il PERCORSO PIU' BREVE
      per arrivare a destinazione?""
> Prim
    - Data una rete stradale INESISTENTE e tutta DA COSTRUIRE, Prim determina
      la rete di collegamenti di COSTO TOTALE MINIMO che consente di collegare 
      tutte le citta."
    - Prim risponde alla domanda dell'ente pubblico:"Qual'e' la RETE stradale
      di COSTO MINIMO per collegare tutte le citta'?"
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math
from collections import deque
from decimal import Decimal


# Classi di utilita' ----------------------------------------------------------

class HeapNode:
    
    # Constructor
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
    
    # Method defining Sorting Criteria in Sortable Data Structures
    # Method equivalent to compareTo(...)
    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        
    # Method defining Equality Criteria in Data Structures
    # Method equivalent to equals(...)
    def __eq__(self, other):
        return (self.node == other.node and 
                self.cost == other.cost)
    
    # Method converting the Class Instance into a String
    # Method equivalent to ToString()
    def __str__(self):
        return f"{self.node} ({self.cost})"


# ========================== ALGORITMO di PRIM ================================


# ALGORITMO di PRIM - CLASSICO con VETTORE [Grafi Diretti e Indiretti]
# ------------------------------------------------------------------------
def MinimumSpanningTree_Prim_v01(G,u):                      # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    nodi = []                                               # Θ(n)
    padri[u] = u                                            # Θ(1)
    nodi.append(u)                                          # Θ(1)
    costi = {key: math.inf for key in G}                    # Θ(n)
    costi[u] = 0                                            # Θ(1)
    while True:                                             # n*Θ(1)+Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        costo_min = math.inf                                # Θ(1)
        for u in G:                                         # v*Θ(1)+Θ(1)
            if padri[u] != -1:                              # Θ(1)
                for v in G[u]:                              # k*Θ(1)+Θ(1)
                    if padri[v[0]] == -1:                   # Θ(1)
                        costo = v[1]                        # Θ(1)
                        if costo < costo_min:               # Θ(1)
                            costo_min = costo               # Θ(1)
                            u_min = u                       # Θ(1)
                            v_min = v[0]                    # Θ(1)
        if u_min == None:                                   # Θ(1)
            break                                           # Θ(1)
        nodi.append(v_min)                                  # Θ(1)
        padri[v_min] = u_min                                # Θ(1)
        costi[v_min] = costo_min                            # Θ(1)
    return nodi, padri, costi                               # Θ(1)

# Costo Computazionale: O(n*m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso



# ALGORITMO di PRIM - AVANZATO con VETTORE [Grafi Diretti e Indiretti]
# ------------------------------------------------------------------------
def MinimumSpanningTree_Prim_v02(G,s):                      # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    costi = {key: math.inf for key in G}                    # Θ(n)
    padri[s] = s                                            # Θ(1)
    costi[s] = 0                                            # Θ(1)
    nodi = []                                               # Θ(1)
    A = list(G.keys())                                      # Θ(n)
    while len(A)!=0:                                        # n*Θ(1)+Θ(1)
        costo_min = math.inf                                # Θ(1)
        u = None                                            # Θ(1)
        for n in A:                                         # n*Θ(1)+Θ(1)
            if costi[n] < costo_min:                        # Θ(1)
                costo_min = costi[n]                        # Θ(1)
                u = n                                       # Θ(1)
        if u is None:                                       # Θ(1) 
            u = A[0]                                        # Θ(1)
        A.remove(u)                                         # Θ(n) (##)
        nodi.append(u)                                      # Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if v[0] in A and v[1] < costi[v[0]]:            # Θ(1)
                padri[v[0]] = u                             # Θ(1)
                costi[v[0]] = v[1]                          # Θ(1)
    return nodi, padri, costi                               # Θ(1)

# T(n,m) = 2*Θ(n) + 3*Θ(1) + Θ(n)*(Θ(n)+O(n)+Θ(m)) 
#        = Θ(n) + Θ(n^2) + Θ(n*m) = O(n^2)
# 
# Costo Computazionale : O(n^2) - CASO PEGGIORE (*)
#                        Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso
# (##): Rimuovere un elemento di un array comporta la sua ricerca O(n) e
#       lo shift dei restanti elementi a seguito della cancellazione O(n).
#       - Primo elemento  -> Θ(1)[Ricerca] + Θ(1)[Delete] + Θ(n)[Shift] = Θ(n)
#       - Ultimo elemento -> Θ(n)[Ricerca] + Θ(1)[Delete] + Θ(1)[Shift] = Θ(n)     



# ALGORITMO di PRIM - AVANZATO con HEAP MINIMO [Grafi Diretti e Indiretti]
# ----------------------------------------------------------------------------

# Funzioni di supporto per l'Algoritmo di Prim Avanzato ----------------------

# HEAP MINIMO
# N   -> array dei nodi in ordine di Heap (la struttura vera e propria)
# D   -> array delle chiavi/priorita', parallelo a N (stessa posizione)
# pos -> dizionario nodo -> indice corrente in N/D
#
# 'pos' e' cio' che rende possibile il decremento chiave in O(logn): senza
# di esso, individuare la posizione di un nodo nell'Heap richiederebbe una
# ricerca O(n), vanificando il vantaggio della struttura dati.

# HEAPIFY - ripristina la proprieta' di Heap Minimo scendendo dalla radice
def heapify(N,C,pos,n,i):                       # T(n)
    left=2*i+1                                  # Θ(1)
    right=2*i+2                                 # Θ(1)
    if (left<n)and(C[left]<C[i]):               # Θ(1)
        iMin=left                               # Θ(1)
    else:                                       # Θ(1)
        iMin=i                                  # Θ(1)
    if (right<n)and(C[right]<C[iMin]):          # Θ(1)
        iMin=right                              # Θ(1)
    if iMin!=i:                                 # Θ(1)
        N[i],N[iMin] = N[iMin],N[i]             # Θ(1)
        C[i],C[iMin] = C[iMin],C[i]             # Θ(1)
        pos[N[i]] = i                           # Θ(1)
        pos[N[iMin]] = iMin                     # Θ(1)
        heapify(N,C,pos,n,iMin)                 # T(2/3n)
    return                                      # Θ(1)

# Costo Computazionale: O(logn) - altezza dell'Heap

# BUILDHEAP - costruisce l'Heap Minimo a partire dagli array N e D
def buildHeap(N,C,pos):                         # T(n)
    m=len(N)                                    # Θ(1)
    for i in range(m):                          # Θ(n)
        pos[N[i]]=i                             # Θ(1)
    for i in range(m//2-1,-1,-1):                # n/2*O(logn)+Θ(1)
        heapify(N,C,pos,m,i)
    return                                      # Θ(1)

# Costo Computazionale: O(n) - somma delle altezze di tutti i nodi dell'Heap

# ESTRAI MIN - estrae e restituisce il nodo con chiave (Dist) minima
def estraiMin(N,C,pos):                         # T(n)
    u = N[0]                                    # Θ(1) nodo di valore minimo
    ultimo = len(N)-1                           # Θ(1)
    N[0] = N[ultimo]                            # Θ(1)
    C[0] = C[ultimo]                            # Θ(1)
    pos[N[0]] = 0                               # Θ(1)
    N.pop()                                     # Θ(1)
    C.pop()                                     # Θ(1)
    del pos[u]                                  # Θ(1)
    if N:                                       # Θ(1)
        heapify(N,C,pos,len(N),0)               # O(logn)
    return u                                    # Θ(1)

# Costo Computazionale: O(logn) - un heapify dalla radice ad una foglia

# DECREMENTA CHIAVE - abbassa la chiave (Dist) di un nodo e risale l'Heap
def decrementaChiave(N,D,pos,v,nuovaChiave):    # T(n)
    i = pos[v]                                  # Θ(1)
    D[i] = nuovaChiave                          # Θ(1)
    while (i>0)and(D[(i-1)//2]>D[i]):           # O(logn)
        padre = (i-1)//2                        # Θ(1)
        N[i],N[padre] = N[padre],N[i]           # Θ(1)
        D[i],D[padre] = D[padre],D[i]           # Θ(1)
        pos[N[i]] = i                           # Θ(1)
        pos[N[padre]] = padre                   # Θ(1)
        i = padre                               # Θ(1)
    return                                      # Θ(1)

# Costo Computazionale: O(logn) - risalita dalla foglia alla radice


# Algoritmo di Prim - Avanzato con Heap Minimo -------------------------------
def MinimumSpanningTree_Prim_v03(G,s):                      # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    costi = {key: math.inf for key in G}                    # Θ(n)
    nodi = []                                               # Θ(n)
    padri[s] = s                                            # Θ(1)
    costi[s] = 0                                            # Θ(1)
    N = list(G.keys())                                      # Θ(n)
    C = [costi[nodo] for nodo in N]                         # Θ(n)
    pos = {}                                                # Θ(1)
    buildHeap(N,C,pos)                                      # O(n)
    while N:                                                # n*Θ(1)+Θ(1)
        u = estraiMin(N,C,pos)                              # O(logn)
        nodi.append(u)                                      # Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if v[0] in pos and v[1] < costi[v[0]]:          # Θ(1)
                padri[v[0]] = u                             # Θ(1)
                costi[v[0]] = v[1]                          # Θ(1)
                decrementaChiave(N,C,pos,v[0],costi[v[0]])  # O(logn)
    return nodi, padri, costi                               # Θ(1)

# T(n,m) = 4*Θ(n) + 3*Θ(1) + O(n) + Θ(n)*O(logn) + Θ(m)*O(logn)
#        = O(n) + O(n*logn) + O(m*logn) = O((n+m)*logn)
#
# Costo Computazionale : O((n+m)logn) - CASO PEGGIORE e MIGLIORE (*)
#
# (*): A differenza di v01/v02, l'Heap Minimo con decremento chiave rende
#      costante il numero di operazioni O(logn) sia per l'estrazione del
#      minimo sia per l'aggiornamento delle distanze: non c'e' piu' bisogno
#      di scandire linearmente l'insieme dei nodi per trovare il minimo
#      (v01, v02) ne' di ricercare linearmente un nodo per rimuoverlo da un
#      array (v02, ##), da cui il miglioramento asintotico rispetto a O(n^2).



" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi due esempi
piu' complessi: uno ispirato alla progettazione della rete viaria dell'antico
impero romano e uno ispirato al film Matrix.

"""


# LISTE DI ADIACENZA ----------------------------------------------------------


'Grafo Indiretto Connesso - Esempio Numerico ---------------------------------' 
L_gc_Numeric = {
    "A": [("B",2),("C",4),("D",7),("F",5)],
    "B": [("A",2),("D",6),("E",3),("G",8)],
    "C": [("A",4),("F",6)],
    "D": [("A",7),("B",6),("F",1),("G",6)],
    "E": [("B",3),("G",7)],
    "F": [("A",5),("C",6),("D",1),("G",6)],
    "G": [("B",8),("D",6),("E",7),("F",6)]}


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
'''
Costo degli Archi -> Costo realizzazione connessione in migliaia di Sesterzi
''' 
L_gc_Roman = {
    "Alexandria": [("Bisantium", 33), ("Carthago", 57), ("Corduba", 97), 
                   ("Massilia", 76), ("Ravenna", 64), ("Roma", 59), 
                   ("Tarraco", 84)],
    "Aquincum": [("Augusta Treverorum", 3080), ("Bisantium", 35), 
                 ("Colonia Agrippina", 3330), ("Mediolanum", 2100), 
                 ("Ravenna", 990), ("Vindobona", 220)],
    "Augusta Treverorum": [("Aquincum", 3080), ("Colonia Agrippina", 230), 
                           ("Eboracum", 20), ("Londinium", 17), 
                           ("Lugdunum", 900), ("Lutetia", 400), 
                           ("Mediolanum", 1680), ("Vindobona", 2939)],
    "Bisantium": [("Alexandria", 33), ("Aquincum", 35), ("Capua", 36), 
                  ("Corduba", 96), ("Narbo", 78), ("Ravenna", 33), 
                  ("Vindobona", 39)],
    "Burdigala": [("Corduba", 36), ("Eboracum", 33), ("Emerita Augusta", 1350), 
                  ("Londinium", 21), ("Lugdunum", 810), ("Lutetia", 500), 
                  ("Narbo", 300)],
    "Capua": [("Bisantium", 36), ("Carthago", 17), ("Carthago Nova", 30), 
              ("Corduba", 60), ("Ravenna", 720), ("Roma", 190), 
              ("Tarraco", 34)],
    "Carthago": [("Alexandria", 57), ("Capua", 17), ("Carthago Nova", 30), 
                 ("Emerita Augusta", 44), ("Massilia", 25), ("Narbo", 28), 
                 ("Roma", 18), ("Tarraco", 27)],
    "Carthago Nova": [("Capua", 30), ("Carthago", 30), ("Corduba", 500), 
                      ("Emerita Augusta", 860), ("Massilia", 15), 
                      ("Narbo", 11), ("Roma", 27), ("Tarraco", 230)],
    "Colonia Agrippina": [("Aquincum", 3330), ("Augusta Treverorum", 230), 
                          ("Eboracum", 17), ("Londinium", 14), 
                          ("Lutetia", 320), ("Mediolanum", 1930), 
                          ("Vindobona", 1930)],
    "Corduba": [("Alexandria", 97), ("Bisantium", 96), ("Burdigala", 36), 
                ("Capua", 60), ("Carthago Nova", 500), 
                ("Emerita Augusta", 250), ("Massilia", 39), ("Tarraco", 1930)],
    "Eboracum": [("Augusta Treverorum", 20), ("Burdigala", 33), 
                 ("Colonia Agrippina", 17), ("Londinium", 320), 
                 ("Lutetia", 21), ("Narbo", 43), ("Tarraco", 63)],
    "Emerita Augusta": [("Burdigala", 1350), ("Carthago", 44), 
                        ("Carthago Nova", 860), ("Corduba", 250), 
                        ("Londinium", 49), ("Massilia", 60), ("Roma", 78), 
                        ("Tarraco", 30)],
    "Londinium": [("Augusta Treverorum", 17), ("Burdigala", 21), 
                  ("Colonia Agrippina", 14), ("Eboracum", 320), 
                  ("Emerita Augusta", 49), ("Lutetia", 11), ("Tarraco", 57)],
    "Lugdunum": [("Augusta Treverorum", 900), ("Burdigala", 810), 
                 ("Lutetia", 460), ("Massilia", 500), ("Mediolanum", 1120), 
                 ("Narbo", 540), ("Vindobona", 2630)],
    "Lutetia": [("Augusta Treverorum", 400), ("Burdigala", 500), 
                ("Colonia Agrippina", 320), ("Eboracum", 21), 
                ("Londinium", 11), ("Lugdunum", 460), ("Narbo", 1252)],
    "Massilia": [("Alexandria", 76), ("Carthago", 25), ("Carthago Nova", 15), 
                 ("Corduba", 39), ("Emerita Augusta", 60), ("Lugdunum", 500), 
                 ("Mediolanum", 500), ("Narbo", 150), ("Roma", 20)],
    "Mediolanum": [("Aquincum", 2100), ("Augusta Treverorum", 1680), 
                   ("Colonia Agrippina", 1930), ("Lugdunum", 1120), 
                   ("Massilia", 500), ("Ravenna", 220), ("Roma", 1680), 
                   ("Vindobona", 2100)],
    "Narbo": [("Bisantium", 78), ("Burdigala", 300), ("Carthago", 28), 
              ("Carthago Nova", 11), ("Eboracum", 43), ("Lugdunum", 540), 
              ("Lutetia", 1252), ("Massilia", 150), ("Tarraco", 230)],
    "Ravenna": [("Alexandria", 64), ("Aquincum", 990), ("Bisantium", 33), 
                ("Capua", 720), ("Mediolanum", 220), ("Roma", 540), 
                ("Vindobona", 860)],
    "Roma": [("Alexandria", 59), ("Capua", 190), ("Carthago", 18), 
             ("Carthago Nova", 27), ("Emerita Augusta", 78), ("Massilia", 20), 
             ("Mediolanum", 1680), ("Ravenna", 540)],
    "Tarraco": [("Alexandria", 84), ("Capua", 34), ("Carthago", 27), 
                ("Carthago Nova", 230), ("Corduba", 1930), ("Eboracum", 63), 
                ("Emerita Augusta", 30), ("Londinium", 57), ("Narbo", 230)],
    "Vindobona": [("Aquincum", 220), ("Augusta Treverorum", 2939), 
                  ("Bisantium", 39), ("Colonia Agrippina", 1930), 
                  ("Lugdunum", 2630), ("Mediolanum", 2100), ("Ravenna", 860)]
}


'Grafo Indiretto Connesso - Esempio Matrix  ----------------------------------'
'''
A: Thomas Anderson's Apartment
B: Heart O' The City Hotel
C: Adams Street Subway Station
D: The Metacortex Building
E: Abandoned Government Office
F: Chinatown Safe House
G: Warehouse 17
H: Riverfront Dockyard
I: Old Power Station
J: St. Michael's Cathedral Rooftop
K: Telephone Extraction Hub
L: Zion Access Broadcast Relay

Costo degli Archi -> Numero di Agenti presenti sul percorso

'''
L_gc_Matrix = {
    "A": [("B", 1), ("C", 5), ("D", 7), ("F", 3), ("G", 2), ("J", 2), 
          ("K", 4)],
    "B": [("A", 1), ("C", 5), ("E", 6), ("F", 1), ("G", 4), ("H", 5), ("I", 3), 
          ("J", 3), ("K", 5), ("L", 1)],
    "C": [("A", 5), ("B", 5), ("D", 5), ("E", 7), ("F", 4), ("I", 1), 
          ("J", 6)],
    "D": [("A", 7), ("C", 5), ("F", 3), ("I", 5), ("J", 5), ("K", 5), 
          ("L", 6)],
    "E": [("B", 6), ("C", 7), ("H", 2), ("I", 3), ("J", 4), ("K", 3)],
    "F": [("A", 3), ("B", 1), ("C", 4), ("D", 3), ("G", 3), ("I", 6)],
    "G": [("A", 2), ("B", 4), ("F", 3), ("H", 3), ("I", 2)],
    "H": [("B", 5), ("E", 2), ("G", 3), ("I", 2), ("J", 7), ("K", 4)],
    "I": [("B", 3), ("C", 1), ("D", 5), ("E", 3), ("F", 6), ("G", 2), ("H", 2), 
          ("K", 3)],
    "J": [("A", 2), ("B", 3), ("C", 6), ("D", 5), ("E", 4), ("H", 7), 
          ("K", 3)],
    "K": [("A", 4), ("B", 5), ("D", 5), ("E", 3), ("H", 4), ("I", 3), ("J", 3), 
          ("L", 1)],
    "L": [("B", 1), ("D", 6), ("K", 1)]
}
       

     
# ALGORITMO di PRIM con LISTE di ADIACENZA --------------------------------

'Grafo Indiretto Connesso - Esempio Numerico -----------------------------'
u = "A"   
prim_v01 = MinimumSpanningTree_Prim_v01(L_gc_Numeric,u)
prim_v02 = MinimumSpanningTree_Prim_v02(L_gc_Numeric,u)
prim_v03 = MinimumSpanningTree_Prim_v03(L_gc_Numeric,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Prim con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v01[2].values())) +"\n"+
      " > Algoritmo di Prim con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v02[2].values())) +"\n"+
      " > Algoritmo di Prim con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v03[2].values())))


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
u = "Roma"   
prim_v01 = MinimumSpanningTree_Prim_v01(L_gc_Roman,u)
prim_v02 = MinimumSpanningTree_Prim_v02(L_gc_Roman,u)
prim_v03 = MinimumSpanningTree_Prim_v03(L_gc_Roman,u)

print("-----------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Roman Road Network: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Prim con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v01[2].values())) +"\n"+      
      " > Algoritmo di Prim con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v02[2].values())) +"\n"+      
      " > Algoritmo di Prim con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v03[2].values())) +"\n")


'Grafo Indiretto Connesso - Esempio Matrix  ----------------------------------'
u = "A"   
prim_v01 = MinimumSpanningTree_Prim_v01(L_gc_Matrix,u)
prim_v02 = MinimumSpanningTree_Prim_v02(L_gc_Matrix,u)
prim_v03 = MinimumSpanningTree_Prim_v03(L_gc_Matrix,u)

print("-----------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Matrix: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Prim con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v01[2].values())) +"\n"+  
      " > Algoritmo di Prim con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v02[2].values())) +"\n"+    
      " > Algoritmo di Prim con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(prim_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(prim_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(prim_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(prim_v03[2].values())) +"\n")