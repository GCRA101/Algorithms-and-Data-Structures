# -*- coding: utf-8 -*-
"""
LEZIONE 11 - ALGORITMI GREEDY - Parte 02

Gli Algoritmi Greedy sono una specifica categoria di algoritmi che costruiscono
la soluzione del problema computazionale accrescendo gradualmente soluzioni
parziali selezionando sempre e solo la piu' conveniente ad ogni step.
I due algoritmi greedy classici sono l'Algoritmo di Selezione delle Attivita' (
Activity Selection) e l'Algoritmo di Partizionamento delle Attivita' (Internal
Partitioning).
    
Algoritmi di Partizionamento delle Attivita' - INTERNAL PARTITIONING'
    - Formulazione classica con vettore - O(n^2)
    - Formulazione avanzata con heap - O(nlogn)
    - Esempio Problema Museo

"""


" ALGORITMI *****************************************************************"


# Librerie --------------------------------------------------------------------

from datetime import time



# Classi di utilita' ----------------------------------------------------------

class Activity:
    
    # Constructor
    def __init__(self, name, startTime, endTime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
    
    # Method defining Sorting Criteria in Sortable Data Structures
    # Method equivalent to compareTo(...)
    def __lt__(self, other):
        if self.endTime != other.endTime:
            return self.endTime < other.endTime
        
    # Method defining Equality Criteria in Data Structures
    # Method equivalent to equals(...)
    def __eq__(self, other):
        return (self.name == other.name and 
                self.startTime == other.startTime and 
                self.endTime == other.endTime)
    
    # Method converting the Class Instance into a String
    # Method equivalent to ToString()
    def __str__(self):
        return f"{self.name} ({self.startTime} → {self.endTime})"
        
    

# ============== ALGORITMO di PARTIZIONAMENTO delle ATTIVITA' =================


# INTERVAL PARTITIONING - CLASSICO con VETTORE
# -----------------------------------------------------------------------------
def intervalPartition_v01(activities,resources):            # T(n)
    activities.sort(key=lambda a: a.startTime)              # Θ(nlogn)     (A)
    numResources = 0                                        # Θ(1)         (B)
    numActivities = len(activities)                         # Θ(1)
    resEndTimes = [time(0,0)] * numActivities               # Θ(n)         (C)
    sol = []                                                # Θ(1)         (D)
    for i in range(len(activities)):                        # n*Θ(1)+Θ(1)  (E)
        k = 0                                               # Θ(1)
        while k <= numResources and \
            resEndTimes[k]>activities[i].startTime:         # k*Θ(1)+Θ(1)   
            k += 1                                          # Θ(1)
        if k == numResources + 1:                           # Θ(1)
            numResources += 1                               # Θ(1)
        sol.append((activities[i], resources[k]))           # Θ(1)
        resEndTimes[k] = activities[i].endTime              # Θ(1)
    return numResources, sol                                # Θ(1)

# Commenti
# (A): Le attivita' vengono ordinate per ordine crescente del tempo di 
#      INIZIO (il contrario dell' ACTIVITY SELECTION).
#      Per ottenere cio' si assegna al metodo .sort() di python un comparer
#      on-the-fly che ridefinisce il method __lt__ a livello locale e basato
#      su startTime invece di endTime.
# (B): Inizializzazione del contatore delle risorse necessarie - si inizia con
#      con 0 e si aumenta in base alle necessita'.
# (C): Inizializzazione del vettore di dimensione n (n = numero attivita')
#      contenente, per ciascuna risorsa, il tempo di FINE dell'ultima attivita'
#      in esso contenuta.
# (D): Inizializzazione del vettore soluzione, contenente le coppie di
#      assegnamenti (attivita', risorsa) in ordine crescente di tempo di INIZIO
# (E): Si scorrono tutte le attivita' in ordine crescente di tempo di INIZIO.
#      Si scorrono le risorse esistenti. Se tutte hanno tempo di FINE maggiore
#      del tempo di INIZIO dell'attivita' corrente, si aggiunge una nuova
#      risorsa, altrimenti si seleziona la prima risorsa esistente avente tempo
#      di FINE minore del tempo di INIZIO dell'attivita' corrente.
#      Si assegna quindi l'attivita' corrente alla risorsa e si aggiorna il
#      tempo di FINE della risorsa con il tempo di FINE dell'attivita' appena
#      assegnata ad essa.

# Costo Computazionale: O(n^2) - CASO PEGGIORE (*)
#                       Ω(n)   - CASO MIGLIORE (**)   
#
# (*): Una risorsa per ciascuna attivita'
# (**): Un'unica risorsa per tutte le attivita'
                                                                   


# INTERVAL PARTITIONING - AVANZATO con HEAP MINIMO
# -----------------------------------------------------------------------------

# HEAP MINIMO -----------------------------------------------------------------

# HEAPIFY Function
def heapifyMin(A,n,i):                          # T(n)               '--(A)--'
    left=2*i+1                                  # Θ(1)               '--(B)--'
    right=2*i+2                                 # Θ(1)
    if (left<n)and(A[left]<A[i]):               # Θ(1)
        iMin=left                               # Θ(1)
    else:                                       # Θ(1)
        iMin=i                                  # Θ(1)
    if (right<n)and(A[right]<A[iMin]):          # Θ(1)
        iMin=right                              # Θ(1)
    if iMin!=i:                                 # Θ(1)
        temp=A[i]                               # Θ(1)
        A[i]=A[iMin]                            # Θ(1)
        A[iMin]=temp                            # Θ(1)
        heapifyMin(A,n,iMin)                    # T(2/3n)
    return
    
# BUILDHEAP Function
def buildHeapMin(A):                            # T(n)
    m=len(A)                                    # Θ(1)               '--(C)--'
    for i in range(m//2-1,-1,-1):               # n/2*O(logn)+Θ(1)
        heapifyMin(A,m,i)                            
    return                                      # Θ(1)
    

' FUNZIONE HEAPSORT'

def heapSortMin(A):                         # T(n)
    buildHeapMin(A)                         # O(n)
    for heapSize in range(len(A)-1,-1,-1):  # (n-1) + Θ(1)        
        temp=A[heapSize]                    # Θ(1)
        A[heapSize]=A[0]                    # Θ(1)
        A[0]=temp                           # Θ(1)
        heapifyMin(A,heapSize,0)            # O(logn)                '--(D)--'
    return                                  # Θ(1)

'''
Note Importanti
(A): Passare il parametro variabile n nella funzione heapify e' cio' che
     consente di considerare una porzione di vettore A sempre piu' piccola (
     1 elemento in meno ad ogni ciclo nella funzione heapSort) senza dover 
     passare il corrispondente sotto-vettore di A. A rimane sempre della stessa 
     lunghezza cosi da poter essere modificato e ordinato in loco mentre la 
     porzione di esso che si va via via a considerare e' compresa tra 0 e n.
(B): left=2*i e right=2*i+1 sarebbero corretti solo se il primo indice dell'array
     fosse 1! Dato che il primo indice e' sempre =0, dobbiamo aggiungere un 1
     alle espressioni sopra in modo che, quando i=0 -> left=1 e right=2.
     Abbiamo quindi left=2*i+1 e right=2*i+2!
(C): Chiamiamo la funzione heapify sul vettore A, con dimensione costante m
     e elemento di indice variabile i dalla mezzeria del vettore alla posizione
     iniziale (indice 0)
(D): Richiamiamo la funzione heapify passandole sempre lo stesso vettore A,
     lo stesso indice di radice 0 ma con indice massimo che si riduce di 1 
     ad ogni ciclo.

'''

# Dimensione input: numero n di elementi nell'array A
# Caso migliore e caso peggiore coincidono.
# Il costo computazionale dei 3 algoritmi Heapify, BuildHeap e HeapSort e' 
# come segue:
# - Heapify:   T(n)=T(2/3n)+Θ(1)  -> T(n)=O(logn)
# - BuildHeap: T(n)=O(n)          -> T(n)=O(n)
# - HeapSort:  T(n)=O(nlogn)      -> T(n)=O(nlogn)


# FUNZIONI AUSILIARI SU HEAP MINIMO -------------------------------------------

# ESTRAZIONE MINIMO da HEAP MINIMO 
# Funzione con il compito di estrarre (rimuovendolo!) il valore minimo 
# contenuto nello Heap Minimo passato in input e di ripristianare la restante
# parte di vettore come heap minimo (tramite funzione ricorsiva heapify)
def extractMin(A):                              # T(n)        (A)
    minItem = A[0]                              # Θ(1)        (B)
    last = A.pop()                              # Θ(1)        (C)
    if len(A)!=0:                               # Θ(1)        (D)
        A[0] = last                             # Θ(1)
        heapifyMin(A, len(A), 0)                # Θ(logn)
    return minItem                              # Θ(1)        (E)

# Commenti
# (A): La funzione prende in input il vettore di Heap Minimo
# (B): Salva la radice dello Heap in una variabile per poterla restituire come
#      output (la radice di uno Heap Minimo e' il valore minimo)
# (C): Rimuovi l'ultimo elemento del vettore heap (non il primo proprio per 
#      evitare il costo di dover fare slittare le celle del vettore a seguito
#      della rimozione dell'elemento).
# (D): Se il vettore heap ha ancora elementi dopo la rimozione dell'ultimo,
#      sostituisci il primo elemento (minimo estratto) con l'ultimo (last) e
#      ripristina la proprieta' di heap per il vettore cosi' modificato.
# (E): Restituisci il valore minimo estratto come output

# Costo Computazionale: O(logn)


# RIPRISTINO PROPRIETA' DI HEAP IN RISALITA
# Funzione analoga ad heapifyMin ma diretta in senso opposto.
# Mentre heapifyMin ripristina la proprieta' di heap dall'alto verso il basso
# (dalla radice alle foglie) confrontando ciascun nodo con i suoi due figli, 
# siftUp procede dal basso verso l'alto (dalla foglia alla radice) confrontando
# ciascun nodo con suo padre.
def siftUp(A, i):                               # T(n)        (A)
    while i > 0:                                # O(log n)    (B)
        parent = (i - 1) // 2                   # Θ(1)        (C)
        if A[parent][1] > A[i][1]:              # Θ(1)        (D)
            A[parent], A[i] = A[i], A[parent]   # Θ(1)
            i = parent                          # Θ(1)
        else:                                   # Θ(1)
            break                               # Θ(1)
    return                                      # Θ(1)

# Commenti
# (A): La funzione prende in input il vettore di Heap Minimo e l'indice dell'
#      elemento che potrebbe violare la proprieta' di heap
# (B): Si itera su tutti i livelli tra il nodo considerato e la radice (quindi
#      al piu' logn)
# (C): Determina l'indice del nodo padre all'interno del vettore di heap
# (D): Se il nodo padre ha valore (endTime) maggiore del nodo figlio, questo
#      viola l'ordinamento di heap minimo ed e' necessario scambiare i valori
#      tra nodo padre e nodo figlio.
#      Si aggiorna il contantore i con l'indice del nodo padre per poter
#      ripetere il ciclo al livello superiore dello heap controllando cosi
#      che la violazione dell'ordinamento di heap non sia stata propagata al
#      livello superiore. Si continua fino al raggiungimento della radice...

# Costo Computazionale: O(logn)


# INSERIMENTO MINIMO in HEAP MINIMO
# Funzione con il compito di aggiungere una nuova coppia (resource, endTime) 
# allo Heap Minimo assicurandosi di mantenere la proprieta' di heap nel vettore
# cosi' modificato. Cio' e' ottenuto aggiungendo la coppia alla fine del
# vettore ed eseguendo un ripristino della proprieta' di heap minimo partendo
# dall'ultimo elemento e risalendo verso la radice del vettore di heap.
def insertMin(A, item):                         # T(n)        (A)
    A.append(item)                              # Θ(1)        (B)
    siftUp(A, len(A) - 1)                       # Θ(logn)     (C)

# Commenti
# (A): La funzione prende in input il vettore di Heap Minimo e l'elemento da
#      inserire in esso.
# (B): Aggiungi l'elemento alla fine del vettore (non all'inizio proprio per
#      evitare il costo di dover fare slittare le celle del vettore a seguito
#      dell'inserimento).
# (C): Ripristina la proprieta' di heap per il vettore cosi' modificato

# Costo Computazionale: O(logn)


# INTERVAL PARITITIONING con HEAP MINIMO --------------------------------------

def intervalPartition_v02(activities,resources):           # T(n)        (A)
    activities.sort(key=lambda a: a.startTime)             # Θ(nlogn)    (B)
    numResources = 0                                       # Θ(1)        (C)
    sol = []                                               # Θ(1)        (D)
    heapMin = [(resources[0],time(0,0))]                   # Θ(1)        (E)
    for i in range(len(activities)):                       # n*Θ(1)+Θ(1) (F)
        resource = heapMin[0][0]                           # Θ(1)        (G)
        endTime = heapMin[0][1]                            # Θ(1)
        if activities[i].startTime >= endTime :            # Θ(1)        (H)
            sol.append((activities[i], resource))          # Θ(1)
            extractMin(heapMin)                            # Θ(logk)
            endTime = activities[i].endTime                # Θ(1)
            insertMin(heapMin, (resource, endTime))        # Θ(logk)
        else:                                              # Θ(1)        (I)
            numResources += 1                              # Θ(1)
            resource = resources[numResources]             # Θ(1)
            sol.append((activities[i], resource))          # Θ(1)
            endTime = activities[i].endTime                # Θ(1)
            insertMin(heapMin, (resource, endTime))        # Θ(logk)
    return numResources, sol                               # Θ(1)

# Commenti
# (A): La funzione prende in input il vettore delle attivita' e un vettore di
#      possibili risorse disponibili.
# (B): Ordina le attivita' in ordine crescente sulla base del tempo di inizio
#      di ciascuna.
# (C): Inizializza il contatore delle risorse necessarie.
# (D): Inizializza il vettore soluzione contenente le coppie.
#      (attivita', risorsa) in ordine di tempo di inizio crescente.
# (E): Inizializza lo Heap Minimo con la prima risorsa associata a tempo di
#      fine nullo.
# (F): Scorri tutte le attivita' in ordine di tempo di inizio crescente
# (G): Estrai dallo Heap la risorsa che si libera prima con il suo 
#      corrispondente tempo di fine - ovvero il tempo in cui si libera.
# (H): Controlla se l'attivita' corrente inizia dopo che questa risorsa divenga
#      libera. Se si, assegna l'attivita' alla risorsa e salva la coppia nel 
#      vettore soluzione. Aggiorna quindi la suddetta risorsa nello heap prima
#      rimuovendola (extractMin) e quindi reinserendola con tempo di fine 
#      aggiornato al tempo di fine dell'attivita' appena assegnata ad essa 
#      (endTime, insertMin).
#      In tale modo, lo Heap Minimo continua a contenere tutte le risorse che
#      mano a mano si utilizzano con tempo di fine corrispondente. La risorsa
#      che si libera prima (tempo di fine minimo) sara' sempre in prima
#      posizione nel vettore dello Heap Minimo.
# (I): Se l'attivita' corrente inizia prima della risorsa che, tra tutte, si
#      libera per prima, vuol dire che serve una nuova risorsa.
#      Il contatore delle risorse viene incrementato e una nuova risorsa viene
#      estratta dal pool resources in input. Si assegna l'attivita' corrente
#      alla nuova risorsa e si salva la coppia (attivita',risorsa) nel vettore
#      soluzione.
#      Infine, si inserisce la nuova risorsa, associata con il tempo di fine
#      dell'attivita' ad essa assegnata, all'interno del vettore di heap minimo
#      insertMin() si occupa sia dell'inserimento che del ripristino dell'
#      ordinamento di heap minimo a seguito dell'inserimento stesso.

# Costo Computazionale: O(nlogn)



# INTERVAL PARTITIONING - ESEMPIO MUSEO
# -----------------------------------------------------------------------------
def intervalPartition_Museum(framePositions,guardMaxDist):   # T(n)        (A)
    guardPositions = []                                      # Θ(1)        (B)
    i = 0                                                    # Θ(1)
    n = len(framePositions)                                  # Θ(1)
    while i<n:                                               # n*Θ(1)+Θ(1) (C) 
        p = framePositions[i] + guardMaxDist                 # Θ(1)
        guardPositions.append(p)                             # Θ(1)
        while i<n and framePositions[i]<p+guardMaxDist:      # k*Θ(1)+Θ(1) (D)
            i += 1                                           # Θ(1)
    return guardPositions                                    # Θ(1)

# Commenti
# (A): La funzione prende in input il vettore delle posizioni x dei quadri del
#      museo e la massima distanza in metri che una guardia puo' sorvegliare
# (B): Inizializza il vettore delle posizioni delle guardie necessarie per
#      sorvegliare tutti i quadri, il contatore e il numero dei quadri.
# (C): Itera fino a che non si raggiunge l'ultimo quadro. Calcola la posizione
#      della guardia necessaria e salvala nel vettore guardPositions
# (D): Incrementa i fino a raggiungere la posizione del successivo quadro che
#      si trova a distanza limite dall'ultima guardia.

# Costo Computazionale: O(n)


" ESEMPI ********************************************************************"

"""
Vediamo alcune applicazioni pratiche dell'algoritmo greedy di selezione delle
attivita'.
Caso 01 -> attivita': lezioni di informatica
           risorse: giornata di studio
Caso 02 -> attivita': attivita' giornaliere in tailandia
           risorse: giornata di vacanza
Caso 03 -> attivita': sessioni di atterraggio aerei
           risorse: pista di atterraggio'
Caso 04 -> attivita': posizioni quadri museo
           risorse: guardie'

"""
' Case 01 - Computer Science Lessons'
activities01 = [Activity("Web Architecture - Backend", time(10,0), time(12,0)),
                Activity("Algorithms - Graphs", time(9,0), time(11,0)),
                Activity("Software Eng - Unit Tests", time(14,0), time(16,0)),
                Activity("Algorithms - Greedy Algos", time(15,0), time(17,0)),
                Activity("Digital Systems - Automata", time(10,0), time(12,0)),
                Activity("DataBases - SQL", time(14,0), time(18,0)),
                Activity("OOP - Design Patterns", time(15,00), time(17,0)),
                Activity("Programming - Recursion", time(17,0), time(18,0))]

resources01 =  ["Fermi Hall", "Meucci Hall", "Faggin Hall", "Da Vinci Hall"]

'Case 02 - Daily Activities in Thailand'
activities02 = [Activity("Muay Thai Training", time(7,0), time(8,0)),
                Activity("Coco Tam Fire Show", time(19,0), time(21,0)),
                Activity("Jet Ski Session", time(14,0), time(17,0)),
                Activity("Gym Training", time(8,30), time(10,0)),
                Activity("Boat Trip to Koh Phanghan", time(19,30), time(20,0)),
                Activity("Thai Cooking Class", time(11,0), time(13,0)),
                Activity("Spa Session", time(14,30), time(17,00)),
                Activity("Muay Thai Fight Show", time(19,30), time(22,0)),
                Activity("Date with Russian Girl", time(20,30), time(23,30)),
                Activity("Swimming Pool", time(14,0), time(14,30)),
                Activity("Snorkeling Session", time(12,0), time(13,30)),
                Activity("Scuba Diving Class", time(10,30), time(13,30)),
                Activity("Tennis Club", time(15,30), time(17,30)),
                Activity("Full Moon Party", time(20,00), time(23,30))]

resources02 =  ["Giorgio", "Tanya", "Hannah", "Anastasia", "Mike"]

'Case 03 - Requested Landing Slots'
activities03 = [Activity("AF1580 - Paris CDG (CDG)", time(7, 26), time(7, 38)),
                Activity("BA1326 - Edinburgh (EDI)", time(7, 0),  time(7, 12)),
                Activity("EI168 - Dublin (DUB)",     time(7, 35), time(7, 47)),
                Activity("FR8421 - Dublin (DUB)",    time(7, 8),  time(7, 20)),
                Activity("IB3166 - Madrid (MAD)",    time(7, 58), time(8, 10)),
                Activity("KL1007 - Amsterdam (AMS)", time(7, 40), time(7, 52)),
                Activity("LH924 - Frankfurt (FRA)",  time(7, 18), time(7, 30)),
                Activity("SN2098 - Brussels (BRU)",  time(8, 5),  time(8, 17)),
                Activity("TP1364 - Lisbon (LIS)",    time(8, 15), time(8, 27)),
                Activity("U28453 - Barcelona (BCN)", time(7, 50), time(8, 2))]

resources03 =  ["Lane 01","Lane 02","Lane 03","Lane 04"]

'Case 04 - Required Museum Guards'
framePositions = [1.0, 3.0, 8.0, 9.0, 14.0, 17.5, 20.0, 21.0, 22.0, 25.0, 30.0]
guardMaxDist = 5


# ALGORITMO GREEDY di PARTIZIONAMENTO delle ATTIVITA' -------------------------

print("\nPARTIZIONAMENTO ATTIVITA' tramite ALGORITMO GREEDY *****************"+
      "****************************************************************"+"\n")

'Case 01 - Computer Science Lessons ------------------------------------------'
                       
print("Case 01 - Computer Science Lessons")
print("--------------------------------------------------")
print("Vettore lezioni non ordinato:")
print(*activities01, sep="\n")

ip01 = intervalPartition_v01(activities01, resources01)
print("--------------------------------------------------")
print("Vettore lezioni ordinato:")
print(*activities01, sep="\n")
print("--------------------------------------------------")
print("Vettore assegnamenti Lezione<->Studente:")
print("\n".join(f"[{x}] <==> [{y}]" for x, y in ip01[1]))
print("\n\n")


'Case 02 - Daily Activities in Thailand --------------------------------------'
                      
print("Case 02 - Daily Activities in Thailand")
print("--------------------------------------------------")
print("Vettore attivita' non ordinato:")
print(*activities02, sep="\n")

ip02 = intervalPartition_v02(activities02, resources02)
print("--------------------------------------------------")
print("Vettore attivita' ordinato:")
print(*activities02, sep="\n")
print("--------------------------------------------------")
print("Vettore assegnamenti Attivita'<->Turista:")
print("\n".join(f"[{x}] <==> [{y}]" for x, y in ip02[1]))
print("\n\n")


'Case 03 - Requested Landing Slots -------------------------------------------'                        

print("Case 03 - Requested Landing Slots")
print("--------------------------------------------------")
print("Vettore sessioni di atterraggio non ordinato:")
print(*activities03, sep="\n")

ip03 = intervalPartition_v02(activities03, resources03)
print("--------------------------------------------------")
print("Vettore sessioni di atterraggio ordinato:")
print(*activities03, sep="\n")
print("--------------------------------------------------")
print("Vettore assegnamenti Volo<->Pista")
print("\n".join(f"[{x}] <==> [{y}]" for x, y in ip03[1]))
print("\n\n")


'Case 04 - Museum Guards ----------------------------------------------------'                        

print("Case 04 - Museum Guards")
print("--------------------------------------------------")
ip04 = intervalPartition_Museum(framePositions, guardMaxDist)
print("--------------------------------------------------")
print("Vettore posizioni quadri:")
print(*framePositions, sep="\n")
print("--------------------------------------------------")
print("Vettore posizioni guardie:")
print(*ip04, sep="\n")
print("\n\n")
