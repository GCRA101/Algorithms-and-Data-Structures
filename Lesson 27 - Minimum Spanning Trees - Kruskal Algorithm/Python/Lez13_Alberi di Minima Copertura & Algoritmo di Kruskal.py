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
  - Formulazione con E ordinato + v_CC  - O(mlogn+n^2)
  - Formulazione con E ordinato + fa_CC  - O(mlogn)
    
  dove E    : vettore degli Archi (Edges)
       v_CC : vettore delle Componenti Connesse
       fa_CC : foresta di alberi delle Componenti Connesse con Unione per Rango


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
import copy


# Classi di utilita' ----------------------------------------------------------

# Arco Pesato
# Definiamo ogni arco pesato del grafo come un oggetto avente 3 proprieta': il
# nodo di partenza u, il nodo di arrivo v e il costo/peso costo.
# La classe ArcoPesato definisce il criterio di ordinamento basato sui valori
# crescenti dell'attributo 'costo'.

class ArcoPesato:
    
    # Costruttore
    def __init__(self, u, v, costo):
        self.u = u
        self.v = v
        self.costo = costo
    
    # Definizione criterio di ordinanemto per strutture dati ordinabili
    # Metodo equivalente a compareTo(...)
    def __lt__(self, altro):
        if self.costo != altro.costo:
            return self.costo < altro.costo
    def __le__(self, altro):
            return self.costo <= altro.costo
        
    # Definizione criterio di uguaglianza per ricerca in strutture dati
    # Metodo equivalente a equals(...)
    def __eq__(self, altro):
        return (self.u == altro.u and self.v == altro.v and
                self.costo == altro.costo)
    
    # Conversione istanza di classe in stringa
    # Metodo equivalente a ToString()
    def __str__(self):
        return f"{self.u}-{self.v} ({self.costo})"


# Lista Linkata
# Definiamo la struttura dati di Lista Linkata (LinkedList) che non e' nativa
# in Python. Questa struttura dati ci consentira' di eseguire l'operazione
# di cancellazione del valore minimo in tempo costante Θ(1) anziche' O(n) se
# utilizzassimo un vettore.

class Nodo:
    
    # Costruttore
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class ListaConcatenata:
    
    # Costruttore
    def __init__(self, valore):                               # T(n) 
        self.head = Nodo(valore)                              # Θ(1) 
        self.head.next = None                                 # Θ(1) 
    # T(n) = Θ(1) 

    # Append
    def append(self, valore):                                 # T(n)
        nuovoNodo = Nodo(valore)                              # Θ(1) 
        if self.head is None:                                 # Θ(1) 
            self.head = nuovoNodo                             # Θ(1) 
            return                                            # Θ(1) 
        current = self.head                                   # Θ(1) 
        while current.next != None:                           # Θ(n)  
            current = current.next                            # Θ(1) 
        current.next = nuovoNodo                              # Θ(1) 
    # T(n) = Θ(n) - CASO PEGGIORE/MIGLIORE (##)
    # (##): Qualunque sia il numero di elementi contenuti nella lista linkata,
    # l'algoritmo li scorrera' tutti fino all'ultimo.
    
    # Prepend
    def prepend(self, valore):                                # T(n)
        nuovoNodo = Nodo(valore)                              # Θ(1) 
        nuovoNodo.next = self.head                            # Θ(1) 
        self.head = nuovoNodo                                 # Θ(1)
    # T(n) = Θ(1) - CASO PEGGIORE/MIGLIORE (##)
    # (##): Qualunque sia il numero di elementi contenuti nella lista linkata,
    # l'algoritmo eseguira' sempre la stessa operazione.
        
    # Insert
    def insert(self, valore, nodoPrecedente):                 # T(n)
        if nodoPrecedente is not None:                        # Θ(1) 
            nuovoNodo = Nodo(valore)                          # Θ(1) 
            nuovoNodo.next = nodoPrecedente.next              # Θ(1) 
            nodoPrecedente.next = nuovoNodo                   # Θ(1)
    # T(n) = Θ(1) - CASO PEGGIORE/MIGLIORE (##)
    # (##): Qualunque sia il numero di elementi contenuti nella lista linkata,
    # l'algoritmo eseguira' sempre la stessa operazione.
        
    # Remove
    def remove(self, valore):                                 # T(n)
        if self.head is None:                                 # Θ(1) 
            return                                            # Θ(1) 
        if self.head.valore == valore:                        # Θ(1) 
            self.head = self.head.next                        # Θ(1) 
            return                                            # Θ(1) 
        current = self.head                                   # Θ(1) 
        while current.next is not None:                       # Ω(1) / O(n) 
            if current.next.data != valore:                   # Θ(1) 
                current = current.next                        # Θ(1) 
            else:                                             # Θ(1) 
                break                                         # Θ(1) 
        if current.next is not None:                          # Θ(1) 
            current.next = current.next.next                  # Θ(1)
    # T(n) = O(n) - CASO PEGGIORE 
    #        Ω(1) - CASO MIGLIORE (##)
    # (##): Se l'elemento da rimuovere e' il primo della lista, T(n)=Ω(1), 
    #       mentre se l'elemento e' l'ultimo o e' addirittura non presente 
    #       nella lista, T(n)=O(n)
    
    # Length
    def __len__(self):                                        # T(n)
        if self.head is None:                                 # Θ(1) 
            return 0                                          # Θ(1) 
        current = self.head                                   # Θ(1) 
        i = 1                                                 # Θ(1) 
        while current.next != None:                           # n*Θ(1)+Θ(1) 
            current = current.next                            # Θ(1) 
            i = i + 1                                         # Θ(1) 
        return i                                              # Θ(1) 
    # T(n) = Θ(n) - CASO MIGLIORE/PEGGIORE 
            


# Metodi di Utilita -----------------------------------------------------------


# Algoritmo di Ordinamento MERGESORT

def merge(A, i_primo, i_medio, i_ultimo):                     # S(n)
    i = i_primo                                               # Θ(1) 
    j = i_medio + 1                                           # Θ(1) 
    k = 0                                                     # Θ(1) 
    B = [None]*(i_ultimo-i_primo+1)                           # Θ(n) 
    while i<=i_medio and j<=i_ultimo :                        # Ω(n/2) / O(n)
        if A[i] <= A[j]:                                      # Θ(1) 
            B[k] = A[i]                                       # Θ(1) 
            i = i + 1                                         # Θ(1) 
        else:                                                 # Θ(1) 
            B[k] = A[j]                                       # Θ(1) 
            j = j + 1                                         # Θ(1) 
        k = k + 1                                             # Θ(1) 
    while i<=i_medio:                                         # O(n/2) / Ω(1)
        B[k] = A[i]                                           # Θ(1) 
        i = i + 1                                             # Θ(1) 
        k = k + 1                                             # Θ(1) 
    while j<= i_ultimo:                                       # O(n/2) / Ω(1)
        B[k] = A[j]                                           # Θ(1) 
        j = j + 1                                             # Θ(1) 
        k = k + 1                                             # Θ(1) 
    k = 0                                                     # Θ(1) 
    for i in range(i_primo, i_ultimo+1):                      # O(n)
        A[i] = B[k]                                           # Θ(1) 
        k = k + 1                                             # Θ(1)
    return
        
# Costo Computazionale: S(n) = Θ(n) - CASO PEGGIORE/MIGLIORE


def mergeSort(A, i_primo, i_ultimo):                          # T(n)
    if i_primo < i_ultimo:                                    # Θ(1) 
        i_medio = (i_primo + i_ultimo)//2                     # Θ(1) 
        mergeSort(A, i_primo, i_medio)                        # T(n/2)
        mergeSort(A, i_medio + 1, i_ultimo)                   # T(n/2)
        merge(A, i_primo, i_medio, i_ultimo)                  # Θ(n)
    return
        
# Equazione di Ricorrenza: T(n) = 2T(n/2) + Θ(n)
#                          T(1) = Θ(1)
# 
# Costo Computazionale: T(n) = Θ(nlogn)
            

# DFS con LISTE di ADIACENZA
def DFS_la(u,G):                                            # T(n)
    def DFSricors(x,G,visitati):                            # S(m)
        visitati[x]=True                                    # Θ(1)
        for (y,w) in G[x]:                                  # k*Θ(1)+Θ(1)
            if visitati[y]==False:                          # Θ(1)
                DFSricors(y,G,visitati)                     # S(v)
    visitati={v: False for v in G}                          # Θ(n)
    DFSricors(u, G, visitati)                               # S(m)
    return visitati                                         # Θ(1)
# Costo Computazionale: O(n+m) - CASO PEGGIORE
#                       Ω(n)   - CASO MIGLIORE        


# Conversione LISTA di ARCHI a LISTA di ADIACENZA
def convertEToG(E):                                         # T(n,m)
    nodi = set()                                            # Θ(1)        (A)
    for e in E:                                             # m*Θ(1)+Θ(1)
        if e.u not in nodi:                                 # Θ(1)        (B)
            nodi.add(e.u)                                   # Θ(1)
        if e.v not in nodi:                                 # Θ(1)        (B)
            nodi.add(e.v)                                   # Θ(1)
    G = {n: [] for n in nodi}                               # Θ(n)        (C)
    for e in E:                                             # m*Θ(1)+Θ(1)
        G[e.u].append((e.v, e.costo))                       # Θ(1)
        G[e.v].append((e.u, e.costo))                       # Θ(1)
    return G                                                # Θ(1)

# Costo Computazionale: T(n,m) = Θ(m)+Θ(n)+Θ(m)+Θ(1) = Θ(n+m)

# Commenti
# (A): La struttura dati volta a contenere la lista dei nodi estratta da E
#      viene scelta some HashSet (HashTable) per garantire che il costo
#      computazionale della ricerca sia Θ(1). Se nodi, infatti, fosse un
#      Le operazioni di ricerca di e[0] e e[1] (vedi (B)) avrebbero costo O(n)
#      anziche' Θ(1) e cio' porterebbe l'intero algoritmo ad avere costo O(n*m)
#      anziche' O(n+m)....
# (B): L'operazione di ricerca in una struttura dati HashSet ha costo Θ(1).
# (C): Definire la lista di Adiacenza come un dizionario (Hash Table) consente
#      di effetturare la ricerca di una sua chiave, e la conseguente aggiunta
#      di un valore ad essa, di costo unitario # Θ(1).


# Conntrollo CREAZIONE di CICLI
def isCycle(E,u,v):                                         # T(n,m)
    if len(E) == 0:                                         # Θ(1)
        return False                                        # Θ(1)
    G = convertEToG(E)                                      # Θ(n+m)      (A)
    if not (u in G.keys() and v in G.keys()):               # Θ(1)        (B)
        return False                                        # Θ(1)  
    visitati = DFS_la(u,G)                                  # O(n+m)      (C)
    if visitati[v] == True:                                 # Θ(1)        (D)
        return True                                         # Θ(1)
    else:                                                   # Θ(1)
        return False                                        # Θ(1)

# Costo Computazionale: T(n,m) = Θ(n+m)+O(n+m)+Θ(1)+Θ(1) = Θ(n+m)

# Commenti
# (A): Convertire la Lista degli Archi E in Lista di Adiacenza G consente di
#      esegurire la DFS con costo O(n+m) invece di O(n*m) - vedi (C)
# (B): Dato che G, lista di adiacenza, e' implementato come dizionario / hash
#      table, la ricerca e il confronto con una sua chiave ha costo Θ(1) in
#      quanto sfrutta la proprieta' di hash.
#      Dato che E (e quindi G) non e' detto che contenga ne' u ne' v, bisogna
#      prima controllare che u e v siano nella lista delle chiavi di G.
# (D): Se il nodo v e' contenuto nel vettore visitati vuol dire che e' gia'
#      stato visitato e l'arco {u,v} che vogliamo inserire creerebbe un ciclo.
#      Dato che visitati e' un Hash Table, il costo della ricerca e' Θ(1).
#      Se visitati fosse un vettore, il costo della ricerca sarebbe O(n) ma 
#      l'impatto sul costo complessivo dell'algoritmo sarebbe il medesimo.



# ======================== ALGORITMO di KRUSKAL ===============================


# ALGORITMO di KRUSKAL - v01 - Vettore Archi Disordinato
# ----------------------------------------------------------------------------
''' 
Per eseguire il controllo della presenza di cicli nell'albero minimo di
copertura SOL, e' necessario eseguire una DFS (Visita in Profondita').
La DFS puo' essere eseguita sulla Lista di Adiacenza G o sulla lista degli
Archi E. Per il primo caso, il costo computazionale e' il classico O(n+m),
mentre per il secondo e' O(n*m) in quanto per ogni nodo bisogna scorrere tutti
gli archi per trovare quelli ad esso adiacenti.
Usando la DFS su E, quindi, il costo computazionale complessivo di Kruskal
diviene m*O(n*m)=O(n*m^2).
Per ottenere O(m^2) e' quindi necessario convertire la Lista degli Archi E in
Lista di Adiacenza G con costo O(n+m) e poi eseguire la DFS su G con costo,
ancora, O(n+m). In tal modo il T(n,m) complessivo di Kruskal resta m*O(n+m) = 
O(m^2).'
'''

def MinimumSpanningTree_Kruskal_v01(E,u):                   # T(n,m)
    sol = []                                                # Θ(1)         (A)
    E_disordinato = copy.deepcopy(E)                        # Θ(m)         (B)
    while len(E_disordinato) != 0:                          # m*Θ(1)+Θ(1)
        costo_min = math.inf                                # Θ(1)
        e_min = None                                        # Θ(1)
        for e in E_disordinato:                             # m*O(1)+Θ(1)  (C)
            if e.costo < costo_min:                         # Θ(1)
                costo_min = e.costo                         # Θ(1)
                e_min = e                                   # Θ(1)
        E_disordinato.remove(e_min)                         # O(m)         (D)
        if not isCycle(sol,e_min.u,e_min.v):                # Θ(k+s)       (E)
            sol.append(e_min)                               # Θ(1)
    return sol                                              # Θ(1)

# Costo Computazionale: T(n,m) = m*[Θ(1)+Θ(m)+O(m)+O(m)+O(n)+Θ(1)] = O(m^2)

# Commenti
# (A): sol, ovvero la lista degli archi dell'albero di minima copertura di
#      Kruskal viene definaita come una lista. In tal modo, il costo di
#      inizializzazione resta Θ(1) anziche' Θ(n) (vettore).
# (B): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (C): A ogni iterazione, il numero di archi contenuti in E si riduce di un'
#      unita'. Cosi' che se e' vero che il ciclo while si ripete m volte, il
#      ciclo for al suo interno si ripete m-i volte.
#      Quindi Sommatoria(i=1->m)[m-i] = (m^2)/2 + m/2 = m^2 (serie numeriche)
# (D): Rimuovere un elemento da un vettore comporta la sua ricerca all'interno
#      del vettore (O(m)), la sua eliminazione (Θ(1)) e lo scorrimento degli
#      elementi per chiudere il vuoto lasciato (O(m)). Questa operazione,
#      ripetuta m volte dal ciclo while esterno corrisponde a O(m^2) (vedi
#      serie numeriche)
# (E): Il controllo dell'esistenza di cicli ha costo (Θ(k+s)) dove k = numero
#      nodi contenuti in sol e s = numero archi contenuti in sol. Dato che 
#      k<=n e s<=m, si potrebbe dire che Θ(k+s) = O(n+m) ma...si nota che sol,
#      proprio perche' albero minimo di copertura, puo' avere solo al piu' n
#      archi (dove n = numero dei nodi). Quindi Θ(k+s) = O(n).



# ALGORITMO di KRUSKAL - v02 - Vettore Archi Ordinato
# ----------------------------------------------------------------------------

def MinimumSpanningTree_Kruskal_v02a(E,u):                  # T(n,m)
    sol = []                                                # Θ(1)         (A)
    E_ordinato = copy.deepcopy(E)                           # Θ(m)         (B) 
    mergeSort(E_ordinato, 0, len(E_ordinato) - 1)           # Θ(mlogn)     (C)
    i = 0                                                   # Θ(1) 
    while i<len(E_ordinato):                                # m*Θ(1)+Θ(1)  (D)
        e_min = E_ordinato[i]                               # Θ(1)         (E)
        if not isCycle(sol,e_min.u,e_min.v):                # Θ(k+s)       (F)
            sol.append(e_min)                               # Θ(1)
        i = i + 1                                           # Θ(1)         (G)
    return sol                                              # Θ(1)

# Costo Computazionale: T(n,m) = Θ(m)+Θ(mlogn)+m*[O(n)+Θ(1)] = O(n*m)

# Commenti
# (A): sol, ovvero la lista degli archi dell'albero di minima copertura di
#      Kruskal viene definaita come una lista. In tal modo, il costo di
#      inizializzazione resta Θ(1) anziche' Θ(n) (vettore).
# (B): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (C): Il vettore degli archi viene ordinato usando un algoritmo ottimale di 
#      ordinamento basato sui confronti (MERGESORT).
# (D): Anziche' eliminare step-by-step tutti gli archi contenuti in E, si
#      utilizza un contatore indice per estrarre (senza cancellare) ciascun
#      arco contenuto in E. Volendo mantenere E come vettore (anziche' come
#      lista) questo e' l'unico modo per eseguire l'algoritmo senza dover
#      eliminare ciascuna volta l'elemento che si estrae e che, per i vettori,
#      ha cost O(n). Se si vuole eseguire l'algoritmo eliminando gli archi via
#      a via da E fino a svuotarlo (condizione di termine del ciclo), E deve
#      essere convertito in una lista linkata - Vedi v02b.
# (E): Dato che il vettore E e' stato ordinato, l'elemento all'indice i, mano
#      a mano crescente di un'unita' a ogni ciclo, coincide sempre con il
#      valore minimo seguente.
# (F): Il controllo dell'esistenza di cicli ha costo (Θ(k+s)) dove k = numero
#      nodi contenuti in sol e s = numero archi contenuti in sol. Dato che 
#      k<=n e s<=m, si potrebbe dire che Θ(k+s) = O(n+m) ma...si nota che sol,
#      proprio perche' albero minimo di copertura, puo' avere solo al piu' n
#      archi (dove n = numero dei nodi). Quindi Θ(k+s) = O(n).
# (G): Dato che scorriamo il vettore degli archi tramite indice incrementale i,
#      a ogni ciclo dobbiamo ricordarci di aumentare i di un'unita'.


def MinimumSpanningTree_Kruskal_v02b(E,u):                  # T(n,m)
    sol = []                                                # Θ(1)         (A)
    E_ordinato = copy.deepcopy(E)                           # Θ(m) 
    mergeSort(E_ordinato, 0, len(E_ordinato) - 1)           # Θ(mlogn)     (B)
    E_list = ListaConcatenata(E_ordinato[0])                # Θ(1)         (C)
    for i in range(1,len(E_ordinato)):                      # (m-1)*Θ(1)
        E_list.append(E_ordinato[i])                        # Θ(1) 
    while E_list.head!=None:                                # m*Θ(1)+Θ(1)  (D)
        e_min = E_list.head.valore                          # Θ(1)         (E)
        E_list.remove(e_min)                                # Θ(1)         (F)
        if not isCycle(sol,e_min.u,e_min.v):                # Θ(k+s)       (G)
            sol.append(e_min)                               # Θ(1)
    return sol                                              # Θ(1)

# Costo Computazionale: T(n,m) = Θ(m)+Θ(mlogn)+Θ(m)+m*[O(n)+Θ(1)] = O(n*m)

# Commenti
# (A): sol, ovvero la lista degli archi dell'albero di minima copertura di
#      Kruskal viene definaita come una lista. In tal modo, il costo di
#      inizializzazione resta Θ(1) anziche' Θ(n) (vettore).
# (B): Il vettore degli archi viene ordinato usando un algoritmo ottimale di 
#      ordinamento basato sui confronti (MERGESORT).
# (C): Per poter garantire che l'eliminazione del primo elemento di E sia di
#      costo unitario Θ(1), E dev'essere trasformato da un vettore a una lista
#      linkata. Eliminare il primo elemento di un vettore ha infatti costo Θ(n)
#      dato dal costo di eliminazione (Θ(1)) + il costo di slittamento di tutti
#      gli altri elementi del vettore (Θ(n-1)).
#      Se si vuole mantenere E come vettore, bisogna allora usare un contatore
#      per scorrere a mano a mano tutti i suoi elementi - Vedi v02a.
# (D): Si ripete il ciclo fino a che tutti gli archi contenuti nella lista
#      linkata E_list sono stati eliminati - ovvero E_list diviene vuota.
#      Invece di controllare ogni volta la lunghezza della lista, che avrebbe
#      costo O(n) - while len(E_list)!=0: - meglio semplicemente controllare
#      se la testa della lista e' ancora non nulla - while E_list.head != None.
# (E): L'arco di costo minimo e' sempre in testa alla lista in quanto ordinata.
# (F): Ogni volta che si estrae l'arco di costo minimo, lo si elimina dalla
#      lista. Dato che si tratta di una lista linkata e l'elemento e' sempre
#      quello in testa, il costo della sua eliminazione e' sempre costante e
#      unitario.
# (G): Il controllo dell'esistenza di cicli ha costo (Θ(k+s)) dove k = numero
#      nodi contenuti in sol e s = numero archi contenuti in sol. Dato che 
#      k<=n e s<=m, si potrebbe dire che Θ(k+s) = O(n+m) ma...si nota che sol,
#      proprio perche' albero minimo di copertura, puo' avere solo al piu' n
#      archi (dove n = numero dei nodi). Quindi Θ(k+s) = O(n).



# ALGORITMO di KRUSKAL - v03 - Vettore Archi Ordinato + Vettore Comp. Connesse
# ----------------------------------------------------------------------------
def MinimumSpanningTree_Kruskal_v03(E,u):                   # T(n,m)
    sol = []                                                # Θ(1)         (A)
    E_ordinato = copy.deepcopy(E)                           # Θ(m)         (B) 
    mergeSort(E_ordinato, 0, len(E_ordinato)-1)             # Θ(mlogn)     (C)
    nodiSet = set()                                         # Θ(1)         (D)
    for e in E_ordinato:                                    # m*Θ(1)+Θ(1)  (E)
        if e.u not in nodiSet:                              # Θ(1)         
            nodiSet.add(e.u)                                # Θ(1)
        if e.v not in nodiSet:                              # Θ(1)
            nodiSet.add(e.v)                                # Θ(1)
    nodi = [None]*len(nodiSet)                              # Θ(n)         (F)
    i = 0                                                   # Θ(1)
    for nodo in nodiSet:                                    # n*Θ(1)+Θ(1)
        nodi[i] = nodo                                      # Θ(1)
        i = i + 1                                           # Θ(1)
    E_list = ListaConcatenata(E_ordinato[0])                # Θ(1)         (G)
    for i in range(1, len(E_ordinato)):                     # (m-1)*Θ(1)
        E_list.append(E_ordinato[i])                        # Θ(1) 
    cc = {nodo:-1 for nodo in nodi}                         # Θ(n)         (H)
    for i in range(0,len(nodi)):                            # n*Θ(1)+Θ(1)  (I)
        cc[nodi[i]]=i                                       # Θ(1) 
    while E_list.head!=None:                                # m*Θ(1)+Θ(1)  (J)                       
        e_min = E_list.head.valore                          # Θ(1)         (K)                   
        E_list.remove(e_min)                                # Θ(1)         (L)                          
        if cc[e_min.u]!=cc[e_min.v]:                        # Θ(1)         (M) 
            sol.append(e_min)                               # Θ(1)         (N) 
            a = min(cc[e_min.u], cc[e_min.v])               # Θ(1)         (O) 
            b = max(cc[e_min.u], cc[e_min.v])               # Θ(1)
            for i in range(0,len(nodi)):                    # n*Θ(1)+Θ(1)  (P)
                if cc[nodi[i]] == b:                        # Θ(1) 
                    cc[nodi[i]] = a                         # Θ(1) 
    return sol
    
# Costo Computazionale: T(n,m) = Θ(m)+Θ(mlogn)+Θ(m)+Θ(n)+Θ(n)+Θ(m)+Θ(n)+Θ(n)+
#                                +m*[Θ(n)+Θ(1)] = Θ(mlogn + n^2)
# IMPORTANTE!
# Il cicle for (P), all'interno del while (J), ha costo Θ(n) ma non viene 
# eseguito tutte le m volte in cui viene ripetuto il ciclo while!
# Infatti il ciclo for e' all'interno di un if (M) che controlla se i nodi dell
# arco appartengono alla stessa componente! Per ottenere un'unica componente
# che copre tutto il grafo, bastano n-1 fusioni. Cio' significa che la
# condizione dell'if (M) sara' soddisfatta solo n-1 volte. Le restanti
# m-(n-1) volte non sara' soddisfatta e, quindi, il codice in esso contenuto
# non verra' eseguito. Cio' significa che il costo del ciclo while e' come
# segue:
# [m-(n-1)]*Θ(1) + (n-1)*Θ(n) = Θ(m) - Θ(n) + Θ(1) + Θ(n^2) - Θ(n) = Θ(n^2)

# Commenti
# (A): sol, ovvero la lista degli archi dell'albero di minima copertura di
#      Kruskal viene definita come una lista. In tal modo, il costo di
#      inizializzazione resta Θ(1) anziche' Θ(n) (vettore).
# (B): Il Vettore degli Archi passato in input viene ricopiato in un nuovo
#      vettore cosi che tutte le operazioni eseguite su di esso non vadano a
#      modificare l'originale.
# (C): Il Vettore degli Archi viene ordinato per ordine di costo crescente
#      utilizzando l'algoritmo MergeSort - algoritmo ottimale di ordinamento
#      basato sui confronti.
# (D): L'estrazione dei nodi dal Vettore degli Archi richiederebbe costo Θ(n*m)
#      se utilizzassimo un vettore per immagazzinare i nodi. Infatti, si
#      scorrono tutti gli archi estraend i nodi u e v corrispondenti e li si 
#      ricercano scorrendo ogni volta l'intero vettore dei nodi.
#      Usando un HashSet per immagazzinare i nodi, invece, il costo della
#      ricerca diviene Θ(1). Quindi l'intera costruzione del vettore dei nodi
#      costa semplicemente Θ(m).
# (E): Si estraggono i nodi dal Vettore degli Archi e li si immagazzinano nel
#      Vettore dei Nodi.
# (F): A questo punto e' possibile ri-costruire il vettore dei nodi copiandoli
#      direttamente dall'HashSet creato con costo complessivo Θ(n)
# (G): Se vogliamo eliminare dal Vettore degli Archi l'arco di costo minimo ad
#      ogni iterazione, ad ogni iterazione il costo di tale eliminazione sara'
#      Θ(n). Troppo!
#      O scorriamo il vettore con un indice (vedi v02a sopra) o convertiamo il
#      vettore in una lista linkata per la quale l'eliminazione del primo
#      elemento (ovver arco di costo minimo) ha costo unitario Θ(1).
# (H): Dato che e' necessario eseguire ricerche di nodi all'interno del Vettore
#      delle Componenti Connesse cc...se vogliamo evitare che ciascuna di esse
#      comporti costo O(n) dobbiamo rappresentare la struttura dati come una
#      Hash Table...per cui il costo della ricerca diviene unitario Θ(1).
# (I): Si scorrono tutti i nodi (ovvero le chiavi della HashTable cc) e si 
#      assegna un numero intero crescente a ciascuno all'interno di cc.
#      Ovvero, ad ogni nodo si associa una componente connessa di indice intero
#      e che corrisponde al nodo stesso.
# (J): Si ripete il ciclo fino a che tutti gli archi contenuti nella lista
#      linkata E_list sono stati eliminati - ovvero E_list diviene vuota.
#      Invece di controllare ogni volta la lunghezza della lista, che avrebbe
#      costo O(n) - while len(E_list)!=0: - meglio semplicemente controllare
#      se la testa della lista e' ancora non nulla - while E_list.head != None.
# (K): Si estra la testa della lista linkata che corrisponde all'arco di costo
#      minimo
# (L): Si rimuove la testa della lista linkata. L'operazione e' di costo Θ(1).
# (M): Se la componente connessa dei due nodi u e v dell'arco e' la stessa,vuol
#      dire che i due nodi sono gia' connessi e, quindi, aggiungere l'arco all'
#      albero di minima copertura genererebbe un ciclo, il che' non e'
#      consentito. Altrimenti prosegui come segue...
# (N): Aggiungi l'arco minimo all'albero minimo di copertura
# (O): Ricava la componente di indice minimo (a) e quella di indice massimo (b)
#      L'algoritmo di Kruskal prevede, come convenzione, che quando due
#      componenti a e b disconnesse vengono connesse, la nuova componente
#      risultante sara' a dove a<b.
# (P): Scorri l'intera Hash Table delle componenti connesse (dimensione n =
#      numero di nodi) e per ogni nodo aggiorna la componente corrispondente.



# # ALGORITMO di KRUSKAL - v04 - Vettore Archi Ordinato + Foresta di Alberi
#                                per Componenti Connesse + Unione per Rango
# # ---------------------------------------------------------------------------

def find(cc,s):                                             # S(n)
    nodo = s                                                # Θ(1)
    while cc[nodo][0] != nodo:                              # Ω(1)/O(logn) (A)
        nodo = cc[nodo][0]                                  # Θ(1)         (B)
    return nodo                                             # Θ(1)

# Costo Computazionale
# S(n) = O(logn) CASO PEGGIORE
#        Ω(1)    CASO MIGLIORE

# Commenti:
# (A): Dato che cc e' un vettore dei padri (implementato qui come hash table)
#      per ricavare la radice del nodo s basta spostarsi di padre in padre
#      fino a trovare il nodo che ha come padre se' medesimo.
# (B): Dato che il valore corrispondente alla chiave nodo e' una coppia
#      [u,size], il nodo e' l'elemento in indice 0 - ovvero cc[nodo][0]

def union(cc, r1, r2):                                      # R(n)
    newSize = cc[r1][1] + cc[r2][1]                         # Θ(1)         (A)
    if cc[r1][1] <= cc[r2][1]:                              # Θ(1)         (B)
        cc[r1][0] = r2                                      # Θ(1)
        cc[r1][1] = newSize                                 # Θ(1)
    else:                                                   # Θ(1)
        cc[r2][0] = r1                                      # Θ(1)
        cc[r2][1] = newSize                                 # Θ(1)
        
# Costo Computazionale
# R(n) = Θ(1)

# Commenti:
# (A): SOLO nel caso delle RADICI, il campo size (i.e. cc[nodo][1]) contiene il
#      numero dei nodi contenuti nella componente facente capo a quella radice.
#      Dato che le due componenti devono essere unite, la dimensione della
#      risultante sara' data dalla somma delle due.
# (B): In base a quale radice corrisponde all'albero componente piu' piccolo,
#      si colleghera' la radice dell'albero piu' piccolo alla radice dell'
#      albero piu' grande.

    
def MinimumSpanningTree_Kruskal_v04(E,u):                   # T(n,m)
    E_ordinato = copy.deepcopy(E)                           # Θ(n)         (A)
    mergeSort(E_ordinato, 0, len(E_ordinato)-1)             # Θ(mlogn)     (B)
    nodiSet = set()                                         # Θ(1)         (C)
    for e in E_ordinato:                                    # m*Θ(1)+Θ(1)
        if not e.u in nodiSet:                              # Θ(1)
            nodiSet.add(e.u)                                # Θ(1)
        if not e.v in nodiSet:                              # Θ(1)
            nodiSet.add(e.v)                                # Θ(1)
    nodi = [None]*len(nodiSet)                              # 2*Θ(n)       (D)
    i = 0                                                   # Θ(1)
    for nodo in nodiSet:                                    # Θ(n)+Θ(1)
        nodi[i] = nodo                                      # Θ(1)
        i = i + 1                                           # Θ(1)
    sol = [None]*(len(nodi)-1)                              # Θ(n)         (E)
    E_list = ListaConcatenata(E_ordinato[0])                # Θ(1)         (F)
    for i in range(1, len(E_ordinato)):                     # Θ(m-1)+Θ(1)
        E_list.append(E_ordinato[i])                        # Θ(1)
    cc = {nodo: [nodo,1] for nodo in nodi}                  # Θ(n)         (G)
    i = 0                                                   # Θ(1)
    while E_list.head!=None:                                # m*Θ(1)+Θ(1)  (H)
        e_min = E_list.head.valore                          # Θ(1)         (I)
        E_list.remove(e_min)                                # Θ(1)         (J)
        radice1 = find(cc,e_min.u)                          # Ω(1)/O(logn) (K)                       
        radice2 = find(cc,e_min.v)                          # Ω(1)/O(logn) (K)
        if radice1 != radice2:                              # Θ(1)         (L)
            sol[i]=e_min                                    # Θ(1)
            union(cc,radice1, radice2)                      # Θ(1)      
            i = i + 1                                       # Θ(1)     
    return sol                                              # Θ(1)

# Costo Computazionale
# T(n,m) = Θ(n)+Θ(mlogn)+Θ(1)+Θ(m)+Θ(n)+Θ(n)+Θ(n)+Θ(m)+Θ(n)+m*O(logn) =
#        = O(mlogn)

# Commenti
# (A): Per evitare di modificare il vettore degli archi originale passato in
#      input, lo cloniamo in una copia ed operiamo direttamente su di essa.
# (B): Si ordinano tutti gli archi contenuti nel vettore degli archi per costo
#      crescente ed utilizzando un algoritmo ottimale di ordinamento basato
#      sui confronti: il MergeSort
# (C): L'estrazione di nodi al vettore degli archi richiederebbe costo Θ(n*m)
#      se volessimo direttamente immagazzinarli in un vettore.
#      Usando, invece, un HashSet, la ricerca e l'inserimento in esso di un
#      nodo sono entrambe operazioni di costo unitario Θ(1).
#      In tal modo il costo di estrazione dei nodi dal vettore degli archi ha
#      costo Θ(m).
# (D): Trasformiamo l'HashSet in un vettore contenente i nodi per tornare in
#      linea con la formulazione classica dell'algoritmo.
#      L'operazione di copiatura di tutti i nodi dall'HashSet al Vettore ha
#      ovviamente costo lineare Θ(n)
# (E): In questo caso, definiamo sol come vettore (non come lista).
#      Avendo il numero dei nodi del grafo, sappiamo che certamente il numero
#      di archi di un suo qualsiasi albero minimo di copertura sara' m=n-1.
# (F): Convertiamo il vettore ordinato contente gli archi in una lista
#      concatenata. Cio' consente di scorrere gli archi senza un indice
#      incrementale e consente di rimuovere l'arco di costo minimo con costo
#      unitario Θ(1).
# (G): Inizializzamo la struttura dati delle componenti connesse come hash
#      table e con lo stesso funzionamento del vettore dei padri di un albero.
#      A ciascun nodo viene associato se' stesso in quanto padre di se'
#      medesimo. Nella configurazione iniziale, infatti, si hanno tante
#      componenti quanto il numero dei nodi.
# (H): Si ripete il ciclo fino a che tutti gli archi contenuti nella lista
#      linkata E_list sono stati eliminati - ovvero E_list diviene vuota.
#      Invece di controllare ogni volta la lunghezza della lista, che avrebbe
#      costo O(n) - while len(E_list)!=0: - meglio semplicemente controllare
#      se la testa della lista e' ancora non nulla - while E_list.head != None
# (I): L'arco di costo minimo e' l'oggetto contenuto nel campo "valore" del
#      nodo corrispondente alla testa della lista concatenata.
# (J): La testa della lista concatenata viene rimossa a costo unitario.
# (K): Le radici corrispondenti alle componenti connesse a cui appartengono
#      i nodi u e v dell'arco e_min vengono estratte usando la funzione find
# (L): Se le radici coincidono vuol dire che i due nodi sono gia' connessi
#      e aggiungere l'arco e_min all'albero dei cammini minimi genererebbe
#      un ciclo e cio' non lo vogliamo....quindi non lo si considera.
#      Altrimenti, si aggiunge l'arco all'albero minimo di copertura e 
#      si esegue l'unione delle due componenti semplicemente imponendo che
#      il padre della radice dell'una coincida con la radice dell'altra.
#      Per garantire che gli alberi delle componenti connesse siano meno
#      profondi possibile (e quindi il costo di FIND sia O(logn) invece di O(n)
#      ) si colleghera' la radice dell'albero PIU' PICCOLO a quella dell'albero
#      PIU' GRANDE! Questo si ottiene assegnando ad ogni nodo del vettore dei
#      padri la coppia [u,size] dove u e' il nodo radice e size e' il numero
#      di nodi nell'insieme.

" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi due esempi
piu' complessi: uno ispirato alla progettazione della rete viaria dell'antico
impero romano e uno ispirato al film Matrix.

"""


# LISTE DI ADIACENZA ----------------------------------------------------------


'Grafo Indiretto Connesso - Esempio Numerico ---------------------------------' 
E_gc_Numeric = [
      ArcoPesato("A", "B", 2),
      ArcoPesato("A", "C", 4),
      ArcoPesato("A", "D", 7),
      ArcoPesato("A", "F", 5),
      ArcoPesato("B", "D", 6),
      ArcoPesato("B", "E", 3),
      ArcoPesato("B", "G", 8),
      ArcoPesato("C", "F", 6),
      ArcoPesato("D", "F", 1),
      ArcoPesato("D", "G", 6),
      ArcoPesato("E", "G", 7),
      ArcoPesato("F", "G", 6)
]


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
'''
Costo degli Archi -> Costo realizzazione connessione in migliaia di Sesterzi
''' 
E_gc_Roman = [
    ArcoPesato("Alexandria",         "Bisantium",          33),
    ArcoPesato("Alexandria",         "Carthago",           57),
    ArcoPesato("Alexandria",         "Corduba",            97),
    ArcoPesato("Alexandria",         "Massilia",           76),
    ArcoPesato("Alexandria",         "Ravenna",            64),
    ArcoPesato("Alexandria",         "Roma",               59),
    ArcoPesato("Alexandria",         "Tarraco",            84),
    ArcoPesato("Aquincum",           "Augusta Treverorum", 3080),
    ArcoPesato("Aquincum",           "Bisantium",          35),
    ArcoPesato("Aquincum",           "Colonia Agrippina",  3330),
    ArcoPesato("Aquincum",           "Mediolanum",         2100),
    ArcoPesato("Aquincum",           "Ravenna",            990),
    ArcoPesato("Aquincum",           "Vindobona",          220),
    ArcoPesato("Augusta Treverorum", "Colonia Agrippina",  230),
    ArcoPesato("Augusta Treverorum", "Eboracum",           20),
    ArcoPesato("Augusta Treverorum", "Londinium",          17),
    ArcoPesato("Augusta Treverorum", "Lugdunum",           900),
    ArcoPesato("Augusta Treverorum", "Lutetia",            400),
    ArcoPesato("Augusta Treverorum", "Mediolanum",         1680),
    ArcoPesato("Augusta Treverorum", "Vindobona",          2939),
    ArcoPesato("Burdigala",          "Corduba",            36),
    ArcoPesato("Burdigala",          "Eboracum",           33),
    ArcoPesato("Burdigala",          "Emerita Augusta",    1350),
    ArcoPesato("Burdigala",          "Londinium",          21),
    ArcoPesato("Burdigala",          "Lugdunum",           810),
    ArcoPesato("Burdigala",          "Lutetia",            500),
    ArcoPesato("Burdigala",          "Narbo",              300),
    ArcoPesato("Bisantium",          "Capua",              36),
    ArcoPesato("Bisantium",          "Corduba",            96),
    ArcoPesato("Bisantium",          "Narbo",              78),
    ArcoPesato("Bisantium",          "Ravenna",            33),
    ArcoPesato("Bisantium",          "Vindobona",          39),
    ArcoPesato("Capua",              "Carthago",           17),
    ArcoPesato("Capua",              "Carthago Nova",      30),
    ArcoPesato("Capua",              "Corduba",            60),
    ArcoPesato("Capua",              "Ravenna",            720),
    ArcoPesato("Capua",              "Roma",               190),
    ArcoPesato("Capua",              "Tarraco",            34),
    ArcoPesato("Carthago",           "Carthago Nova",      30),
    ArcoPesato("Carthago",           "Emerita Augusta",    44),
    ArcoPesato("Carthago",           "Massilia",           25),
    ArcoPesato("Carthago",           "Narbo",              28),
    ArcoPesato("Carthago",           "Roma",               18),
    ArcoPesato("Carthago",           "Tarraco",            27),
    ArcoPesato("Carthago Nova",      "Corduba",            500),
    ArcoPesato("Carthago Nova",      "Emerita Augusta",    860),
    ArcoPesato("Carthago Nova",      "Massilia",           15),
    ArcoPesato("Carthago Nova",      "Narbo",              11),
    ArcoPesato("Carthago Nova",      "Roma",               27),
    ArcoPesato("Carthago Nova",      "Tarraco",            230),
    ArcoPesato("Colonia Agrippina",  "Eboracum",           17),
    ArcoPesato("Colonia Agrippina",  "Londinium",          14),
    ArcoPesato("Colonia Agrippina",  "Lutetia",            320),
    ArcoPesato("Colonia Agrippina",  "Mediolanum",         1930),
    ArcoPesato("Colonia Agrippina",  "Vindobona",          1930),
    ArcoPesato("Corduba",            "Emerita Augusta",    250),
    ArcoPesato("Corduba",            "Massilia",           39),
    ArcoPesato("Corduba",            "Tarraco",            1930),
    ArcoPesato("Eboracum",           "Londinium",          320),
    ArcoPesato("Eboracum",           "Lutetia",            21),
    ArcoPesato("Eboracum",           "Narbo",              43),
    ArcoPesato("Eboracum",           "Tarraco",            63),
    ArcoPesato("Emerita Augusta",    "Londinium",          49),
    ArcoPesato("Emerita Augusta",    "Massilia",           60),
    ArcoPesato("Emerita Augusta",    "Roma",               78),
    ArcoPesato("Emerita Augusta",    "Tarraco",            30),
    ArcoPesato("Londinium",          "Lutetia",            11),
    ArcoPesato("Londinium",          "Tarraco",            57),
    ArcoPesato("Lugdunum",           "Lutetia",            460),
    ArcoPesato("Lugdunum",           "Massilia",           500),
    ArcoPesato("Lugdunum",           "Mediolanum",         1120),
    ArcoPesato("Lugdunum",           "Narbo",              540),
    ArcoPesato("Lugdunum",           "Vindobona",          2630),
    ArcoPesato("Lutetia",            "Narbo",              1252),
    ArcoPesato("Massilia",           "Mediolanum",         500),
    ArcoPesato("Massilia",           "Narbo",              150),
    ArcoPesato("Massilia",           "Roma",               20),
    ArcoPesato("Mediolanum",         "Ravenna",            220),
    ArcoPesato("Mediolanum",         "Roma",               1680),
    ArcoPesato("Mediolanum",         "Vindobona",          2100),
    ArcoPesato("Narbo",              "Tarraco",            230),
    ArcoPesato("Ravenna",            "Roma",               540),
    ArcoPesato("Ravenna",            "Vindobona",          860),
]


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
E_gc_Matrix = [
    # --- GREEN edges (weight 1-2, low risk) ---
    ArcoPesato("A", "B", 1), # Thomas Anderson's Apt ↔ Heart O' The City Hotel
    ArcoPesato("A", "G", 2), # Thomas Anderson's Apt ↔ Warehouse 17
    ArcoPesato("A", "J", 2), # Thomas Anderson's Apt ↔ St. Michael's Cathedral
    ArcoPesato("B", "F", 1), # Heart O'The City Hotel ↔ Chinatown Safe House
    ArcoPesato("B", "L", 1), # Heart O'The City Hotel ↔ Zion Access Broadcast Relay
    ArcoPesato("C", "I", 1), # Adams Street Subway ↔ Old Power Station ← East River
    ArcoPesato("E", "H", 2), # Abandoned Gov. Office ↔ Riverfront Dockyard
    ArcoPesato("G", "I", 2), # Warehouse 17 ↔ Old Power Station
    ArcoPesato("H", "I", 2), # Riverfront Dockyard ↔ Old Power Station ← East River
    ArcoPesato("K", "L", 1), # Telephone Extraction Hub ↔ Zion Access Broadcast Relay
    # --- ORANGE edges (weight 3-4, moderate risk) ---
    ArcoPesato("A", "F", 3), # Thomas Anderson's Apt ↔ Chinatown Safe House
    ArcoPesato("A", "K", 4), # Thomas Anderson's Apt ↔ Telephone Extraction Hub
    ArcoPesato("B", "G", 4), # Heart O'The City Hotel ↔ Warehouse 17
    ArcoPesato("B", "I", 3), # Heart O'The City Hotel ↔ Old Power Station
    ArcoPesato("B", "J", 3), # Heart O'The City Hotel ↔ St. Michael's Cathedral
    ArcoPesato("D", "F", 3), # Metacortex Building ↔ Chinatown Safe House
    ArcoPesato("E", "I", 3), # Abandoned Gov. Office ↔ Old Power Station
    ArcoPesato("E", "J", 4), # Abandoned Gov. Office ↔ St. Michael's Cathedral
    ArcoPesato("E", "K", 3), # Abandoned Gov. Office ↔ Telephone Extraction Hub
    ArcoPesato("F", "G", 3), # Chinatown Safe House ↔ Warehouse 17
    ArcoPesato("G", "H", 3), # Warehouse 17 ↔ Riverfront Dockyard
    ArcoPesato("H", "K", 4), # Riverfront Dockyard ↔ Telephone Extraction Hub
    ArcoPesato("I", "K", 3), # Old Power Station ↔ Telephone Extraction Hub
    ArcoPesato("J", "K", 3), # St.Michael'sCathedral ↔ Telephone Extraction Hub
    ArcoPesato("C", "F", 4), # Adams Street Subway ↔ Chinatown Safe House
    # --- RED edges (weight 5-7, high risk) ---
    ArcoPesato("A", "C", 5), # Thomas Anderson's Apt ↔ Adams Street Subway
    ArcoPesato("A", "D", 7), # Thomas Anderson's Apt ↔ Metacortex Building
    ArcoPesato("B", "C", 5), # Heart O'The City Hotel ↔ Adams Street Subway
    ArcoPesato("B", "E", 6), # Heart O'The City Hotel ↔ Abandoned Gov. Office
    ArcoPesato("B", "H", 5), # Heart O'The City Hotel ↔ Riverfront Dockyard
    ArcoPesato("B", "K", 5), # Heart O'The City Hotel ↔ Telephone Extraction Hub
    ArcoPesato("C", "D", 5), # Adams Street Subway ↔ Metacortex Building
    ArcoPesato("C", "E", 7), # Adams Street Subway ↔ Abandoned Gov. Office
    ArcoPesato("C", "J", 6), # Adams Street Subway ↔ St. Michael's Cathedral
    ArcoPesato("D", "I", 5), # Metacortex Building ↔ Old Power Station
    ArcoPesato("D", "J", 5), # Metacortex Building ↔ St. Michael's Cathedral
    ArcoPesato("D", "K", 5), # Metacortex Building ↔ Telephone Extraction Hub
    ArcoPesato("D", "L", 6), # Metacortex Building ↔ Zion Access Broadcast Relay
    ArcoPesato("F", "I", 6), # Chinatown Safe House ↔ Old Power Station
    ArcoPesato("H", "J", 7), # Riverfront Dockyard ↔ St. Michael's Cathedral
]
       


# ALGORITMO di KRUSKAL con LISTE di ARCHI ------------------------------------

'Grafo Indiretto Connesso - Esempio Numerico -----------------------------'
u = "A"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Numeric,u)
kruskal_v02a = MinimumSpanningTree_Kruskal_v02a(E_gc_Numeric,u)
kruskal_v02b = MinimumSpanningTree_Kruskal_v02b(E_gc_Numeric,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Numeric,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Numeric,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v01)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v01)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v01))+"\n"+
      " > Algoritmo di Kruskal con E Vettore Ordinato [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02a)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02a)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02a))+"\n"+
      " > Algoritmo di Kruskal con E Lista Linkata Ordinata [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02b)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02b)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02b))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v03)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v03)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v03))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + fa_CC [O(mlogn)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v04)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v04)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v04)))


'Grafo Indiretto Connesso - Esempio Roman Road Network  ----------------------'
u = "Roma"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Roman,u)
kruskal_v02a = MinimumSpanningTree_Kruskal_v02a(E_gc_Roman,u)
kruskal_v02b = MinimumSpanningTree_Kruskal_v02b(E_gc_Roman,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Roman,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Roman,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Roman Road Network: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v01)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v01)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v01))+"\n"+
      " > Algoritmo di Kruskal con E Vettore Ordinato [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02a)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02a)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02a))+"\n"+
      " > Algoritmo di Kruskal con E Lista Linkata Ordinata [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02b)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02b)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02b))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v03)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v03)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v03))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + fa_CC [O(mlogn)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v04)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v04)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v04)))


'Grafo Indiretto Connesso - Esempio Matrix  ----------------------------------'
u = "A"   
kruskal_v01 = MinimumSpanningTree_Kruskal_v01(E_gc_Matrix,u)
kruskal_v02a = MinimumSpanningTree_Kruskal_v02a(E_gc_Matrix,u)
kruskal_v02b = MinimumSpanningTree_Kruskal_v02b(E_gc_Matrix,u)
kruskal_v03 = MinimumSpanningTree_Kruskal_v03(E_gc_Matrix,u)
kruskal_v04 = MinimumSpanningTree_Kruskal_v04(E_gc_Matrix,u)

print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Matrix: "+"\n"+
      "Albero di Copertura Minimo in Grafo Pesato "+"\n"+
      " > Algoritmo di Kruskal con E Disordinato [O(m^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v01)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v01)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v01))+"\n"+
      " > Algoritmo di Kruskal con E Vettore Ordinato [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02a)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02a)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02a))+"\n"+
      " > Algoritmo di Kruskal con E Lista Linkata Ordinata [O(n*m)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v02b)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v02b)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v02b))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + v_CC [O(mlogn + n^2)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v03)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v03)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v03))+"\n"+
      " > Algoritmo di Kruskal con E Ordinato + fa_CC [O(mlogn)]: "+"\n"+
      "   - Archi Visitati: "+", ".join(str(arco) for arco in kruskal_v04)+"\n"+
      "   - Costi: "+", ".join(str(arco.costo) for arco in kruskal_v04)+"\n"+
      "   - Costo Min Tot: "+ str(sum(arco.costo for arco in kruskal_v04)))