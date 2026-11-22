# -*- coding: utf-8 -*-
"""
LEZIONE 14b - ALGORITMI di APPROSSIMAZIONE e COPERTURA TRAMITE NODI [IPERGRAFI]

Gli Algoritmi di Approssimazione sono quella categoria di algoritmi creati per
risolvere problemi computazionalmente difficili e per i quali non esiste un
algoritmo che produca una soluzione esatta in tempi umanamente fattibili.
Gli Algoritmi di Approssimazione garantiscono che la soluzione da essi
raggiunta sia in grado di approssimare la soluzione esatta per un certo
rapporto/fattore di approssimazione.

Un classico esempio di Algoritmo di Approssimazione e' utilizzato per la
risoluzione del Problema di Copertura tramite Nodi (Vertex Cover).

Dopo averne vista l'applicazione su Grafi, vediamone ora l'applicazione su
Ipergrafi.

Gli Ipergrafi ----------------------------------------------------------------
Gli Ipergrafi sono grafi i cui archi connettono contemporaneamente piu' di 2
nodi.
Essi vengono rappresentati in forme molteplici
- Forme grafiche: Grafo di Eulero, Grafo Bipartito di Incidenza
- Forme analitiche: Matrice di Incidenza, Vettore dei Pesi dei Nodi, Lista di
                    Iperarchi
La rappresentazione usata in programmazione e' data dalla combinazione di
Lista di Iperarchi e Vettore dei Pesi dei Nodi (vedi esercizi sotto)

Algoritmo approssimato di Vertex Cover su Ipergrafi ---------------------------
Su grafi l’algoritmo greedy dà una 2-approssimazione garantita (prendi entrambi
gli estremi di ogni arco non coperto). 
Su ipergrafi con iperarchi di cardinalità d, aggiungere tutti i nodi di un 
iperarco dà una d-approssimazione — il fattore peggiora con la cardinalità. 
Se d è fissato, questa è un’approssimazione costante.

Algoritmo per Copertura Tramite Nodi
  - Formulazione Greedy         - O(n + m·d)
  - Formulazione Approssimante  - O(n + m·d)

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

# IperArco Pesato
# Definiamo ogni iperarco pesato del grafo come un oggetto avente 3 proprieta': 
# il nome, la lista dei nodi da esso collegati e il costo/peso dell'iper-arco.
# La classe IperArcoPesato definisce il criterio di ordinamento basato sui 
# valori crescenti dell'attributo 'costo'.

class IperArcoPesato:
    
    # Costruttore
    def __init__(self, nome, nodi, costo):
        self.nome = nome
        self.nodi = nodi
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
        return (self.nodi == altro.nodi and self.costo == altro.costo)
    
    # Conversione istanza di classe in stringa
    # Metodo equivalente a ToString()
    def __str__(self):
        return f"{self.nome}: {self.nodi} ({self.costo})"


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


# ALGORITMO di VERTEX COVER per IPER-GRAFI NON PESATI
# ----------------------------------------------------------------------------
''' 
L'algoritmo di Vertex Cover su Iper-grafo e' anche detto algoritmo di Hitting
Set su Ipergrafi.
L'algoritmo scorre tutti gli iperarchi uno ad uno e se l'ipergrafo considerato
non ha alcun nodo ancora coperto, l'algoritmo li copre tutti e passa a
considerare l'iperarco successivo.
Al contrario, se l'iperarco presenta anche solo un nodo gia' coperto,
l'algoritmo passa direttamente all'iperarco successivo senza coprire i nodi
restanti.
'''

def VertexCover_HyperGraphs(E):                             # T(n,m)
    nodiSet = set()                                         # Θ(1)         (A)
    for e in E:                                             # m*Θ(|e|)+Θ(1)
        for v in e.nodi:                                    # |e|*Θ(1)
            if v not in nodiSet:                            # Θ(1)         
                nodiSet.add(v)                              # Θ(1)
    nodiCopertura = {nodo:False for nodo in nodiSet }       # Θ(n)         (B)
    iperArchi = copy.deepcopy(E)                            # Θ(m)         (C)
    IperArchi_list = ListaConcatenata(iperArchi[0])         # Θ(1)         (D)
    for i in range(1,len(iperArchi)):                       # (m-1)*O(1)
        IperArchi_list.append(iperArchi[i])                 # Θ(1) 
    while IperArchi_list.head!=None:                        # m*O(1)+Θ(1)  (E)
        iperArco = IperArchi_list.head.valore               # Θ(1)      
        IperArchi_list.remove(iperArco)                     # Θ(1)
        count = 0                                           # Θ(1)
        for nodo in iperArco.nodi:                          # |e|*Θ(1)     (F) 
            if nodiCopertura[nodo] == False:                # Θ(1) 
                count += 1                                  # Θ(1) 
        if count == len(iperArco.nodi):                     # Θ(|e|)       (G)
            for nodo in iperArco.nodi:                      # |e|*Θ(1)
                nodiCopertura[nodo] = True                  # Θ(1)             
    return nodiCopertura                                    # Θ(1)

# Costo Computazionale: T(n,m) = Θ(1)+Θ(m·d)+Θ(n)+O(m·d)+O(m·d) = O(n + m·d)
# dove d = max|e| = cardinalità massima di un iperarco
# |e| = cardinalita' di uno specifico iperarco in un ipergrafo non uniforme
# cardinalita' = numero dei nodi dell'iperarco

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi dell'ipergrafo dalla lista degli iper
#      archi passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1)
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m·d)
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Per far si che la rimozione di ciascun iperarco dal vettore degli 
#      iperarchi abbia costo unitario Θ(1), e' necessario convertire tale 
#      vettore in una lista concatenata.
# (E): Si scorrono tutti gli iper-archi contenuti nella lista concatenata
#      rimuovendoli ad uno ad uno fino a che la lista non risulta essere vuota.
# (F): Si scorrono tutti i nodi contenuti nell'iperarco di cardinalita' |e| e
#      si contano i nodi non ancora coperti. Per controllare se un nodo e'
#      coperto o meno lo si ricerca nella HashTable dei nodi di copertura e si
#      controlla che il valore associato alla chiave sia True o False.
#      Questa operazione di ricerca ha costo unitario Θ(1), ma se la struttura
#      dati utilizzata fosse stata un vettore, essa avrebbe avuto costo O(n)
#      rendendo il costo complessivo del ciclo while O(m·d·n) invece di O(m·d).
# (G): Se nessuno dei nodi dell'iperarco risulta essere coperto, li si segnano
#      tutti come coperti all'interno della HashTable nodiCopertura.


# ALGORITMO di VERTEX COVER per IPER-GRAFI PESATI (Bar-Yehuda & Even 1982)
# ----------------------------------------------------------------------------
''' 
L'algoritmo di Vertex Cover su IperGrafo Pesato scorre tutti gli iperarchi uno 
ad uno e se tutti i nodi dell'arco risultano ancora non coperti, l'algoritmo 
ne estrae il peso corrispondente dal vettore dei pesi dei nodi, sottrae il
peso minimo fra tutti questi dal peso di ciascuno e va a coprire il nodo
che ora risulta avere peso = 0 (ovvero il nodo di peso minimo).
Al contrario, se l'iperarco presenta anche solo un nodo gia' coperto,
l'algoritmo passa direttamente all'iperarco successivo senza coprire i nodi
restanti.
'''

def VertexCover_WeightedHyperGraphs(E, pesiNodi, IsMinWeight, costoMin=0):   
    nodiSet = set()                                             # Θ(1)     (A)
    for e in E:                                                 # m*Θ(|e|)+Θ(1)
        for v in e.nodi:                                        # |e|*Θ(1)
            if v not in nodiSet:                                # Θ(1)         
                nodiSet.add(v)                                  # Θ(1)
    nodiCopertura = {nodo:False for nodo in nodiSet }           # Θ(n)     (B)
    iperArchi = copy.deepcopy(E)                                # Θ(m)     (C)
    iperArchi = [e for e in iperArchi if e.costo >= costoMin]   # Θ(m)     (D)
    if len(iperArchi)== 0:                                      # Θ(1)     (E)  
        return nodiCopertura                                    # Θ(1)   
    IperArchi_list = ListaConcatenata(iperArchi[0])             # Θ(1)     (F)
    for i in range(1,len(iperArchi)):                           # (m-1)*O(1)
        IperArchi_list.append(iperArchi[i])                     # Θ(1)
    dictPesiNodi = copy.deepcopy(pesiNodi)                      # Θ(n)     (G)
    sign = 1 if IsMinWeight else -1                             # Θ(1)     (H)    
    for k, v in dictPesiNodi.items():                           # Θ(n)
        dictPesiNodi[k] = sign*float(v)                         # Θ(1)
    while IperArchi_list.head!=None:                            # O(m)+Θ(1)(I)
        iperArco = IperArchi_list.head.valore                   # Θ(1)      
        IperArchi_list.remove(iperArco)                         # Θ(1)
        count = 0                                               # Θ(1)     (J)
        for nodo in iperArco.nodi:                              # Θ(|e|)+Θ(1) 
            if nodiCopertura[nodo] == False:                    # Θ(1)
                count += 1                                      # Θ(1)
        if count == len(iperArco.nodi):                         # Θ(|e|)   (K)
            minPeso = math.inf                                  # Θ(1)
            for nodo in iperArco.nodi:                          # Θ(|e|)+Θ(1)
                if minPeso > dictPesiNodi[nodo]:                # Θ(1) 
                    minPeso = dictPesiNodi[nodo]                # Θ(1) 
            for nodo in iperArco.nodi:                          # Θ(|e|)+Θ(1)
                dictPesiNodi[nodo] -= minPeso                   # Θ(1)     (L)
                if dictPesiNodi[nodo] == 0:                     # Θ(1) 
                    nodiCopertura[nodo] = True                  # Θ(1) 
    return nodiCopertura                                        # Θ(1) 

# Costo Computazionale: T(n,m) = Θ(1)+Θ(m·d)+Θ(n)+Θ(m)+O(m·d) = O(n+m·d)
# dove d = max|e| = cardinalità massima di un iperarco
# |e| = cardinalita' di uno specifico iperarco in un ipergrafo non uniforme
# cardinalita' = numero dei nodi dell'iperarco

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1)
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m·d)
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Nel caso in cui si vogliano trascurare tutti gli iperarchi avente costo
#      inferiore al costo minimo in input, si copia il vettore degli iperarchi 
#      aventi costo/peso maggiore in un nuovo vettore e si eliminano gli altri.
# (E): Se il vettore degli iperarchi rimanenti e' vuoto, l'algoritmo non 
#      prosegue e si restituisce il vettore dei nodi di copertura vuoto.
# (F): Per far si che la rimozione di ciascun iperarco dal vettore degli 
#      iperarchi abbia costo unitario Θ(1), e' necessario convertire tale 
#      vettore in una lista concatenata.
# (G): Per poter riutilizzare la HashTable contenente i pesi dei nodi in altri 
#      algoritmi nello stesso file python, e' bene creare una copia del vettore 
#      originale e operare solo su di essa. Operazione extra non prevista 
#      dall'algoritmo classico come riportato in letteratura.
# (H): Si vuole usare l'algoritmo per trovare la minima copertura tramite nodi
#      sia minimizzando che massimizzando il costo totale del minimo numero di
#      nodi coperti. Questo si ottiene specificando il parametro input booleano
#      isMinWeight = True/False. In base ad esso si definisce il paramter sign
#      = 1/-1 che consente di invertire l'ordinamento dei costi dei nodi.
#      In base al valore di sign, si aggiornano i costi dei nodi
#      moltiplicandoli per esso.
# (I): Si scorrono tutti gli iperarchi contenuti nella lista concatenata
#      rimuovendoli ad uno ad uno fino a che la lista non risulta essere vuota.
# (J): Si scorrono tutti i nodi contenuti nell'iperarco di cardinalita' |e| e
#      si contano i nodi non ancora coperti. Per controllare se un nodo e'
#      coperto o meno lo si ricerca nella HashTable dei nodi di copertura e si
#      controlla che il valore associato alla chiave sia True o False.
#      Questa operazione di ricerca ha costo unitario Θ(1), ma se la struttura
#      dati utilizzata fosse stata un vettore, essa avrebbe avuto costo Θ(n)
#      rendendo il costo complessivo del ciclo while O(m·d·n) invece di O(m·d).
# (K): Se tutti i nodi dell'iperarco risultano non coperti, si estrae il costo 
#      minimo fra i costi associati a tutti i nodi dell'iperarco considerato e 
#      lo si va a sottrarre ai costi di ciascuno.
#      In tal modo il costo corrispondente al nodo di costo minimo diviene = 0.
# (L): Fra tutti i nodi, si aggiunge alla lista dei nodi di copertura quello di
#      costo minimo.



# =================== ALGORITMI ESATTI di FORZA BRUTA =========================


# ALGORITMO ESATTO per IPER-GRAFI NON PESATI (Lovász 1975)
# ----------------------------------------------------------------------------
'''
L'algoritmo di Vertex Cover su IperGrafo NON Pesato esplora tutti i possibili
sottoinsiemi di nodi tramite backtracking ricorsivo. Per ogni nodo decide se
includerlo o escluderlo dalla copertura (albero binario di profondita' n).
Raggiunta una foglia (tutti i nodi decisi), verifica se il sottoinsieme corrente
copre almeno un nodo per ogni iperarco. Se la verifica ha successo e la
cardinalita' e' minore del miglior risultato trovato finora, aggiorna il best.
Il pruning anticipa il taglio dei rami gia' peggiori del best corrente.
'''

def VertexCover_HyperGraphs_BruteForce(E):                    # T(n,m)
    nodiSet = set()                                           # Θ(1)       (A)
    for e in E:                                               # Θ(m·d)
        for v in e.nodi:                                      # Θ(d)
            nodiSet.add(v)                                    # Θ(1)
    nodiCopertura = {nodo: False for nodo in nodiSet}         # Θ(n)       (B)
    iperarchi = copy.deepcopy(E)                              # Θ(m·d)     (C)
    nodi = list(nodiSet)                                      # Θ(n)       (D)
    n    = len(nodi)                                          # Θ(1)
    best_set  = None                                          # Θ(1)       (E)
    best_size = float('inf')                                  # Θ(1)       (F)

    def backtrack(idx, S_corrente):                           # O(2^n·m·d)
        nonlocal best_set, best_size
        if len(S_corrente) >= best_size:                      # Θ(1)       (G)
            return                                            # Θ(1)
        if idx == n:                                          # Θ(1)       (H)
            count = 0                                         # Θ(1)
            for e in iperarchi:                               # Θ(m)       (I)
                for v in e.nodi:                              # Θ(d)
                    if v in S_corrente:                       # Θ(1)
                        count += 1                            # Θ(1)
                        break                                 # Θ(1)
            if count == len(iperarchi):                       # Θ(1)       (J)
                if len(S_corrente) < best_size:               # Θ(1)
                    best_set  = set(S_corrente)               # Θ(n)
                    best_size = len(S_corrente)               # Θ(1)
            return                                            # Θ(1)
        v = nodi[idx]                                         # Θ(1)       (K)
        backtrack(idx + 1, S_corrente)                        # T(n-idx-1) (L)
        S_corrente.add(v)                                     # Θ(1)       (M)
        backtrack(idx + 1, S_corrente)                        # T(n-idx-1) (N)
        S_corrente.remove(v)                                  # Θ(1)       (O)

    backtrack(0, set())                                       # O(2^n·m·d) (P)
    if best_set is not None:                                  # Θ(1)       (Q)
        for v in best_set:                                    # Θ(n)
            nodiCopertura[v] = True                           # Θ(1)
    return nodiCopertura                                      # Θ(1)

# Costo Computazionale: T(n,m) = O(2^n · m · d)

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1).
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m·d).
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Converte l'HashSet in vettore (una list in python corrisponde a un
#      vettore classico) per accesso posizionale Θ(1) tramite indice.
#      Per eseguire l'algoritmo backtrack(), infatti, si usano vettori!
#      Quindi l'HashSet si usa per raccogliere i nodi senza duplicati, mentre
#      il vettore nodi[] è il vettore utilizzato per il backtracking.
# (E): best_set: variabile contenente il miglior vertex cover trovato.
#      La variabile viene inizializzata a None in quanto non ne e' ancora stato
#      trovato nessuno.
# (F): best_size: variabile contenente la cardinalità (numero di nodi)
#      del miglior vertex cover trovato.
#      La variabile viene inizializzata con best_size=inf in modo tale che
#      qualsiasi soluzione valida sarà migliore di quella inizializzata.
#      Si minimizza il NUMERO di nodi (non il peso: versione NON pesata).
# (G): PRUNING ANTICIPATO: se il sottoinsieme corrente ha già tanti nodi quanti
#      il miglior risultato trovato finora, qualsiasi scelta futura non potrà
#      che peggiorare o pareggiare — mai migliorare. Il ramo viene potato.
#      Questo pruning è possibile SOLO nella versione NON pesata: aggiungere
#      un nodo aumenta sempre la cardinalità di esattamente 1.
# (H): CASO BASE: sono stati presi tutti gli n nodi. Si verifica ora se
#      S_corrente e' un vertex cover valido prima di aggiornare il best.
# (I): Verifica di validità: per ogni iperarco e deve esistere almeno un nodo
#      v ∈ S_corrente. Il break esce dal ciclo interno appena trovato il primo
#      nodo che copre e, evitando controlli inutili: costo Θ(m·d) worst case,
#      Θ(m) best case (ogni iperarco coperto dal primo nodo controllato).
# (J): Se count == m tutti gli iperarchi sono coperti: S_corrente è un hitting
#      set valido. Se inoltre è più piccolo del best attuale, aggiorna best_set
#      e best_size. set(S_corrente) crea una COPIA: necessario perché
#      S_corrente verrà modificato dai livelli superiori della ricorsione.
# (K): Nodo corrente su cui prendere la decisione includi/escludi.
#      Accesso posizionale Θ(1) grazie alla conversione list() al passo (D).
# (L): RAMO 1 — ESCLUDI v: ricorre sul nodo successivo senza modificare
#      S_corrente. v non entra nel sottoinsieme corrente.
# (M): Aggiunge v a S_corrente prima di ricorrere nel Ramo 2.
# (N): RAMO 2 — INCLUDI v: ricorre sul nodo successivo con v dentro
#      S_corrente. Esplora tutti i sottoinsiemi che contengono v.
# (O): RIPRISTINO (backtrack): rimuove v da S_corrente prima di tornare
#      al chiamante. S_corrente è CONDIVISO su tutta la ricorsione; senza
#      questo remove, il Ramo 1 del livello superiore erediterebbe le
#      modifiche fatte dal Ramo 2 del livello corrente → soluzioni errate.
# (P): Avvio del backtracking: idx=0 (primo nodo), S_corrente={} (vuoto).
#      Esplora l'intero albero binario di profondità n → 2^n foglie totali.
#      Ogni foglia costa Θ(m·d) per la verifica → T(n,m) = O(2^n · m · d).
# (Q): Costruisce il dizionario di output nel formato standard del progetto:
#      imposta a True solo i nodi appartenenti al miglior hitting set trovato.
#      Se best_set è None (nessun hitting set valido esiste) il dizionario
#      rimane tutto False.


# ALGORITMO ESATTO per IPER-GRAFI PESATI (Bar-Yehuda & Even 1985)
# ----------------------------------------------------------------------------
'''
L'algoritmo di Vertex Cover su IperGrafo Pesato esplora tutti i possibili
sottoinsiemi di nodi tramite backtracking ricorsivo. Per ogni nodo decide se
includerlo o escluderlo dalla copertura (albero binario di profondita' n),
accumulando il peso totale del sottoinsieme corrente lungo ogni ramo.
Raggiunta una foglia (tutti i nodi decisi), verifica se il sottoinsieme corrente
copre almeno un nodo per ogni iperarco attivo (costo >= costoMin).
Se la verifica ha successo, aggiorna il best secondo il criterio scelto:
  - IsMinWeight=True : minimizza il peso totale; a parita' di peso, min nodi.
  - IsMinWeight=False: minimizza la cardinalita'; a parita' di nodi, max peso.
'''

def VertexCover_WeightedHyperGraphs_BruteForce(E, pesiNodi,
                                    IsMinWeight, costoMin=0): # T(n,m)
    nodiSet = set()                                           # Θ(1)       (A)
    for e in E:                                               # Θ(m·d)
        for v in e.nodi:                                      # Θ(d)
            nodiSet.add(v)                                    # Θ(1)
    nodiCopertura = {nodo: False for nodo in nodiSet}         # Θ(n)       (B)
    iperarchi = copy.deepcopy(E)                              # Θ(m·d)     (C)
    iperarchi = [e for e in iperarchi if e.costo >= costoMin] # Θ(m)       (D)
    if len(iperarchi) == 0:                                   # Θ(1)       (E)
        return nodiCopertura                                  # Θ(1)
    nodi         = list(nodiSet)                              # Θ(n)       (F)
    n            = len(nodi)                                  # Θ(1)
    dictPesiNodi = copy.deepcopy(pesiNodi)                    # Θ(n)       (G)
    best_set  = None                                          # Θ(1)       (H)
    best_size = float('inf')                                  # Θ(1)       (I)
    best_cost = float('-inf')                                 # Θ(1)       (J)

    def backtrack(idx, S_corrente, costo_corrente):           # O(2^n·m·d)
        nonlocal best_set, best_size, best_cost
        if idx == n:                                          # Θ(1)       (K)
            count = 0                                         # Θ(1)
            for e in iperarchi:                               # Θ(m)       (L)
                for v in e.nodi:                              # Θ(d)
                    if v in S_corrente:                       # Θ(1)
                        count += 1                            # Θ(1)
                        break                                 # Θ(1)
            if count == len(iperarchi):                       # Θ(1)       (M)
                size = len(S_corrente)                        # Θ(1)
                if IsMinWeight:                               # Θ(1)       (N)
                    # minimizza peso
                    if costo_corrente < best_cost or \
                       (costo_corrente == best_cost and
                        size < best_size):
                        best_set  = set(S_corrente)
                        best_size = size
                        best_cost = costo_corrente
                else:
                    # min cardinalità, a parità max peso
                    if size < best_size or \
                       (size == best_size and
                        costo_corrente > best_cost):          # Θ(1)
                        best_set  = set(S_corrente)           # Θ(n)
                        best_size = size                      # Θ(1)
                        best_cost = costo_corrente            # Θ(1)
            return                                            # Θ(1)
        v = nodi[idx]                                         # Θ(1)       (O)
        backtrack(idx + 1, S_corrente, costo_corrente)        # T(n-idx-1) (P)
        S_corrente.add(v)                                     # Θ(1)       (Q)
        backtrack(idx + 1, S_corrente,                        # T(n-idx-1) (R)
                  costo_corrente + dictPesiNodi[v])           # Θ(1)
        S_corrente.remove(v)                                  # Θ(1)       (S)

    backtrack(0, set(), 0)                                    # O(2^n·m·d) (T)
    if best_set is not None:                                  # Θ(1)       (U)
        for v in best_set:                                    # Θ(n)
            nodiCopertura[v] = True                           # Θ(1)
    return nodiCopertura                                      # Θ(1)

# Costo Computazionale: T(n,m) = O(2^n · m · d)

# Commenti
# (A): Per costruire l'HashTable contenente la selezione dei nodi di copertura
#      dobbiamo prima estrarre i nodi del grafo dalla lista degli archi
#      passata in input alla funzione.
# (B): I nodi di copertura vengono immagazzinati non in un vettore ma in una
#      HashTable. Questa struttura dati, a differenza del vettore, consente di
#      eseguire l'operazione di ricerca e di inserimento in costo unitario Θ(1).
#      Questo e' fondamentale per mantenere il costo del ciclo while sulla
#      lista degli archi limitato a O(m·d).
# (C): Per poter riutilizzare il vettore E in input in altri algoritmi nello
#      stesso file python e' bene creare una copia del vettore originale e
#      operare solo su di essa. Operazione extra non prevista dall'algoritmo
#      classico come riportato in letteratura.
# (D): Filtra gli iperarchi attivi: vengono considerati solo gli iperarchi il
#      cui costo e' maggiore o uguale alla soglia costoMin. Gli iperarchi sotto
#      soglia vengono ignorati dalla copertura. Parametro opzionale: se omesso
#      costoMin=0 e tutti gli iperarchi sono attivi.
# (E): Caso degenere: nessun iperarco attivo dopo il filtro → la copertura
#      vuota e' gia' valida, non occorre coprire nulla.
# (F): Converte l'HashSet in vettore per accesso posizionale Θ(1) tramite
#      indice. L'HashSet si usa per raccogliere i nodi senza duplicati, mentre
#      il vettore nodi[] e' il vettore utilizzato per il backtracking.
# (G): Copia difensiva dei pesi dei nodi per non alterare il dizionario
#      originale passato in input. Operazione extra rispetto alla letteratura.
# (H): best_set: variabile contenente il miglior vertex cover trovato.
#      Inizializzata a None: nessun hitting set valido trovato ancora.
# (I): best_size: variabile contenente la cardinalita' del miglior vertex cover.
#      Inizializzata a +inf: qualsiasi soluzione valida sara' migliore.
# (J): best_cost: variabile contenente il peso totale del miglior vertex cover.
#      Inizializzata a -inf: qualsiasi peso reale sara' maggiore all'inizio.
#      Serve per lo spareggio: a parita' di cardinalita' si preferisce max peso.
# (K): CASO BASE: sono stati presi tutti gli n nodi. Si verifica ora se
#      S_corrente e' un hitting set valido prima di aggiornare il best.
#      Nota: nella versione PESATA non esiste pruning anticipato come nella
#      versione non pesata — aggiungere un nodo aumenta il peso ma non
#      necessariamente peggiora la soluzione, quindi non si puo' potare.
# (L): Verifica di validita': per ogni iperarco e deve esistere almeno un nodo
#      v ∈ S_corrente. Il break esce dal ciclo interno appena trovato il primo
#      nodo che copre e: costo Θ(m·d) worst case, Θ(m) best case.
# (M): Se count == m tutti gli iperarchi sono coperti: S_corrente e' un hitting
#      set valido. Se soddisfa il criterio scelto meglio del best attuale,
#      aggiorna best_set, best_size e best_cost. set(S_corrente) crea una COPIA:
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
#      Ogni foglia costa Θ(m·d) per la verifica → T(n,m) = O(2^n · m · d).
# (U): Costruisce il dizionario di output nel formato standard del progetto:
#      imposta a True solo i nodi appartenenti al miglior hitting set trovato.
#      Se best_set e' None (nessun hitting set valido esiste) il dizionario
#      rimane tutto False.



" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...e poi due esempi
piu' complessi: uno ispirato alla minimizzazione dei costi di mantenimento
delle legioni dell'Antica Roma e uno sulla minimizzazione del numero di
gladiatori per coprire i principali eventi gladiatori annuali del Colosseo.

"""


# LISTE DI ADIACENZA ----------------------------------------------------------


'Grafo Indiretto Connesso - Esempio Numerico ---------------------------------' 
E_Numeric = [
      IperArcoPesato('01',['A', 'D', 'E', 'G'],1),
      IperArcoPesato('02',['A', 'B', 'D'],1),
      IperArcoPesato('03',['C', 'D', 'F'],1),
      IperArcoPesato('04',['C', 'D'],1),
      IperArcoPesato('05',['E', 'G'],1)
]


'Grafo Indiretto Connesso - Esempio Legioni Antica Roma ----------------------'
'''
Costo dei Nodi -> Costo di mantenimento della legione
''' 
E_Legioni = [
    IperArcoPesato('AEGYPTUS', ['LEGIO II', 'LEGIO X', 'LEGIO XXII'], 1),
    IperArcoPesato('AFRICA', ['LEGIO III', 'LEGIO V', 'LEGIO X'], 1),
    IperArcoPesato('GERMANIA INF', ['LEGIO I', 'LEGIO III', 'LEGIO V', 
                                    'LEGIO VI', 'LEGIO XIII', 'LEGIO XX'], 1),
    IperArcoPesato('GERMANIA SUP', ['LEGIO V', 'LEGIO VI', 'LEGIO XIII', 
                                    'LEGIO XVI', 'LEGIO XX'], 1),
    IperArcoPesato('HISPANIA', ['LEGIO I', 'LEGIO III', 'LEGIO VI', 
                                'LEGIO X', 'LEGIO XIII', 'LEGIO XVI'], 1),
    IperArcoPesato('SYRIA', ['LEGIO II', 'LEGIO VI', 'LEGIO X', 
                             'LEGIO XXII'], 1),
]

nw_Legioni = {
    "LEGIO I": 5,
    "LEGIO II": 6,
    "LEGIO III": 7,
    "LEGIO V": 9,
    "LEGIO VI": 9,
    "LEGIO X": 10,
    "LEGIO XIII": 8, 
    "LEGIO XVI": 4,
    "LEGIO XX": 6,
    "LEGIO XXII": 3
    }


'Grafo Indiretto Connesso - Esempio Gladiatori Antica Roma ------------------'
'''
Costo dei Nodi -> Numero di combattimenti in carriera (indicatore esperienza)
Costo degli Archi -> Numero di spettatori attesi

'''
E_Gladiatori = [
    IperArcoPesato('LUDI ROMANI', ['FLAMMA', 'PRISCUS', 
                                   'SPICULUS', 'VERUS'], 78),
    IperArcoPesato('VENATIO COLOSSEO', ['ASTYANAX', 'CARPOPHORUS', 'COLUMBUS', 
                                        'FLAMMA'], 65),
    IperArcoPesato('LUDI APOLLINARES', ['ASTYANAX', 'PETRAITES', 'PRISCUS', 
                                        'TETRAITES'], 48),
    IperArcoPesato('LUDI VICTORIAE SULLAE', ['FLAMMA', 'MARCUS ATTILIUS', 
                                             'PRISCUS', 'SPICULUS'], 72),
    IperArcoPesato('LUDI PLEBEII', ['ASTYANAX', 'COLUMBUS', 'TETRAITES'], 28),
    IperArcoPesato('MUNERA PRIVATA POMPEI', ['COLUMBUS', 'PETRAITES', 
                                             'TETRAITES', 'VERUS'], 12),
]

nw_Gladiatori = {
    "FLAMMA": 34,
    "SPICULUS": 28,
    "CARPOPHORUS": 22,
    "PETRAITES": 20,
    "COLUMBUS": 18,
    "PRISCUS": 17,
    "VERUS": 15,
    "TETRAITES": 12,
    "ASTYANAX": 9,
    "MARCUS ATTILIUS": 21
}
       


# ALGORITMO di VERTEX COVER per GRAFI -----------------------------------------

'IperGrafo Indiretto Connesso - Esempio Numerico -----------------------------'   
vc_HGraphs_Exact =  VertexCover_HyperGraphs_BruteForce(E_Numeric)
vc_HGraphs_Approx =  VertexCover_HyperGraphs(E_Numeric)


print("\n---------------------------------------------------------------"+"\n"+
      "IperGrafo Indiretto Connesso - Esempio Numerico: "+"\n"+
      "Copertura tramite Nodi in IperGrafo Indiretto "+"\n"+
      " > Algoritmo Esatto con IperGrafo Non Pesato: "+"\n"+
      "   - Nodi di Copertura: "+", "
      .join(str(k) for k,v in vc_HGraphs_Exact.items() if v) +"\n"+
      " > Algoritmo di Approssimazione con IperGrafo Non Pesato: "+"\n"+
      "   - Nodi di Copertura: "+", "
      .join(str(k) for k,v in vc_HGraphs_Approx.items() if v))


'IperGrafo Indiretto Connesso - Esempio Legioni Antica Roma  -----------------'
 
vc_HGraphs_Exact =  VertexCover_HyperGraphs_BruteForce(E_Legioni)
vc_HGraphs_Approx =  VertexCover_HyperGraphs(E_Legioni)
vc_WHGraphs_Exact = VertexCover_WeightedHyperGraphs_BruteForce(
    E_Legioni, nw_Legioni, True, 0)
vc_WHGraphs_Approx = VertexCover_WeightedHyperGraphs(
    E_Legioni, nw_Legioni, True, 0)

print(
    "\n---------------------------------------------------------------------\n"
    "IperGrafo Indiretto Connesso - Esempio Legioni Antica Roma:\n"
    "Copertura tramite Nodi in IperGrafo Indiretto\n"
    "-> Algoritmo Esatto con IperGrafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_HGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con IperGrafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_HGraphs_Approx.items() if v)
    + "\n"
    "-> Algoritmo Esatto con IperGrafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WHGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con IperGrafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WHGraphs_Approx.items() if v)
)


'IperGrafo Indiretto Connesso - Esempio Gladiatori Antica Roma  --------------'
vc_HGraphs_Exact =  VertexCover_HyperGraphs_BruteForce(E_Gladiatori)
vc_HGraphs_Approx =  VertexCover_HyperGraphs(E_Gladiatori)
vc_WHGraphs_Exact = VertexCover_WeightedHyperGraphs_BruteForce(
    E_Gladiatori, nw_Gladiatori, False, 40)
vc_WHGraphs_Approx = VertexCover_WeightedHyperGraphs(
    E_Gladiatori, nw_Gladiatori, False, 40)

print(
    "\n---------------------------------------------------------------------\n"
    "IperGrafo Indiretto Connesso - Esempio Gladiatori Antica Roma:\n"
    "Copertura tramite Nodi in IperGrafo Indiretto\n"
    "-> Algoritmo Esatto con IperGrafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_HGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con IperGrafo Non Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_HGraphs_Approx.items() if v)
    + "\n"
    "-> Algoritmo Esatto con IperGrafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WHGraphs_Exact.items() if v)
    + "\n"
    "-> Algoritmo di Approssimazione con IperGrafo Pesato:\n"
    " - Nodi di Copertura: "
    + ", ".join(str(k) for k, v in vc_WHGraphs_Approx.items() if v)
)