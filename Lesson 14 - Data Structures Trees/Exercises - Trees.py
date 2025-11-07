

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





'''
TUTTI GLI ALTRI ESERCIZI CHE NON COMPAIONO QUI SONO RIPORTATI FRA GLI 
ESERCIZI SVOLTI SU CARTA '''


# ESERCIZIO 1 ################################################################

'''
Progettare un algoritmo che, dato un albero binario memorizzato tramite vettore
dei padri, restituisca il vettore relativo alla rappresentazione posizionale
dello stesso albero. Calcolare il costo computazionale.
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



'Funzione AUSILIARIA per Ricerca Indici'
def trovaIndici(array,el):              # S(n)
    indici=[]                           # Θ(1)
    for i in range(0,len(array),1):     # n*Θ(1)+Θ(1)
        if array[i]==el:                # Θ(1)
            indici.append(i)            # Θ(1)
    if len(indici)==0:                  # Θ(1)
        return None                     # Θ(1)
    return indici                       # Θ(1)

# Computational Cost
# Dimensione Input: numero elementi nell'array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'Funzione PRINCIPALE per conversione Vettore'
'dei Padri in Vettore Posizionale'
def convertiAPosizionale(R,P,Q=None,i=None,j=[0]):                #T(n)
    
    'CASO INIZIALE'
    # Inizializzatione del Vettore Posizionale
    if i==None:                                                   #Θ(1)                       
        maxLength=2**(math.floor(math.log(len(R),2))+1)-1         #Θ(1)
        Q=[None]*maxLength                                        #Θ(1)
        
    'CASO BASE'
    # Se l'indice del node non e' contenuto nel vettore dei padri,
    # vuol dire che esso non ha figli ed e' quindi una foglia.
    if P.count(i)==0:                                             #Θ(n)
        return Q                                                  #Θ(1)
    
    'CODICE PASSO'
    # Si ricavano gli indici dei figli nel Vettore dei padri, li si 
    # scorrono in un for loop e per ciascuno di essi si estrae il valore del
    # figlio da R, lo si inserisce in Q e si richiama la funzione
    # ricorsivamente su di esso.
    indici=trovaIndici(P,i)                                       #Θ(n)
    for n in range(0,len(indici),1):                              #k*Θ(1)+Θ(1)
        figlio=R[indici[n]]                                       #Θ(1)
        Q[j[n]]=figlio                                            #Θ(1)
        'PASSO RICORSIVO'                                        
        convertiAPosizionale(R,P,Q,indici[n],[2*j[n]+1,2*j[n]+2]) #T(n/2) 
    return Q

# Computational Cost
# Input size = numero elementi nel vettore dei padri
# T(n)=Θ(1)+Θ(n)+Θ(n)+2*(Θ(1)+T(n/2))  - dove k=2 nel caso peggiore (2 figli)
# T(n)=2*T(n/2)+Θ(n) -> T(n)=Θ(n*logn) [tramite Metodo Principale]


'TEST 1'
R=['A','B','C','D','E','F','G','H','I','L','M','N','P','Q']
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
Progettare un algoritmo che, dato un albero binario memorizzato tramite 
rappresentazione posizionale, restituisca il vettore dei padri dello stesso
albero. Calcolare il costo computazionale.
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


'Funzione AUSILIARIA per Calcolo Numero Nodi'
def numeroNodi(array,nullValue=None):   # S(n)
    numNodi=0                           # Θ(1)
    for el in array:                    # n*Θ(1)+Θ(1)
        if el!=nullValue:               # Θ(1)
            numNodi+=1                  # Θ(1)
    return numNodi                      # Θ(1)

# Computational Cost
# Dimensione Input: numero elementi nell'array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'Funzione PRINCIPALE per conversione Vettore Posizionale a Vettore dei Padri'
def convertiAPadri(Q,R=None, P=None):                         #T(n)
    
    # Inizializzatione del Vettore dei Padri (vettori P e R)   
    'Si scorre il vettore posizionale e si contano le caselle aventi valore' 
    'non nullo. Tale numero definira la dimensione del vettore dei padri'                   
    R=[None]*numeroNodi(Q,None)                               #Θ(n)
    P=[None]*len(R)                                           #Θ(1)
    
    # Inizializzazione Vettore di Supporto per Indici dei Padri
    'Ha la stessa lunghezza del vettore posizionale e immagazzina gli indici'
    'dei padri sia dei nodi presenti che dei nodi assenti.'
    Ptemp=[None]*len(Q)                                       #Θ(1)
    
    # Calcolo indici dei padri di ciascun elemento del vettore posizionale
    'Valendo la regola di 2*i+1 e 2*i+2, i sara uguale a floor((i-1)/2)'
    for i in range(0,len(Q),1):                               #n*Θ(1)+Θ(1)
        j=math.floor((i-1)/2)                                 #Θ(1)
        Ptemp[i]=j                                            #Θ(1)
    
    # Costruzione Vettore dei Padri
    'Scorriamo il vettore posizionale Q e dove troviamo un elemento NON nullo'
    'andiamo a inserire il suo valore e lindice del padre corrispondente all'
    'interno dei vettori R e P rispettivamente'
    j=0                                                       #Θ(1)
    for i in range(0,len(Q),1):                               #n*Θ(1)+Θ(1)
        if Q[i]!=None:                                        #Θ(1)
            R[j]=Q[i]                                         #Θ(1)
            P[j]=Ptemp[i]                                     #Θ(1)
            j+=1                                              #Θ(1)

    return R,P                                                #Θ(1)

# Computational Cost
# Input size = numero elementi nel Vettore Posizionale
# T(n)=Θ(1)+Θ(n)+Θ(1)+Θ(n)+Θ(1) -> T(n)=Θ(n)


'TEST 1'
Q=['A', 'B', 'I', 'C', 'F', 'L', 'P', 'D', 'E', 'G', 'H', 'M', 'N', 'Q', None]
R,P=convertiAPadri(Q)    


'TEST 2'
Q=['Building', 'Substructure', 'Superstructure', 'Foundation', 
   'Retaining Wall', 'Core', 'Frame', 'Raft', None, 'Capping Beam', 
   'Piled Wall', 'Spandrel', 'Wall', 'Beam', 'Column']
R,P=convertiAPadri(Q) 