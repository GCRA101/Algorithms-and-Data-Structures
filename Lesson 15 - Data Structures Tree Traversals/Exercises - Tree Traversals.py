

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:10:30 2023

@author: giorg
"""

'Import main libraries'
import math as math
import numpy as np
import time

import matplotlib.pyplot as plt


# IMPORT PACKAGE CLASSES
from Modified_Stack import Pila 
from BinaryNode import Nodo
from BinaryTree import AlberoBinario




'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


'''
PREPARAZIONE ALBERO
'''

'COSTRUZIONE ARRAY DI RECORDS DOPPI'
valoriNodi=[3,1,5,8,4,3,2,8,0,8,5]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,(len(nodi)-2)//2+1,1):
        nodi[i].setFiglioSx(nodi[2*i+1])
        nodi[i].setFiglioDx(nodi[2*i+2])
        
vettorePosizionale=nodi
        
'COSTRUZIONE ALBERO BINARIO'     
radice=nodi[0]
albero=AlberoBinario(radice)





# ESERCIZIO 1 ################################################################

'''
Scrivere lo pseudocodice ITERATIVO della Visita in PREORDINE.
'''

# Considerazioni
'''La Visita in PREORDINE e' INERENTEMENTE RICORSIVA.
Per renderla ITERATIVA, analogamente a quanto visto per le visite per livelli, 
abbiamo bisogno di una Struttura Dati di Appoggio (un'idea davvero geniale!) 
che prenda e restituisca i riferimenti ai nodi dell'albero nell'ordine 
desiderato.
Utilizzeremo la PILA (QUEUE).
''' 

# Risoluzione
'Funzione AUSILIARIA per Controllo RiempimentoPila'
def isPilaVuota(pila):
    if pila==None:
        return None
    if pila.length()==0: 
        return True
    return False


'Funzione di VISITA in PREORDINE tramite ITERAZIONE'
def visitaInPreOrdineIter(p):                                     #T(n)
    # 1. Controllo Input
    if p==None:                                                   #Θ(1) 
        return                                                    #Θ(1) 
    # 2. Inizializzazione pila di supporto
    pila=Pila()                                                   #Θ(1) 
    # 3. Impilamento della radice dell'albero
    pila.push(p)                                                  #Θ(1) 
    # 4. Impilamento/Spilamento nodi albero...
    while(not isPilaVuota(pila)):                                 #n*Θ(1)+Θ(1)  
        p=pila.pop()                                              #Θ(1) 
        print(p,end=" ")                                          #Θ(1) 
        psx=p.getFiglioSx()                                       #Θ(1) 
        pdx=p.getFiglioDx()                                       #Θ(1) 
        if pdx!=None:                                             #Θ(1)  
            pila.push(pdx)                                        #Θ(1) 
        if psx!=None:                                             #Θ(1) 
            pila.push(psx)                                        #Θ(1) 
    return                                                        #Θ(1) 

# Computational Cost
# Dimensione Input: numero dei nodi dell'albero (incognito a priori)
# T(n)=Θ(1)+n*Θ(1)+Θ(1)=Θ(n)


'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
print("Visita in PreOrdine Iterativa - Array ~ T(n)=Θ(n)")
visitaInPreOrdineIter(albero.getRoot())




    
# ESERCIZIO 2 ################################################################

'''
Calcolare il costo computazionale delle visite quando l'albero venga 
memorizzato tramite rappresentazione POSIZIONALE (usare la funzione TrovaFigli)
'''

# Considerazioni
'''L'albero e' una struttura dati nodale estremamente efficiente e versatile.
La sua memorizzazione come vettore posizionale prevede la scrittura, all'interno
di un array, di tutti i valori dei suoi nodi dalla radice alle foglie e da 
sinistra verso destra procedendo verso il basso a partire dalla radice.
La sua memorizzazione tramite vettore dei padri prevede la realizzazione di due
vettori paralleli R e P. R contenente tutti i valori di tutti i nodi e P 
contenente l'indice del padre di ciascun elemento corrispondente dell'albero.
''' 


'Funzione Ricerca Lineare'
def linearSearch(A,v):                   # S(n)
    i=0                                  # Θ(1)
    while((i<len(A))and(A[i]!=v)):       # n*Θ(1)+Θ(1)
        i+=1                             # Θ(1)
    if (i<len(A)):                       # Θ(1)
        return i                         # Θ(1)
    else:                                # Θ(1)
        return -1                        # Θ(1)

# Computational Cost: S(n)=Θ(n)


'Funzione Ausiliaria TrovaFigli'
def trovaFigli(Q,v):                     # V(n)
    i=linearSearch(Q,v)                  # Ω(1),O(n)
    lq=len(Q)                            # Θ(n)
    if (2*i+1)<lq:                       # Θ(1)
        sx=Q[2*i+1]                      # Θ(1)
    else:                                # Θ(1)
        sx=None                          # Θ(1)
    if (2*i+2)<lq:                       # Θ(1)
        dx=Q[2*i+2]                      # Θ(1)
    else:                                # Θ(1)
        dx=None                          # Θ(1)
    return sx,dx                         # Θ(1)
    
# Computational Cost: V(n)=Θ(n)


'Funzione di Visita In Preordine'
def visitaInPreOrdineRecurs(Q,v):            # T(n)
    if Q==None:                              # Θ(1)
        return                               # Θ(1)
    if v!=None:                              # Θ(1)
        print(v,end=" ")                     # Θ(1)
        sx,dx=trovaFigli(Q,v)                # Θ(m)
        if sx!=None:                         # Θ(1)
            visitaInPreOrdineRecurs(Q,sx)    # T(k)
        if dx!=None:                         # Θ(1)
            visitaInPreOrdineRecurs(Q,dx)    # T(n-k-1)
    return

# Computational Cost: T(n)=T(k)+T(n-k-1)+Θ(m)  -> T(n)=Θ(n^2)

'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
Q=vettorePosizionale
print("\nVisita in PreOrdine Ricorsiva - Array ~ T(n)=Θ(n^2)")
visitaInPreOrdineRecurs(Q,Q[0])





# ESERCIZIO 3 ################################################################

'''
Nell'esercizio precedente, se usassimo un vettore ausiliario in cui memorizzare
in fase di pre-processing, i figli di ciascun nodo come diventerebbe lo
pseudocodice? Ed il costo computazionale?
'''

# Considerazioni
'''In questo caso andremo a utilizzare, come vettore ausiliario, una Hash Table
Ovvero una struttura dati costituita da una serie di buckets, uno per ciascun
nodo, contenenti la lista dei figli del nodo corrispondente.
L'accesso ai buckets e' immediato e ha costo computazionale costante Θ(1).
In Python, la struttura dati concreta che rappresenta la struttura dati
astratta HashTable prende il nome di dict (Dizionario)
''' 


'Funzione Ausiliaria TrovaFigli'
def trovaFigliHash(H,v):                     # V(n)
    if v!=None:                              # Θ(1)
        if v.getFiglioSx()!=None:            # Θ(1)
            sx=H[v][0]                       # Θ(1)
        else:                                # Θ(1)                        
            sx=None                          # Θ(1)                        
        if v.getFiglioDx()!=None:            # Θ(1)                        
            dx=H[v][1]                       # Θ(1)
        else:                                # Θ(1)                        
            dx=None                          # Θ(1)                                                 
    return sx,dx                             # Θ(1)                        

# Computational Cost: V(n)=Θ(1)


'Funzione di Visita In Preordine'
def visitaInPreOrdineRecurs(H,v):            # T(n)
    if H==None:                              # Θ(1)
        return                               # Θ(1)
    if v!=None:                              # Θ(1)
        print(v,end=" ")                     # Θ(1)
        sx,dx=trovaFigliHash(H,v)            # Θ(1)
        if sx!=None:                         # Θ(1)
            visitaInPreOrdineRecurs(H,sx)    # T(k)
        if dx!=None:                         # Θ(1)
            visitaInPreOrdineRecurs(H,dx)    # T(n-k-1)
    return

# Computational Cost: T(n)=T(k)+T(n-k-1)+Θ(1)  -> T(n)=Θ(n)

'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
Q=vettorePosizionale
H=dict()
for i in range(0,math.ceil((len(vettorePosizionale)-2)//2+1),1):
    H[Q[i]]=[Q[2*i+1],Q[2*i+2]]

print("\nVisita in PreOrdine Ricorsiva - HashTable ~ T(n)=Θ(n)")
visitaInPreOrdineRecurs(H,Q[0])