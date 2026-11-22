# -*- coding: utf-8 -*-
"""
LEZIONE 14a - ALGORITMI di APPROSSIMAZIONE e COPERTURA TRAMITE NODI [GRAFI]

Gli Algoritmi di Approssimazione sono quella categoria di algoritmi creati per
risolvere problemi computazionalmente difficili e per i quali non esiste un
algoritmo che produca una soluzione esatta in tempi umanamente fattibili.
Gli Algoritmi di Approssimazione garantiscono che la soluzione da essi
raggiunta sia in grado di approssimare la soluzione esatta per un certo
rapporto/fattore di approssimazione.

Un classico esempio di Algoritmo di Approssimazione e' utilizzato per la
risoluzione del Problema di Copertura tramite Nodi (Vertex Cover).

Il Problema di Copertura tramite Nodi e' utilizzato per modellare numerosi
problemi computazionali reali (per esempio l'ottimizzazione di allocamento
delle risorse) e la forma che vediamo di seguito e' quella piu' semplice -
ovvero avente cardinalita' 2.
Il Problema viene modellato tramite un grafo in cui i nodi rappresentano le
risorse e gli archi le mansioni che le risorse possono eseguire (max 2).
La soluzione consiste nel trovare il sottoinsieme di nodi di cardinalita' 
minima che copre tutti gli archi del grafo (un nodo copre un arco se e' uno
dei suoi due estremi). 
Tale sottoinsieme di nodi rappresenta quindi l'insieme minimo di risorse che
puo' eseguire tutte le mansioni richieste.

Algoritmo per Copertura Tramite Nodi
  - Formulazione Greedy         - O(n+m)
  - Formulazione Approssimante  - O(n+m)

Formulazione Greedy
    - Soluzione Approssimata (non esatta)
    - Rapporto/Fattore di Approssimazione NON GARANTITO
    
Formulazione Approssimante
    - Soluzione Approssimata (non esatta)
    - Rapporto/Fattore di Approssimazione GARANTITO!
      
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



# ====================== ALGORITMO di VERTEX COVER ============================


# ALGORITMO di VERTEX COVER per GRAFI NON PESATI
# ----------------------------------------------------------------------------
''' 
L'algoritmo di Vertex Cover su Grafo non pesato scorre tutti gli archi uno ad 
uno e se entrambi i nodi dell'arco risultano ancora non coperti, l'algoritmo 
li copre entrambi e passa a considerare l'arco successivo.
Al contrario, se l'arco presenta anche solo un nodo gia' coperto,
l'algoritmo passa direttamente all'arco successivo senza coprire il nodo
restante.
'''

def VertexCover_Graphs(E):                                  # T(n,m)
    nodiSet = set()                                         # Θ(1)         (A)
    for e in E:                                             # m*Θ(1)+Θ(1)
        if e.u not in nodiSet:                              # Θ(1)         
            nodiSet.add(e.u)                                # Θ(1)
        if e.v not in nodiSet:                              # Θ(1)
            nodiSet.add(e.v)                                # Θ(1)    
    nodiCopertura = {nodo:False for nodo in nodiSet }       # Θ(n)         (B)
    archi = copy.deepcopy(E)                                # Θ(m)         (C)
    Archi_list = ListaConcatenata(archi[0])                 # Θ(1)         (D)
    for i in range(1,len(archi)):                           # (m-1)*O(1)
        Archi_list.append(archi[i])                         # Θ(1) 
    while Archi_list.head!=None:                            # m*O(1)+Θ(1)  (E)
        arco = Archi_list.head.valore                       # Θ(1)      
        Archi_list.remove(arco)                             # Θ(1)
        if nodiCopertura[arco.u]==False and \
        nodiCopertura[arco.v]==False:                       # Θ(1)         (F)
            nodiCopertura[arco.u] = True                    # Θ(1)         (G)
            nodiCopertura[arco.v] = True                    # Θ(1)
    return nodiCopertura                                    # Θ(1)

# Costo Computazionale: T(n,m) = Θ(1)+Θ(m)+Θ(n)+O(m)+O(m) = O(n+m)

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1)
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m)
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Per far si che la rimozione di ciascun arco dal vettore degli archi
#      abbia costo unitario Θ(1), e' necessario convertire tale vettore in una
#      lista concatenata.
# (E): Si scorrono tutti gli archi contenuti nella lista concatenata
#      rimuovendoli ad uno ad uno fino a che la lista non risulta essere vuota.
# (F): Si effettua la ricerca dei due nodi u e v dell'arco all'interno della
#      HashTable. Questa operazione, eseguita su vettore, avrebbe avuto costo
#      Θ(n). Usando la struttura dati di HashTable, invece, il costo e' Θ(1) in
#      quanto, per la ricerca, si sfrutta l'utilizzo di hashes.
# (J): Se nessuno dei nodi e' gia' stato selezionato, li si selezionano 
#      entrambi.


# ALGORITMO di VERTEX COVER per GRAFI PESATI (Bar-Yehuda & Even 1982)
# ----------------------------------------------------------------------------
''' 
L'algoritmo di Vertex Cover su Grafo Pesato scorre tutti gli archi uno ad 
uno e se entrambi i nodi dell'arco risultano ancora non coperti, l'algoritmo 
ne estra il peso corrispondente dal vettore dei pesi dei nodi, sottrae il
peso minimo dei due da entrambi e va a coprire il nodo dei due che ora risulta
avere peso = 0 (ovvero il nodo di peso minimo).
Al contrario, se l'arco presenta anche solo un nodo gia' coperto,
l'algoritmo passa direttamente all'arco successivo senza coprire il nodo
restante.
'''

def VertexCover_WeightedGraphs(E, pesiNodi, costoMin=0):    # T(n,m)
    nodiSet = set()                                         # Θ(1)         (A)
    for e in E:                                             # m*Θ(1)+Θ(1)
        if e.u not in nodiSet:                              # Θ(1)         
            nodiSet.add(e.u)                                # Θ(1)
        if e.v not in nodiSet:                              # Θ(1)
            nodiSet.add(e.v)                                # Θ(1)    
    nodiCopertura = {nodo:False for nodo in nodiSet }       # Θ(n)         (B)
    archi = copy.deepcopy(E)                                # Θ(m)         (C)
    archi = [a for a in archi if a.costo>= costoMin]        # Θ(m)         (D)
    if len(archi)== 0:                                      # Θ(1)         (E)  
        return nodiCopertura                                # Θ(1)   
    Archi_list = ListaConcatenata(archi[0])                 # Θ(1)         (F)
    for i in range(1,len(archi)):                           # (m-1)*O(1)
        Archi_list.append(archi[i])                         # Θ(1)
    dictPesiNodi = copy.deepcopy(pesiNodi)                  # Θ(n)         (G)
    while Archi_list.head!=None:                            # m*O(1)+Θ(1)  (H)
        arco = Archi_list.head.valore                       # Θ(1)      
        Archi_list.remove(arco)                             # Θ(1)
        if nodiCopertura[arco.u]==False and \
        nodiCopertura[arco.v]==False:                       # Θ(1)         (I)
            minPeso = min(dictPesiNodi[arco.u], \
                          dictPesiNodi[arco.v])             # Θ(1)         (J)  
            dictPesiNodi[arco.u] -= minPeso                 # Θ(1)  
            dictPesiNodi[arco.v] -= minPeso                 # Θ(1)
            for nodo in (arco.u, arco.v):                   # Θ(1)         (K) 
                if dictPesiNodi[nodo] == 0:                 # Θ(1)  
                    nodiCopertura[nodo] = True              # Θ(1)
    return nodiCopertura                                    # Θ(1)

# Costo Computazionale: T(n,m) = Θ(1)+Θ(m)+Θ(n)+O(m)+O(m) = O(n+m)

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1)
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m)
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Nel caso in cui si vogliano trascurare tutti gli archi avente costo/peso
#      inferiore al costo minimo in input, si copia il vettore degli archi 
#      aventi costo/peso maggiore in un nuovo vettore e si eliminano gli altri.
# (E): Se il vettore degli archi rimanenti e' vuoto, l'algoritmo non prosegue
#      e si restituisce il vettore dei nodi di copertura vuoto.
# (F): Per far si che la rimozione di ciascun arco dal vettore degli archi
#      abbia costo unitario Θ(1), e' necessario convertire tale vettore in una
#      lista concatenata.
# (G): Per poter riutilizzare la HashTable contenente i pesi dei nodi in altri 
#      algoritmi nello stesso file python, e' bene creare una copia del vettore 
#      originale e operare solo su di essa. Operazione extra non prevista 
#      dall'algoritmo classico come riportato in letteratura.
# (H): Si scorrono tutti gli archi contenuti nella lista concatenata
#      rimuovendoli ad uno ad uno fino a che la lista non risulta essere vuota.
# (I): Si effettua la ricerca dei due nodi u e v dell'arco all'interno della
#      HashTable. Questa operazione, eseguita su vettore, avrebbe avuto costo
#      Θ(n). Usando la struttura dati di HashTable, invece, il costo e' Θ(1) in
#      quanto, per la ricerca, si sfrutta l'utilizzo di hashes.
# (J): Si estrae il costo minimo fra i costi associati ai due nodi estremi dell
#      arco considerato e lo si va a sottrarre ai costi di entrambi.
#      In tal modo il costo corrispondente al nodo di costo minimo diviene = 0.
# (K): Fra i due nodi, si aggiunge alla lista dei nodi di copertura quello di
#      costo minimo.



# =================== ALGORITMI ESATTI di FORZA BRUTA =========================


# ALGORITMO ESATTO per GRAFI NON PESATI (Karp 1972)
# ----------------------------------------------------------------------------
'''
L'algoritmo di Vertex Cover Esatto su Grafo non pesato esplora tutti i possibili
sottoinsiemi di nodi tramite backtracking ricorsivo. Per ogni nodo decide se
includerlo o escluderlo dalla copertura (albero binario di profondita' n).
Raggiunta una foglia (tutti i nodi decisi), verifica se il sottoinsieme corrente
copre almeno un estremo per ogni arco. Se la verifica ha successo e la
cardinalita' e' minore del miglior risultato trovato finora, aggiorna il best.
Il pruning anticipa il taglio dei rami gia' peggiori del best corrente.
'''

def VertexCover_Graphs_BruteForce(E):                       # T(n,m)
    nodiSet = set()                                         # Θ(1)         (A)
    for e in E:                                             # m*Θ(1)+Θ(1)
        nodiSet.add(e.u)                                    # Θ(1)
        nodiSet.add(e.v)                                    # Θ(1)
    nodiCopertura = {nodo: False for nodo in nodiSet}       # Θ(n)         (B)
    archi = copy.deepcopy(E)                                # Θ(m)         (C)
    nodi = list(nodiSet)                                    # Θ(n)         (D)
    n    = len(nodi)                                        # Θ(1)
    best_set  = None                                        # Θ(1)         (E)
    best_size = float('inf')                                # Θ(1)         (F)

    def backtrack(idx, S_corrente):                         # O(2^n·m)
        nonlocal best_set, best_size
        if len(S_corrente) >= best_size:                    # Θ(1)         (G)
            return                                          # Θ(1)
        if idx == n:                                        # Θ(1)         (H)
            count = 0                                       # Θ(1)
            for a in archi:                                 # Θ(m)         (I)
                if a.u in S_corrente or a.v in S_corrente:  # Θ(1)
                    count += 1                              # Θ(1)
            if count == len(archi):                         # Θ(1)         (J)
                if len(S_corrente) < best_size:             # Θ(1)
                    best_set  = set(S_corrente)             # Θ(n)
                    best_size = len(S_corrente)             # Θ(1)
            return                                          # Θ(1)
        v = nodi[idx]                                       # Θ(1)         (K)
        backtrack(idx + 1, S_corrente)                      # T(n-idx-1)   (L)
        S_corrente.add(v)                                   # Θ(1)         (M)
        backtrack(idx + 1, S_corrente)                      # T(n-idx-1)   (N)
        S_corrente.remove(v)                                # Θ(1)         (O)

    backtrack(0, set())                                     # O(2^n·m)     (P)
    if best_set is not None:                                # Θ(1)         (Q)
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
# (D): Converte l'HashSet in vettore (una list in python corrisponde a un
#      vettore classico) per accesso posizionale Θ(1) tramite indice.
#      L'HashSet si usa per raccogliere i nodi senza duplicati, mentre
#      il vettore nodi[] e' il vettore utilizzato per il backtracking.
# (E): best_set: variabile contenente il miglior vertex cover trovato.
#      Inizializzata a None: nessun vertex cover valido trovato ancora.
# (F): best_size: variabile contenente la cardinalita' (numero di nodi)
#      del miglior vertex cover trovato.
#      Inizializzata a +inf: qualsiasi soluzione valida sara' migliore.
#      Si minimizza il NUMERO di nodi (versione NON pesata).
# (G): PRUNING ANTICIPATO: se il sottoinsieme corrente ha gia' tanti nodi quanti
#      il miglior risultato trovato finora, qualsiasi scelta futura non potra'
#      che peggiorare o pareggiare — mai migliorare. Il ramo viene potato.
#      Questo pruning e' possibile SOLO nella versione NON pesata: aggiungere
#      un nodo aumenta sempre la cardinalita' di esattamente 1.
# (H): CASO BASE: sono stati presi tutti gli n nodi. Si verifica ora se
#      S_corrente e' un vertex cover valido prima di aggiornare il best.
# (I): Verifica di validita': per ogni arco almeno uno dei due estremi u o v
#      deve essere in S_corrente. Il lookup sull'HashSet e' Θ(1).
#      Costo totale: Θ(m).
# (J): Se count == m tutti gli archi sono coperti: S_corrente e' un vertex cover
#      valido. Se inoltre e' piu' piccolo del best attuale, aggiorna best_set e
#      best_size. set(S_corrente) crea una COPIA: necessario perche' S_corrente
#      verra' modificato dai livelli superiori della ricorsione.
# (K): Nodo corrente su cui prendere la decisione includi/escludi.
#      Accesso posizionale Θ(1) grazie alla conversione list() al passo (D).
# (L): RAMO 1 — ESCLUDI v: ricorre sul nodo successivo senza modificare
#      S_corrente. v non entra nel sottoinsieme corrente.
# (M): Aggiunge v a S_corrente prima di ricorrere nel Ramo 2.
# (N): RAMO 2 — INCLUDI v: ricorre sul nodo successivo con v dentro S_corrente.
#      Esplora tutti i sottoinsiemi che contengono v.
# (O): RIPRISTINO (backtrack): rimuove v da S_corrente prima di tornare
#      al chiamante. S_corrente e' CONDIVISO su tutta la ricorsione; senza
#      questo remove, il Ramo 1 del livello superiore erediterebbe le
#      modifiche fatte dal Ramo 2 del livello corrente → soluzioni errate.
# (P): Avvio del backtracking: idx=0 (primo nodo), S_corrente={} (vuoto).
#      Esplora l'intero albero binario di profondita' n → 2^n foglie totali.
#      Ogni foglia costa Θ(m) per la verifica → T(n,m) = O(2^n · m).
#      Nota: rispetto agli ipergrafi non compare d (d=2 per grafi, costante).
# (Q): Costruisce il dizionario di output nel formato standard del progetto:
#      imposta a True solo i nodi appartenenti al miglior vertex cover trovato.
#      Se best_set e' None (nessun vertex cover valido esiste) il dizionario
#      rimane tutto False.


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
Iniziamo, per semplicita', con un esempio puramente numerico...e poi due esempi
piu' complessi: uno ispirato alla minimizzazione delle marcature sul Barcellona
calcio e uno sulla minimizzazione dei test su persone affette da epidemia.

"""


# LISTE DI ADIACENZA ----------------------------------------------------------


'Grafo Indiretto Connesso - Esempio Numerico ---------------------------------' 
E_Numeric = [
      ArcoPesato("A", "B", 1),
      ArcoPesato("A", "D", 1),
      ArcoPesato("A", "E", 1),
      ArcoPesato("B", "C", 1),
      ArcoPesato("C", "D", 1),
      ArcoPesato("C", "F", 1),
      ArcoPesato("D", "G", 1),
      ArcoPesato("E", "G", 1),
      ArcoPesato("F", "G", 1)
]


'Grafo Indiretto Connesso - Esempio Barcellona calcio  ----------------------'
'''
Costo dei Nodi -> Numero di marcatori richiesti per bloccare il giocatore
Costo degli Archi -> Numero di passaggi ogni 10 mins di gioco
''' 
E_Barcelona = [
    ArcoPesato('Abidal',     'Busquets',    5),
    ArcoPesato('Abidal',     'Dani Alves',  2),
    ArcoPesato('Abidal',     'Iniesta',     6),
    ArcoPesato('Abidal',     'Pique',       3),
    ArcoPesato('Abidal',     'Valdes',      3),
    ArcoPesato('Abidal',     'Villa',       4),
    ArcoPesato('Abidal',     'Xavi',        4),
    ArcoPesato('Busquets',   'Dani Alves',  5),
    ArcoPesato('Busquets',   'Iniesta',     8),
    ArcoPesato('Busquets',   'Mascherano',  6),
    ArcoPesato('Busquets',   'Pique',       7),
    ArcoPesato('Busquets',   'Xavi',        9),
    ArcoPesato('Dani Alves', 'Iniesta',     5),
    ArcoPesato('Dani Alves', 'Mascherano',  3),
    ArcoPesato('Dani Alves', 'Pedro',       6),
    ArcoPesato('Dani Alves', 'Valdes',      3),
    ArcoPesato('Dani Alves', 'Xavi',        6),
    ArcoPesato('Iniesta',    'MESSI',       9),
    ArcoPesato('Iniesta',    'Pedro',       4),
    ArcoPesato('Iniesta',    'Villa',       8),
    ArcoPesato('Iniesta',    'Xavi',        10),
    ArcoPesato('Mascherano', 'Pique',       9),
    ArcoPesato('Mascherano', 'Valdes',      6),
    ArcoPesato('MESSI',      'Pedro',       6),
    ArcoPesato('MESSI',      'Villa',       7),
    ArcoPesato('MESSI',      'Xavi',        8),
    ArcoPesato('Pedro',      'Villa',       4),
    ArcoPesato('Pique',      'Valdes',      6),
    ArcoPesato('Villa',      'Xavi',        5),
]

nw_Barcelona = {
    "Abidal": 1,
    "Busquets": 1,
    "Dani Alves": 1,
    "Iniesta": 2,
    "Mascherano": 1,
    "MESSI": 3,
    "Pedro": 1, 
    "Pique": 0,
    "Valdes": 0,
    "Villa": 2,
    "Xavi": 2
    }


'Grafo Indiretto Connesso - Esempio Epidemia  --------------------------------'
'''
Costo dei Nodi -> Resistenza del soggetto in scala 1-5
Costo degli Archi -> Numero di Incontri settimanali

'''
E_Epidemia = [
    ArcoPesato('Giulia',  'Marco',      3),
    ArcoPesato('Marco',   'Hans',       1),
    ArcoPesato('Hans',    'Fatima',     1),
    ArcoPesato('Fatima',  'Yuki',       3),
    ArcoPesato('Yuki',    'Giulia',     5),
    ArcoPesato('Giulia',  'Francesca',  7),
    ArcoPesato('Giulia',  'Alessandro', 5),
    ArcoPesato('Marco',   'Sophie',     1),
    ArcoPesato('Marco',   'Carlos',     4),
    ArcoPesato('Hans',    'Chiara',     8),
    ArcoPesato('Hans',    'Matteo',     3),
    ArcoPesato('Fatima',  'Olga',       1),
    ArcoPesato('Fatima',  'Liu Wei',    6),
    ArcoPesato('Yuki',    'Valentina',  4),
    ArcoPesato('Yuki',    'Lorenzo',    7),
]

nw_Epidemia = {
    "Giulia": 15,
    "Marco": 4,
    "Hans": 4,
    "Fatima": 4,
    "Yuki": 4,
    "Francesca": 3,
    "Alessandro": 3,
    "Sophie": 3,
    "Carlos": 3,
    "Chiara": 2,
    "Matteo": 1,
    "Olga": 1,
    "Liu Wei": 2,
    "Valentina": 2,
    "Lorenzo": 2
}
       


# ALGORITMO di VERTEX COVER per GRAFI -----------------------------------------

'Grafo Indiretto Connesso - Esempio Numerico -----------------------------'  
vc_Graphs_Exact =  VertexCover_Graphs_BruteForce(E_Numeric) 
vc_Graphs_Approx =  VertexCover_Graphs(E_Numeric)


print("\n---------------------------------------------------------------"+"\n"+
      "Grafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Copertura tramite Nodi in Grafo Indiretto "+"\n"+
      " > Algoritmo Esatto con Grafo Non Pesato: "+"\n"+
      "   - Nodi di Copertura: "+", "
      .join(str(k) for k,v in vc_Graphs_Exact.items() if v) +"\n"+
      " > Algoritmo di Approssimazione con Grafo Non Pesato: "+"\n"+
      "   - Nodi di Copertura: "+", "
      .join(str(k) for k,v in vc_Graphs_Approx.items() if v))


'Grafo Indiretto Connesso - Esempio Barcellona Calcio  ----------------------'
 
vc_Graphs_Exact =  VertexCover_Graphs_BruteForce(E_Barcelona)
vc_Graphs_Approx =  VertexCover_Graphs(E_Barcelona)
vc_WGraphs_Exact = VertexCover_WeightedGraphs_BruteForce(
    E_Barcelona, nw_Barcelona, True, 6)
vc_WGraphs_Approx = VertexCover_WeightedGraphs(
    E_Barcelona, nw_Barcelona, 6)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Barcellona Calcio:\n"
    "Copertura tramite Nodi in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_Graphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_Graphs_Approx.items() if v)
    + "\n"
    "-> Algoritmo Esatto con Grafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Approx.items() if v)
)


'Grafo Indiretto Connesso - Esempio Epidemia  --------------------------------'
vc_Graphs_Exact =  VertexCover_Graphs_BruteForce(E_Epidemia)
vc_Graphs_Approx =  VertexCover_Graphs(E_Epidemia)
vc_WGraphs_Exact = VertexCover_WeightedGraphs_BruteForce(
    E_Epidemia, nw_Epidemia, True, 2)
vc_WGraphs_Approx = VertexCover_WeightedGraphs(
    E_Epidemia, nw_Epidemia, 2)

print(
    "\n---------------------------------------------------------------------\n"
    "Grafo Indiretto Connesso - Esempio Epidemia:\n"
    "Copertura tramite Nodi in Grafo Indiretto\n"
    "-> Algoritmo Esatto con Grafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_Graphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_Graphs_Approx.items() if v)
    + "\n"
    "-> Algoritmo Esatto con Grafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con Grafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WGraphs_Approx.items() if v)
)