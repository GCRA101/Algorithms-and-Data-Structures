# -*- coding: utf-8 -*-
"""
LEZIONE 01 - I GRAFI

Algoritmi di Verifica e di Ricerca del Pozzo Universale

"""


" ALGORITMI *****************************************************************"


# VERIFICA POZZO UNIVERSALE in O(n)
def pozzo(u,M):                                              # T(n)
    for i in range(0,len(M)):                                # n*Θ(1)+Θ(1)
        if (i!=u and (M[i][u]==0 or M[u][i]==1)):            # Θ(1)
            return False                                     # Θ(1)
    return True                                              # Θ(1)
# Costo Computazionale: O(n) - CASO PEGGIORE
#                       Ω(1) - CASO MIGLIORE


# RICERCA POZZO UNIVERSALE in O(n^2)
def pozzoUniversale1(M):                                     # T(n)
    for i in range(0,len(M)):                                # n*Θ(1)+Θ(1)
        if (pozzo(i,M)): return i                            # Θ(n)
    return "N/A"                                             # Θ(1)
# Costo Computazionale: O(n^2) - CASO PEGGIORE
#                       Ω(1)   - CASO MIGLIORE


# RICERCA POZZO UNIVERSALE in O(n)
def pozzoUniversale2(M):                                     # T(n)
    p=0                                                      # Θ(1)
    for i in range(1,len(M)):                                # (n-1)*Θ(1)+Θ(1)
        if (M[p][i]==1):                                     # Θ(1)
            p=i                                              # Θ(1)
    x=pozzo(p,M)                                             # Θ(n)
    if x: return p                                           # Θ(1)
    return "N\A"                                             # Θ(1)
# Costo Computazionale: O(n) - CASO PEGGIORE
#                       Ω(1) - CASO MIGLIORE



" ESEMPIO *******************************************************************"

# Matrice con Pozzo Universale nel Nodo 2
MM=[[0,1,1,0,0], # Riga di adiacenza del nodo 0
    [0,0,1,0,0], # Riga di adiacenza del nodo 1
    [0,0,0,0,0], # Riga di adiacenza del nodo 2
    [0,0,1,0,0], # Riga di adiacenza del nodo 3
    [0,1,1,0,0]] # Riga di adiacenza del nodo 4

# Ricerca Pozzo Universale
print("Il pozzo universale calcolato con l'algoritmo 1 e' il nodo " 
          + str(pozzoUniversale1(MM)))
print("Il pozzo universale calcolato con l'algoritmo 2 e' il nodo " 
          + str(pozzoUniversale2(MM)))

