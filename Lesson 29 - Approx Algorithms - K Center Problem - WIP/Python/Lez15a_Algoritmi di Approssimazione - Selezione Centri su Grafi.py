# -*- coding: utf-8 -*-
"""
LEZIONE 15a - ALGORITMI di APPROSSIMAZIONE e SELEZIONE CENTRI [GRAFI]

Gli Algoritmi di Approssimazione sono quella categoria di algoritmi creati per
risolvere problemi computazionalmente difficili e per i quali non esiste un
algoritmo che produca una soluzione esatta in tempi umanamente fattibili.
Gli Algoritmi di Approssimazione garantiscono che la soluzione da essi
raggiunta sia in grado di approssimare la soluzione esatta per un certo
rapporto/fattore di approssimazione.

Un classico esempio di Algoritmo di Approssimazione e' utilizzato per la
risoluzione del Problema di Selezione dei Centri (K-Center).

Il Problema si Selezione dei Centri e' utilizzato per modellare numerosi
problemi computazionali reali e consiste nel posizionare k centri in modo
tale che la massima distanza di qualunque sito fra n siti dati da qualunque
centro sia minimizzata.

Il Problema viene modellato tramite un grafo in cui i nodi rappresentano i siti 
e gli archi le distanze fra questi.
La soluzione consiste nel trovare il sottoinsieme di nodi di cardinalita' k
che consente di minimizzare la distanza di qualsiasi nodo del grafo dal k-esimo
centro posizionato in prossimita' di esso.

Algoritmo per Selezione dei Centri (K-Center)
  - Formulazione Greedy Ingenua - O(n·k^2)
  - Formulazione Greedy Efficiente  - O(n·k)

Formulazione Greedy Inguenua
    - Soluzione Approssimata (non esatta)
    - Rapporto/Fattore di Approssimazione NON GARANTITO
    
Formulazione Greedy Efficiente
    - Algoritmo Greedy di Gonzalez (1985)
    - Soluzione Approssimata (non esatta)
    - Rapporto/Fattore di Approssimazione GARANTITO!
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math


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
def dijkstra_heapMin(G,s):                                  # T(n,m)
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




# ================== ALGORITMO di SELEZIONE dei CENTRI ========================


# ALGORITMO di SELEZIONE dei CENTRI (K-CENTER) per GRAFI NON PESATI
# ----------------------------------------------------------------------------
''' 
L'algoritmo approssimante greedy di Gonzalez per la selezione dei centri va di
volta in volta a posizionare un nuovo centro in corrispondenza del nodo del
grafo posto alla massima distanza da tutti i centri selezionati fino a quel
momento.
Ogni volta che un nuovo centro viene aggiunto alla selezione bisogna calcolare
le distanze di tutti i nodi del grafo da questo nuovo centro per poter passare
a selezionare quello successivo. Il calcolo delle distanze dovra' essere
effettuato usando l'algoritmo di ricerca dei cammini minimi di Dijkstra'
Il rapporto di approssimazione garantito dall'algorimo e' 2.
'''

'Implementazione ERRATA ------------------------------------------------------'
'''
L'implementazione seguente e' corretta in termini di principio ma il suo
costo computazionale e' eccessivo O((k^2)*n) in quanto si modella in modo
inefficiente la struttura dati che deve tenere traccia delle distanze minime
dei nodi dai centri via via selezionati.
Andando a immagazzinare tutti i vettori delle distanze minime di dijkstra per
tutti i centri e dovendoli scorrere tutte le volte per trovare il nuovo
centro (nodo avente massima distanza tra tutti quelli piu' vicini a ciascun
centro selezionato) crea un un triplo ciclo for di costo O(k*n*k).
Per k grandi questo termine diventa quello prevalente nel calcolo di T(n,m,k)
e risulta maggiore di quello corretto da letteratura previsto per algoritmo
di approssimazione greedy di Gonzalez.
'''
def KCenter_Graphs_Wrong(G,u,k):                            # T(n,m)
    centers = [None]*k                                      # k*Θ(1)
    dictDistanze = {}                                       # Θ(1)         (A)
    nodi = list(G.keys())                                   # n*Θ(1)
    i_center = 0                                            # Θ(1)
    centers[i_center] = u                                   # Θ(1)
    for i in range(0,k-1):                                  # k*Θ(1)+Θ(1)
        distanze = dijkstra_heapMin(G,centers[i_center])[1] # Θ((n+m)logn)
        dictDistanze[centers[i_center]] = distanze          # Θ(1)         (A)
        distMax = (-1)*math.inf                             # Θ(1)
        i_max = -1                                          # Θ(1)
        for j in range(0,len(nodi)):                        # n*Θ(1)+Θ(1)
            distMin = math.inf                              # Θ(1)
            for node in dictDistanze.keys():                # O(k)+Θ(1)    (A)
                if distMin > dictDistanze[node][nodi[j]]:   # Θ(1)
                    distMin = dictDistanze[node][nodi[j]]   # Θ(1)
            if distMax < distMin:                           # Θ(1)
                distMax = distMin                           # Θ(1)
                i_max = j                                   # Θ(1)
        i_center +=1                                        # Θ(1)
        centers[i_center]= nodi[i_max]                      # Θ(1)
    return centers                                          # Θ(1)

# Costo Computazionale: T(n,m,k) = Θ(k)+Θ(n)+k*[Θ((n+m)logn)+O(k*n)]
#                       T(n,m,k) = Θ(k*(n+m)logn)+O((k^2)*n)

# Commenti
# (A): La differenza tra l'implementazione scorretta/inefficiente (vedi sopra)
#      e l'implementazione corretta/efficiente (vedi sotto) dell'algoritmo
#      di approssimazione greedy di Gonzalez per il problema del K-Center sta
#      nella struttura dati scelta per immagazzinare le distanze minime dei
#      nodi del grafo dai centri selezionati.
#      Usare una Hash Table contenente tutti i vettori delle distanze minime
#      di Dijkstra per tutti i centri selezionati dovendoli quindi riscorrerli
#      ogni volta per ritrovare il nodo avente la massima delle distanze minime
#      e' inefficiente in quanto necessita di un doppio ciclo all'interno del
#      ciclo principale (3 cicli annidati -> O(k^2*n)).
#      Meglio utilizzare un singolo vettore contenente i valori finali e 
#      aggiornati delle distanze minime di Dijkstra (vedi implementazione
#      CORRETTA seguente).


'Implementazione CORRETTA ----------------------------------------------------'
'''
L'implementazione seguente e' invece corretta sia in termini di principio sia
di costo computazionale Θ(k*(n+m)logn) in quanto si modella in modo
efficiente la struttura dati che deve tenere traccia delle distanze minime
dei nodi dai centri via via selezionati.
Invece di immagazzinare tutti i vettori delle distanze minime di dijkstra per
tutti i centri si registra in un vettore unico le distanze minime via via 
aggiornate scorrendo tutti i centri. In tal modo il costo for rimane doppio
(non triplo) e il suo costo e' O(k*n).
Questo termine e' piccolo rispetto a Θ(k*(n+m)logn) come previsto per algoritmo
di approssimazione greedy di Gonzalez.
'''
def KCenter_Graphs(G,u,k):                                  # T(n,m)
    centers = [None]*k                                      # k*Θ(1)       (A)
    nodi = list(G.keys())                                   # n*Θ(1)       (B) 
    distMin = [math.inf]*len(nodi)                          # n*Θ(1)       (C)
    i_center = 0                                            # Θ(1)         (D)
    centers[i_center] = u                                   # Θ(1)
    for i in range(0,k-1):                                  # (k-1)*Θ(1)+Θ(1)
        distanze = dijkstra_heapMin(G,centers[i_center])[1] # Θ((n+m)logn) (E)
        distMax = (-1)*math.inf                             # Θ(1)
        i_max = -1                                          # Θ(1)
        for j in range(0,len(nodi)):                        # n*Θ(1)+Θ(1)  (F)
            if distMin[j] > distanze[nodi[j]]:              # Θ(1)         (G)
                distMin[j] = distanze[nodi[j]]              # Θ(1)
            if distMax < distMin[j]:                        # Θ(1)         (H)
                distMax = distMin[j]                        # Θ(1)
                i_max = j                                   # Θ(1)
        i_center += 1                                       # Θ(1)         (I)
        centers[i_center] = nodi[i_max]                     # Θ(1)         (J)
    return centers                                          # Θ(1)

# Costo Computazionale: T(n,m,k) = Θ(k)+Θ(n)+k*[Θ((n+m)logn)+O(n)]
#                       T(n,m,k) = Θ(k*(n+m)logn)+O(k*n)= Θ(k*(n+m)logn)

# Commenti
# (A): I centri selezionati vengono immagazzinati in un vettore di dimensione k
# (B): Si estraggono i nodi dalla Hash Table che modella la Lista di Adiacenza
#      del Grafo e li si salvano in un vettore.
# (C): Si inizializza il vettore delle distanze minime che viene aggiornato 
#      ogni volta che si aggiunge un nuovo centro alla selezione.
# (D): Si aggiunge il nodo selezionato u al vettore dei centri con indice = 0
# (E): Per ciascuno dei k centri da selezionare, si esegue l'algoritmo di
#      ricerca dei cammini minimi di Dijkstra (con Heap Minimo) a partire dal
#      centro selezionato in partenza / nella iterazione precedente. Si
#      inizializza il parametro distMax = -inf e i_max = -1 per individuare il
#      successivo centro da selezionare: ovvero il nodo avente massima distanza
#      minima dal gruppo di centri selezionati fino a quel momento.
# (F): Si scorrono tutte le n distanze minime di Dijkstra per il centro
# (G)  corrente aggiornando il vettore delle distanze minime distMin. 
# (H)  Si aggiorna anche in parallelo distMax e i_max in modo da individuare il
#      nodo avente la massima delle distanze minime dai centri selezionati fino
#      a quel momento.
# (I): Si incrementa il contatore dei centri selezionati.
# (J): Si salva il nodo corrispondente nel vettore dei centri selezionati.


# ALGORITMO di SELEZIONE dei CENTRI (K-CENTER) per GRAFI con PESI NODI ADDITIVI
# ----------------------------------------------------------------------------
''' 
La seguente e' una variante alternativa dell'algoritmo classico di Gonzalez e
che tiene conto del peso dei nodi come pesi additivi a quelli calcolati sugli
archi del grafo.
NON e' la VERSIONE per GRAFI PESATI di Gonzalez in quanto l'algoritmo di
Gonzalez e' progettato senza mai tenere conto del peso assegnato ai nodi!
Per una versione propriamente pesata (peso dei nodi) dell'algoritmo di
Selezione dei Centri, e' necessario usare l'algoritmo di 
'''

def KCenter_Graphs_variant(G,pesiNodi,u,k):                 # T(n,m)
    centers = [None]*k                                      # k*Θ(1)
    nodi = list(G.keys())                                   # n*Θ(1)
    distConPesiNodi = {nodo:None for nodo in nodi}          # n*Θ(1)       (A)   
    distMin = [math.inf]*len(nodi)                          # n*Θ(1)
    i_center = 0                                            # Θ(1)
    centers[i_center] = u                                   # Θ(1)
    for i in range(0,k-1):                                  # (k-1)*Θ(1)+Θ(1)
        distanze = dijkstra_heapMin(G,centers[i_center])[1] # Θ((n+m)logn)
        for nodo in nodi:                                   # n*Θ(1)+Θ(1)
            distConPesiNodi[nodo] = \
                distanze[nodo] + pesiNodi[nodo]             # Θ(1)
        distConPesiNodi[centers[i_center]] = 0              # Θ(1)         (A) 
        distMax = (-1)*math.inf                             # Θ(1)
        i_max = -1                                          # Θ(1)
        for j in range(0,len(nodi)):                        # n*Θ(1)+Θ(1)
            if distMin[j] > distConPesiNodi[nodi[j]]:       # Θ(1)         (A)
                distMin[j] = distConPesiNodi[nodi[j]]       # Θ(1)         (A)
            if distMax < distMin[j]:                        # Θ(1)
                distMax = distMin[j]                        # Θ(1)
                i_max = j                                   # Θ(1)
        i_center += 1                                       # Θ(1)
        centers[i_center] = nodi[i_max]                     # Θ(1)
    return centers                                          # Θ(1)

# Costo Computazionale: T(n,m,k) = Θ(k)+Θ(n)+k*[Θ((n+m)logn)+Θ(n)+Θ(n)]
#                       T(n,m,k) = Θ(k*(n+m)logn)

# Commenti
# (A): L'unica aggiunta rispetto all'implementazione CORRETTA e CLASSICA dell'
#      algoritmo greedy di Gonzalez consiste nel sommare il peso di ciascun 
#      nodo, nodo a nodo, alla corrispondente distanza minima di Dijkstra
#      calcolata. La restante parte dell'algoritmo viene eseguita tale e quale
#      utilizzando questi nuovi valori.
#      Questo perche' il peso del nodo deve essere considerato solo quando
#      il nodo e' la destinazione del cammino. Quando il nodo viene 
#      semplicemente attraversato da un cammino che punta a un altro nodo, il
#      suo peso non viene considerato.


# ALGORITMO di SELEZIONE dei CENTRI (K-CENTER) per GRAFI PESATI
# ----------------------------------------------------------------------------
'''
L'algoritmo di Plesnik (CENTER, 1987) risolve in modo approssimato il Priority
K-Center su Grafo con pesi sui nodi: si scelgono k centri che minimizzano il
massimo, su tutti i nodi v, del prodotto w(v)*d(v,S), con d cammino minimo.
Fissata una soglia R, ogni nodo v ha raggio r(v) = R/w(v). La procedura Filter
scorre i nodi in ordine di priorita' decrescente (raggio crescente): il primo
nodo non ancora coperto diventa centro e copre tutti i nodi scoperti v con
d(u,v) <= r(u)+r(v). Se Filter apre al piu' k centri la soglia e' accettabile.
Il valore ottimo e' uno dei prodotti w(v)*d(u,v): si cerca con una ricerca 
binaria il piu' piccolo R accettabile. Il valore della soluzione e' al piu' 
2R <= 2*OTT: approssimazione di fattore 2. Con tutti i pesi uguali coincide con 
il metodo a soglie di Hochbaum e Shmoys.
'''

def Filter_Plesnik(nodi,nodiOrdinati,matrixDistMin,pesiNodi,R,k): # T(n,k)
    scoperti = {v:True for v in nodi}                             # n*Θ(1) (J)
    S = []                                                        # Θ(1)
    for u in nodiOrdinati:                                        # n*Θ(1) (K)
        if scoperti[u]:                                           # Θ(1)
            S.append(u)                                           # Θ(1)   (L)
            if len(S) > k:                                        # Θ(1)   (M) 
                return S                                          # Θ(1)
            for v in nodi:                                        # n*Θ(1)+Θ(1)
                if scoperti[v] and \
                   matrixDistMin[u][v]*pesiNodi[u]*pesiNodi[v] \
                       <= R*(pesiNodi[u]+pesiNodi[v]):            # Θ(1)   (N) 
                    scoperti[v] = False                           # Θ(1)
    return S                                                      # Θ(1)

def KCenter_WeigthedGraphs(G,pesiNodi,k):                       # T(n,m)
    nodi = list(G.keys())                                       # n*Θ(1)   (A)
    if k >= len(nodi):                                          # Θ(1)     (B)
        return nodi                                             # Θ(1)
    matrixDistMin = {}                                          # Θ(1)     (C)
    for v in nodi:                                              # n*Θ(1)+Θ(1)
        matrixDistMin[v] = dijkstra_heapMin(G,v)[1]             # Θ((n+m)logn)
    nodiOrdinati = sorted(nodi,key=lambda v:-pesiNodi[v])       # Θ(nlogn) (D)
    candidatiSogliaR = set()                                    # Θ(1)     (E)
    for u in nodi:                                              # n*Θ(1)+Θ(1)
        for v in nodi:                                          # n*Θ(1)+Θ(1)
            if u != v:                                          # Θ(1)
                candidatiSogliaR.add(matrixDistMin[u][v]*pesiNodi[v]) # Θ(1)
    candidatiSogliaR = sorted(candidatiSogliaR)                 # Θ(n²logn)
    i_start = 0                                                 # Θ(1)     (F)
    i_end = len(candidatiSogliaR)-1                             # Θ(1)
    while i_start < i_end:                                      # Θ(logn)
        mid = (i_start + i_end)//2                              # Θ(1)
        S = Filter_Plesnik(nodi,nodiOrdinati, matrixDistMin, \
                           pesiNodi,candidatiSogliaR[mid],k)    # Θ(nk)    (G)
        if len(S) <= k:                                         # Θ(1)
            i_end = mid                                         # Θ(1)
        else:                                                   # Θ(1)
            i_start = mid+1                                     # Θ(1)
    centers = Filter_Plesnik(nodi,nodiOrdinati,matrixDistMin, \
                             pesiNodi,candidatiSogliaR[i_end],k)# Θ(nk)    (H)
    distMin = [math.inf]*len(nodi)                              # n*Θ(1)   (I)
    for c in centers:                                           # |S|*Θ(1)+Θ(1)
        for j in range(0,len(nodi)):                            # n*Θ(1)   (O)
            if distMin[j] > matrixDistMin[c][nodi[j]]:          # Θ(1)
                distMin[j] = matrixDistMin[c][nodi[j]]          # Θ(1)
    while len(centers) < k:                                     # (k-|S|)*Θ(1)
        distMax = (-1)*math.inf                                 # Θ(1)     (P)
        i_max = -1                                              # Θ(1)     (Q)
        for j in range(0,len(nodi)):                            # n*Θ(1)+Θ(1)
            if distMax < distMin[j]*pesiNodi[nodi[j]]:          # Θ(1)
                distMax = distMin[j]*pesiNodi[nodi[j]]          # Θ(1)
                i_max = j                                       # Θ(1)
        centers.append(nodi[i_max])                             # Θ(1)     (R)
        for j in range(0,len(nodi)):                            # n*Θ(1)   (S)
            if distMin[j] > matrixDistMin\
                                [nodi[i_max]][nodi[j]]:         # Θ(1)
                distMin[j] = matrixDistMin\
                                [nodi[i_max]][nodi[j]]          # Θ(1)
    return centers                                              # Θ(1)     (T)

# Costo Computazionale: T(n,m) = n*Θ((n+m)logn)+Θ(n²logn)+Θ(logn)*Θ(nk)+Θ(nk)
#                       T(n,m) = Θ(n(n+m)logn) (U)

# Commenti
# (A): Accesso ai nodi e al grafo come dizionario {nodo: lista di (vicino, 
#      peso)}. Il grafo deve essere connesso, con archi e pesi dei nodi 
#      positivi.
# (B): Se k >= n ogni nodo e' un centro e il valore e' 0: caso banale.
# (C): Andiamo a costrutire la matrice delle distanze minime di Dijkstra.
#      Questa e' una Hash Table di Hash Tables dove ciascuna chiave corrisponde
#      a un nodo del grafo e il valore e' a sua voltauna Hash Table contenente 
#      le distanze calcolate con Dijkstra tra il nodo stesso e ciascun altro
#      nodo del grafo.
#      Una generica cella di tale matrice matrixDistMin[c][v] contiene quindi 
#      la distanza minima da c a v.
#      La matrice delle distanze minime di Dijkstra e' calcolata con n visite 
#      di Dijkstra (dijkstra_heapMin ritorna un dizionario {nodo:distanza}).
#      Tale matrice e' necessaria per lo svolgimento dell'algoritmo di Plesnik
#      perche' Filter confronta d(u,v) per coppie qualsiasi. 
#      Il costo per la creazione di suddetta matrice e' quindi dato da n volte
#      il costo di una singola esecuzione di Dijkstra.
#      Dato che utilizziamo l'implementazione efficiente di Dijkstra - ovvero
#      quella che sfrutta l'Heap Minimo con costo Θ((n+m)logn) - il costo
#      totale per la costruzione della matrice risulta essere Θ(n(n+m)logn).
#      Con la matrice gia' disponibile, come nell'articolo originale, 
#      il costo scende a O(n²logn).
#      La space complexity risulta invece Θ(n²), data dalla dimensione della
#      matrice.
# (D): I nodi sono ordinati per peso decrescente, cioe' per raggio r(v)=R/w(v)
#      crescente. L'ordine non dipende da R e si calcola una sola volta. E' la
#      condizione che garantisce r(u) <= r(v) per ogni v assegnato a u, quindi
#      d(u,v) <= r(u)+r(v) <= 2r(v).
# (E): Valori candidati per la soglia R: il valore ottimo, se positivo,e' uno 
#      dei prodotti w(v)*d(u,v) con u diverso da v.
#      Questi sono al piu' n(n-1) valori distinti.
#      Sono n(n-1) in quanti si hanno n possibili valori di u e n-1 possibili
#	   valori di v. Non n(n-1)/2!! Infatti se e' vero che la distanza d(u,v)
#	   e' simmetrica, il peso non lo e' e, quindi, w(v)·d(u,v) è in generale 
#	   diverso da w(u)·d(u,v).
#      Per ciascun nodo del grafo, si scorrono i nodi restanti, si calcola
#      il prodotto dist(u,v)*w(v) corrispondente e si aggiunge il valore nello
#      HashSet dei valori candidati di R. Dato che si tratta di uno HashSet
#      qualsiasi valore duplicato verra' automaticamente scartato mantenendo
#      solo i valori unici.
#      Fatto cio' si ordinano tutti i valori unici raccolti in ordine di
#      prodotto dist(u,v)*w(v) crescente usando un algoritmo di ordinamento
#      ottimale basato sui confronti - ad esempio MergeSort/QuickSort/HeapSort.
#      Dato che il numero di valori candidati e', nel caso peggiore, pari a n²,
#      il costo dell'ordinamento e' dato da n²logn²=2·n²·logn=n²·logn.
# (F): Dato che i valori candidati di R sono gia' ordinati in ordine crescente, 
#      per trovarne il valore minimo che consente di ottenere num_centri<=K,
#	   possiamo eseguire una ricerca binaria.
#	   Si esegue, quindi, la ricerca binaria sull'indice del piu' piccolo R per 
#	   cui Filter apre al piu' k centri. 
#	   Dato che abbiamo un numero di candidati O(n²), la ricerca binaria avra' 
#	   costo Θ(logn²)=Θ(2·logn)=Θ(logn)
# (G): Ogni chiamata di Filter costa Θ(nk) grazie all'arresto a k+1 centri (M).
# (H): Filter finale con R* = candidati[end]. Il valore della soluzione e' al 
#      piu' 2R* <= 2*OTT.
# (I): Completamento a k centri (facoltativo): se Filter apre meno di k centri 
#      si aggiungono nodi con w(v)*distMin massimo; aggiungere centri non 
#      peggiora il valore. distMin e' aggiornato in modo incrementale, Θ(n) per 
#      centro aggiunto.
# (J): scoperti[v] vale True se v non e' ancora coperto da nessun centro.
# (K): I nodi si scorrono in ordine di priorita' decrescente: il primo nodo 
#      scoperto che si incontra e' sempre quello con raggio r minimo tra gli 
#      scoperti.
# (L): u diventa centro (rappresentante), viene aggiunto alla lista soluzione
#      S e verra' tolto dai nodi scoperti, perche' dist[u][u] = 0 soddisfa 
#      la condizione (N).
# (M): Arresto anticipato: se il numero di centri supera k, la soglia R e' 
#      troppo piccola (nessuna soluzione di valore R esiste). 
#      Costo di Filter: Θ(nk) invece di O(n²).
# (N): Condizione d(u,v) <= r(u)+r(v) con r(x)=R/w(x)
#      Per semplicita' viene scritta senza divisioni. 
#      Qui di seguito i passaggi.
#      1) d(u,v) <= R/w(u)+R/w(v)
#	   2) d(u,v) <= [R·(w(u)+w(v))]/[w(u)·w(v)]
#	   3) d(u,v)·[w(u)·w(v)] <= R·[w(u)+w(v)]
#      Quindi, d(u,v)*w(u)*w(v) <= R*(w(u)+w(v)). 
#      Con pesi e distanze interi il confronto e' esatto: niente errori di 
#      arrotondamento. I nodi v che la soddisfano formano D(u).
# (O): Si costruisce il vettore distMin contenente, per ciascun nodo, la 
#      distanza minima calcolata per quel nodo da tutti i centri selezionati 
#      fino ad ora.
# (P): Fino a che il numero di centri selezionati non raggiunge il target k,
#      continuiamo ad aggiungere nuovi centri. Uno ad ogni ciclo.
# (Q): Fra tutti i nodi del grafo, selezioniamo quello corrispondente alla max
#      delle distanze minime dai centri. La domanda che ci si pone e'...ma non
#      andremo a prendere nodi che non sono scoperti (ovvero che sono coperti
# 	   da altri centri)??...Certamente, ed e' giusto cosi. I centri selezionati
# 	   Fino ad ora gia' garantiscono una copertura di tutti i nodi del grafo.
# 	   I centri che andiamo ad aggiungere saranno presi fra questi andando a
# 	   prediligere quelli aventi distanza d(c,v) (non pesata!) minima dai 
#      centri selezionati fino a quel punto.
# (R): Il nodo selezionato viene aggiunto alla lista dei centri 	   
# (S): Data l'aggiunta del nuovo centro, si aggiorna il vettore delle distanze
#      minime distMin andando a confrontare i valori in esso contenuti con le
# 	   corrispondenti distanze dal nuovo centro. Se i primi sono maggiori dei
# 	   secondi, li si sostituiscono con i secondi cosi' da garantire che 
#      distMin contenga i valori minimi assoluti aggiornati.
# (T): Restituisce i k centri. Per ogni v assegnato al proprio u vale
#      w(v)*d(u,v) <= 2R; i centri di Filter hanno palle B(u,r(u)) disgiunte, 
#      quindi un ottimo di valore R ha bisogno di tanti centri quanti ne apre 
#      Filter.
# (U): Il valore ottenuto e' al piu' 2*OTT: fattore 2, il migliore possibile in 
#      tempo polinomiale salvo P = NP. Greedy con w*d (farthest-first pesato): 
#      euristica senza garanzia nota, non e' questo algoritmo.




# =================== ALGORITMI ESATTI di FORZA BRUTA =========================


# ALGORITMO ESATTO per GRAFI NON PESATI tramite ENUMERAZIONE
# ----------------------------------------------------------------------------
'''
L'algoritmo di K-Center Esatto (Forza Bruta) su Grafo esplora tutti i possibili
sottoinsiemi di k nodi del grafo. Per ogni sottoinsieme, preso come insieme di
centri, calcola il raggio: la massima distanza di un nodo dal centro piu'vicino
(distanze minime calcolate una sola volta con Dijkstra da ogni nodo). Tra tutti
gli C(n,k) sottoinsiemi restituisce quello di raggio minimo: soluzione ottima.
I sottoinsiemi non sono generati con la ricorsione, ma con un vettore di k 
indici crescenti che avanza in ordine lessicografico. 
In questa versione non c'e' pruning: l'enumerazione e' esaustiva. 
Cio' significa che si esamina ogni sottoinsieme di k nodi, tutti e per intero. 
Questa versione non salta nulla. Per ciascuno dei C(n, k) sottoinsiemi si 
calcola il raggio fino in fondo, con tutti gli n·k confronti, anche quando è 
già evidente che quel sottoinsieme è peggiore del migliore trovato.
Questo algoritmo di forza bruta serve come ottimo di riferimento su istanze 
piccole, ad esempio per misurare il rapporto di approssimazione dell'algoritmo 
di Gonzalez.
'''

def KCenter_Graphs_BruteForce(G,k):                         # T(n,m)
    nodi = list(G.keys())                                   # n*Θ(1)       (A)
    n = len(nodi)                                           # Θ(1)
    matrixDistMin = {}                                      # Θ(1)         (B)
    for v in nodi:                                          # n*Θ(1)+Θ(1)
        matrixDistMin[v] = dijkstra_heapMin(G,v)[1]         # Θ((n+m)logn)
    raggioMin = math.inf                                    # Θ(1)         (C)
    centers = None                                          # Θ(1)
    idx = list(range(0,k))                                  # k*Θ(1)       (D)
    while True:                                             # C(n,k)       (E)
        raggio = (-1)*math.inf                              # Θ(1)         (F)
        for v in nodi:                                      # n*Θ(1)+Θ(1)
            distMin = math.inf                              # Θ(1)         (G)
            for i in idx:                                   # k*Θ(1)+Θ(1)
                if distMin > matrixDistMin[nodi[i]][v]:     # Θ(1)         (H)
                    distMin = matrixDistMin[nodi[i]][v]     # Θ(1)
            if raggio < distMin:                            # Θ(1)         (I)
                raggio = distMin                            # Θ(1)
        if raggio < raggioMin:                              # Θ(1)         (J)
            raggioMin = raggio                              # Θ(1)
            centers = [nodi[i] for i in idx]                # Θ(k)
        j = k-1                                             # Θ(1)         (K)
        while j >= 0 and idx[j] == n-k+j:                   # O(k)
            j -= 1                                          # Θ(1)
        if j < 0:                                           # Θ(1)         (L)
            break                                           # Θ(1)
        idx[j] += 1                                         # Θ(1)         (M)
        for t in range(j+1,k):                              # O(k)
            idx[t] = idx[t-1]+1                             # Θ(1)         (N)
    return centers, raggioMin                               # Θ(1)         (O)

# Costo Computazionale: T(n,m,k) = n*Θ((n+m)logn) + C(n,k)*Θ(nk)
#                       T(n,m,k) = Θ(n(n+m)logn + C(n,k)·n·k)              (P)

# Commenti
# (A): Data la lista di adiacenza del grafo, si estraggono i suoi nodi.
#      La lista di adiacenza deve essere data come una Hash Table avente i nodi
#      come chiavi e, come valori, le liste dei corrispondenti archi (
#      rappresentati come coppie (nodo, peso)).
# (B): Andiamo a costrutire la matrice delle distanze minime di Dijkstra.
#      Questa e' una Hash Table di Hash Tables dove ciascuna chiave corrisponde
#      a un nodo del grafo e il valore e' a sua volta una Hash Table contenente 
#      le distanze calcolate con Dijkstra tra il nodo stesso e ciascun altro
#      nodo del grafo.
#      Una generica cella di tale matrice matrixDist[c][v] contiene quindi 
#      la distanza minima da c a v.
#      La matrice delle distanze minime di Dijkstra e' calcolata con n visite 
#      di Dijkstra (dijkstra_heapMin ritorna un dizionario {nodo:distanza}).
#      Il costo per la creazione di suddetta matrice e' quindi dato da n volte
#      il costo di una singola esecuzione di Dijkstra.
#      Dato che utilizziamo l'implementazione efficiente di Dijkstra - ovvero
#      quella che sfrutta l'Heap Minimo con costo Θ((n+m)logn) - il costo
#      totale per la costruzione della matrice risulta essere Θ(n(n+m)logn).
#      Con la matrice gia' disponibile, come nell'articolo originale, 
#      il costo scende a O(n²logn).
#      La space complexity risulta invece Θ(n²), data dalla dimensione della
#      matrice.
#      Il grafo deve essere connesso, altrimenti compaiono distanze infinite e 
#      il raggio puo' valere inf.
# (C): Si inizializza la variabile usata per contenere il minimo dei raggi 
#      massimi ricavati dalle distanze minime di dijkstra calcolate per ciascun 
#      insieme di centri - ovvero, raggioMin = raggio del miglior sottoinsieme 
#      trovato finora. Esso viene inizializzato a +inf cosi che qualsiasi 
#      sottoinsieme sara' migliore. 
#      Si inizializza inoltre il vettore contenente il miglior insieme.
#      L'obiettivo e' minimizzare il RAGGIO, cioe'la distanza massima di un 
#      nodo dal centro piu' vicino (obiettivo del k-center).
# (D): idx: vettore di k indici in ordine crescente che rappresenta il 
#      sottoinsieme corrente di centri. Questo vettore deve essere usato in 
#      concomitanza con il vettore dei nodi (da cui estrarre i centri tramite
#      indice) Il primo sottoinsieme e' {0,1,...,k-1}.
# (E): Il ciclo esegue una iterazione per ogni sottoinsieme di k nodi: in tutto
#      C(n,k) iterazioni, e termina con il break al passo (L).
# (F): VALUTAZIONE DEL SOTTOINSIEME CORRENTE: il raggio e' il massimo, su tutti 
#      i nodi v, della distanza di v dal centro piu' vicino in idx.
#      Sostanzialmente, per ciascun nodo v del grafo si ricava la distanza 
#      minima tra esso e tutti i centri contenuti nel sottoinsieme corrente.
#      Da tutti i valori di distanza minima ricavati per tutti i nodi v, si 
#      salva nella variabile raggio il massimo di loro. Questa sara' la massima
#      delle minime distanze di dijkstra calcolate per il sottoinsieme di 
#      centri corrente.
#      Costo per sottoinsieme: n*k confronti, cioe' Θ(nk).
# (G): distMin: distanza del nodo v dal centro piu' vicino. Va riazzerata a inf
#      per ogni nodo v. Se v e' esso stesso un centro vale 0, perche' 
#      dist[v][v]=0.
# (H): Aggiorna il minimo sui k centri del sottoinsieme. 
#      Il lookup nel dizionario dist[nodi[i]][v] costa Θ(1).
# (I): Il nodo servito peggio determina il raggio: si tiene il massimo delle
#      distanze minime distMin su tutti i nodi.
# (J): Se il raggio e' minore del migliore trovato,aggiorna raggioMin e centers.
#      Il confronto e' stretto (<): a parita' di raggio resta il primo 
#      sottoinsieme in ordine lessicografico. 
#      [nodi[i] for i in idx] crea una COPIA: necessario perche' idx verra' 
#      modificato dalle iterazioni successive.
# (K): GENERAZIONE DEL SOTTOINSIEME SUCCESSIVO (ordine lessicografico).L'indice
#      idx[j] e' al suo massimo quando vale n-k+j: le posizioni a destra sono
#      gia' occupate dagli ultimi nodi. Si cerca da destra il primo indice j 
#      non al massimo. Costo O(k), trascurabile rispetto al Θ(nk) di (F).
# (L): Se nessun indice e' incrementabile (j < 0) l'ultimo sottoinsieme
#      {n-k,...,n-1} e' appena stato valutato: l'enumerazione e' finita
#      e il numero totale di iterazioni e' esattamente C(n,k).
# (M): Incrementa di 1 l'indice idx[j] trovato al passo (K).
# (N): Riscrive gli indici a destra di j come consecutivi: idx[t] = idx[t-1]+1.
#      Esempio con n=5 e k=3: {0,1,2}->{0,1,3}->{0,1,4}->{0,2,3}->{0,2,4}
#      ->{0,3,4}->{1,2,3}->{1,2,4}->{1,3,4}->{2,3,4}:C(5,3)=10 sottoinsiemi.
# (O): Restituisce i centri ottimi e il raggio ottimo. Con k=n tutti i nodi son
#      centri e il raggio vale 0. 
#      Il raggio restituito e' il riferimento r* con cui confrontare Gonzalez: 
#      raggio_gonzalez <= 2·r*.
# (P): Il termine dominante e' C(n,k)·n·k, circa O(n^(k+1)) per k piccolo: 
#      esponenziale nel caso peggiore perche' il problema e' NP-difficile. 
#      Esempi: n=12 e k=3 danno 220 sottoinsiemi, n=50 e k=5 ne danno circa 
#      2,1 milioni, n=800 e k=12 sono impraticabili. 
#      Pruning non presente: una possibile ottimizzazione e'
#      interrompere il ciclo su v appena raggio >= raggioMin (non cambia il 
#      caso peggiore).



# ALGORITMO ESATTO per GRAFI PESATI tramite ENUMERAZIONE
# ----------------------------------------------------------------------------
'''
L'algoritmo di Priority K-Center Esatto (Forza Bruta) su Grafo con pesi sui 
nodi esplora tutti i possibili sottoinsiemi di k nodi del grafo. 
Per ogni sottoinsieme, preso come insieme di centri, calcola il tempo ponderato 
massimo: il massimo, su tutti i nodi v, del prodotto tra il peso (priorita') 
w(v) e la distanza di v dal centro piu' vicino (distanze minime calcolate una 
sola volta con Dijkstra da ogni nodo). 
Tra tutti gli C(n,k) sottoinsiemi restituisce quello di valore minimo:
soluzione ottima. I sottoinsiemi sono generati con un vettore di k indici
crescenti che avanza in ordine lessicografico.
Con tutti i pesi uguali a 1 coincide con il K-Center esatto.
Serve come ottimo di riferimento su istanze piccole, ad esempio per misurare il 
rapporto di approssimazione dell'algoritmo di Plesnik.
L'unica cosa che differenzia questo algoritmo da quello di forza bruta per il
caso non pesato consiste nel moltiplicare le distanze di dijkstra per il peso
del nodo v corrispondente.
'''

def KCenter_WeightedGraphs_BruteForce(G,pesiNodi,k):        # T(n,m)
    nodi = list(G.keys())                                   # n*Θ(1)       
    n = len(nodi)                                           # Θ(1)
    dist = {}                                               # Θ(1)
    for v in nodi:                                          # n*Θ(1)+Θ(1)
        dist[v] = dijkstra_heapMin(G,v)[1]                  # Θ((n+m)logn)
    valoreMin = math.inf                                    # Θ(1)         (A)
    centers = None                                          # Θ(1)
    idx = list(range(0,k))                                  # k*Θ(1)
    while True:                                             # C(n,k)
        valore = (-1)*math.inf                              # Θ(1)         (B)
        for v in nodi:                                      # n*Θ(1)+Θ(1)
            distMin = math.inf                              # Θ(1)
            for i in idx:                                   # k*Θ(1)+Θ(1)
                if distMin > dist[nodi[i]][v]:              # Θ(1)
                    distMin = dist[nodi[i]][v]              # Θ(1)
            if valore < distMin*pesiNodi[v]:                # Θ(1)         (C)
                valore = distMin*pesiNodi[v]                # Θ(1)
        if valore < valoreMin:                              # Θ(1)         (D)
            valoreMin = valore                              # Θ(1)
            centers = [nodi[i] for i in idx]                # Θ(k)
        j = k-1                                             # Θ(1)
        while j >= 0 and idx[j] == n-k+j:                   # O(k)
            j -= 1                                          # Θ(1)
        if j < 0:                                           # Θ(1) 
            break                                           # Θ(1)
        idx[j] += 1                                         # Θ(1)
        for t in range(j+1,k):                              # O(k)
            idx[t] = idx[t-1]+1                             # Θ(1)
    return centers, valoreMin                               # Θ(1)

# Costo Computazionale: T(n,m,k) = n*Θ((n+m)logn) + C(n,k)*Θ(nk)
#                       T(n,m,k) = Θ(n(n+m)logn + C(n,k)·n·k)

# Commenti
# (A): Si inizializza il valoreMin (corrispondente a raggioMin)
# (B): Si inizializza il valore (corrispondente a raggio)
# (C): Si assegna a valore il massimo dei minimi prodotti dist*pesoNodo
#      ricavati per l'insieme di centri corrente.
# (D): Fra tutti i valori massimi ricavati si va a trovare quello minimo.
#      Questo rappresenta la distanza minima finale corrispondente alla
#      selezione dei centri corrente e che consente di trovare quella migliore.



" ESEMPI ********************************************************************"

"""
Consideriamo due esempi: uno ispirato alla selezione di hub in una rete di
aeroporti e uno alla selezione di postazioni di guarnigioni su una rete di
isole tailandesi.
"""


# LISTE DI ADIACENZA ----------------------------------------------------------

'Grafo Indiretto Connesso Non Pesato - Esempio Scali Aerei  ------------------'
'''
Costo dei Nodi -> Nessuno
Costo degli Archi -> Nessuno (si assegna 1 a tutti per semplicita')
''' 
L_ScaliAerei = {
    "MXP": [("FCO", 1), ("VCE", 1), ("CDG", 1), ("FRA", 1), ("ZRH", 1)],
    "FCO": [("MXP", 1), ("NAP", 1), ("FRA", 1), ("MAD", 1), 
            ("ATH", 1), ("IST", 1)],
    "VCE": [("MXP", 1), ("FRA", 1), ("VIE", 1)],
    "NAP": [("FCO", 1)],
    "CDG": [("MXP", 1), ("LHR", 1), ("AMS", 1), ("FRA", 1), ("MAD", 1)],
    "LHR": [("CDG", 1), ("AMS", 1), ("FRA", 1), ("DUB", 1)],
    "AMS": [("CDG", 1), ("LHR", 1), ("FRA", 1), ("CPH", 1), ("BRU", 1)],
    "FRA": [("MXP", 1), ("FCO", 1), ("VCE", 1), ("CDG", 1), ("LHR", 1),
            ("AMS", 1), ("ZRH", 1), ("VIE", 1), ("IST", 1), ("WAW", 1)],
    "MAD": [("FCO", 1), ("CDG", 1), ("BCN", 1), ("LIS", 1)],
    "BCN": [("MAD", 1)],
    "LIS": [("MAD", 1)],
    "ZRH": [("MXP", 1), ("FRA", 1)],
    "VIE": [("VCE", 1), ("FRA", 1), ("WAW", 1)],
    "CPH": [("AMS", 1), ("ARN", 1)],
    "ARN": [("CPH", 1)],
    "ATH": [("FCO", 1), ("IST", 1)],
    "IST": [("FCO", 1), ("FRA", 1), ("ATH", 1)],
    "DUB": [("LHR", 1)],
    "WAW": [("FRA", 1), ("VIE", 1)],
    "BRU": [("AMS", 1)],
}


'Grafo Indiretto Connesso Pesato - Esempio Isole Tailandesi ------------------'
'''
Costo dei Nodi    -> Giorni di cammino per raggiungere il monastero / 
                     Priorita' del monastero 
Costo degli Archi -> Giorni di navigazione per raggiungere l'isola
'''
L_Tailandia = {
    "Bulon Le":  [("Libong",2),("Lipe",2),("Sukorn",2),("Tarutao",1)],
    "Kho Khao":  [("Phayam",3),("Similan",4),("Surin",2),("Yao Noi",5)],
    "Lanta":     [("Mook",1),("Ngai",1),("Phi Phi",2),("Racha Yai",3)],
    "Libong":    [("Bulon Le",2),("Mook",1),("Ngai",1),("Sukorn",1)],
    "Lipe":      [("Bulon Le",2),("Tarutao",2)],
    "Mook":      [("Lanta",1),("Libong",1),("Ngai",1)],
    "Ngai":      [("Lanta",1),("Libong",1),("Mook",1)],
    "Phayam":    [("Kho Khao",3),("Surin",3)],
    "Phi Phi":   [("Lanta",2),("Phuket",2),("Racha Yai",2),("Yao Noi",2)],
    "Phuket":    [("Phi Phi",2),("Racha Yai",1),("Similan",5),("Yao Noi",1)],
    "Racha Yai": [("Lanta",3),("Phi Phi",2),("Phuket",1)],
    "Similan":   [("Kho Khao",4),("Phuket",5),("Surin",4),("Yao Noi",5)],
    "Sukorn":    [("Bulon Le",2),("Libong",1)],
    "Surin":     [("Kho Khao",2),("Phayam",3),("Similan",4)],
    "Tarutao":   [("Bulon Le",1),("Lipe",2)],
    "Yao Noi":   [("Kho Khao",5),("Phi Phi",2),("Phuket",1),("Similan",5)],
}

nw_Tailandia = {
    "Bulon Le":  1,
    "Kho Khao":  2,
    "Lanta":     2,
    "Libong":    2,
    "Lipe":      1,
    "Mook":      1,
    "Ngai":      1,
    "Phayam":    3,
    "Phi Phi":   1,
    "Phuket":    2,
    "Racha Yai": 1,
    "Similan":   2,
    "Sukorn":    1,
    "Surin":     4,
    "Tarutao":   6,
    "Yao Noi":   2
}
       


# ALGORITMO di VERTEX COVER per GRAFI -----------------------------------------

'Grafo Indiretto Connesso - Esempio Scali Aerei  -----------------------------'
u, k = "MXP", 3
cc_Graphs_Exact =  KCenter_Graphs_BruteForce(L_ScaliAerei,k)[0]
cc_Graphs_Approx = KCenter_Graphs(L_ScaliAerei,u,k)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Scali Aerei:\n"
    "Selezione dei Centri in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Exact)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Approx)
)


'Grafo Indiretto Connesso - Esempio Isole Tailandesi  ------------------------'
u, k = "Bulon Le", 5
cc_Graphs_Exact =  KCenter_Graphs_BruteForce(L_Tailandia,k)[0]
cc_Graphs_Approx = KCenter_Graphs(L_Tailandia, u, k)
cc_Graphs_Approx_v2 = KCenter_Graphs_variant(L_Tailandia, nw_Tailandia, u, k)
cc_WGraphs_Exact =  KCenter_WeightedGraphs_BruteForce( \
                            L_Tailandia,nw_Tailandia, k)[0]
cc_WGraphs_Approx = KCenter_WeigthedGraphs(L_Tailandia,nw_Tailandia,k)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Isole Tailandesi:\n"
    "Selezione dei Centri in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Exact)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato (Gonzalez):\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Approx)
    + "\n"
    "-> Algoritmo di Approssimazione con Pesi Additivi sui Nodi:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Approx_v2)
    + "\n"
    "-> Algoritmo Esatto con Grafo Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_WGraphs_Exact)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Pesato (Plesnik):\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_WGraphs_Approx)
)