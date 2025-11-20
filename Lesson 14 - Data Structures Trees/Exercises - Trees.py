

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





'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Design an algorithm that, given to tree binario stored through vector
dei padri, restituisca the vector relativo to the rappresentazione posizionale
of the same tree. calculate the computational cost.
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



'function AUSILIARIA for Search indices'
def trovaIndici(array,el): # S(n)
 indices=[] # Θ(1)
 for the in range(0,len(array),1): # n*Θ(1)+Θ(1)
 if array[the]==el: # Θ(1)
 indices.append(the) # Θ(1)
 if len(indices)==0: # Θ(1)
 return None # Θ(1)
 return indices # Θ(1)

# Computational Cost
# Dimension Input: number elements in the array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'function PRINCIPALE for conversione Vector'
'dei Padri in Vector Posizionale'
def convertiAPosizionale(R,P,Q=None,the=None,j=[0]): #T(n)
 
 'CASO INIZIALE'
 # Inizializzatione del Vector Posizionale
 if the==None: #Θ(1) 
 maxLength=2**(math.floor(math.log(len(R),2))+1)-1 #Θ(1)
 Q=[None]*maxLength #Θ(1)
 
 'CASO BASE'
 # If l'index del node not is contained in the vector dei padri,
 # vuol dire that esso not ha figli ed is therefore a foglia.
 if P.count(the)==0: #Θ(n)
 return Q #Θ(1)
 
 'CODICE PASSO'
 # Si ricavano the indices dei figli nel Vector dei padri, li si 
 # scorrono in a for loop and for ciascuno of essi si estrae the value del
 # figlio from R, the si inserisce in Q and si richiama the function
 # ricorsivamente on of esso.
 indices=trovaIndici(P,the) #Θ(n)
 for n in range(0,len(indices),1): #k*Θ(1)+Θ(1)
 figlio=R[indices[n]] #Θ(1)
 Q[j[n]]=figlio #Θ(1)
 'PASSO RICORSIVO' 
 convertiAPosizionale(R,P,Q,indices[n],[2*j[n]+1,2*j[n]+2]) #T(n/2) 
 return Q

# Computational Cost
# Input size = number elements nel vector dei padri
# T(n)=Θ(1)+Θ(n)+Θ(n)+2*(Θ(1)+T(n/2)) - where k=2 nel worst case (2 figli)
# T(n)=2*T(n/2)+Θ(n) -> T(n)=Θ(n*logn) [through Metodo Principale]


'TEST 1'
R=['To','B','C','D','E','F','G','H','I','L','M','N','P','Q']
P=[None,0,1,2,2,1,5,5,0,8,9,9,8,12] 
Q=convertiAPosizionale(R,P) 


'TEST 2'
R=['Beam','Building','Capping Beam','Column','Core','Foundation','Frame',
 'Piled Wall','Raft','Retaining Wall','Spandrel','Substructure',
 'Superstructure','Wall']
P=[6,None,9,6,12,11,12,9,5,11,4,1,1,4]
Q=convertiAPosizionale(R, P)



 
# ESERCIZIO 2 ################################################################

'''
Design an algorithm that, given to tree binario stored through 
rappresentazione posizionale, restituisca the vector dei padri of the same
tree. calculate the computational cost.
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


'AUXILIARY function for Calculating number of Nodes'
def numeroNodi(array,nullValue=None): # S(n)
 numNodi=0 # Θ(1)
 for el in array: # n*Θ(1)+Θ(1)
 if el!=nullValue: # Θ(1)
 numNodi+=1 # Θ(1)
 return numNodi # Θ(1)

# Computational Cost
# Dimension Input: number elements in the array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'MAIN function for converting Positional Vector to Parent Vector'
def convertiAPadri(Q,R=None, P=None): #T(n)
 
 # Initialization of Parent Vector (vectors P and R) 
 'Scan the positional vector and count the cells having non-null value' 
 'This number will define the size of the parent vector' 
 R=[None]*numeroNodi(Q,None) #Θ(n)
 P=[None]*len(R) #Θ(1)
 
 # Inizializzazione Vector of Supporto for Indices dei Padri
 'Ha the same lunghezza del vector posizionale and immagazzina the indices'
 'dei padri sia dei nodi presenti that dei nodi assenti.'
 Ptemp=[None]*len(Q) #Θ(1)
 
 # Calcolo indices dei padri of ciascun element del vector posizionale
 'Valendo the rule of 2*the+1 and 2*the+2, the sara uguale to floor((the-1)/2)'
 for the in range(0,len(Q),1): #n*Θ(1)+Θ(1)
 j=math.floor((the-1)/2) #Θ(1)
 Ptemp[the]=j #Θ(1)
 
 # Costruzione Vector dei Padri
 'Scorriamo the vector posizionale Q and where troviamo a element NON nullo'
 'andiamo to inserire the suo value and lindice del padre corrispondente all'
 'inner dei vectors R and P rispettivamente'
 j=0 #Θ(1)
 for the in range(0,len(Q),1): #n*Θ(1)+Θ(1)
 if Q[the]!=None: #Θ(1)
 R[j]=Q[the] #Θ(1)
 P[j]=Ptemp[the] #Θ(1)
 j+=1 #Θ(1)

 return R,P #Θ(1)

# Computational Cost
# Input size = number elements nel Vector Posizionale
# T(n)=Θ(1)+Θ(n)+Θ(1)+Θ(n)+Θ(1) -> T(n)=Θ(n)


'TEST 1'
Q=['To', 'B', 'I', 'C', 'F', 'L', 'P', 'D', 'E', 'G', 'H', 'M', 'N', 'Q', None]
R,P=convertiAPadri(Q) 


'TEST 2'
Q=['Building', 'Substructure', 'Superstructure', 'Foundation', 
 'Retaining Wall', 'Core', 'Frame', 'Raft', None, 'Capping Beam', 
 'Piled Wall', 'Spandrel', 'Wall', 'Beam', 'Column']
R,P=convertiAPadri(Q) 