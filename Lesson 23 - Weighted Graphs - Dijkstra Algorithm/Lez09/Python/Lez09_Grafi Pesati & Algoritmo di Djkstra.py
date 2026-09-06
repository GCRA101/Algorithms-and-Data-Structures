# -*- coding: utf-8 -*-
"""
LEZIONE 09 - GRAFI PESATI e ALGORITMO di DIJKSTRA

I grafi pesati sono grafi ai cui archi e' assegnato un peso che definisce
il costo per attraversare ciascuno di essi sulla base di un certo parametro.
L'algoritmo di Dijktstra consente di ricavare i cammini minimi di un grafo 
pesato a partire da un nodo sorgente/radice arbitrario ed e' definito con tre 
formulazioni di costo computazionale differente.'
    
Algoritmo di Dijkstra
    - Formulazione classica con vettore - O(n*m)
    - Formulazione avanzata con vettore - O(n^2)
    - Formulazione avanzata con heap    - O((n+m)logn)
    
Algoritmi di utilita'
    - Ricerca cammino minimo tra due nodi specifici
    - Ricerca Nodi alla stessa Distanza Pesata da due nodi specifici
    - Ricerca Cammini vincolati al passaggio per determinati nodi
"""


" ALGORITMI *****************************************************************"

import math
from collections import deque
from decimal import Decimal


# ======================== ALGORITMO di DIJKSTRA ==============================


# ALGORITMO di DIJKSTRA - CLASSICO con VETTORE [Grafi Diretti e Indiretti]
# ------------------------------------------------------------------------
def ricercaCamminiMinimiPesati_v01(G,u):                    # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    dist = {key: math.inf for key in G}                     # Θ(n)
    padri[u] = u                                            # Θ(1)
    dist[u] = 0                                             # Θ(1)
    while True:                                             # Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        peso_min = math.inf                                 # Θ(1)
        for u in G:
            if padri[u] != -1:                              # Θ(1)
                for v in G[u]:
                    if padri[v[0]] == -1:                   # Θ(1)
                        peso = dist[u] + v[1]               # Θ(1)
                        if peso < peso_min:                 # Θ(1)
                            peso_min = peso                 # Θ(1)
                            u_min = u                       # Θ(1)
                            v_min = v[0]                    # Θ(1)
        if u_min == None:                                   # Θ(1)
            break                                           # Θ(1)
        padri[v_min] = u_min                                # Θ(1)
        dist[v_min] = peso_min                              # Θ(1)
    return padri, dist                                      # Θ(1)

# Costo Computazionale: O(n*m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso
# (##): Istruzioni aggiuntive/modificate rispetto alla BFS classica



# ALGORITMO di DIJKSTRA - AVANZATO con VETTORE [Grafi Diretti e Indiretti]
# ------------------------------------------------------------------------
def ricercaCamminiMinimiPesati_v02(G,s):                    # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    dist = {key: math.inf for key in G}                     # Θ(n)
    padri[s] = s                                            # Θ(1)
    dist[s] = 0                                             # Θ(1)
    A = list(G.keys())                                      # Θ(1)
    while len(A)!=0:                                        # n*Θ(1)+Θ(1)
        dist_min = math.inf                                 # Θ(1)
        for n in A:                                         # n*Θ(1)+Θ(1)
            if dist[n] < dist_min:                          # Θ(1)
                dist_min = dist[n]                          # Θ(1)
                u = n                                       # Θ(1)
        if u in A:                                          # Θ(1)
            A.remove(u)                                     # Θ(n) (##)
        else:                                               # Θ(1)
            u = A[0]                                        # Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if dist[u] + v[1] < dist[v[0]]:                 # Θ(1)
                padri[v[0]] = u                             # Θ(1)
                dist[v[0]] = dist[u] + v[1]                 # Θ(1)
    return padri, dist                                      # Θ(1)

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



# ALGORITMO di DIJKSTRA - AVANZATO con HEAP MINIMO [Grafi Diretti e Indiretti]
# ----------------------------------------------------------------------------

# Funzioni di supporto per l'Algoritmo di Dijkstra Avanzato ------------------

# HEAP MINIMO
# N   -> array dei nodi in ordine di Heap (la struttura vera e propria)
# D   -> array delle chiavi/priorita', parallelo a N (stessa posizione)
# pos -> dizionario nodo -> indice corrente in N/D
#
# 'pos' e' cio' che rende possibile il decremento chiave in O(logn): senza
# di esso, individuare la posizione di un nodo nell'Heap richiederebbe una
# ricerca O(n), vanificando il vantaggio della struttura dati.

# HEAPIFY - ripristina la proprieta' di Heap Minimo scendendo dalla radice
def heapify(N,D,pos,n,i):                       # T(n)
    left=2*i+1                                  # Θ(1)
    right=2*i+2                                 # Θ(1)
    if (left<n)and(D[left]<D[i]):               # Θ(1)
        iMin=left                               # Θ(1)
    else:                                       # Θ(1)
        iMin=i                                  # Θ(1)
    if (right<n)and(D[right]<D[iMin]):          # Θ(1)
        iMin=right                              # Θ(1)
    if iMin!=i:                                 # Θ(1)
        N[i],N[iMin] = N[iMin],N[i]             # Θ(1)
        D[i],D[iMin] = D[iMin],D[i]             # Θ(1)
        pos[N[i]] = i                           # Θ(1)
        pos[N[iMin]] = iMin                     # Θ(1)
        heapify(N,D,pos,n,iMin)                 # T(2/3n)
    return                                      # Θ(1)

# Costo Computazionale: O(logn) - altezza dell'Heap

# BUILDHEAP - costruisce l'Heap Minimo a partire dagli array N e D
def buildHeap(N,D,pos):                         # T(n)
    m=len(N)                                    # Θ(1)
    for i in range(m):                          # Θ(n)
        pos[N[i]]=i                             # Θ(1)
    for i in range(m//2-1,-1,-1):                # n/2*O(logn)+Θ(1)
        heapify(N,D,pos,m,i)
    return                                      # Θ(1)

# Costo Computazionale: O(n) - somma delle altezze di tutti i nodi dell'Heap

# ESTRAI MIN - estrae e restituisce il nodo con chiave (Dist) minima
def estraiMin(N,D,pos):                         # T(n)
    u = N[0]                                    # Θ(1) nodo di valore minimo
    ultimo = len(N)-1                           # Θ(1)
    N[0] = N[ultimo]                            # Θ(1)
    D[0] = D[ultimo]                            # Θ(1)
    pos[N[0]] = 0                               # Θ(1)
    N.pop()                                     # Θ(1)
    D.pop()                                     # Θ(1)
    del pos[u]                                  # Θ(1)
    if N:                                       # Θ(1)
        heapify(N,D,pos,len(N),0)               # O(logn)
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


# Algoritmo di Dijkstra - Avanzato con Heap Minimo ----------------------------
def ricercaCamminiMinimiPesati_v03(G,s):                    # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    dist = {key: math.inf for key in G}                     # Θ(n)
    padri[s] = s                                            # Θ(1)
    dist[s] = 0                                             # Θ(1)
    N = list(G.keys())                                      # Θ(n)
    D = [dist[nodo] for nodo in N]                          # Θ(n)
    pos = {}                                                # Θ(1)
    buildHeap(N,D,pos)                                      # O(n)
    while N:                                                # n*Θ(1)+Θ(1)
        u = estraiMin(N,D,pos)                              # O(logn)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if dist[u] + v[1] < dist[v[0]]:                 # Θ(1)
                padri[v[0]] = u                             # Θ(1)
                dist[v[0]] = dist[u] + v[1]                 # Θ(1)
                decrementaChiave(N,D,pos,v[0],dist[v[0]])   # O(logn)
    return padri, dist                                      # Θ(1)

# T(n,m) = 2*Θ(n) + 3*Θ(1) + Θ(n) + O(n) + Θ(n)*O(logn) + Θ(m)*O(logn)
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




# ======================== ALGORITMI di UTILITA' ==============================


# RICERCA CAMMINO MINIMO fra DUE NODI -----------------------------------------

# A partire dai vettori padri e distanze --------------------------------------
def ricercaCamminoMinimoPesato_v01(padri,dist,s,t):         # T(n)
    if (t not in padri) or (padri[t]==-1):                  # Θ(1)
        return None, None                                   # Θ(1)
    cammino = [t]                                           # Θ(1)
    nodo = t                                                # Θ(1)
    while nodo != s:
        nodo = padri[nodo]                                  # Θ(1)
        cammino.append(nodo)                                # Θ(1)
    cammino.reverse()                                       # Θ(n)
    distanze = []                                           # Θ(1)
    for nodo in cammino:                                    # n*Θ(1)+Θ(1)
        distanze.append(dist[nodo])                         # Θ(1)
    return cammino, distanze                                # Θ(1)

# IMPORTANTE!
# Prima di eseguire l'algoritmo sopra, bisogna eseguire l'algortimo di Dijkstra
# per poter ottenere il vettore padri e dist da passargli in input !
# Il nodo sorgente s deve coincidere con il nodo usato come radice della 
# ricerca di tutti i cammini minimi tramite algoritmo di Dijkstra !

# Costo Computazionale : O(n) - CASO PEGGIORE (*)
#                        Ω(1) - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso


# A partire dal Grafo ---------------------------------------------------------
def ricercaCamminoMinimoPesato_v02(G,s,t):                  # T(n)
    padri, dist = ricercaCamminiMinimiPesati_v03(G,s)       # O((n+m)logn)
    if (t not in padri) or (padri[t]==-1):                  # Θ(1)
        return None, None                                   # Θ(1)
    cammino = [t]                                           # Θ(1)
    nodo = t                                                # Θ(1)
    while nodo != s:
        nodo = padri[nodo]                                  # Θ(1)
        cammino.append(nodo)                                # Θ(1)
    cammino.reverse()                                       # Θ(n)
    distanze = []                                           # Θ(1)
    for nodo in cammino:                                    # n*Θ(1)+Θ(1)
        distanze.append(dist[nodo])                         # Θ(1)
    return cammino, distanze                                # Θ(1)

# IMPORTANTE! 
# Prima di poter ricavare cammino minimo e distanze dai nodi s e t in input,
# e' necessario eseguire l'algoritmo di Dijkstra sul Grafo considerando il nodo
# s come radice da cui farlo partire !

# Costo Computazionale : O((n+m)logn) - CASO PEGGIORE (*)
#                        Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso



# RICERCA NODI alla STESSA DISTANZA PESATA [Grafi Indiretti e Connessi] -------

# A partire dal Grafo ---------------------------------------------------------
def ricercaNodiStessaDist(G,u,v):                           # T(n,m)
    dist_u = ricercaCamminiMinimiPesati_v03(G,u)[1]         # O((n+m)logn)
    dist_v = ricercaCamminiMinimiPesati_v03(G,v)[1]         # O((n+m)logn)
    nodi = []                                               # Θ(1)
    for w in G.keys():                                      # n*Θ(1)+Θ(1)
        if dist_u[w]==dist_v[w] and dist_u[w]!=math.inf:    # Θ(1)
            nodi.append(w)                                  # Θ(1)
    return nodi                                             # Θ(1)

# Costo Computazionale: O((n+m)logn) - CASO PEGGIORE (*)
#                       Ω(1)         - CASO MIGLIORE (**)
#
# (*): Nodi di partenza connessi a tutti i nodi del grafo
# (**): Nodi di partenza completamente disconnessi



# RICERCA CAMMINIMI MINIMI VINCOLATI AL PASSAGGIO PER DETERMINATI NODI --------

# Algoritmo di Trasposizione del Grafo ----------------------------------------
def grafoTrasposto_la(G):                                   # S(n,m)
    GT = {v:[] for v in G}                                  # Θ(n)
    for u in G:                                             # n*Θ(1)+Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            GT[v[0]].append([u,v[1]])                       # Θ(1)
    return GT                                               # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
# (*):  Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso


# A partire dal Grafo ---------------------------------------------------------
# Funzione main
def ricercaCamminoVincolato(G,u,v,r):                           # T(n,m)
    padri, dist = ricercaCamminiMinimiPesati_v03(G,r)           # Θ((n+m)logn)
    GT = grafoTrasposto_la(G)                                   # Θ(n+m)
    padriT, distT = ricercaCamminiMinimiPesati_v03(GT,r)        # Θ((n+m)logn)
    C_u = []                                                    # Θ(1)
    D_u = []                                                    # Θ(1)
    u0 = u                                                      # Θ(1)
    while True:                                                 # k*Θ(1)+Θ(1)
        if padriT[u] == -1:                                     # Θ(1)
            return None, None                                   # Θ(1)
        C_u.append(u)                                           # Θ(1)
        D_u.append(dist[u0]- dist[u])                           # Θ(1)
        u = padriT[u]                                           # Θ(1)
        if not u != r:                                          # Θ(1)
            C_u.append(r)                                       # Θ(1)
            D_u.append(dist[u0] - dist[r])                      # Θ(1)
            break                                               # Θ(1)
    C_v = []                                                    # Θ(1)
    D_v = []                                                    # Θ(1)
    while v != r and v != -1:                                   # s*Θ(1)+Θ(1)
        if padri[v] == -1:                                      # Θ(1)
            return None, None                                   # Θ(1)
        C_v.insert(0, v)                                        # Θ(1)
        D_v.insert(0,dist[u0] + dist[v])                        # Θ(1)
        v = padri[v]                                            # Θ(1)
    C = C_u + C_v                                               # Θ(k+s)
    D = D_u + D_v                                               # Θ(k+s)
    return C, D                                                 # Θ(1)

# T(n,m) = Θ((n+m)logn) + Θ(n+m) + O(n) + O(n) = Θ((n+m)logn)
#
# Costo Computazionale: O((n+m)logn) - CASO PEGGIORE (*)
#                       Ω(1)         - CASO MIGLIORE (**)
# (*):  Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso


" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi un
esempio ispirato all'utilizzo di Uber a Londra e un esempio ispirato al 
movimento automatizzato dei robot nei centri di smaltimento di Amazon.

"""

# LISTE DI ADIACENZA ----------------------------------------------------------

'Grafo Indiretto Non Connesso ------------------------------------------------' 
L_gnc={0: [(1,8),(2,2),(4,15)],
       1: [(0,8),(2,13),(3,4)],
       2: [(0,2),(1,13),(3,7),(4,10),(5,1)],
       3: [(1,4),(2,7),(4,2)],
       4: [(0,15),(2,10),(3,2)],
       5: [(2,1)],
       6: [(7,2),(8,11)],
       7: [(6,2),(8,6)],
       8: [(6,11),(7,6)]}

'Grafo Indiretto Connesso - Esempio Uber -------------------------------------' 
L_gc_Uber = {
    "Angel": [("Chapel Market", Decimal("0.3")), 
              ("Islington Green", Decimal("0.6")), 
              ("Sadler's Wells", Decimal("0.5"))],
    "Barnsbury": [("Brewery Road", Decimal("0.8")), 
                  ("Caledonian Road", Decimal("1.1")), 
                  ("Islington Green", Decimal("1.5"))],
    "Brewery Road": [("Barnsbury", Decimal("0.8")), 
                     ("Caledonian Road", Decimal("0.5"))],
    "Caledonian Road": [("Barnsbury", Decimal("1.1")), 
                        ("Brewery Road", Decimal("0.5")), 
                        ("Chapel Market", Decimal("2.5")), 
                        ("King's Cross", Decimal("2.4"))],
    "Chapel Market": [("Angel", Decimal("0.3")), 
                      ("Caledonian Road", Decimal("2.5")), 
                      ("Penton Rise", Decimal("0.8"))],
    "Euston": [("Mornington Cr.", Decimal("1.0")), 
               ("St Pancras", Decimal("0.8")), 
               ("Warren Street", Decimal("0.7"))],
    "Exmouth Market": [("Mount Pleasant", Decimal("0.4")), 
                       ("Sadler's Wells", Decimal("0.7"))],
    "Gower St.": [("Russell Square", Decimal("0.7")), 
                  ("Warren Street", Decimal("0.7"))],
    "Islington Green": [("Angel", Decimal("0.6")), 
                        ("Barnsbury", Decimal("1.5"))],
    "King's Cross": [("Caledonian Road", Decimal("2.4")), 
                     ("Mount Pleasant", Decimal("1.4")), 
                     ("Penton Rise", Decimal("0.9")), 
                     ("St Pancras", Decimal("0.4")), 
                     ("Swinton Street", Decimal("0.6")), 
                     ("Tavistock Square", Decimal("1.2"))],
    "Marchmont Street": [("Russell Square", Decimal("0.5")), 
                         ("Tavistock Square", Decimal("0.4"))],
    "Mornington Cr.": [("Euston", Decimal("1")), 
                       ("Warren Street", Decimal("1.4"))],
    "Mount Pleasant": [("Exmouth Market", Decimal("0.4")), 
                       ("King's Cross", Decimal("1.4")), 
                       ("Sadler's Wells", Decimal("0.7")), 
                       ("Swinton Street", Decimal("0.9"))],
    "Penton Rise": [("Chapel Market", Decimal("0.8")), 
                    ("King's Cross", Decimal("0.9"))],
    "Russell Square": [("Gower St.", Decimal("0.7")), 
                       ("Marchmont Street", Decimal("0.5")), 
                       ("Tavistock Square", Decimal("0.5"))],
    "Sadler's Wells": [("Angel", Decimal("0.5")), 
                       ("Exmouth Market", Decimal("0.7")), 
                       ("Mount Pleasant", Decimal("0.7"))],
    "St Pancras": [("Euston", Decimal("0.8")), 
                   ("King's Cross", Decimal("0.4"))],
    "Swinton Street": [("King's Cross", Decimal("0.6")), 
                       ("Mount Pleasant", Decimal("0.9"))],
    "Tavistock Square": [("King's Cross", Decimal("1.2")), 
                         ("Marchmont Street", Decimal("0.4")), 
                         ("Russell Square", Decimal("0.5"))],
    "Warren Street": [("Euston", Decimal("0.7")), 
                      ("Gower St.", Decimal("0.7")), 
                      ("Mornington Cr.", Decimal("1.4"))]
}

'Grafo Indiretto Connesso - Esempio Amazon Robots ----------------------------' 
L_gc_Amazon = {
    "A01": [("B01", 1.5)],
    "A02": [],
    "A03": [],
    "A04": [],
    "A05": [("B05", 1.5)],
    "A06": [],
    "A07": [("A08", 1.5)],
    "A08": [("A07", 1.5), ("A09", 1.5)],
    "A09": [("A08", 1.5), ("A10", 1.5)],
    "A10": [("A09", 1.5)],
    "B01": [("A01", 1.5), ("B02", 1.5), ("C01", 1.5)],
    "B02": [("B01", 1.5), ("B03", 1.5)],
    "B03": [("B02", 1.5), ("C03", 1.5)],
    "B04": [],
    "B05": [("A05", 1.5), ("B06", 1.5), ("C05", 1.5)],
    "B06": [("B05", 1.5), ("C06", 1.5)],
    "B07": [],
    "B08": [],
    "B09": [],
    "B10": [],
    "C01": [("B01", 1.5), ("D01", 1.5)],
    "C02": [],
    "C03": [("B03", 1.5), ("C04", 1.5), ("D03", 1.5)],
    "C04": [("C03", 1.5), ("C05", 1.5), ("D04", 1.5)],
    "C05": [("B05", 1.5), ("C04", 1.5), ("C06", 1.5), ("D05", 1.5)],
    "C06": [("B06", 1.5), ("C05", 1.5), ("C07", 1.5), ("D06", 1.5)],
    "C07": [("C06", 1.5), ("C08", 1.5), ("D07", 1.5)],
    "C08": [("C07", 1.5), ("D08", 1.5)],
    "C09": [],
    "C10": [],
    "D01": [("C01", 1.5), ("D02", 1.5), ("E01", 1.5)],
    "D02": [("D01", 1.5), ("D03", 1.5), ("E02", 1.5)],
    "D03": [("C03", 1.5), ("D02", 1.5), ("D04", 1.5)],
    "D04": [("C04", 1.5), ("D03", 1.5), ("D05", 1.5), ("E04", 1.5)],
    "D05": [("C05", 1.5), ("D04", 1.5), ("D06", 1.5), ("E05", 1.5)],
    "D06": [("C06", 1.5), ("D05", 1.5), ("D07", 1.5), ("E06", 1.5)],
    "D07": [("C07", 1.5), ("D06", 1.5), ("D08", 1.5), ("E07", 1.5)],
    "D08": [("C08", 1.5), ("D07", 1.5), ("D09", 1.5)],
    "D09": [("D08", 1.5), ("D10", 1.5)],
    "D10": [("D09", 1.5), ("E10", 1.5)],
    "E01": [("D01", 1.5), ("E02", 1.5), ("F01", 1.5)],
    "E02": [("D02", 1.5), ("E01", 1.5), ("F02", 1.5)],
    "E03": [],
    "E04": [("D04", 1.5), ("E05", 1.5)],
    "E05": [("D05", 1.5), ("E04", 1.5), ("E06", 1.5)],
    "E06": [("D06", 1.5), ("E05", 1.5), ("E07", 1.5)],
    "E07": [("D07", 1.5), ("E06", 1.5), ("F07", 1.5)],
    "E08": [],
    "E09": [],
    "E10": [("D10", 1.5), ("F10", 1.5)],
    "F01": [("E01", 1.5), ("F02", 1.5)],
    "F02": [("E02", 1.5), ("F01", 1.5), ("F03", 1.5), ("G02", 1.5)],
    "F03": [("F02", 1.5), ("G03", 1.5)],
    "F04": [],
    "F05": [],
    "F06": [],
    "F07": [("E07", 1.5), ("F08", 1.5), ("G07", 1.5)],
    "F08": [("F07", 1.5), ("G08", 1.5)],
    "F09": [],
    "F10": [("E10", 1.5), ("G10", 1.5)],
    "G01": [],
    "G02": [("F02", 1.5), ("G03", 1.5), ("H02", 1.5)],
    "G03": [("F03", 1.5), ("G02", 1.5), ("G04", 1.5), ("H03", 1.5)],
    "G04": [("G03", 1.5), ("H04", 1.5)],
    "G05": [],
    "G06": [("G07", 1.5), ("H06", 1.5)],
    "G07": [("F07", 1.5), ("G06", 1.5), ("G08", 1.5)],
    "G08": [("F08", 1.5), ("G07", 1.5), ("G09", 1.5), ("H08", 1.5)],
    "G09": [("G08", 1.5), ("G10", 1.5)],
    "G10": [("F10", 1.5), ("G09", 1.5), ("H10", 1.5)],
    "H01": [("H02", 1.5), ("I01", 1.5)],
    "H02": [("G02", 1.5), ("H01", 1.5), ("H03", 1.5)],
    "H03": [("G03", 1.5), ("H02", 1.5), ("H04", 1.5), ("I03", 1.5)],
    "H04": [("G04", 1.5), ("H03", 1.5), ("I04", 1.5)],
    "H05": [],
    "H06": [("G06", 1.5)],
    "H07": [],
    "H08": [("G08", 1.5), ("I08", 1.5)],
    "H09": [],
    "H10": [("G10", 1.5), ("I10", 1.5)],
    "I01": [("H01", 1.5), ("J01", 1.5)],
    "I02": [],
    "I03": [("H03", 1.5), ("I04", 1.5), ("J03", 1.5)],
    "I04": [("H04", 1.5), ("I03", 1.5), ("I05", 1.5)],
    "I05": [("I04", 1.5), ("J05", 1.5)],
    "I06": [],
    "I07": [("I08", 1.5), ("J07", 1.5)],
    "I08": [("H08", 1.5), ("I07", 1.5), ("I09", 1.5), ("J08", 1.5)],
    "I09": [("I08", 1.5), ("I10", 1.5), ("J09", 1.5)],
    "I10": [("H10", 1.5), ("I09", 1.5), ("J10", 1.5)],
    "J01": [("I01", 1.5), ("J02", 1.5)],
    "J02": [("J01", 1.5), ("J03", 1.5)],
    "J03": [("I03", 1.5), ("J02", 1.5)],
    "J04": [],
    "J05": [("I05", 1.5), ("J06", 1.5)],
    "J06": [("J05", 1.5), ("J07", 1.5)],
    "J07": [("I07", 1.5), ("J06", 1.5), ("J08", 1.5)],
    "J08": [("I08", 1.5), ("J07", 1.5), ("J09", 1.5)],
    "J09": [("I09", 1.5), ("J08", 1.5), ("J10", 1.5)],
    "J10": [("I10", 1.5), ("J09", 1.5)]
}


            
# ALGORITMO di DIJKSTRA con LISTE di ADIACENZA --------------------------------

print("\nRICERCA CAMMINI MINIMI in GRAFO PESATO tramite DIJKSTRA ************"+
      "****************************************************************"+"\n")

'Grafo Indiretto Non Connesso - Esempio Numerico -----------------------------'
u = 0                           
djk01_01=ricercaCamminiMinimiPesati_v01(L_gnc,u)                                
djk01_02=ricercaCamminiMinimiPesati_v02(L_gnc,u)
djk01_03=ricercaCamminiMinimiPesati_v03(L_gnc,u)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Non Connesso - Esempio Numerico: "+"\n"+
      "Ricerca Cammini Minimi in Grafo Pesato "+"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk01_01[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk01_01[1]) +"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk01_02[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk01_02[1]) +"\n"+
      " > Algoritmo di Dijkstra con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk01_03[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk01_03[1]) +"\n")


'Grafo Indiretto Connesso 02 - Esempio Uber ----------------------------------'
u = "King's Cross"                           
djk02_01=ricercaCamminiMinimiPesati_v01(L_gc_Uber,u)                                
djk02_02=ricercaCamminiMinimiPesati_v02(L_gc_Uber,u)
djk02_03=ricercaCamminiMinimiPesati_v03(L_gc_Uber,u)

round_djk02_01 = {k: round(v, 1) for k, v in djk02_01[1].items()}
round_djk02_02 = {k: round(v, 1) for k, v in djk02_02[1].items()}
round_djk02_03 = {k: round(v, 1) for k, v in djk02_03[1].items()}

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Uber: "+"\n"+
      "Ricerca Cammini Minimi in Grafo Pesato "+"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk02_01[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(round_djk02_01) +"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk02_02[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(round_djk02_02) +"\n"+
      " > Algoritmo di Dijkstra con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk02_03[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(round_djk02_03) +"\n")


'Grafo Indiretto Connesso 03 - Esempio Amazon --------------------------------'
u = "A01"                           
djk03_01=ricercaCamminiMinimiPesati_v01(L_gc_Amazon,u)                                
djk03_02=ricercaCamminiMinimiPesati_v02(L_gc_Amazon,u)
djk03_03=ricercaCamminiMinimiPesati_v03(L_gc_Amazon,u)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Amazon: "+"\n"+
      "Ricerca Cammini Minimi in Grafo Pesato "+"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n*m)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk03_01[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk03_01[1]) +"\n"+
      " > Algoritmo di Dijkstra con Vettore [O(n^2)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk03_02[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk03_02[1]) +"\n"+
      " > Algoritmo di Dijkstra con Heap Minimo [O((n+m)*logn)]: "+"\n"+
      "    - Vettore dei Padri: "+ str(djk03_03[0]) +"\n"+
      "    - Vettore dei delle Distanze: "+ str(djk03_03[1]) +"\n")



# RICERCA CAMMINO MINIMO FRA 2 NODI ------------------------------------------

print("\nRICERCA CAMMINO MINIMO fra 2 NODI ******************************"+
      "****************************************************************"+"\n")

'Grafo Indiretto Non Connesso - Esempio Numerico -----------------------------'

'Da vettore dei padri e delle distanze'
s1, t1 = 0, 4
padri = djk01_03[0]
distanze = djk01_03[1]
va01 = ricercaCamminoMinimoPesato_v01(padri,distanze, s1, t1)
'Da grafo pesato'
s2, t2 = 1, 2
va02 = ricercaCamminoMinimoPesato_v02(L_gnc, s2, t2)
'Da grafo pesato'
s3, t3 = 3, 8 
va03 = ricercaCamminoMinimoPesato_v02(L_gnc, s3, t3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Ricerca Cammino Minimo Pesato fra 2 nodi "+"\n"+
      "("+str(s1)+","+str(t1)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(va01[1])+"\n"+
      "("+str(s2)+","+str(t2)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(va02[1])+"\n"+
      "("+str(s3)+","+str(t3)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(va03[1])+"\n")


'Grafo Indiretto Connesso 02 - Esempio Uber ----------------------------------'

'Da vettore dei padri e delle distanze'
s1, t1 = "King's Cross", "Islington Green"
padri = djk02_03[0]
distanze = djk02_03[1]
va01 = ricercaCamminoMinimoPesato_v01(padri,distanze, s1, t1)
'Da grafo pesato'
s2, t2 = "Chapel Market", "Barnsbury"
va02 = ricercaCamminoMinimoPesato_v02(L_gc_Uber, s2, t2)
'Da grafo pesato'
s3, t3 = "Swinton Street", "Chapel Market" 
va03 = ricercaCamminoMinimoPesato_v02(L_gc_Uber, s3, t3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Uber: "+"\n"+
      "Ricerca Cammino Minimo Pesato fra 2 nodi "+"\n"+
      "("+str(s1)+","+str(t1)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(va01[1])+"\n"+
      "("+str(s2)+","+str(t2)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(va02[1])+"\n"+
      "("+str(s3)+","+str(t3)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(va03[1])+"\n")


'Grafo Indiretto Connesso 03 - Esempio Amazon --------------------------------'

'Da vettore dei padri e delle distanze'
s1, t1 = "A01", "J10"
padri = djk03_03[0]
distanze = djk03_03[1]
va01 = ricercaCamminoMinimoPesato_v01(padri,distanze, s1, t1)
'Da grafo pesato'
s2, t2 = "J01", "J10"
va02 = ricercaCamminoMinimoPesato_v02(L_gc_Amazon, s2, t2)
'Da grafo pesato'
s3, t3 = "A07", "J10" 
va03 = ricercaCamminoMinimoPesato_v02(L_gc_Amazon, s3, t3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Amazon: "+"\n"+
      "Ricerca Cammino Minimo Pesato fra 2 nodi "+"\n"+
      "("+str(s1)+","+str(t1)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(va01[1])+"\n"+
      "("+str(s2)+","+str(t2)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(va02[1])+"\n"+
      "("+str(s3)+","+str(t3)+")" +"\n"+ 
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(va03[1])+"\n")



# RICERCA NODI alla STESSA DISTANZA PESATA [Grafi Indiretti e Connessi] -------

print("\nRICERCA NODI alla STESSA DISTANZA PESATA ***********************"+
      "****************************************************************"+"\n")

'Grafo Indiretto Non Connesso - Esempio Numerico -----------------------------'

'Da grafo pesato'
u1, v1 = 0, 3
va01 = ricercaNodiStessaDist(L_gnc, u1, v1)
u2, v2 =  1, 5
va02 = ricercaNodiStessaDist(L_gnc, u2, v2)
u3, v3 = 3, 8
va03 = ricercaNodiStessaDist(L_gnc, u3, v3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Ricerca Nodi alla stessa Distanza Pesata da u e v"+"\n"+
      "("+str(u1)+","+str(v1)+")"+"\n"+
      " -> Lista Nodi: "+ str(va01)+"\n"+
      "("+str(u2)+","+str(v2)+")"+"\n"+
      " -> Lista Nodi: "+ str(va02)+"\n"+
      "("+str(u3)+","+str(v3)+")"+"\n"+
      " -> Lista Nodi: "+ str(va03)+"\n")


'Grafo Indiretto Connesso 02 - Esempio Uber ----------------------------------'

'Da grafo pesato'
u1, v1 = "Euston", "Tavistock Square"
va01 = ricercaNodiStessaDist(L_gc_Uber, u1, v1)
u2, v2 = "Euston", "St Pancras"
va02 = ricercaNodiStessaDist(L_gc_Uber, u2, v2)
u3, v3 = "Euston", "King's Cross"
va03 = ricercaNodiStessaDist(L_gc_Uber, u3, v3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Uber: "+"\n"+
      "Ricerca Nodi alla stessa Distanza Pesata da u e v"+"\n"+
      "("+str(u1)+","+str(v1)+")"+"\n"+
      " -> Lista Nodi: "+ str(va01)+"\n"+
      "("+str(u2)+","+str(v2)+")"+"\n"+
      " -> Lista Nodi: "+ str(va02)+"\n"+
      "("+str(u3)+","+str(v3)+")"+"\n"+
      " -> Lista Nodi: "+ str(va03)+"\n")


'Grafo Indiretto Connesso 03 - Esempio Amazon --------------------------------'

'Da grafo pesato'
u1, v1 = "A01", "J10"
va01 = ricercaNodiStessaDist(L_gc_Amazon, u1, v1)
u2, v2 = "A01", "J10"
va02 = ricercaNodiStessaDist(L_gc_Amazon, u2, v2)
u3, v3 = "A01", "J10"
va03 = ricercaNodiStessaDist(L_gc_Amazon, u3, v3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Amazon: "+"\n"+
      "Ricerca Nodi alla stessa Distanza Pesata da u e v"+"\n"+
      "("+str(u1)+","+str(v1)+")"+"\n"+
      " -> Lista Nodi: "+ str(va01)+"\n"+
      "("+str(u2)+","+str(v2)+")"+"\n"+
      " -> Lista Nodi: "+ str(va02)+"\n"+
      "("+str(u3)+","+str(v3)+")"+"\n"+
      " -> Lista Nodi: "+ str(va03)+"\n")



# RICERCA CAMMINIMI MINIMO VINCOLATO AL PASSAGGIO PER DETERMINATO NODO --------

print("\nRICERCA CAMMINIMI MINIMO VINCOLATO AL PASSAGGIO PER DETERMINATO NODO"+
      "****************************************************************"+"\n")

'Grafo Indiretto Non Connesso - Esempio Numerico -----------------------------'

'Da grafo pesato'
u1, v1, r1 = 0, 3, 4
va01 = ricercaCamminoVincolato(L_gnc, u1, v1, r1)
u2, v2, r2 =  1, 5, 2
va02 = ricercaCamminoVincolato(L_gnc, u2, v2, r2)
u3, v3, r3 = 3, 8, 1 
va03 = ricercaCamminoVincolato(L_gnc, u3, v3, r3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Ricerca Cammino Vincolato a Passaggio per Determinato Nodo"+"\n"+
      "("+str(u1)+","+str(v1)+","+str(r1)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(va01[1])+"\n"+
      "("+str(u2)+","+str(v2)+","+str(r2)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(va02[1])+"\n"+
      "("+str(u3)+","+str(v3)+","+str(r3)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(va03[1])+"\n")


'Grafo Indiretto Connesso 02 - Esempio Uber ----------------------------------'

'Da grafo pesato'
u1, v1, r1 = "King's Cross", "Swinton Street", "Angel"
va01 = ricercaCamminoVincolato(L_gc_Uber, u1, v1, r1)
u2, v2, r2 = "Russell Square", "Euston", "Caledonian Road"
va02 = ricercaCamminoVincolato(L_gc_Uber, u2, v2, r2)
u3, v3, r3 = "St Pancras", "Angel", "Exmouth Market"
va03 = ricercaCamminoVincolato(L_gc_Uber, u3, v3, r3)

round_va01 = [round(v, 1) for v in va01[1]]
round_va02 = [round(v, 1) for v in va02[1]]
round_va03 = [round(v, 1) for v in va03[1]]

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Uber: "+"\n"+
      "Ricerca Cammino Vincolato a Passaggio per Determinato Nodo"+"\n"+
      "("+str(u1)+","+str(v1)+","+str(r1)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(round_va01)+"\n"+
      "("+str(u2)+","+str(v2)+","+str(r2)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(round_va02)+"\n"+
      "("+str(u3)+","+str(v3)+","+str(r3)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(round_va03)+"\n")


'Grafo Indiretto Connesso 03 - Esempio Amazon --------------------------------'

'Da grafo pesato'
u1, v1, r1 = "A01", "J10", "F03"
va01 = ricercaCamminoVincolato(L_gc_Amazon, u1, v1, r1)
u2, v2, r2 = "A01", "J10", "H06"
va02 = ricercaCamminoVincolato(L_gc_Amazon, u2, v2, r2)
u3, v3, r3 = "A01", "J10", "A08" 
va03 = ricercaCamminoVincolato(L_gc_Amazon, u3, v3, r3)

print("------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Amazon: "+"\n"+
      "Ricerca Cammino Vincolato a Passaggio per Determinato Nodo"+"\n"+
      "("+str(u1)+","+str(v1)+","+str(r1)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va01[0])+"\n"+
      " -> Distanze Minime: "+ str(va01[1])+"\n"+
      "("+str(u2)+","+str(v2)+","+str(r2)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va02[0])+"\n"+
      " -> Distanze Minime: "+ str(va02[1])+"\n"+
      "("+str(u3)+","+str(v3)+","+str(r3)+")"+"\n"+
      " -> Cammino Minimo: "+ str(va03[0])+"\n"+
      " -> Distanze Minime: "+ str(va03[1])+"\n")



