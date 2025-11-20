

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 2 22:10:30 2023

@author: giorg
"""

'Import main libraries'
import math as math
import numpy as np
import time

import matplotlib.pyplot as plt


# IMPORT PACKAGE CLASSES
from Modified_Stack import Stack 
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
root=nodi[0]
tree=AlberoBinario(root)





# ESERCIZIO 1 ################################################################

'''
Scrivere the pseudocodice ITERATIVO of the Visita in PREORDINE.
'''

# Considerations
'''The PREORDER Traversal is INHERENTLY RECURSIVE.
To make it ITERATIVE, analogously to what was seen for level-order traversal, 
we need a Supporting Data Structure (a truly brilliant idea!) 
that takes and returns the references to the tree nodes in the desired 
order.
Utilizzeremo the PILA (QUEUE).
''' 

# Risoluzione
'function AUSILIARIA for Controllo RiempimentoPila'
def isPilaVuota(stack):
 if stack==None:
 return None
 if stack.length()==0: 
 return True
 return False


'function of VISITA in PREORDINE through ITERAZIONE'
def visitaInPreOrdineIter(p): #T(n)
 # 1. Controllo Input
 if p==None: #Θ(1) 
 return #Θ(1) 
 # 2. Inizializzazione stack of supporto
 stack=Stack() #Θ(1) 
 # 3. Impilamento of the root dell'tree
 stack.push(p) #Θ(1) 
 # 4. Impilamento/Spilamento nodi tree...
 while(not isPilaVuota(stack)): #n*Θ(1)+Θ(1) 
 p=stack.pop() #Θ(1) 
 print(p,end=" ") #Θ(1) 
 psx=p.getFiglioSx() #Θ(1) 
 pdx=p.getFiglioDx() #Θ(1) 
 if pdx!=None: #Θ(1) 
 stack.push(pdx) #Θ(1) 
 if psx!=None: #Θ(1) 
 stack.push(psx) #Θ(1) 
 return #Θ(1) 

# Computational Cost
# Dimension Input: number dei nodi dell'tree (incognito to priori)
# T(n)=Θ(1)+n*Θ(1)+Θ(1)=Θ(n)


'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
print("Visita in PreOrdine Iterativa - Array ~ T(n)=Θ(n)")
visitaInPreOrdineIter(tree.getRoot())




 
# ESERCIZIO 2 ################################################################

'''
calculate the computational cost of the visite when l'tree venga 
stored through rappresentazione POSIZIONALE (usare the function TrovaFigli)
'''

# Considerazioni
'''L'tree is a struttura data nodale estremamente efficiente and versatile.
The sua storazione as vector posizionale prevede the scrittura, all'inner
of a array, of all the values dei suoi nodi from the root to the leaves and from 
sinistra verso destra procedendo verso the basso to partire from the root.
The sua storazione through vector dei padri prevede the realizzazione of two
vectors paralleli R and P. R containing all the values of all the nodi and P 
containing l'index del padre of ciascun element corrispondente dell'tree.
''' 


'function Search Lineare'
def linearSearch(To,v): # S(n)
 the=0 # Θ(1)
 while((the<len(To))and(To[the]!=v)): # n*Θ(1)+Θ(1)
 the+=1 # Θ(1)
 if (the<len(To)): # Θ(1)
 return the # Θ(1)
 else: # Θ(1)
 return -1 # Θ(1)

# Computational Cost: S(n)=Θ(n)


'function Ausiliaria TrovaFigli'
def trovaFigli(Q,v): # V(n)
 the=linearSearch(Q,v) # Ω(1),O(n)
 lq=len(Q) # Θ(n)
 if (2*the+1)<lq: # Θ(1)
 sx=Q[2*the+1] # Θ(1)
 else: # Θ(1)
 sx=None # Θ(1)
 if (2*the+2)<lq: # Θ(1)
 dx=Q[2*the+2] # Θ(1)
 else: # Θ(1)
 dx=None # Θ(1)
 return sx,dx # Θ(1)
 
# Computational Cost: V(n)=Θ(n)


'function of Visita In Preordine'
def visitaInPreOrdineRecurs(Q,v): # T(n)
 if Q==None: # Θ(1)
 return # Θ(1)
 if v!=None: # Θ(1)
 print(v,end=" ") # Θ(1)
 sx,dx=trovaFigli(Q,v) # Θ(m)
 if sx!=None: # Θ(1)
 visitaInPreOrdineRecurs(Q,sx) # T(k)
 if dx!=None: # Θ(1)
 visitaInPreOrdineRecurs(Q,dx) # T(n-k-1)
 return

# Computational Cost: T(n)=T(k)+T(n-k-1)+Θ(m) -> T(n)=Θ(n^2)

'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
Q=vettorePosizionale
print("\nVisita in PreOrdine Ricorsiva - Array ~ T(n)=Θ(n^2)")
visitaInPreOrdineRecurs(Q,Q[0])





# ESERCIZIO 3 ################################################################

'''
Nell'esercizio precedente, if usassimo a auxiliary vector where storare
in fase of pre-processing, the figli of ciascun nodo as diventerebbe the
pseudocodice? Ed the computational cost?
'''

# Considerations
'''In this case we will use, as auxiliary vector, a Hash Table
That is, a data structure consisting of a series of buckets, one for each
node, containing the list of children of the corresponding node.
Access to buckets is immediate and has constant computational cost Θ(1).
In Python, the concrete data structure that represents the data structure
astratta HashTable prende the nome of dict (Dizionario)
''' 


'function Ausiliaria TrovaFigli'
def trovaFigliHash(H,v): # V(n)
 if v!=None: # Θ(1)
 if v.getFiglioSx()!=None: # Θ(1)
 sx=H[v][0] # Θ(1)
 else: # Θ(1) 
 sx=None # Θ(1) 
 if v.getFiglioDx()!=None: # Θ(1) 
 dx=H[v][1] # Θ(1)
 else: # Θ(1) 
 dx=None # Θ(1) 
 return sx,dx # Θ(1) 

# Computational Cost: V(n)=Θ(1)


'function of Visita In Preordine'
def visitaInPreOrdineRecurs(H,v): # T(n)
 if H==None: # Θ(1)
 return # Θ(1)
 if v!=None: # Θ(1)
 print(v,end=" ") # Θ(1)
 sx,dx=trovaFigliHash(H,v) # Θ(1)
 if sx!=None: # Θ(1)
 visitaInPreOrdineRecurs(H,sx) # T(k)
 if dx!=None: # Θ(1)
 visitaInPreOrdineRecurs(H,dx) # T(n-k-1)
 return

# Computational Cost: T(n)=T(k)+T(n-k-1)+Θ(1) -> T(n)=Θ(n)

'TEST 1'
# Risultato atteso: [3,1,8,8,0,4,8,5,5,3,2] 
Q=vettorePosizionale
H=dict()
for the in range(0,math.ceil((len(vettorePosizionale)-2)//2+1),1):
 H[Q[the]]=[Q[2*the+1],Q[2*the+2]]

print("\nVisita in PreOrdine Ricorsiva - HashTable ~ T(n)=Θ(n)")
visitaInPreOrdineRecurs(H,Q[0])