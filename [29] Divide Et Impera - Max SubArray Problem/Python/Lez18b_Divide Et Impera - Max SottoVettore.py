# -*- coding: utf-8 -*-
"""
LEZIONE 18a - DIVIDE ET IMPERA - PROBLEMA del MAX SOTTO-VETTORE

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
        
Di seguito, vediamo la soluzione del Problema delle Massimo Sotto-Vettore in
forma iterativa e ricorsiva.
    - Algoritmo Iterativo in O(n^3)
    - Algoritmo Iterativo in O(n^2)
    - Algoritmo Ricorsivo in O(nlogn)
      
"""


" ALGORITMI *****************************************************************"

# Librerie --------------------------------------------------------------------
import math

# Classi di utilita' ----------------------------------------------------------

# Object

class Object:
    
    # Costruttore
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    # Definizione criterio di ordinanemto per strutture dati ordinabili
    # Metodo equivalente a compareTo(...)
    def __lt__(self, altro):
        if self.value != altro.value:
            return self.value < altro.value
    def __le__(self, altro):
            return self.value <= altro.value
        
    # Definizione criterio di uguaglianza per ricerca in strutture dati
    # Metodo equivalente a equals(...)
    def __eq__(self, altro):
        return (self.name == altro.name and self.value == altro.value)
    
    # Conversione istanza di classe in stringa
    # Metodo equivalente a ToString()
    def __str__(self):
        return f"{self.name} ({self.value})"


# =================== ALGORITMO del MAX SOTTO-VETTORE ========================


# ALGORITMO ITERATIVO in O(n^3)
# ----------------------------------------------------------------------------
''' 
L'algoritmo ricava il massimo sotto-vettore considerando le somme di tutti i
possibili sotto-vettori e andando a prenderne il massimo.'
'''

def maxSubArray_Iter01(A):                     # T(n)
    sumMax = 0                                 # Θ(1)
    i_max, j_max = 0, -1                       # Θ(1)
    n = len(A)                                 # Θ(n)              (A)
    for i in range(0,n):                       # n*Θ(1)+Θ(1)
        for j in range(i,n):                   # (n-i)*Θ(1)+Θ(1)
            sumij= 0                           # Θ(1)
            for k in range(i,j+1):             # (j-i+1)*Θ(1)+Θ(1)
                sumij= sumij + A[k].value      # Θ(1)
            if sumij> sumMax:                  # Θ(1)
                sumMax = sumij                 # Θ(1)
                i_max = i                      # Θ(1)
                j_max = j                      # Θ(1)
    return sumMax, A[i_max:j_max+1]            # Θ(1)

# Costo Computazionale: T(n) = Θ(1)+n*[(n-i)*Θ(j-i)] = Θ(n^3)
#   T(n) = Σ_{i=0}^{n-1} Σ_{j=i}^{n-1} Θ(j-i+1) = Θ(n(n+1)(n+2)/6) = Θ(n^3)

# Commenti
# (A): Teoricamente il calcolo della lunghezza di un vettore o di una lista
#      ha costo Θ(n) ma, in Python, l'oggetto lista conserva la sua lunghezza
#      corrente salvata in un attributo specifico che viene restituito usando
#      len(). Quindi il costo e' in realta' Θ(1).


# ALGORITMO ITERATIVO in O(n^2)
# ----------------------------------------------------------------------------
''' 
L'algoritmo ricava il massimo sotto-vettore sfruttando il fatto che la somma
di un sotto-vettore [i...j] e' uguale alla somma del sottovettore [i...j-1] +
A[j].'
'''

def maxSubArray_Iter02(A):                     # T(n)
    sumMax = 0                                 # Θ(1)
    i_max, j_max = 0, -1                       # Θ(1)
    n = len(A)                                 # Θ(n)
    for i in range(0,n):                       # n*Θ(1)+Θ(1)
        sumij = 0                              # Θ(1)
        for j in range(i,n):                   # (n-i)*Θ(1)+Θ(1)
            sumij = sumij + A[j].value         # Θ(1)
            if sumij > sumMax:                 # Θ(1)
                sumMax = sumij                 # Θ(1)
                i_max = i                      # Θ(1)
                j_max = j                      # Θ(1)
    return sumMax, A[i_max:j_max+1]            # Θ(1)

# Costo Computazionale: T(n) = Θ(1)+n*[(n-i)*Θ(1)] = Θ(n^2)
#   T(n) = Σ_{i=0}^{n-1} Σ_{j=i}^{n-1} Θ(1) =Θ((n-1)*(n-1))-Θ((n-1)*n/2)=Θ(n^2)    


# ALGORITMO RICORSIVO in O(nlogn)
# ----------------------------------------------------------------------------
''' 
L'algoritmo ricava il massimo sotto-vettore sfruttando il fatto che un
sottovettore di somma massima e' tale che il suo prefisso (parte nella prima
meta' del vettore) ha somma massima tra quelle di tutti i prefissi e il suo
suffisso (parte nella seconda meta' del vettore) ha somma massima tra quelle
di tutti i suffissi.
Basta quindi calcolare la somma massima dei prefissi e quella dei suffissi.
La somma delle due sara' la somma massima tra tutti i sottovettori a cavallo.'
'''

def maxSubArray_Recur02(a, b, A):                     # T(n)
    if a == b:                                        # Θ(1)            (A)
        if A[a].value > 0:                            # Θ(1)
            return A[a].value, [A[a]]                 # Θ(1)
        else:                                         # Θ(1)
            return 0, []                              # Θ(1)
    m = (a+b)//2                                      # Θ(1)            (B)
    max1 = maxSubArray_Recur02(a, m, A)               # T(n/2)          (C)
    max2 = maxSubArray_Recur02(m+1, b, A)             # T(n/2)          (D)
    prefix = 0                                        # Θ(1)            (E)
    i_pf, j_sf = m+1, m                               # Θ(1)
    sumMax = 0                                        # Θ(1)
    for i in range(m,a-1,-1):                         # n/2*Θ(1)+Θ(1)
        sumMax = sumMax + A[i].value                  # Θ(1)
        if sumMax > prefix:                           # Θ(1)
            prefix = sumMax                           # Θ(1)
            i_pf = i                                  # Θ(1)
    suffix = 0                                        # Θ(1)            (F)
    sumMax = 0                                        # Θ(1)
    for i in range(m+1, b+1):                         # n/2*Θ(1)+Θ(1)
        sumMax = sumMax + A[i].value                  # Θ(1)
        if sumMax > suffix:                           # Θ(1)
            suffix = sumMax                           # Θ(1)
            j_sf = i                                  # Θ(1)
    m = max(max1[0], max2[0], prefix + suffix)        # Θ(1)            (G)
    if m == max1[0]:                                  # Θ(1)            (H)
        maxSubArray = max1[1]                         # Θ(n)
    elif m == max2[0]:                                # Θ(1)
        maxSubArray = max2[1]                         # Θ(n)
    else:                                             # Θ(1)
        maxSubArray = A[i_pf:j_sf+1]                  # Θ(n)
    return m, maxSubArray                             # Θ(1)

# Costo Computazionale: T(n) = 2*T(n/2)+O(n) = O(nlogn)
# c = 1 = logb_a = log2_2 -> 2o caso del Teorema Master

# Commenti
# (A): Caso base corrispondente al sottovettore di dimensione unitaria (a=b)
#      Per il caso base, ovvero sottovettore costituito da una sola cella,
#      si ritorna il valore stesso contenuto in essa. Questo, essendo l'unico
#      valore contenuto nel sottovettore rappresenta quindi anche la somma
#      massima calcolata su di esso.
# (B): Si calcola l'indice di valore medio tra a e b che serve per spezzare
#      il vettore a meta'.
# (C): 1o Passo Ricorsivo con cui si chiama la funzione sul sotto-vettore
#      sinistro (prefisso) per calcolarne la somma massima.
# (D): 2o Passo Ricorsivo con cui si chiama la funzione sul sotto-vettore
#      destro (suffisso) per calcolarne la somma massima.
# (E): Si calcola la somma massima del prefisso (meta' sinistra del vettore)
#      calcolando la somma dei valori di tutte le celle prese una ad una e 
#      aggiornando il valore massimo solo quando esso viene superato.
#      In tal modo, qualsiasi sia il sotto-vettore corrispondente alla somma
#      massima, il valore salvato nella variabile prefix sara' la somma massima 
#      possibile all'interno del prefisso.
# (F): Si calcola la somma massima del suffisso (meta' destra del vettore)
#      calcolando la somma dei valori di tutte le celle prese una ad una e 
#      aggiornando il valore massimo solo quando esso viene superato.
#      In tal modo, qualsiasi sia il sotto-vettore corrispondente alla somma
#      massima, il valore salvato nella variabile suffix sara' la somma massima
#      possibile all'interno del suffisso.
# (G): Si calcola infine il massimo tra la somma massima del sotto-vettore sx,
#      la somma massima del sotto-vettore dx e la somma massima tra tutti i
#      sotto-vettori a cavallo.
# (H): Estrazione dal vettore originario del sotto-vettore di somma massima
#      utilizzando indici di inizio e di fine diversi a seconda di dove sia
#      stata trovata la somma massima



" ESEMPI *********************************************************************"

'Esempio - Prestazione calciatore --------------------------------------------'
'''
Dato il numero di passaggi riusciti da un calciatore in ognuno dei 18 
intervalli di 5 minuti di una partita (da 0-5 a 85-90) e una soglia di 
riferimento (il numero medio di passaggi riusciti per intervallo), trovare gli 
intervalli consecutivi in cui il calciatore supera di più la soglia, cioè il 
periodo della partita in cui ha giocato meglio. Descrivere un algoritmo divide 
et impera che risolva il problema e valutarne la complessità.

Perché si sottrae la soglia
I passaggi riusciti sono tutti positivi, quindi il sottovettore massimo sarebbe 
l'intera partita. Sottraendo la media, ogni valore diventa il surplus 
(positivo) o il deficit (negativo) di quell'intervallo, e la somma su un tratto 
è il surplus cumulato dei suoi intervalli.
'''

A = [Object("0-5", 3),
     Object("5-10", 4),
     Object("10-15", 8),
     Object("15-20", 11),
     Object("20-25", 9),
     Object("25-30", 5),
     Object("30-35", 10),
     Object("35-40", 8),
     Object("40-45", 4),
     Object("45-50", 3),
     Object("50-55", 2),
     Object("55-60", 7),
     Object("60-65", 9),
     Object("65-70", 6),
     Object("70-75", 4),
     Object("75-80", 3),
     Object("80-85", 7),
     Object("85-90", 5)]

refValue = 6

for obj in A:
    obj.value = obj.value - refValue

# Algoritmo Iterativo in O(n^3)
msaI01 = maxSubArray_Iter01(A)
# Algoritmo Iterativo in O(n^2)
msaI02 = maxSubArray_Iter02(A)
# Algoritmo Ricorsivo in O(nlogn)
a, b = 0, len(A)-1
msaR03 = maxSubArray_Recur02(a, b, A)

print(
    "\n---------------------------------------------------------------------\n"
    "Divide Et Impera - Massimo Sotto-Vettore:\n"
    "Esempio - Prestazione calciatore\n"
    "-> Algoritmo Iterativo in O(n^3):\n"
    " - Somma Massima: " + str(msaI01[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaI01[1])
    + "]\n"
    "-> Algoritmo Iterativo in O(n^2):\n"
    " - Somma Massima: " + str(msaI02[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaI02[1])
    + "]\n"
    "-> Algoritmo Ricorsivo in O(nlogn):\n"
    " - Somma Massima: " + str(msaR03[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaR03[1]) + "]\n"
)



'Esempio - Flusso Visitatori alla Fontana di Trevi ---------------------------'
'''
Dato il flusso orario di visitatori della Fontana di Trevi dalle 6 alle 24 e 
una soglia di affollamento (la capienza sicura), trovare le fasce orarie 
consecutive in cui il flusso supera di più la soglia, cioè dove è necessario 
controllare gli accessi.

Perché si sottrae la soglia
I flussi sono tutti positivi, quindi il sottovettore massimo sarebbe l'intera 
giornata. Sottraendo la capienza, ogni valore diventa l'eccesso (positivo) o il 
margine libero (negativo) di quell'ora, e la somma su un tratto è l'eccesso 
cumulato delle sue ore.
'''

ore = [f"{h}-{h+1}" for h in range(6, 24)]
flusso = [300, 700, 1400, 2300, 3100, 3400, 2600, 1700, 1500,
          2100, 2900, 3500, 4200, 4800, 4300, 3300, 2200, 1200]
capienza = 2500                       # persone/ora (ipotesi)

A = [Object(o, f - capienza) for o, f in zip(ore, flusso)]

# Algoritmo Iterativo in O(n^3)
msaI01 = maxSubArray_Iter01(A)
# Algoritmo Iterativo in O(n^2)
msaI02 = maxSubArray_Iter02(A)
# Algoritmo Ricorsivo in O(nlogn)
a, b = 0, len(A)-1
msaR03 = maxSubArray_Recur02(a, b, A)

print(
    "\n---------------------------------------------------------------------\n"
    "Divide Et Impera - Massimo Sotto-Vettore:\n"
    "Esempio - Flusso Visitatori alla Fontana di Trevi\n"
    "-> Algoritmo Iterativo in O(n^3):\n"
    " - Somma Massima: " + str(msaI01[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaI01[1])
    + "]\n"
    "-> Algoritmo Iterativo in O(n^2):\n"
    " - Somma Massima: " + str(msaI02[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaI02[1])
    + "]\n"
    "-> Algoritmo Ricorsivo in O(nlogn):\n"
    " - Somma Massima: " + str(msaR03[0]) + "\n" +
    " - Massimo Sottovettore: ["
    + ", ".join(str(obj) for obj in msaR03[1]) + "]"
)