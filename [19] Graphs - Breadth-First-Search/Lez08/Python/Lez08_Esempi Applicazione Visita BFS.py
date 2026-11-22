# -*- coding: utf-8 -*-
"""
LEZIONE 08 - ESEMPI DI APPLICAZIONE VISITA BFS

Algoritmi di utilita' tramite uso di BFS
    - Conteggio Numero Cammini Minimi
    - Ricerca Nodi alla stessa Distanza
    - Calcolo Distanza tra Due Insiemi
    - Ricerca Cammini vincolati al passaggio per determinati nodi
    - Calcolo Distanze a partire dall'Albero dei Padri della BFS
    
"""


" ALGORITMI *****************************************************************"

import math
from collections import deque

# BFS con LISTE di ADIACENZA
def BFS_la(G,u):                                            # T(n,m)
    padri = {key: -1 for key in G}                          # Θ(n)
    dist = {key: math.inf for key in G}                     # Θ(n)
    padri[u] = u                                            # Θ(1)
    dist[u] = 0                                             # Θ(1)
    q = deque()                                             # Θ(1)
    q.append(u)                                             # Θ(1)
    while len(q)!=0:                                        # v*Θ(1)+Θ(1)
        u = q.popleft()                                     # Θ(1)
        for y in G[u]:                                      # k*Θ(1)+Θ(1)
            if padri[y] == -1:                              # Θ(1)
                padri[y] = u                                # Θ(1)
                dist[y] = dist[u] + 1                       # Θ(1)
                q.append(y)                                 # Θ(1)
        print(str(u) + " <-- " + str(q))                    # Θ(1)
    return padri, dist                                      # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso

# ----------------------------------------------------------------------------

# CONTEGGIO NUMERO CAMMINI MINIMI [Grafi Diretti e Indiretti]
def conteggioCamminiMinimi(G,u):                            # T(n,m)
    minimi = {key: 0 for key in G}                          # Θ(n)   (##)
    dist = {key: math.inf for key in G}                     # Θ(n)
    dist[u] = 0                                             # Θ(1)
    minimi[u] = 1                                           # Θ(1)   (##)
    q = deque()                                             # Θ(1)
    q.append(u)                                             # Θ(1)
    while len(q)!=0:                                        # v*Θ(1)+Θ(1)
        u = q.popleft()                                     # Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if dist[v] == math.inf:                         # Θ(1)
                dist[v] = dist[u] + 1                       # Θ(1) 
                minimi[v] = minimi[u]                       # Θ(1)   (##)
                q.append(v)                                 # Θ(1)
            else:                                           # Θ(1)   (##)
                if dist[v] == dist[u] + 1:                  # Θ(1)   (##)
                    minimi[v] = minimi[v] + minimi[u]       # Θ(1)   (##)
        print(str(u) + " <-- " + str(q))                    # Θ(1)
    return minimi, dist                                     # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso
# (##): Istruzioni aggiuntive/modificate rispetto alla BFS classica


# RICERCA NODI alla STESSA DISTANZA [Grafi Indiretti e Connessi]
def ricercaNodiStessaDist(G,u,v):                           # T(n,m)
    dist_u = BFS_la(G,u)[1]                                 # O(n+m)
    dist_v = BFS_la(G,v)[1]                                 # O(n+m)
    nodi = []                                               # Θ(1)
    for w in G.keys():                                      # n*Θ(1)+Θ(1)
        if dist_u[w]==dist_v[w] and dist_u[w]!=math.inf:    # Θ(1)
            nodi.append(w)                                  # Θ(1)
    print("Dist_u: " + str(dist_u.values()) + "\n" +
          "Dist_v: " + str(dist_v.values()) + "\n" )        # Θ(1)
    return nodi                                             # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodi di partenza connessi a tutti i nodi del grafo
# (**): Nodi di partenza completamente disconnessi


# CALCOLO DISTANZA tra DUE INSIEMI [Grafi Indiretti]

# Algoritmo BFS Modificato
def BFS_SET(G,A):                                           # S(n,m)
    dist_A = {key: math.inf for key in G}                   # Θ(n)
    q = deque()                                             # Θ(1)
    for u in A:                                             # a*Θ(1)+Θ(1) (##)
        dist_A[u] = 0                                       # Θ(1)        (##)
        q.append(u)                                         # Θ(1)        (##)
    while len(q)!=0:                                        # v*Θ(1)+Θ(1)
        u = q.popleft()                                     # Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            if dist_A[v] == math.inf:                       # Θ(1)
                dist_A[v] = dist_A[u] + 1                   # Θ(1)
                q.append(v)                                 # Θ(1)
        print(str(u) + " <-- " + str(q))                    # Θ(1)
    return dist_A                                           # Θ(1)

# Funzione main
def calcoloDistInsiemi(G,A,B):                              # T(n,m)
    dist_A = BFS_SET(G,A)                                   # O(n+m)
    d = math.inf                                            # Θ(1)
    for u in B:                                             # b*Θ(1)+Θ(1)
        if dist_A[u] < d:                                   # Θ(1)
            d = dist_A[u]                                   # Θ(1)
    return d                                                # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*):  Nodi di partenza connessi a tutti i nodi del grafo
# (**): Nodi di partenza completamente disconnessi
# (##): Istruzioni aggiuntive/modificate rispetto alla BFS classica


# RICERCA CAMMINI VINCOLATI al PASSAGGIO per DETERMINATI NODI

# Algoritmo di Trasposizione del Grafo
def grafoTrasposto_la(G):                                   # S(n,m)
    GT = {v:[] for v in G}                                  # Θ(n)
    for u in G:                                             # n*Θ(1)+Θ(1)
        for v in G[u]:                                      # k*Θ(1)+Θ(1)
            GT[v].append(u)                                 # Θ(1)
    return GT                                               # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
# (*):  Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso

# Funzione main
def ricercaCamminiVincolati(G,u,v,r):                       # T(n,m)
    padri = BFS_la(G,r)[0]                                  # O(n+m)
    GT = grafoTrasposto_la(G)                               # O(n+m)
    padriT = BFS_la(GT,r)[0]                                # O(n+m)
    C_u = []                                                # Θ(1)
    while True:                                             # k*Θ(1)+Θ(1) 
        C_u.append(u)                                       # Θ(1)
        u = padriT[u]                                       # Θ(1)
        if not u != r:                                      # Θ(1)
            C_u.append(r)                                   # Θ(1)
            break                                           # Θ(1)
    C_v = []                                                # Θ(1)
    while v != r and v != -1:                               # s*Θ(1)+Θ(1) 
        C_v.insert(0, v)                                    # Θ(1)
        v = padri[v]                                        # Θ(1)
    C = C_u + C_v                                           # Θ(k+s)
    return C                                                # Θ(1)

# Costo Computazionale: O(n+m) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
# (*):  Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso


# CALCOLO DISTANZE a partire dall'ALBERO dei PADRI della BFS

# Funzione ausiliaria ricorsiva
def DIST(v, padri, dist):                                   # S(n)
    if padri[v] == v:                                       # Θ(1)
        return 0                                            # Θ(1)
    if padri[v] == -1:                                      # Θ(1)
        return -1                                           # Θ(1)
    if dist[padri[v]]!=-1:                                  # Θ(1)
        return dist[padri[v]] + 1                           # Θ(1)
    h = DIST(padri[v], padri, dist)                         # S(n-1)
    return h + 1                                            # Θ(1)

# Funzione main
def calcoloDistDaPadriBFS(padri_BFS):                       # T(n,m)
    dist = {key:-1 for key in padri_BFS}                    # Θ(n)
    for w in padri_BFS:                                     # n*Θ(1)+Θ(1) 
        if dist[w] == -1:                                   # Θ(1)
            dist[w] = DIST(w, padri_BFS, dist)              # S(n)
    return dist                                             # Θ(1)
            
# Costo Computazionale: O(n)   - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
# (*):  Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso  


" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi un
esempio ispirato all'utilizzo di Uber a Londra.

"""

# LISTE DI ADIACENZA

'Grafo Indiretto Non Connesso' 
L_gnc={0: [1,2,4],
       1: [0,2,3],
       2: [0,1,3,4],
       3: [1,2,4],
       4: [0,2,3],
       5: [6,7],
       6: [5,7],
       7: [5,6]}

'Grafo Indiretto Connesso'
L_gc = {
    "Angel":            ["Chapel Market", "Islington Green", "Sadler's Wells"],
    "Barnsbury":        ["Brewery Road", "Caledonian Road", "Islington Green"],
    "Brewery Road":     ["Barnsbury", "Caledonian Road"],
    "Caledonian Road":  ["Barnsbury", "Brewery Road", "Chapel Market", 
                         "King's Cross"],
    "Chapel Market":    ["Angel", "Caledonian Road", "Penton Rise"],
    "Euston":           ["Mornington Cr.", "St Pancras", "Warren Street"],
    "Exmouth Market":   ["Mount Pleasant", "Sadler's Wells"],
    "Gower St. (UCL)":  ["Russell Square", "Warren Street"],
    "Islington Green":  ["Angel", "Barnsbury"],
    "King's Cross":     ["Caledonian Road", "Mount Pleasant", "Penton Rise", 
                         "St Pancras",
                         "Swinton Street", "Tavistock Square"],
    "Marchmont Street": ["Russell Square", "Tavistock Square"],
    "Mornington Cr.":   ["Euston", "Warren Street"],
    "Mount Pleasant":   ["Exmouth Market", "King's Cross", "Sadler's Wells", 
                         "Swinton Street"],
    "Penton Rise":      ["Chapel Market", "King's Cross"],
    "Russell Square":   ["Gower St. (UCL)", "Marchmont Street", 
                         "Tavistock Square"],
    "Sadler's Wells":   ["Angel", "Exmouth Market", "Mount Pleasant"],
    "St Pancras":       ["Euston", "King's Cross"],
    "Swinton Street":   ["King's Cross", "Mount Pleasant"],
    "Tavistock Square": ["King's Cross", "Marchmont Street", "Russell Square"],
    "Warren Street":    ["Euston", "Gower St. (UCL)", "Mornington Cr."],
}



# BFS con LISTE di ADIACENZA

# CONTEGGIO NUMERO CAMMINI MINIMI [Grafi Diretti e Indiretti]
'Grafo Indiretto Non Connesso'
u0, u1 = 0, 5
va0=conteggioCamminiMinimi(L_gnc,u0)
va1=conteggioCamminiMinimi(L_gnc,u1)

print("------------------------------------------"+"\n"+
      "BFS per Conteggio Numero Cammini Minimi - "+"\n"+
      "Grafo Indiretto Non Connesso: "+"\n"+
      str(u0) + " -> Vettore dei Cammini Minimi: "+ str(va0[0])+"\n"+
      str(u0) + " -> Vettore dei Distanze Minime: "+ str(va0[1])+"\n"+
      str(u1) + " -> Vettore dei Cammini Minimi: "+ str(va1[0])+"\n"+
      str(u1) + " -> Vettore dei Distanze Minime: "+ str(va1[1])+"\n")


'Grafo Indiretto Connesso'
u0, u1 = "King's Cross", "Exmouth Market"
va0=conteggioCamminiMinimi(L_gc,u0)
va1=conteggioCamminiMinimi(L_gc,u1)

print("------------------------------------------"+"\n"+
      "BFS per Conteggio Numero Cammini Minimi - "+"\n"+
      "Grafo Indiretto Connesso: "+"\n"+
      str(u0) + " -> Vettore dei Cammini Minimi: "+ str(va0[0])+"\n"+
      str(u0) + " -> Vettore dei Distanze Minime: "+ str(va0[1])+"\n"+
      str(u1) + " -> Vettore dei Cammini Minimi: "+ str(va1[0])+"\n"+
      str(u1) + " -> Vettore dei Distanze Minime: "+ str(va1[1])+"\n")


# RICERCA NODI alla STESSA DISTANZA
'Grafo Indiretto Non Connesso'
u0, v0 = 0, 4
u1, v1 = 3, 7
va0=ricercaNodiStessaDist(L_gnc, u0, v0)
va1=ricercaNodiStessaDist(L_gnc, u1, v1)

print("------------------------------------------"+"\n"+
      "BFS per Ricerca Nodi alla Stessa Distanza - "+"\n"+
      "Grafo Indiretto Non Connesso: "+"\n"+
      "("+str(u0)+","+str(v0)+")-> Vettore Nodi Equidistanti: "+ str(va0)+"\n"+
      "("+str(u1)+","+str(v1)+")-> Vettore Nodi Equidistanti: "+ str(va1)+"\n")


'Grafo Indiretto Connesso'
u0, v0 = "King's Cross", "Tavistock Square"
u1, v1 = "Islington Green", "Euston"
va0=ricercaNodiStessaDist(L_gc, u0, v0)
va1=ricercaNodiStessaDist(L_gc, u1, v1)

print("--------------------------------------------"+"\n"+
      "BFS per Ricerca Nodi alla Stessa Distanza - "+"\n"+
      "Grafo Indiretto Connesso: "+"\n"+
      "("+u0+","+v0+") -> Vettore dei Nodi Equidistanti: "+ str(va0)+"\n"+
      "("+u1+","+v1+") -> Vettore dei Nodi Equidistanti: "+ str(va1)+"\n")


# CALCOLO DISTANZA tra DUE INSIEMI
'Grafo Indiretto Non Connesso'
A0, B0 = [0,2],[1,3]
A1, B1 = [0,1,3],[5,6]
va0=calcoloDistInsiemi(L_gnc, A0, B0)
va1=calcoloDistInsiemi(L_gnc, A1, B1)

print("------------------------------------------"+"\n"+
      "BFS per Calcolo Distanza fra Due Insiemi - "+"\n"+
      "Grafo Indiretto Non Connesso: "+"\n"+
      "A0, B0 -> Distanza Minima: "+ str(va0)+"\n"+
      "A1, B1 -> Distanza Minima: "+ str(va1)+"\n")


'Grafo Indiretto Connesso'
A0, B0 = ["Brewery Road", "Caledonian Road", "Barnsbury"],["Euston", "Angel"]
A1, B1 = ["King's Cross", "St Pancras"],["Russell Square", "Angel","Barnsbury"]
va0=calcoloDistInsiemi(L_gc, A0, B0)
va1=calcoloDistInsiemi(L_gc, A1, B1)

print("------------------------------------------"+"\n"+
      "BFS per Calcolo Distanza fra Due Insiemi - "+"\n"+
      "Grafo Indiretto Connesso: "+"\n"+
      "A0, B0 -> Distanza Minima: "+ str(va0)+"\n"+
      "A1, B1 -> Distanza Minima: "+ str(va1)+"\n")


# RICERCA CAMMINI VINCOLATI al PASSAGGIO per DETERMINATI NODI
'Grafo Indiretto Non Connesso'
u0, v0, r0 = 0, 3, 4
u1, v1, r1 = 4, 5, 0
va0=ricercaCamminiVincolati(L_gnc, u0, v0, r0)
va1=ricercaCamminiVincolati(L_gnc, u1, v1, r1)

print("----------------------------------------------------------------"+"\n"+
      "BFS per Ricerca Cammini Vincolati al Passaggio per certi Nodi - "+"\n"+
      "Grafo Indiretto Non Connesso: "+"\n"+
      "("+str(u0)+","+str(v0)+","+str(r0)+")-> Nodi Cammino: "+ str(va0)+"\n"+
      "("+str(u1)+","+str(v1)+","+str(r1)+")-> Nodi Cammino: "+ str(va1)+"\n")


'Grafo Indiretto Connesso'
u0, v0, r0 = "Russell Square", "Warren Street", "King's Cross"
u1, v1, r1 = "Angel", "St Pancras", "Brewery Road"
va0=ricercaCamminiVincolati(L_gc, u0, v0, r0)
va1=ricercaCamminiVincolati(L_gc, u1, v1, r1)

print("----------------------------------------------------------------"+"\n"+
      "BFS per Ricerca Cammini Vincolati al Passaggio per certi Nodi - "+"\n"+
      "Grafo Indiretto Connesso: "+"\n"+
      "("+u0+","+v0+","+r0+") -> Nodi del Cammino: "+ str(va0)+"\n"+
      "("+u1+","+v1+","+r1+") -> Nodi del Cammino: "+ str(va1)+"\n")


# CALCOLO DISTANZE a partire dall'ALBERO dei PADRI della BFS
'Grafo Indiretto Non Connesso'
u0, u1 = 0, 4
padri_BFS0= BFS_la(L_gnc,u0)[0]
padri_BFS1= BFS_la(L_gnc,u1)[0]
va0=calcoloDistDaPadriBFS(padri_BFS0)
va1=calcoloDistDaPadriBFS(padri_BFS1)

print("---------------------------------------------------------"+"\n"+
      "BFS per Calcolo Distanze a partire da Albero Padri BFS - "+"\n"+
      "Grafo Indiretto Non Connesso: "+"\n"+
      "padri_BFS0 -> Distanze: "+ str(va0)+"\n"+
      "padri_BFS1 -> Distanze: "+ str(va1)+"\n")


'Grafo Indiretto Connesso'
u0, u1 = "Angel", "Tavistock Square"
padri_BFS0= BFS_la(L_gc,u0)[0]
padri_BFS1= BFS_la(L_gc,u1)[0]
va0=calcoloDistDaPadriBFS(padri_BFS0)
va1=calcoloDistDaPadriBFS(padri_BFS1)

print("---------------------------------------------------------"+"\n"+
      "BFS per Calcolo Distanze a partire da Albero Padri BFS - "+"\n"+
      "Grafo Indiretto Connesso: "+"\n"+
      "padri_BFS0 -> Distanze: "+ str(va0)+"\n"+
      "padri_BFS1 -> Distanze: "+ str(va1)+"\n")