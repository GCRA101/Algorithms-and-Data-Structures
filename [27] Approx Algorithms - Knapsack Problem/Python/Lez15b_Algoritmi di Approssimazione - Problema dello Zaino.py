# -*- coding: utf-8 -*-
"""
LEZIONE 15b - ALGORITMI di APPROSSIMAZIONE e PROBLEMA dello ZAINO [GRAFI]

Gli Algoritmi di Approssimazione sono quella categoria di algoritmi creati per
risolvere problemi computazionalmente difficili e per i quali non esiste un
algoritmo che produca una soluzione esatta in tempi umanamente fattibili.
Gli Algoritmi di Approssimazione garantiscono che la soluzione da essi
raggiunta sia in grado di approssimare la soluzione esatta per un certo
rapporto/fattore di approssimazione.

Un classico esempio di Algoritmo di Approssimazione e' utilizzato per la
risoluzione del Problema dello Zaino (Knapsack-Problem).

Il Problema dello Zaino (Knapsack Problem) e' utilizzato per modellare numerosi
problemi computazionali reali che includono i trasporti, la logistica, il
taglio e l'imballaggio, le telecomunicazioni, gli investimenti...
Dati n oggetti ciascuno con uno specifico costo/peso e valore, l'obiettivo e'
selezionare la combinazione di oggetti che massimizza il valore totale senza
che il costo/peso totale sia maggiore di un determinato valore limite.

Il Problema non viene modellato tramite grafo e la struttura dati che utilizza
e' un vettore bidimensionale.

Algoritmo per problema dello Zaino (Knapsack Problem)
  - Formulazione Esatta - O(n^2*vmax)
  - Formulazione Approssimata  - O(n^3/ε)
  
Formulazione Esatta
    - Algoritmo di Programmazione Dinamica (vedi Lezioni 23,24 del corso)
    - Soluzione Esatta

Formulazione Approssimata
    - Algoritmo FPTAS (Fully Polynomial-Time Approximation Scheme)
    - Algoritmo di Ibarra-Kim, 1975
    - Soluzione Approssimata (non esatta)
    - Rapporto/Fattore di Approssimazione GARANTITO = 1 + ε
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math, time, copy
from fractions import Fraction

# Classi di utilita' ----------------------------------------------------------

# Oggetto
# Definiamo la classe oggetto avente tre proprieta': il nome dell'oggetto,
# il valore e il peso corrispondente.

class Object:
    
    # Costruttore
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.cost = cost
    
    # Definizione criterio di ordinanemto per strutture dati ordinabili
    # Metodo equivalente a compareTo(...)
    def __lt__(self, altro):
        if self.cost != altro.cost:
            return self.cost < altro.cost
    def __le__(self, altro):
            return self.cost <= altro.cost
        
    # Definizione criterio di uguaglianza per ricerca in strutture dati
    # Metodo equivalente a equals(...)
    def __eq__(self, altro):
        return (self.name == altro.name and self.value == altro.value and
                self.cost == altro.cost)
    
    # Conversione istanza di classe in stringa
    # Metodo equivalente a ToString()
    def __str__(self):
        return f"{self.name} - (V:{self.value}, C:{self.cost})"
    


# ==================== ALGORITMO per KNAPSACK PROBLEM =========================


# ALGORITMO APPROSSIMATO e ESATTO per il KNAPSACK PROBLEM
# ----------------------------------------------------------------------------
'''
L'algoritmo di Zaino Approssimato (Ibarra-Kim, 1975) - detto anche Knapsack
Problem - e' uno schema di approssimazione completamente polinomiale (FPTAS).
Per ogni ε > 0 produce una soluzione di valore A(I) con OTT(I)/A(I) <= 1+ε 
in tempo O(n^3/ε).
Idea su cui si basa e' la seguente: l'algoritmo ESATTO e' pseudopolinomiale con
costo computazionale O(n^2*vmax), cioe' polinomiale solo se i valori sono 
piccoli (se vmax=2^n, il costo diventa esponenziale!)
Si scalano allora tutti i valori dividendoli per b = ε*vmax/(2n) e arrotondando 
per eccesso, cosi' il valore massimo diventa (2n/ε) approssimato superiore. 
Si risolve in modo esatto l'istanza scalata e la soluzione trovata si considera 
valida per l'istanza originale.
Knapsack_Exact e' la programmazione dinamica sui VALORI: opt[i][v] e' il peso
minimo di un sottoinsieme dei primi i oggetti che ha valore esattamente v.
'''

def Knapsack_Exact(costTotMax,objects,V,P):               # T(n,Vtot)
    t0 = time.perf_counter()                              # Θ(1)
    n = len(V)                                            # Θ(1)       (A)
    Vtot = sum(V)                                         # Θ(n)       (B)
    opt = []                                              # Θ(1)
    for i in range(n+1):                                  # (n+1)*Θ(1) (C)
        opt.append([])                                    # Θ(1)
        for v in range(Vtot+1):                           # (Vtot+1)*Θ(1)+Θ(1)
            opt[i].append(math.inf)                       # Θ(1)
    opt[0][0] = 0                                         # Θ(1)       (D)
    for i in range(1,n+1):                                # n*Θ(1)+Θ(1)
        for v in range(0,Vtot+1):                         # Vtot*Θ(1)+Θ(1)
            opt[i][v] = opt[i-1][v]                       # Θ(1)       (E)
            if v >= V[i-1] and \
               opt[i-1][v-V[i-1]] + P[i-1] < opt[i][v]:   # Θ(1)       (F)
                opt[i][v] = opt[i-1][v-V[i-1]] + P[i-1]   # Θ(1)
    vBest = 0                                             # Θ(1)       (G)
    for v in range(0,Vtot+1):                             # Vtot*Θ(1)+Θ(1)
        if opt[n][v] <= costTotMax:                       # Θ(1)
            vBest = v                                     # Θ(1)
    S = []                                                # Θ(1)       (H)
    v = vBest                                             # Θ(1)
    for i in range(n,0,-1):                               # n*Θ(1)+Θ(1)
        if opt[i][v] != opt[i-1][v]:                      # Θ(1)
            S.append(i-1)                                 # Θ(1)
            v -= V[i-1]                                   # Θ(1)
    S.reverse()                                           # Θ(n)
    t1 = time.perf_counter()                              # Θ(1)
    deltaT = t1 - t0                                      # Θ(1)
    return [objects[j] for j in S], deltaT                # Θ(n)

# Costo Computazionale: T(n,Vtot) = Θ(n)+Θ(n*Vtot)+Θ(Vtot)+Θ(n)
#                       T(n,Vtot) = Θ(n*Vtot) = O(n^2*vmax)  (Vtot <= n*vmax)

def Knapsack_Approx(costTotMax,objects,eps):              # T(n)
    objs = copy.deepcopy(objects)                         # Θ(n)       (I)
    eps = Fraction(eps).limit_denominator(10**9)          # Θ(1)       (J)
    objsAccepted = []                                     # Θ(1) 
    for i in range(len(objs)):                            # Θ(n)       (K)
        if objs[i].cost <= costTotMax:                    # Θ(1)
            objsAccepted.append(objs[i])                  # Θ(1)
    if objsAccepted == []:                                # Θ(1)
        return []                                         # Θ(1)
    vmax = 0                                              # Θ(1)
    for i in range(len(objsAccepted)):                    # Θ(n)       (L)
        if vmax < objsAccepted[i].value:                  # Θ(1)
            vmax = objsAccepted[i].value                  # Θ(1)
    if vmax == 0:                                         # Θ(1)
        return []                                         # Θ(1)
    n = len(objsAccepted)                                 # Θ(1)
    b = eps*vmax/(2*n)                                    # Θ(1)       (M)
    Vs = []                                               # Θ(1)
    Ps = []                                               # Θ(1)
    for o in objsAccepted:                                # Θ(n)       (N)
        Vs.append(math.ceil(Fraction(o.value)/b))         # Θ(1)
        Ps.append(o.cost)                                 # Θ(1)
    S = Knapsack_Exact(costTotMax,objsAccepted,Vs,Ps)     # O(n^3/ε)   (O)
    return S                                              # Θ(n)       (P)

# Costo Computazionale: T(n) = Θ(n)+O(n^2*ceil(2n/ε))
#                       T(n) = O(n^3/ε)

# Commenti
# (A): n e' il numero di oggetti. V e P sono le liste parallele dei valori e dei
#      costi, passate dal chiamante nello stesso ordine di objects: V[i] e' il
#      valore e P[i] il costo dell'oggetto i. Sono interi non negativi.
#      objects serve solo a restituire gli oggetti selezionati.
#      costTotMax e' il limite di costo C.
# (B): Vtot e' la somma dei valori: il valore di un sottoinsieme non puo' 
#      superarlo. Vale Vtot <= n*vmax, da cui la complessita' O(n^2*vmax).
# (C): Tabella (n+1) x (Vtot+1): opt[i][v] = costo minimo per ottenere valore
#      esattamente v con i primi i oggetti, infinito se impossibile.
# (D): Caso base: con zero oggetti l'unico valore ottenibile e' 0, a costo 0.
# (E): Caso 1: l'oggetto i-1 non viene preso, si eredita la riga precedente.
# (F): Caso 2: l'oggetto i-1 viene preso: costo minimo per ottenere v-V[i-1]
#      con i primi i-1 oggetti piu' il costo dell'oggetto. Si tiene il minore.
# (G): Il valore ottimo e' il massimo v per cui il costo minimo non supera
#      costTotMax.
# (H): Ricostruzione: si risale da i=n a i=1. Se opt[i][v] e' diverso da 
#      opt[i-1][v], l'oggetto i-1 e' stato preso e il valore residuo scende
#      di V[i-1]. Gli indici trovati diventano gli OGGETTI selezionati: la
#      funzione restituisce gli oggetti di objects (gli stessi, non copie),
#      nell'ordine in cui compaiono.
# (I): Copia profonda degli oggetti: la funzione non altera quelli dell'utente.
# (J): ε e' portato a frazione esatta (0 < ε <= 1): l'arrotondamento per 
#      eccesso di value/b con un float puo' sbagliare quando il quoziente e' 
#      esattamente intero.
# (K): Si scartano le copie con costo > costTotMax: non possono mai entrare.
#      Serve perche' la dimostrazione usa che l'oggetto di valore massimo, da
#      solo, sia ammissibile. Se non resta nessun oggetto la soluzione e' vuota.
# (L): Primo calcolo di vmax sugli oggetti ammissibili. Se vale 0 tutti i
#      valori sono nulli: la soluzione vuota e' ottima e si evita la divisione
#      per zero nel calcolo di b.
# (M): Si calcola il fattore b = eps*vmax/(2n) con cui scalare i valori degli
#      oggetti.
# (N): Si costruiscono le due liste per l'algoritmo esatto: Vs[i] = ceil(value/b)
#      (scalamento per eccesso: v <= scalato*b <= v+b; il valore massimo
#      scalato e' ceil(2n/eps), indipendente da vmax) e Ps[i] = cost. Gli
#      oggetti non vengono modificati: i valori scalati esistono solo in Vs.
# (O): Si applica l'algoritmo esatto: objsAccepted (per ottenere gli oggetti
#      selezionati) e le liste Vs e Ps. Costo O(n*Vtot_scalato) = O(n^3/ε).
# (P): Knapsack_Exact restituisce gli oggetti selezionati di objsAccepted, cioe'
#      copie degli originali (uguali per ==) con valore e costo ORIGINALI: si
#      possono sommare direttamente per ottenere valore reale e costo totale.



" ESEMPI ********************************************************************"


'Esempio Libreria ------------------------------------------------------------'
'''
Valore degli Oggetti -> Punteggio di Importanza/Interesse da 1 a 10
Costo degli Oggetti  -> Spessore Libro
Costo Totale Massimo -> Larghezza Scaffale (75cm)
''' 
catalogo = [   # (nome, acronimo categoria, spessore in cm)
    ("Introduction to Algorithms, 3rd ed. (Cormen et al.)", "IT", 6),
    ("A Common-Sense Guide to Data Structures and Algorithms (Wengrow)", 
     "IT", 3),
    ("Artificial Intelligence: A Modern Approach, 3rd ed. (Russell, Norvig)", 
     "IT", 6),
    ("Struttura e progetto dei calcolatori (Patterson, Hennessy)", "IT", 3),
    ("The Computational Beauty of Nature (Flake)", "IT", 3),
    ("CODE, 2nd ed. (Petzold)", "IT", 3),
    ("Cracking the Coding Interview, 6th ed. (McDowell)", "IT", 4),
    ("Artificial Intelligence for Dummies (Mueller, Massaron)", "IT", 3),
    ("Lingua Latina – Familia Romana (Ørberg)", "LL", 3),
    ("Lingua Latina – Roma Aeterna (Ørberg)", "LL", 3),
    ("Lingua Latina – Exercitia Latina I", "LL", 2),
    ("Lingua Latina – Exercitia Latina II", "LL", 2),
    ("The Domus Aurea Book", "SR", 4),
    ("Cesare (Vaglio)", "SR", 3),
    ("Nerone (Fini)", "SR", 2),
    ("Storia di Roma (Eutropio)", "SR", 4),
    ("Domus Avrea", "SR", 2),
    ("L'arte culinaria (Apicio)", "SR", 3),
    ("Head First Design Patterns (Freeman, Freeman)", "IP", 4),
    ("The C++ Programming Language, 4th ed. (Stroustrup)", "IP", 5),
    ("Game Programming in C++ (Madhav)", "IP", 3),
    ("Programming in Visual Basic 2010 (Bradley, Millspaugh)", "IP", 3),
    ("Introduction to Software Testing (Ammann, Offutt)", "IP", 3),
    ("Unreal Engine 4 Virtual Reality Projects (Mack, Ruud)", "IP", 4),
    ("Professional Visual Studio 2017 (Johnson)", "IP", 5),
    ("Unreal Engine 4 for Design Visualization (Shannon)", "IP", 2),
    ("Korolev (Harford)", "R" , 4),
    ("Muay Thai Boran – Tecniche Avanzate (De Cesaris)", "R" , 2),
    ("Special Ops Fitness Training (De Lisle)", "R" , 3),
    ("The 3D Printing Handbook (Redwood et al.)", "R" , 3)
]

categorie = {
    "IT": {"nome": "Informatica Teorica", "valore": 10},
    "LL": {"nome": "Lingua Latina",       "valore": 8},
    "SR": {"nome": "Storia Romana",       "valore": 6},
    "IP": {"nome": "Informatica Pratica", "valore": 4},
    "R" : {"nome": "Resto",               "valore": 2}
}

larghezzaScaffale = 60

       
# ALGORITMO per KNAPSACK PROBLEM ----------------------------------------------

'Lista Oggetti con costo e valore - Esempio Libreria -------------------------'

libri = [Object(nome, categorie[cat]["valore"], spessore) 
         for (nome, cat, spessore) in catalogo]
valori = [lib.value for lib in libri]
costi = [lib.cost for lib in libri]

# Algoritmo Esatto
knapsack_Exact = Knapsack_Exact(larghezzaScaffale,libri,valori,costi)
valoreTot_Exact = sum(o.value for o in knapsack_Exact[0])
costoTot_Exact = sum(o.cost for o in knapsack_Exact[0])

# Algoritmo Approssimato
epsilon01 = 0.10
epsilon02 = 0.50
epsilon03 = 0.75
knapsack_Approx01 = Knapsack_Approx(larghezzaScaffale,libri,epsilon01)
knapsack_Approx02 = Knapsack_Approx(larghezzaScaffale,libri,epsilon02)
knapsack_Approx03 = Knapsack_Approx(larghezzaScaffale,libri,epsilon03)
approssimazioni = [(epsilon01, knapsack_Approx01),
                   (epsilon02, knapsack_Approx02),
                   (epsilon03, knapsack_Approx03)]

print(
    "\n---------------------------------------------------------------------\n"
    f"Knapsack Problem - Libreria (scaffale di {larghezzaScaffale} cm):\n\n"
    "-> Algoritmo Esatto:\n"
    f" - Oggetti Selezionati ({len(knapsack_Exact)}): "
    + ", ".join(o.name for o in knapsack_Exact[0]) + "\n"
    f" - Valore Totale: {valoreTot_Exact}\n"
    f" - Costo Totale: {costoTot_Exact} cm\n"
    f" - Tempo di Esecuzione: " + str(round(knapsack_Exact[1]* 1000, 3)) + 
    " ms" + "\n"
)

for eps, sol in approssimazioni:
    valoreTot = sum(o.value for o in sol[0])
    costoTot = sum(o.cost for o in sol[0])
    tempoTot = round(sol[1] * 1000, 3)
    print(
        f"-> Algoritmo di Approssimazione (epsilon = {eps}):\n"
        f" - Oggetti Selezionati ({len(sol)}): "
        + ", ".join(o.name for o in sol[0]) + "\n"
        f" - Valore Totale: {valoreTot}\n"
        f" - Costo Totale: {costoTot} cm\n"
        f" - Rapporto di Approssimazione R = OTT/A = "
        f"{valoreTot_Exact}/{valoreTot} = {valoreTot_Exact/valoreTot:.4f} "
        f"(<= 1+eps = {1+eps})\n"+ 
        f" - Tempo di Esecuzione: {tempoTot} ms" + "\n"
    )

