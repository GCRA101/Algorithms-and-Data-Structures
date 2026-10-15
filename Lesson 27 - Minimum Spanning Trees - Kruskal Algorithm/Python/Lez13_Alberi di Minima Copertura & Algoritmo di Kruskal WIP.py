# -*- coding: utf-8 -*-
"""
LEZIONE 13 - ALBERI MINIMI di COPERTURA e ALGORITMO di KRUSKAL

Un albero minimo di copertura e' un albero di visita di un grafo pesato che 
consente di minimizzare il costo totale richiesto per visitare tutti i nodi a
partire da un nodo sorgente.
Tale albero minimo di copertura differisce dall'albero di visita BFS e DFS e
viene determinato utilizzando l'algoritmo di Kruskal

Algoritmo di Kruskal
    - Formulazione con E disordinato      - O(m^2)
    - Formulazione con E ordinato         - O(n*m)
    - Formulazione con E ordinato + v_CC  - O((n+m)logn)
    - Formulazione con E ordinato + l_CC  - O((n+m)logn)
    
    dove E    : vettore degli Archi (Edges)
         v_CC : vettore delle Componenti Connesse
         l_CC : lista   delle Componenti Connesse


Confronto Algoritmo di Prim vs Algoritmo di Kruskal --------------------------

L'algoritmo di Prim e l'algoritmo di Kruskal hanno esattamente lo stesso scopo 
- ovvero ottenere l'albero di copertura minimo di un grafo indiretto connesso
(MST: Minimum Spanning Tree) - ma lo raggiungono in modo differente.
Prim utilizza la lista di adiacenza mentre Kruskal utilizza la lista
degli archi.

Quando usare Prim
    - Grafo DENSO
    - Grafo rappresentato tramite LISTA/MATRICE di ADIACENZA
    
Quando usare Kruskal
    - Grafo SPARSO
    - Grafo rappresentato tramite LISTA degli ARCHI
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math
from collections import deque
from decimal import Decimal


# ======================== ALGORITMO di KRUSKAL ===============================


# ALGORITMO di KRUSKAL - v01 - Vettore Archi Disordinato
# ----------------------------------------------------------------------------
def MinimumSpanningTree_Kruskal_v01(E,u):                   # T(n,m)
    padri = {key: -1 for key in E}                          # Θ(n)
    nodi = []                                               # Θ(n)
    padri[u] = u                                            # Θ(1)
    nodi.append(u)                                          # Θ(1)
    costi = {key: math.inf for key in E}                    # Θ(n)
    costi[u] = 0                                            # Θ(1)
    while True:                                             # n*Θ(1)+Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        costo_min = math.inf                                # Θ(1)
        for u in E:                                         # v*Θ(1)+Θ(1)
            if padri[u] != -1:                              # Θ(1)
                for v in E[u]:                              # k*Θ(1)+Θ(1)
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



# ALGORITMO di KRUSKAL - v02 - Vettore Archi Ordinato
# ----------------------------------------------------------------------------
def MinimumSpanningTree_Kruskal_v02(E,u):                   # T(n,m)
    padri = {key: -1 for key in E}                          # Θ(n)
    nodi = []                                               # Θ(n)
    padri[u] = u                                            # Θ(1)
    nodi.append(u)                                          # Θ(1)
    costi = {key: math.inf for key in E}                    # Θ(n)
    costi[u] = 0                                            # Θ(1)
    while True:                                             # n*Θ(1)+Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        costo_min = math.inf                                # Θ(1)
        for u in E:                                         # v*Θ(1)+Θ(1)
            if padri[u] != -1:                              # Θ(1)
                for v in E[u]:                              # k*Θ(1)+Θ(1)
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



# ALGORITMO di KRUSKAL - v03 - Vettore Archi Ordinato + Vettore Comp. Connesse
# ----------------------------------------------------------------------------
def MinimumSpanningTree_Kruskal_v03(E,u):                   # T(n,m)
    padri = {key: -1 for key in E}                          # Θ(n)
    nodi = []                                               # Θ(n)
    padri[u] = u                                            # Θ(1)
    nodi.append(u)                                          # Θ(1)
    costi = {key: math.inf for key in E}                    # Θ(n)
    costi[u] = 0                                            # Θ(1)
    while True:                                             # n*Θ(1)+Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        costo_min = math.inf                                # Θ(1)
        for u in E:                                         # v*Θ(1)+Θ(1)
            if padri[u] != -1:                              # Θ(1)
                for v in E[u]:                              # k*Θ(1)+Θ(1)
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



# ALGORITMO di KRUSKAL - v04 - Vettore Archi Ordinato + Lista Comp. Connesse
# ----------------------------------------------------------------------------
def MinimumSpanningTree_Kruskal_v04(E,u):                   # T(n,m)
    padri = {key: -1 for key in E}                          # Θ(n)
    nodi = []                                               # Θ(n)
    padri[u] = u                                            # Θ(1)
    nodi.append(u)                                          # Θ(1)
    costi = {key: math.inf for key in E}                    # Θ(n)
    costi[u] = 0                                            # Θ(1)
    while True:                                             # n*Θ(1)+Θ(1)
        u_min = None                                        # Θ(1)
        v_min = None                                        # Θ(1)
        costo_min = math.inf                                # Θ(1)
        for u in E:                                         # v*Θ(1)+Θ(1)
            if padri[u] != -1:                              # Θ(1)
                for v in E[u]:                              # k*Θ(1)+Θ(1)
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





" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi due esempi
piu' complessi: uno ispirato alla progettazione della rete viaria dell'antico
impero romano e uno ispirato al film Matrix.

"""


# LISTE DI ADIACENZA ----------------------------------------------------------


'Grafo Indiretto Connesso - Esempio Numerico ---------------------------------' 
E_gc_Numeric = {
      ("A", "B", 2),
      ("A", "C", 4),
      ("A", "D", 7),
      ("A", "F", 5),
      ("B", "D", 6),
      ("B", "E", 3),
      ("B", "G", 8),
      ("C", "F", 6),
      ("D", "F", 1),
      ("D", "G", 6),
      ("E", "G", 7),
      ("F", "G", 6)
}


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
'''
Costo degli Archi -> Costo realizzazione connessione in migliaia di Sesterzi
''' 
E_gc_Roman = {
    # --- PLAIN ROADS (green) ---
    ("Roma",              "Capua",              190),
    ("Massilia",          "Narbo",              150),
    ("Narbo",             "Burdigala",          300),
    ("Emerita Augusta",   "Corduba",            250),
    # --- HILL ROADS (blue) ---
    ("Mediolanum",        "Ravenna",            220),
    ("Lugdunum",          "Burdigala",          810),
    ("Corduba",           "Carthago Nova",      500),
    ("Lutetia",           "Narbo",             1252),
    ("Vindobona",         "Augusta Treverorum",2939),
    # --- MOUNTAIN / ALPINE ROADS (red) ---
    ("Roma",              "Mediolanum",        1680),
    ("Mediolanum",        "Colonia Agrippina", 1930),
    ("Colonia Agrippina", "Aquincum",          3330),
    ("Colonia Agrippina", "Augusta Treverorum", 700),
    ("Aquincum",          "Vindobona",          500),
    ("Aquincum",          "Byzantium",           45),
    # --- SEA LANES (purple) ---
    ("Roma",              "Massilia",            20),
    ("Roma",              "Carthago",            18),
    ("Roma",              "Alexandria",          59),
    ("Capua",             "Carthago",            17),
    ("Ravenna",           "Alexandria",          40),
    ("Narbo",             "Byzantium",           78),
    ("Narbo",             "Tarraco",             80),
    ("Tarraco",           "Carthago Nova",      100),
    ("Tarraco",           "Massilia",            90),
    ("Tarraco",           "Carthago",            85),
    ("Tarraco",           "Alexandria",          95),
    ("Corduba",           "Byzantium",           96),
    ("Corduba",           "Carthago",            70),
    ("Corduba",           "Alexandria",          97),
    ("Carthago Nova",     "Carthago",            55),
    ("Carthago Nova",     "Massilia",           110),
    ("Emerita Augusta",   "Carthago",            80),
    ("Emerita Augusta",   "Londinium",           49),
    ("Londinium",         "Lutetia",             11),
    ("Londinium",         "Eboracum",            50),
    ("Eboracum",          "Narbo",               43),
    ("Lutetia",           "Burdigala",          400),
    ("Lugdunum",          "Massilia",           200),
    ("Lugdunum",          "Narbo",              250),
    ("Massilia",          "Carthago",            35),
    ("Massilia",          "Alexandria",          45),
    ("Byzantium",         "Alexandria",          33),
    ("Carthago",          "Alexandria",          25),
    # --- RIVER / DANUBE ROUTE ---
    ("Vindobona",         "Aquincum",           200),
    # --- REMAINING CONNECTIVITY EDGES ---
    ("Burdigala",         "Lutetia",            400),
    ("Augusta Treverorum","Colonia Agrippina",  150),
    ("Augusta Treverorum","Lugdunum",           350),
    ("Mediolanum",        "Lugdunum",           500),
    ("Mediolanum",        "Ravenna",            220),
    ("Ravenna",           "Capua",              400),
    ("Ravenna",           "Byzantium",           50),
    ("Capua",             "Tarraco",            120),
    ("Eboracum",          "Londinium",           50),
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
E_gc_Matrix = {
    # --- GREEN edges (weight 1-2, low risk) ---
    ("A", "B", 1),   # Thomas Anderson's Apt ↔ Heart O' The City Hotel
    ("A", "G", 2),   # Thomas Anderson's Apt ↔ Warehouse 17
    ("A", "J", 2),   # Thomas Anderson's Apt ↔ St. Michael's Cathedral
    ("B", "F", 1),   # Heart O' The City Hotel ↔ Chinatown Safe House
    ("B", "L", 1),   # Heart O' The City Hotel ↔ Zion Access Broadcast Relay
    ("C", "I", 1),   # Adams Street Subway ↔ Old Power Station ← East River
    ("E", "H", 2),   # Abandoned Gov. Office ↔ Riverfront Dockyard
    ("G", "I", 2),   # Warehouse 17 ↔ Old Power Station
    ("H", "I", 2),   # Riverfront Dockyard ↔ Old Power Station ← East River
    ("K", "L", 1),   # Telephone Extraction Hub ↔ Zion Access Broadcast Relay
    # --- ORANGE edges (weight 3-4, moderate risk) ---
    ("A", "F", 3),   # Thomas Anderson's Apt ↔ Chinatown Safe House
    ("A", "K", 4),   # Thomas Anderson's Apt ↔ Telephone Extraction Hub
    ("B", "G", 4),   # Heart O' The City Hotel ↔ Warehouse 17
    ("B", "I", 3),   # Heart O' The City Hotel ↔ Old Power Station
    ("B", "J", 3),   # Heart O' The City Hotel ↔ St. Michael's Cathedral
    ("D", "F", 3),   # Metacortex Building ↔ Chinatown Safe House
    ("E", "I", 3),   # Abandoned Gov. Office ↔ Old Power Station
    ("E", "J", 4),   # Abandoned Gov. Office ↔ St. Michael's Cathedral
    ("E", "K", 3),   # Abandoned Gov. Office ↔ Telephone Extraction Hub
    ("F", "G", 3),   # Chinatown Safe House ↔ Warehouse 17
    ("G", "H", 3),   # Warehouse 17 ↔ Riverfront Dockyard
    ("H", "K", 4),   # Riverfront Dockyard ↔ Telephone Extraction Hub
    ("I", "K", 3),   # Old Power Station ↔ Telephone Extraction Hub
    ("J", "K", 3),   # St. Michael's Cathedral ↔ Telephone Extraction Hub
    ("C", "F", 4),   # Adams Street Subway ↔ Chinatown Safe House
    # --- RED edges (weight 5-7, high risk) ---
    ("A", "C", 5),   # Thomas Anderson's Apt ↔ Adams Street Subway
    ("A", "D", 7),   # Thomas Anderson's Apt ↔ Metacortex Building
    ("B", "C", 5),   # Heart O' The City Hotel ↔ Adams Street Subway
    ("B", "E", 6),   # Heart O' The City Hotel ↔ Abandoned Gov. Office
    ("B", "H", 5),   # Heart O' The City Hotel ↔ Riverfront Dockyard
    ("B", "K", 5),   # Heart O' The City Hotel ↔ Telephone Extraction Hub
    ("C", "D", 5),   # Adams Street Subway ↔ Metacortex Building
    ("C", "E", 7),   # Adams Street Subway ↔ Abandoned Gov. Office
    ("C", "J", 6),   # Adams Street Subway ↔ St. Michael's Cathedral
    ("D", "I", 5),   # Metacortex Building ↔ Old Power Station
    ("D", "J", 5),   # Metacortex Building ↔ St. Michael's Cathedral
    ("D", "K", 5),   # Metacortex Building ↔ Telephone Extraction Hub
    ("D", "L", 6),   # Metacortex Building ↔ Zion Access Broadcast Relay
    ("F", "I", 6),   # Chinatown Safe House ↔ Old Power Station
    ("H", "J", 7),   # Riverfront Dockyard ↔ St. Michael's Cathedral
}
       


    - Formulazione con E ordinato + v_CC  - O((n+m)logn)
    - Formulazione con E ordinato + l_CC  - O((n+m)logn)
     
# ALGORITMO di PRIM con LISTE di ADIACENZA --------------------------------

'Grafo Indiretto Connesso - Esempio Numerico -----------------------------'
u = "A"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Numeric,u)
kruskal_v02 = MinimumSpanningTree_Kruskal_v02(E_gc_Numeric,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Numeric,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Numeric,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v01[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + l_CC [O(mlogn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v03[2].values())))


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
u = "Roma"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Roman,u)
kruskal_v02 = MinimumSpanningTree_Kruskal_v02(E_gc_Roman,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Roman,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Roman,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Roman Road Network: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v01[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + l_CC [O(mlogn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v03[2].values())))


'Grafo Indiretto Connesso - Esempio Matrix  ----------------------------------'
u = "A"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Matrix,u)
kruskal_v02 = MinimumSpanningTree_Kruskal_v02(E_gc_Matrix,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Matrix,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Matrix,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Matrix: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v01[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v01[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v01[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v01[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato [O(n*m)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v02[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v02[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v02[2]) +"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v02[2].values())) +"\n"+
      " > Algoritmo di Kruskal con E Ordinato + l_CC [O(mlogn)]: "+"\n"+
      "    - Vettore dei Nodi Visitati: "+ str(kruskal_v03[0]) +"\n"+
      "    - Vettore dei Padri: "+ str(kruskal_v03[1]) +"\n"+
      "    - Vettore dei Costi: "+ str(kruskal_v03[2])+"\n"+
      "    - Costo Minimo Totale: "+ str(sum(kruskal_v03[2].values())))