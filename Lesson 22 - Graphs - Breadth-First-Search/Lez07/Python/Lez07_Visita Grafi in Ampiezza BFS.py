# -*- coding: utf-8 -*-
"""
LEZIONE 07 - VISITA di GRAFI in AMPIEZZA'

Algoritmi di Visita in Ampiezza BFS
    - Con Liste di Adiacenza
    - Con Matrice di Adiacenza
    
"""


" ALGORITMI *****************************************************************"

import math
from collections import deque

# BFS con LISTE di ADIACENZA
def BFS_la(u,G):                                            # T(n)
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
     
                           
# BFS con MATRICE di ADIACENZA
def BFS_ma(u,M,Mkeys):                                      # T(n)
    padri = {key: -1 for key in Mkeys}                      # Θ(n)
    dist = {key: math.inf for key in Mkeys}                 # Θ(n)
    padri[u] = u                                            # Θ(1)
    dist[u] = 0                                             # Θ(1)
    q = deque()                                             # Θ(1)
    q.append(u)                                             # Θ(1)
    while len(q)!=0:                                        # n*Θ(1)+Θ(1)
        u = q.popleft()                                     # Θ(1)
        for y in range(0,len(M)):                           # n*Θ(1)+Θ(1)
            if (M[Mkeys.index(u)][y] == 1
                and padri[Mkeys[y]] == -1):                 # Θ(1)
                    padri[Mkeys[y]] = u                     # Θ(1)
                    dist[Mkeys[y]] = dist[u] + 1            # Θ(1)
                    q.append(Mkeys[y])                      # Θ(1)
        print(str(u) + " <-- " + str(q))                    # Θ(1)
    return padri, dist                                      # Θ(1)

# Costo Computazionale: O(n^2) - CASO PEGGIORE (*)
#                       Ω(1)   - CASO MIGLIORE (**)
#
# (*): Nodo di partenza connesso a tutti i nodi del grafo
# (**): Nodo di partenza completamente disconnesso
    

" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi un
esempio ispirato alla Metro di Londra.

"""

# LISTE DI ADIACENZA

'Grafo Indiretto Non Connesso' 
L_gnc={0: [1,2],
       1: [0,2],
       2: [0,1],
       3: [4,5],
       4: [3,5],
       5: [3,4],
       6: []}

'Grafo Indiretto Connesso'
L_gc = {
    "Baker Street":      ["Regent's Park"],
    "Bond Street":       ["Green Park", "Marble Arch", "Oxford Circus"],
    "Chancery Lane":     ["Holborn"],
    "Charing Cross":     ["Piccadilly Circus", "Waterloo"],
    "Covent Garden":     ["Holborn", "Leicester Sq"],
    "Green Park":        ["Bond Street", "Oxford Circus", "Piccadilly Circus", 
                          "Victoria"],
    "Holborn":           ["Chancery Lane", "Covent Garden", "Oxford Circus", 
                          "Russell Sq"],
    "Kings Cross":       ["Russell Sq", "Warren Street"],
    "Leicester Sq":      ["Covent Garden", "Piccadilly Circus"],
    "Marble Arch":       ["Bond Street"],
    "Oxford Circus":     ["Bond Street", "Green Park", "Holborn", 
                          "Piccadilly Circus","Regent's Park", 
                          "Warren Street"],
    "Piccadilly Circus": ["Charing Cross", "Green Park", "Leicester Sq", 
                          "Oxford Circus"],
    "Pimlico":           ["Victoria"],
    "Regent's Park":     ["Baker Street", "Oxford Circus"],
    "Russell Sq":        ["Holborn", "Kings Cross"],
    "Victoria":          ["Green Park", "Pimlico"],
    "Warren Street":     ["Kings Cross", "Oxford Circus"],
    "Waterloo":          ["Charing Cross"],
}



# MATRICE DI ADIACENZA

'Grafo Indiretto Non Connesso'
MM_gnc=[[0,1,1,0,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,0,0,0,0],
        [0,0,0,0,1,1,0],
        [0,0,0,1,0,1,0],
        [0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0]]

'Grafo Indiretto Connesso'
MM_gc=[[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
       [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0],
       [0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
       [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0],
       [0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
       [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

MMgnc_keys =[0,1,2,3,4,5,6]

MMgc_keys = ["Baker Street", "Bond Street", "Chancery Lane", "Charing Cross",
           "Covent Garden", "Green Park", "Holborn", "Kings Cross", 
           "Leicester Sq", "Marble Arch", "Oxford Circus", "Piccadilly Circus", 
           "Pimlico", "Regent's Park", "Russell Sq", "Victoria", 
           "Warren Street", "Waterloo"]


# BFS con LISTE di ADIACENZA

'Grafo Indiretto Non Connesso'
va0=BFS_la(0,L_gnc) # Partendo da 0 si possono visitare solo i nodi 1 e 2
va1=BFS_la(1,L_gnc) # Partendo da 1 si possono visitare solo i nodi 0 e 2
va2=BFS_la(2,L_gnc) # Partendo da 2 si possono visitare solo i nodi 0 e 1
va3=BFS_la(3,L_gnc) # Partendo da 3 si possono visitare solo i nodi 4 e 5
va4=BFS_la(4,L_gnc) # Partendo da 4 si possono visitare solo i nodi 3 e 5

print("BFS con Liste di Adiacenza - Grafo Indiretto Non Connesso: "+"\n"+
      "0 -> "+ str(va0)+"\n"+
      "1 -> "+ str(va1)+"\n"+
      "2 -> "+ str(va2)+"\n"+
      "3 -> "+ str(va3)+"\n"+
      "4 -> "+ str(va4)+"\n")


'Grafo Indiretto Connesso'
va0=BFS_la('Baker Street',L_gc)   # Partendo da Baker Street
va1=BFS_la('Covent Garden',L_gc)  # Partendo da Covent Garden
va2=BFS_la('Russell Sq',L_gc)     # Partendo da Russell Square
va3=BFS_la('Oxford Circus',L_gc)  # Partendo da Oxford Circus

print("BFS con Liste di Adiacenza - Grafo Indiretto Connesso: "+"\n"+
      "Baker Street -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va0[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va0[1])+ "\n" +
      "Covent Garden -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va1[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va1[1])+ "\n" +
      "Russell Sq -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va2[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va2[1])+ "\n" +
      "Oxford Circus -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va3[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va3[1]))



# DFS con MATRICE di ADIACENZA

'Grafo Indiretto Non Connesso'
vm0=BFS_ma(0,MM_gnc, MMgnc_keys)
vm1=BFS_ma(1,MM_gnc, MMgnc_keys)
vm2=BFS_ma(2,MM_gnc, MMgnc_keys)
vm3=BFS_ma(3,MM_gnc, MMgnc_keys)
vm4=BFS_ma(4,MM_gnc, MMgnc_keys)

print("BFS con Matrice di Adiacenza - Grafo Indiretto Non Connesso: "+"\n"+
      "0 -> "+ str(vm0)+"\n"+
      "1 -> "+ str(vm1)+"\n"+
      "2 -> "+ str(vm2)+"\n"+
      "3 -> "+ str(vm3)+"\n"+
      "4 -> "+ str(vm4)+"\n")


'Grafo Indiretto Connesso'
vm0=BFS_ma('Baker Street',  MM_gc, MMgc_keys)  # Partendo da Baker Street
vm1=BFS_ma('Covent Garden', MM_gc, MMgc_keys)  # Partendo da Covent Garden
vm2=BFS_ma('Russell Sq', MM_gc, MMgc_keys)     # Partendo da Russell Square
vm3=BFS_ma('Oxford Circus', MM_gc, MMgc_keys)  # Partendo da Oxford Circus

print("BFS con Matrice di Adiacenza - Grafo Indiretto Connesso: "+"\n"+
      "Baker Street -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va0[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va0[1])+ "\n" +
      "Covent Garden -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va1[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va1[1])+ "\n" +
      "Russell Sq -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va2[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va2[1])+ "\n" +
      "Oxford Circus -------------------------\n" +
      "-> Vettore dei Padri: "+ str(va3[0]) + "\n" +
      "-> Vettore delle Distanze: "+ str(va3[1]))