# -*- coding: utf-8 -*-
"""
LEZIONE 10 - ALGORITMI GREEDY - Parte 01

Gli Algoritmi Greedy sono una specifica categoria di algoritmi che costruiscono
la soluzione del problema computazionale accrescendo gradualmente soluzioni
parziali selezionando sempre e solo la piu' conveniente ad ogni step.
I due algoritmi greedy classici sono l'Algoritmo di Selezione delle Attivita' (
Activity Selection) e l'Algoritmo di Partizionamento delle Attivita' (Internal
Partitioning).
    
Algoritmo di Selezione delle Attivita' - ACTIVITY SELECTION
    - Formulazione classica con vettore - O(nlogn)
    - Esempio Problema Files su Disco

"""


" ALGORITMI *****************************************************************"


# Librerie --------------------------------------------------------------------

import math
from collections import deque
from decimal import Decimal
from datetime import time

from MergeSort import mergeSort
from QuickSort import quickSort
from HeapSort import heapSort


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
    
    
class File:
    
    # Constructor
    def __init__(self, name, size_MB):
        self.name = name
        self.size_MB = size_MB
        
    # Method defining Sorting Criteria in Sortable Data Structures
    # Method equivalent to compareTo(...)
    def __lt__(self, other):
        if self.size_MB != other.size_MB:
            return self.size_MB < other.size_MB
        
    # Method defining Equality Criteria in Data Structures
    # Method equivalent to equals(...)
    def __eq__(self, other):
        return (self.name == other.name and
                self.size_MB == other.size_MB)
    
    # Method converting the Class Instance into a String
    # Method equivalent to ToString()
    def __str__(self):
        return f"{self.name} ({self.size_MB})"
        
    

# ================= ALGORITMO di SELEZIONE delle ATTIVITA' ====================


# ACTIVITY SELECTION - CLASSICO con VETTORE
# ------------------------------------------------------------------------
def activitySelection(activities):                          # T(n)
    mergeSort(activities,0,len(activities)-1)               # Θ(nlogn)    (A)
    sol = []                                                # Θ(1)
    endTime = time(0,0)                                     # Θ(1)        (B)
    for i in range(len(activities)):                        # n*Θ(1)+Θ(1) (C)
        if activities[i].startTime >= endTime:              # Θ(1)
            sol.append(activities[i])                       # Θ(1)
            endTime = activities[i].endTime                 # Θ(1)
    return sol                                              # Θ(1)

# Commenti
# (A): Le attivita' vengono ordinate per ordine crescente del tempo di 
#      FINE utilizzando l'algoritmo di ordinamento MergeSort - tipico
#      algoritmo di ordinamento efficiente basato sui confronti.
# (B): Inizializzazione del vettore soluzione (contenente in ordine temporale
#      la selezione di attivita' ottimale) e del tempo di conclusione dell'
#      ultima attivita' selezionata.
# (C): Si scorrono le attivita' secondo l'ordine crescente del loro tempo di
#      conclusione. Se il tempo di inizio dell'attivita' e' maggiore del tempo 
#      finale della precedente attivita' selezionata (endTime), l'attivita'
#      viene aggiunta al vettore soluzione e il tempo finale della precedente
#      attivita' selezionata (endTime) viene aggiornato.

# Costo Computazionale: Θ(nlogn) - CASO PEGGIORE & MIGLIORE


# ACTIVITY SELECTION - ESEMPIO PROBLEMA FILES SU DISCO
# ------------------------------------------------------------------------
def filesOnDisc(files,diskSize):                            # T(n)
    heapSort(files)                                         # Θ(nlogn)    (A)
    sol = []                                                # Θ(1)        (B)
    capacity = diskSize                                     # Θ(1)
    i = 0                                                   # Θ(1)
    while capacity>=files[i].size_MB:                       # O(n)+Θ(1)
        sol.append(files[i])                                # Θ(1)
        capacity -= files[i].size_MB                        # Θ(1)
        i += 1                                              # Θ(1)
    return sol                                              # Θ(1)

# Commenti
# (A): I files vengono ordinati per ordine crescente dello spazio di memoria
#      utilizzando l'algoritmo di ordinamento HeapSort - altro tipico algoritmo
#      di ordinamento efficiente basato sui confronti.
# (B): Inizializzazione del vettore soluzione (contenente in ordine di 
#      dimensione la selezione di files ottimale), della capacita' residua sul 
#      disco e del contatore i usato per scorrere.
# (C): Si scorrono i files secondo l'ordine crescente della loro dimensione. 
#      Se la capacita' residua del disco e' maggiore della dimensione del file,
#      il file viene selezionato ed aggiunto al vettore soluzione.
#      La capacita' residua del disco viene quindi aggiornata e si passa a
#      considerare il file successivo.
#      Il ciclo termina una volta che la capacita' residua del disco non e' piu
#      in grado di ospitare il file dell'iterazione successiva.

# Costo Computazionale: Θ(nlogn) - CASO PEGGIORE & MIGLIORE




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
Caso 04 -> attivita': files
           risorse: capacita' di memoria del disco'

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

'Case 04a - Files on Disc'
files01 = [File("MausoleumOfAugustus.3dm", 22.1),
           File("Annexe Building.3dm", 14.2),
           File("The Pantheon.3dm", 22.4),
           File("Classes Diagram.draw.io", 3.2),
           File("3DMeshes.json", 37.5),
           File("StressResults.json", 49.1),
           File("SummaryReport.xlsx", 5.6)]

'Case 04b - Files on Disc'
files02 = [File("Adobe.ico", 0.0107), File("Alibaba.ico", 0.0551),
           File("Amazon.ico", 0.2000), File("American Express.ico", 0.1451),
           File("Anaconda.ico", 0.0041), File("Angular.ico", 0.2579),
           File("Apple.ico", 0.2579), File("Application.ico", 0.2296),
           File("Axios.ico", 0.0041), File("BH.ico", 0.2538),
           File("BHoM.ico", 0.0041), File("BinaryFile.ico", 0.1728),
           File("BOOTSTRAP.ico", 0.0041), File("BoxFightWin.ico", 0.0041),
           File("C#.ico", 0.0041), File("C++.ico", 0.0041),
           File("CHI.ico", 0.0041), File("CoinBase.ico", 0.0338),
           File("Command Line.ico", 0.0041), File("Compiled Lang.ico", 0.2354),
           File("Connection.ico", 0.2488), File("Copilot.ico", 0.0041),
           File("CSS.ico", 0.0041), File("CSV.ico", 0.0041),
           File("Danger Sign.ico", 0.2579), File("Database.ico", 0.0041), 
           File("Database_Table.ico", 0.2579), File("Database_v2.ico", 0.2296),
           File("Docker.ico", 0.0041), File("Docker Container.ico", 0.1723),
           File("Docker Pipeline.ico", 0.0181), 
           File("Documentation.ico", 0.2579), File("DropBox.ico", 0.2579),
           File("e2k.ico", 0.2071), File("ETABS.ico", 0.0041)]


# ALGORITMO GREEDY di SELEZIONE delle ATTIVITA' -------------------------------

print("\nSELEZIONE ATTIVITA' tramite ALGORITMO GREEDY ***********************"+
      "****************************************************************"+"\n")

'Case 01 - Computer Science Lessons ------------------------------------------'
                       
print("Case 01 - Computer Science Lessons")
print("--------------------------------------------------")
print("Vettore lezioni non ordinato:")
print(*activities01, sep="\n")

as01 = activitySelection(activities01)
print("--------------------------------------------------")
print("Vettore lezioni ordinato:")
print(*activities01, sep="\n")
print("--------------------------------------------------")
print("Vettore lezioni selezionate:")
print(*as01, sep="\n")
print("\n\n")


'Case 02 - Daily Activities in Thailand --------------------------------------'
                      
print("Case 02 - Daily Activities in Thailand")
print("--------------------------------------------------")
print("Vettore attivita' non ordinato:")
print(*activities02, sep="\n")

as02 = activitySelection(activities02)
print("--------------------------------------------------")
print("Vettore attivita' ordinato:")
print(*activities02, sep="\n")
print("--------------------------------------------------")
print("Vettore attivita' selezionate:")
print(*as02, sep="\n")
print("\n\n")


'Case 03 - Requested Landing Slots -------------------------------------------'                        

print("Case 03 - Requested Landing Slots")
print("--------------------------------------------------")
print("Vettore sessioni di atterraggio non ordinato:")
print(*activities03, sep="\n")

as03 = activitySelection(activities03)
print("--------------------------------------------------")
print("Vettore sessioni di atterraggio ordinato:")
print(*activities03, sep="\n")
print("--------------------------------------------------")
print("Vettore sessioni di atterraggio selezionate:")
print(*as03, sep="\n")
print("\n\n")


'Case 04a - Files on Disc ----------------------------------------------------'                        

print("Case 04a - Files on Disc")
print("--------------------------------------------------")
print("Vettore files non ordinato:")
print(*files01, sep="\n")

fc01 = filesOnDisc(files01, 100)
print("--------------------------------------------------")
print("Vettore files ordinato:")
print(*files01, sep="\n")
print("--------------------------------------------------")
print("Vettore files selezionati:")
print(*fc01, sep="\n")
print("\n\n")


'Case 04b - Files on Disc ----------------------------------------------------'                        

print("Case 04b - Files on Disc")
print("--------------------------------------------------")
print("Vettore files non ordinato:")
print(*files02, sep="\n")

fc02 = filesOnDisc(files02, 1.0)
print("--------------------------------------------------")
print("Vettore files ordinato:")
print(*files02, sep="\n")
print("--------------------------------------------------")
print("Vettore files selezionati:")
print(*fc02, sep="\n")
print("\n\n")
