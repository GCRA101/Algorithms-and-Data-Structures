# -*- coding: utf-8 -*-
"""
LEZIONE 18a - DIVIDE ET IMPERA - CALCOLO delle POTENZE

La Tecnica del Divide Et Impera e' una fondamentale tecnica di progettazione
di algoritmi che consiste nello scomporre un problema in sotto-parti piu'
piccole (Divide) fino a che esse non risultano essere risolvibili in modo
semplice in quanto ridotte a sotto-problemi elementari. 
La soluzione del problema globale si ottiene combinando insieme (Impera) tutte
le soluzioni parziali ottenute sui sotto-problemi elementari.

L'implementazione naturale della Tecnica del Divide Et Impera si riconduce
naturalmente all'utilizzo della RICORSIONE.

Il costo computazionale di un algoritmo ricorsivo si ottiene risolvendo la
corrispondente Equazione di Ricorrenza facendo uso del Teorema Master.

Esempi noti di algoritmi che usano la tecnica sono i seguenti:
    - Algoritmi Efficienti di Ordinamento basato sui Confronti
        - MERGESORT
        - QUICKSORT
    - Algoritmi di Ricerca
        - RICERCA BINARIA
        
Di seguito, vediamo la soluzione del Problema delle Potenze confrontando la
versione iterativa con quella ricorsiva
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math


# ================== ALGORITMO di CALCOLO delle POTENZE =======================


# ALGORITMO ITERATIVO
# ----------------------------------------------------------------------------
''' 
Il calcolo dell'elevazione a potenza di un numero puo' essere eseguito
iterativamente moltiplicando il numero per se' medesimo tante volte quanto vale
la potenza stessa.
'''

def powerIter(a,n):                            # T(n)
    x = a                                      # Θ(1)
    for i in range(1,n):                       # (n-1)*Θ(1)+Θ(1)
        x *=a                                  # Θ(1)
    return x                                   # Θ(1)

# Costo Computazionale: T(n) = Θ(n)


# ALGORITMO RICORSIVO
# ----------------------------------------------------------------------------
''' 
Il calcolo dell'elevamento a potenza di un numero può essere eseguito 
ricorsivamente dividendo l'esponente a metà (Divide) a ogni passo ricorsivo, 
fino a raggiungere il caso base (esponente = 0, risultato 1), e ricostruendo 
poi la soluzione complessiva (Combina) moltiplicando per se stessa la 
sotto-soluzione, calcolata una sola volta, e, se l'esponente è dispari, 
moltiplicando ancora per la base. La complessità è Θ(log n) moltiplicazioni.
'''

def powerRecursion(a,n):                       # T(n)
    if n==0:                                   # Θ(1)       (A)
        return 1                               # Θ(1)
    m = n//2                                   # Θ(1)
    x = powerRecursion(a, m)                   # T(n/2)     (B)
    x = x*x                                    # Θ(1)
    if n % 2 !=0:                              # Θ(1)       (C)
        x = a*x                                # Θ(1)
    return x                                   # Θ(1)

# Costo Computazionale: T(n) = T(n/2) + O(1) = Θ(logn)

# Commenti
# (A): Caso Base
# (B): Passo Ricorsivo
# (C): Combinazione delle Sotto-Soluzioni


" ESEMPI ********************************************************************"

a, n = 2, 8
pwIter = powerIter(a,n)
pwRec = powerRecursion(a,n)
