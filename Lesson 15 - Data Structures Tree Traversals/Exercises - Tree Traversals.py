

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

for the in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[the])) 
    
for the in range(0,(len(nodi)-2)//2+1,1):
        nodi[the].setFiglioSx(nodi[2*the+1])
        nodi[the].setFiglioDx(nodi[2*the+2])
        
vettorePosizionale=nodi
        
'COSTRUZIONE ALBERO BINARIO'     
radice=nodi[0]
albero=AlberoBinario(radice)





# ESERCIZIO 1 ################################################################

'''
Scrivere the pseudocodice ITERATIVO della Visita in PREORDINE.
'''

# Considerazioni
'''The Visita in PREORDINE e' INERENTEMENTE RICORSIVA.
For renderla ITERATIVA, analogamente to quanto visto for the visite for livelli, 
abbiamo bisogno of a Struttura Data of Appoggio (a'idea davvero geniale!) 
that prenda e restituisca the riferimenti ai nodi dell'albero nell'ordine 
desiderato.
Utilizzeremo the PILA (QUEUE).
''' 

# Risoluzione
'function AUSILIARIA for Controllo RiempimentoPila'
def isPilaVuota(pila):
    if pila==None:
        return None
    if pila.length()==0: 
        return True
    return False


'function of VISITA in PREORDINE through ITERAZIONE'
def visitaInPreOrdineIter(p):                                     #T(n)
    # 1. Controllo Input
    if p==None:                                                   #Θ(1) 
        return                                                    #Θ(1) 
    # 2. Inizializzazione pila of supporto
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
# Dimensione Input: number dei nodi dell'albero (incognito to priori)
# T(n)=Θ(1)+n*Θ(1)+Θ(1)=Θ(n)


'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
print("Visita in PreOrdine Iterativa - Array ~ T(n)=Θ(n)")
visitaInPreOrdineIter(albero.getRoot())




    
# ESERCIZIO 2 ################################################################

'''
calculate the computational cost delle visite quando l'albero venga 
stored through rappresentazione POSIZIONALE (usare the function TrovaFigli)
'''

# Considerazioni
'''L'albero e' a struttura data nodale estremamente efficiente e versatile.
The sua storazione as vector posizionale prevede the scrittura, all'interno
of a array, of all the values dei suoi nodi dalla radice alle foglie e from 
sinistra verso destra procedendo verso the basso to partire dalla radice.
The sua storazione through vector dei padri prevede the realizzazione of two
vettori paralleli R e P. R containing all the values of all the nodi e P 
containing l'index del padre of ciascun element corrispondente dell'albero.
''' 


'function Ricerca Lineare'
def linearSearch(To,v):                   # S(n)
    the=0                                  # Θ(1)
    while((the<len(To))and(To[the]!=v)):       # n*Θ(1)+Θ(1)
        the+=1                             # Θ(1)
    if (the<len(To)):                       # Θ(1)
        return the                         # Θ(1)
    else:                                # Θ(1)
        return -1                        # Θ(1)

# Computational Cost: S(n)=Θ(n)


'function Ausiliaria TrovaFigli'
def trovaFigli(Q,v):                     # V(n)
    the=linearSearch(Q,v)                  # Ω(1),O(n)
    lq=len(Q)                            # Θ(n)
    if (2*the+1)<lq:                       # Θ(1)
        sx=Q[2*the+1]                      # Θ(1)
    else:                                # Θ(1)
        sx=None                          # Θ(1)
    if (2*the+2)<lq:                       # Θ(1)
        dx=Q[2*the+2]                      # Θ(1)
    else:                                # Θ(1)
        dx=None                          # Θ(1)
    return sx,dx                         # Θ(1)
    
# Computational Cost: V(n)=Θ(n)


'function of Visita In Preordine'
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
Nell'esercizio precedente, if usassimo a auxiliary vector in cui storare
in fase of pre-processing, the figli of ciascun nodo as diventerebbe the
pseudocodice? Ed the costo computazionale?
'''

# Considerazioni
'''In this case we will use, as auxiliary vector, a Hash Table
Ovvero a struttura data costituita from a serie of buckets, one for ciascun
nodo, contenenti the lista dei figli del nodo corrispondente.
L'accesso ai buckets e' immediato e ha costo computazionale costante Θ(1).
In Python, the struttura data concreta that rappresenta the struttura data
astratta HashTable prende the nome of dict (Dizionario)
''' 


'function Ausiliaria TrovaFigli'
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


'function of Visita In Preordine'
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
for the in range(0,math.ceil((len(vettorePosizionale)-2)//2+1),1):
    H[Q[the]]=[Q[2*the+1],Q[2*the+2]]

print("\nVisita in PreOrdine Ricorsiva - HashTable ~ T(n)=Θ(n)")
visitaInPreOrdineRecurs(H,Q[0])