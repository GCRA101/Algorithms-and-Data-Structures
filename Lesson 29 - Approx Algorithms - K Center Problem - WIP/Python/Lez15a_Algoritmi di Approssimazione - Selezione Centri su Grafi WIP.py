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
import copy


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
    dictDistanze = {}                                       # Θ(1)
    nodi = list(G.keys())                                   # n*Θ(1)
    i_center = 0                                            # Θ(1)
    centers[i_center] = u                                   # Θ(1)
    for i in range(0,k-1):                                  # k*Θ(1)+Θ(1)
        distanze = dijkstra_heapMin(G,centers[i_center])    # Θ((n+m)logn)
        dictDistanze[centers[i_center]] = distanze          # Θ(1)
        distMax = (-1)*math.inf                             # Θ(1)
        i_max = -1                                          # Θ(1)
        for j in range(0,len(nodi)):                        # n*Θ(1)+Θ(1)
            distMin = math.inf                              # Θ(1)
            for node in dictDistanze.keys():                # O(k)+Θ(1)
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
        distanze = dijkstra_heapMin(G,centers[i_center])    # Θ((n+m)logn) (E)
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
# (A)
# (B)
# (C)
# (D)
# (E)
# (F)
# (G)
# (H)
# (I)
# (J)


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
    distConPesiNodi = {nodo:None for nodo in nodi}          # n*Θ(1)    
    distMin = [math.inf]*len(nodi)                          # n*Θ(1)
    i_center = 0                                            # Θ(1)
    centers[i_center] = u                                   # Θ(1)
    for i in range(0,k-1):                                  # (k-1)*Θ(1)+Θ(1)
        distanze = dijkstra_heapMin(G,centers[i_center])    # Θ((n+m)logn)
        for nodo in nodi:                                   # n*Θ(1)+Θ(1)
            distConPesiNodi[nodo] = \
                distanze[nodo] + pesiNodi[nodo]             # Θ(1)
        distConPesiNodi[centers[i_center]] = 0              # Θ(1)
        distMax = (-1)*math.inf                             # Θ(1)
        i_max = -1                                          # Θ(1)
        for j in range(0,len(nodi)):                        # n*Θ(1)+Θ(1)
            if distMin[j] > distConPesiNodi[nodi[j]]:       # Θ(1)
                distMin[j] = distConPesiNodi[nodi[j]]       # Θ(1)
            if distMax < distMin[j]:                        # Θ(1)
                distMax = distMin[j]                        # Θ(1)
                i_max = j                                   # Θ(1)
        i_center += 1                                       # Θ(1)
        centers[i_center] = nodi[i_max]                     # Θ(1)
    return centers                                          # Θ(1)

# Costo Computazionale: T(n,m,k) = Θ(k)+Θ(n)+k*[Θ((n+m)logn)+Θ(n)+Θ(n)]
#                       T(n,m,k) = Θ(k*(n+m)logn)

# Commenti
# (A)
# (B)
# (C)
# (D)
# (E)
# (F)
# (G)
# (H)
# (I)
# (J)



# =================== ALGORITMI ESATTI di FORZA BRUTA =========================


# ALGORITMO ESATTO per GRAFI NON PESATI tramite ENUMERAZIONE
# ----------------------------------------------------------------------------
'''
L'algoritmo di K-Center Esatto (Forza Bruta) su Grafo esplora tutti i possibili
sottoinsiemi di k nodi del grafo. Per ogni sottoinsieme, preso come insieme di
centri, calcola il raggio: la massima distanza di un nodo dal centro piu' vicino
(distanze minime calcolate una sola volta con Dijkstra da ogni nodo). Tra tutti
gli C(n,k) sottoinsiemi restituisce quello di raggio minimo: soluzione ottima.
I sottoinsiemi non sono generati con la ricorsione, ma con un vettore di k 
indici crescenti che avanza in ordine lessicografico. 
In questa versione non c'e' pruning: l'enumerazione e' esaustiva. 
Serve come ottimo di riferimento su istanze piccole, ad esempio per
misurare il rapporto di approssimazione dell'algoritmo di Gonzalez.
'''

def KCenter_Graphs_BruteForce(G,k):                         # T(n,m)
    nodi = list(G.keys())                                   # n*Θ(1)       (A)
    n = len(nodi)                                           # Θ(1)
    dist = {}                                               # Θ(1)         (B)
    for v in nodi:                                          # n*Θ(1)+Θ(1)
        dist[v] = dijkstra_heapMin(G,v)                     # Θ((n+m)logn)
    raggioMin = math.inf                                    # Θ(1)         (C)
    centers = None                                          # Θ(1)
    idx = list(range(0,k))                                  # k*Θ(1)       (D)
    while True:                                             # C(n,k)       (E)
        raggio = (-1)*math.inf                              # Θ(1)         (F)
        for v in nodi:                                      # n*Θ(1)+Θ(1)
            distMin = math.inf                              # Θ(1)         (G)
            for i in idx:                                   # k*Θ(1)+Θ(1)
                if distMin > dist[nodi[i]][v]:              # Θ(1)         (H)
                    distMin = dist[nodi[i]][v]              # Θ(1)
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
# (A): Per poter rappresentare un sottoinsieme di centri con k indici e' necessario
#      un accesso posizionale ai nodi: la list ricavata dalle chiavi del grafo
#      (n*Θ(1)) permette di passare da indice a etichetta del nodo in Θ(1).
#      Richiede che il grafo sia dato come dizionario {nodo: lista di (vicino, peso)}.
# (B): dist e' un dizionario di dizionari: dist[c][v] e' la distanza minima da c a v,
#      calcolata una sola volta con n visite di Dijkstra (dijkstra_heapMin restituisce
#      un dizionario {nodo: distanza}). Senza questa precomputazione ogni
#      sottoinsieme richiederebbe k visite di Dijkstra invece di Θ(nk) confronti.
#      Costo: Θ(n(n+m)logn) in tempo e Θ(n²) in memoria. Il grafo deve essere
#      connesso, altrimenti compaiono distanze infinite e il raggio puo' valere inf.
# (C): raggioMin: raggio del miglior sottoinsieme trovato finora. Inizializzato a
#      +inf: qualsiasi sottoinsieme sara' migliore. centers: miglior insieme di
#      centri trovato, inizializzato a None. Si minimizza il RAGGIO, cioe' la
#      distanza massima di un nodo dal centro piu' vicino (obiettivo del k-center).
# (D): idx: vettore di k indici crescenti che rappresenta il sottoinsieme corrente
#      di centri. Il primo sottoinsieme e' {0,1,...,k-1}. Sostituisce
#      itertools.combinations: niente ricorsione, memoria aggiuntiva Θ(k).
#      Richiede 1 <= k <= n.
# (E): Il ciclo esegue una iterazione per ogni sottoinsieme di k nodi: in tutto
#      C(n,k) iterazioni, e termina con il break al passo (L).
# (F): VALUTAZIONE DEL SOTTOINSIEME CORRENTE: il raggio e' il massimo, su tutti i
#      nodi v, della distanza di v dal centro piu' vicino in idx.
#      Costo per sottoinsieme: n*k confronti, cioe' Θ(nk).
# (G): distMin: distanza del nodo v dal centro piu' vicino. Va riazzerata a +inf
#      per ogni nodo v. Se v e' esso stesso un centro vale 0, perche' dist[v][v]=0.
# (H): Aggiorna il minimo sui k centri del sottoinsieme. Il lookup nel dizionario
#      dist[nodi[i]][v] costa Θ(1).
# (I): Il nodo servito peggio determina il raggio: si tiene il massimo delle
#      distanze minime distMin su tutti i nodi.
# (J): Se il raggio e' minore del migliore trovato, aggiorna raggioMin e centers.
#      Il confronto e' stretto (<): a parita' di raggio resta il primo sottoinsieme
#      in ordine lessicografico. [nodi[i] for i in idx] crea una COPIA: necessario
#      perche' idx verra' modificato dalle iterazioni successive.
# (K): GENERAZIONE DEL SOTTOINSIEME SUCCESSIVO (ordine lessicografico). L'indice
#      idx[j] e' al suo massimo quando vale n-k+j: le posizioni a destra sono
#      gia' occupate dagli ultimi nodi. Si cerca da destra il primo indice j non
#      al massimo. Costo O(k), trascurabile rispetto al Θ(nk) di (F).
# (L): Se nessun indice e' incrementabile (j < 0) l'ultimo sottoinsieme
#      {n-k,...,n-1} e' appena stato valutato: l'enumerazione e' finita
#      e il numero totale di iterazioni e' esattamente C(n,k).
# (M): Incrementa di 1 l'indice idx[j] trovato al passo (K).
# (N): Riscrive gli indici a destra di j come consecutivi: idx[t] = idx[t-1]+1.
#      Esempio con n=5 e k=3: {0,1,2} -> {0,1,3} -> {0,1,4} -> {0,2,3} -> {0,2,4}
#      -> {0,3,4} -> {1,2,3} -> {1,2,4} -> {1,3,4} -> {2,3,4}: C(5,3)=10 sottoinsiemi.
# (O): Restituisce i centri ottimi e il raggio ottimo. Con k = n tutti i nodi sono
#      centri e il raggio vale 0. Il raggio restituito e' il riferimento r* con cui
#      confrontare Gonzalez: raggio_gonzalez <= 2·r*.
# (P): Il termine dominante e' C(n,k)·n·k, circa O(n^(k+1)) per k piccolo: esponenziale
#      nel caso peggiore perche' il problema e' NP-difficile. Esempi: n=12 e k=3 danno
#      220 sottoinsiemi, n=50 e k=5 ne danno circa 2,1 milioni, n=800 e k=12 sono
#      impraticabili. Pruning non presente: una possibile ottimizzazione e'
#      interrompere il ciclo su v appena raggio >= raggioMin (non cambia il caso peggiore).


# ALGORITMO ESATTO per GRAFI PESATI (Garey & Johnson 1979)
# ----------------------------------------------------------------------------
'''
L'algoritmo di Vertex Cover Esatto su Grafo Pesato esplora tutti i possibili
sottoinsiemi di nodi tramite backtracking ricorsivo. Per ogni nodo decide se
includerlo o escluderlo dalla copertura (albero binario di profondita' n),
accumulando il peso totale del sottoinsieme corrente lungo ogni ramo.
Raggiunta una foglia (tutti i nodi decisi), verifica se il sottoinsieme corrente
copre almeno un estremo per ogni arco attivo (costo >= costoMin).
Se la verifica ha successo, aggiorna il best secondo il criterio scelto:
  - IsMinWeight=True : minimizza il peso totale; a parita' di peso, min nodi.
  - IsMinWeight=False: minimizza la cardinalita'; a parita' di nodi, max peso.
'''

def VertexCover_WeightedGraphs_BruteForce(E, pesiNodi,
                                IsMinWeight, costoMin=0):   # T(n,m)
    nodiSet = set()                                         # Θ(1)         (A)
    for e in E:                                             # m*Θ(1)+Θ(1)
        nodiSet.add(e.u)                                    # Θ(1)
        nodiSet.add(e.v)                                    # Θ(1)
    nodiCopertura = {nodo: False for nodo in nodiSet}       # Θ(n)         (B)
    archi = copy.deepcopy(E)                                # Θ(m)         (C)
    archi = [a for a in archi if a.costo >= costoMin]       # Θ(m)         (D)
    if len(archi) == 0:                                     # Θ(1)         (E)
        return nodiCopertura                                # Θ(1)
    nodi         = list(nodiSet)                            # Θ(n)         (F)
    n            = len(nodi)                                # Θ(1)
    dictPesiNodi = copy.deepcopy(pesiNodi)                  # Θ(n)         (G)
    best_set  = None                                        # Θ(1)         (H)
    best_size = float('inf')                                # Θ(1)         (I)
    best_cost = float('inf') if IsMinWeight else float('-inf')  # Θ(1)     (J)

    def backtrack(idx, S_corrente, costo_corrente):         # O(2^n·m)
        nonlocal best_set, best_size, best_cost
        if idx == n:                                        # Θ(1)         (K)
            count = 0                                       # Θ(1)
            for a in archi:                                 # Θ(m)         (L)
                if a.u in S_corrente or a.v in S_corrente:  # Θ(1)
                    count += 1                              # Θ(1)
            if count == len(archi):                         # Θ(1)         (M)
                size = len(S_corrente)                      # Θ(1)
                if IsMinWeight:                             # Θ(1)         (N)
                    # minimizza peso; a parita' di peso, min cardinalita'
                    if costo_corrente < best_cost or \
                       (costo_corrente == best_cost and
                        size < best_size):
                        best_set  = set(S_corrente)         # Θ(n)
                        best_size = size                    # Θ(1)
                        best_cost = costo_corrente          # Θ(1)
                else:
                    # min cardinalita'; a parita' di cardinalita', max peso
                    if size < best_size or \
                       (size == best_size and
                        costo_corrente > best_cost):
                        best_set  = set(S_corrente)         # Θ(n)
                        best_size = size                    # Θ(1)
                        best_cost = costo_corrente          # Θ(1)
            return                                          # Θ(1)
        v = nodi[idx]                                       # Θ(1)         (O)
        backtrack(idx + 1, S_corrente, costo_corrente)      # T(n-idx-1)   (P)
        S_corrente.add(v)                                   # Θ(1)         (Q)
        backtrack(idx + 1, S_corrente,                      # T(n-idx-1)   (R)
                  costo_corrente + dictPesiNodi[v])         # Θ(1)
        S_corrente.remove(v)                                # Θ(1)         (S)

    backtrack(0, set(), 0)                                  # O(2^n·m)     (T)
    if best_set is not None:                                # Θ(1)         (U)
        for v in best_set:                                  # Θ(n)
            nodiCopertura[v] = True                         # Θ(1)
    return nodiCopertura                                    # Θ(1)

# Costo Computazionale: T(n,m) = O(2^n · m)

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1).
#      Questo e' fondamentale per mantenere il costo della verifica al caso base
#      limitato a O(m).
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Nel caso in cui si vogliano trascurare tutti gli archi aventi costo
#      inferiore al costoMin in input, si filtra il vettore degli archi
#      mantenendo solo quelli con costo >= costoMin.
# (E): Se il vettore degli archi rimanenti e' vuoto, l'algoritmo non prosegue
#      e si restituisce il dizionario dei nodi di copertura vuoto.
# (F): Converte l'HashSet in vettore per accesso posizionale Θ(1) tramite
#      indice. L'HashSet si usa per raccogliere i nodi senza duplicati, mentre
#      il vettore nodi[] e' il vettore utilizzato per il backtracking.
# (G): Copia difensiva dei pesi dei nodi per non alterare il dizionario
#      originale passato in input. Operazione extra rispetto alla letteratura.
# (H): best_set: variabile contenente il miglior vertex cover trovato.
#      Inizializzata a None: nessun vertex cover valido trovato ancora.
# (I): best_size: variabile contenente la cardinalita' del miglior vertex cover.
#      Inizializzata a +inf: qualsiasi soluzione valida sara' migliore.
# (J): best_cost: variabile contenente il peso totale del miglior vertex cover.
#      Inizializzata a -inf: qualsiasi peso reale sara' maggiore all'inizio.
#      Serve per lo spareggio: a parita' di cardinalita' si preferisce max peso.
# (K): CASO BASE: sono stati presi tutti gli n nodi. Si verifica ora se
#      S_corrente e' un vertex cover valido prima di aggiornare il best.
#      Nota: nella versione PESATA non esiste pruning anticipato — aggiungere
#      un nodo aumenta il peso ma non peggiora necessariamente la soluzione.
# (L): Verifica di validita': per ogni arco almeno uno dei due estremi u o v
#      deve essere in S_corrente. Il lookup sull'HashSet e' Θ(1).
#      Costo totale: Θ(m).
# (M): Se count == m tutti gli archi sono coperti: S_corrente e' un vertex cover
#      valido. Se soddisfa il criterio scelto meglio del best attuale, aggiorna
#      best_set, best_size e best_cost. set(S_corrente) crea una COPIA:
#      necessario perche' S_corrente verra' modificato dai livelli superiori.
# (N): Doppio criterio di aggiornamento controllato da IsMinWeight:
#      IsMinWeight=True  → minimizza peso; a parita' di peso, min cardinalita'.
#      IsMinWeight=False → minimizza cardinalita'; a parita', max peso.
# (O): Nodo corrente su cui prendere la decisione includi/escludi.
#      Accesso posizionale Θ(1) grazie alla conversione list() al passo (F).
# (P): RAMO 1 — ESCLUDI v: ricorre sul nodo successivo senza modificare
#      S_corrente e senza aumentare costo_corrente.
# (Q): Aggiunge v a S_corrente prima di ricorrere nel Ramo 2.
# (R): RAMO 2 — INCLUDI v: ricorre sul nodo successivo con v dentro S_corrente
#      e aggiunge dictPesiNodi[v] al costo corrente accumulato.
# (S): RIPRISTINO (backtrack): rimuove v da S_corrente prima di tornare
#      al chiamante. S_corrente e' CONDIVISO su tutta la ricorsione; senza
#      questo remove, il Ramo 1 del livello superiore erediterebbe le
#      modifiche fatte dal Ramo 2 del livello corrente → soluzioni errate.
# (T): Avvio del backtracking: idx=0 (primo nodo), S_corrente={} (vuoto),
#      costo_corrente=0. Esplora l'intero albero binario di profondita' n.
#      Ogni foglia costa Θ(m) per la verifica → T(n,m) = O(2^n · m).
#      Nota: rispetto agli ipergrafi non compare d (d=2 per grafi, costante).
# (U): Costruisce il dizionario di output nel formato standard del progetto:
#      imposta a True solo i nodi appartenenti al miglior vertex cover trovato.
#      Se best_set e' None (nessun vertex cover valido esiste) il dizionario
#      rimane tutto False.


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
u, k = "CDG", 3
cc_Graphs_Exact =  KCenter_Graphs_BruteForce(L_ScaliAerei,u,k)
cc_Graphs_Approx = KCenter_Graphs(L_ScaliAerei,u,k)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Scali Aerei:\n"
    "Selezione dei Centri in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Exact.items())
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k in cc_Graphs_Approx.items())
)


'Grafo Indiretto Connesso - Esempio Isole Tailandesi  ------------------------'
u, k = "Lipe", 5
cc_Graphs_Exact =  KCenter_Graphs_BruteForce(L_Tailandia,u,k)
cc_Graphs_Approx = KCenter_Graphs(L_Tailandia, u, k)
cc_Graphs_Approx_v2 = KCenter_Graphs_variant(L_Tailandia, nw_Tailandia, u, k)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Isole Tailandesi:\n"
    "Selezione dei Centri in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k, v in vc_Graphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato (Gonzalez):\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k, v in vc_Graphs_Approx.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Pesi Additivi sui Nodi:\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Pesato (Plesnik):\n"
    " - Centri Selezionati: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Approx.items() if v)
)