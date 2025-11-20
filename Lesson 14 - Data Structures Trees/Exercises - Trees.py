

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
Design an algorithm that, given to albero binario stored through vector
dei padri, restituisca the vector relativo alla rappresentazione posizionale
dello stesso albero. calculate the computational cost.
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



'function AUSILIARIA for Ricerca indices'
def trovaIndici(array,el):              # S(n)
    indici=[]                           # Θ(1)
    for the in range(0,len(array),1):     # n*Θ(1)+Θ(1)
        if array[the]==el:                # Θ(1)
            indici.append(the)            # Θ(1)
    if len(indici)==0:                  # Θ(1)
        return None                     # Θ(1)
    return indici                       # Θ(1)

# Computational Cost
# Dimensione Input: number elements in the array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'function PRINCIPALE for conversione Vector'
'dei Padri in Vector Posizionale'
def convertiAPosizionale(R,P,Q=None,the=None,j=[0]):                #T(n)
    
    'CASO INIZIALE'
    # Inizializzatione del Vector Posizionale
    if the==None:                                                   #Θ(1)                       
        maxLength=2**(math.floor(math.log(len(R),2))+1)-1         #Θ(1)
        Q=[None]*maxLength                                        #Θ(1)
        
    'CASO BASE'
    # If l'indice del node not e' contained in the vector dei padri,
    # vuol dire that esso not ha figli ed e' quindi a foglia.
    if P.count(the)==0:                                             #Θ(n)
        return Q                                                  #Θ(1)
    
    'CODICE PASSO'
    # Si ricavano the indici dei figli nel Vector dei padri, li si 
    # scorrono in a for loop e for ciascuno of essi si estrae the value del
    # figlio from R, the si inserisce in Q e si richiama the function
    # ricorsivamente on of esso.
    indici=trovaIndici(P,the)                                       #Θ(n)
    for n in range(0,len(indici),1):                              #k*Θ(1)+Θ(1)
        figlio=R[indici[n]]                                       #Θ(1)
        Q[j[n]]=figlio                                            #Θ(1)
        'PASSO RICORSIVO'                                        
        convertiAPosizionale(R,P,Q,indici[n],[2*j[n]+1,2*j[n]+2]) #T(n/2) 
    return Q

# Computational Cost
# Input size = number elements nel vector dei padri
# T(n)=Θ(1)+Θ(n)+Θ(n)+2*(Θ(1)+T(n/2))  - where k=2 nel worst case (2 figli)
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
Design an algorithm that, given to albero binario stored through 
rappresentazione posizionale, restituisca the vector dei padri dello stesso
albero. calculate the computational cost.
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


'function AUSILIARIA for Calcolo number Nodi'
def numeroNodi(array,nullValue=None):   # S(n)
    numNodi=0                           # Θ(1)
    for el in array:                    # n*Θ(1)+Θ(1)
        if el!=nullValue:               # Θ(1)
            numNodi+=1                  # Θ(1)
    return numNodi                      # Θ(1)

# Computational Cost
# Dimensione Input: number elements in the array
# S(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)



'function PRINCIPALE for conversione Vector Posizionale to Vector dei Padri'
def convertiAPadri(Q,R=None, P=None):                         #T(n)
    
    # Inizializzatione del Vector dei Padri (vettori P e R)   
    'Si scorre the vector posizionale e si contano the caselle aventi value' 
    'not nullo. Tale number definira the dimensione del vector dei padri'                   
    R=[None]*numeroNodi(Q,None)                               #Θ(n)
    P=[None]*len(R)                                           #Θ(1)
    
    # Inizializzazione Vector of Supporto for Indici dei Padri
    'Ha the stessa lunghezza del vector posizionale e immagazzina the indici'
    'dei padri sia dei nodi presenti that dei nodi assenti.'
    Ptemp=[None]*len(Q)                                       #Θ(1)
    
    # Calcolo indices dei padri of ciascun element del vector posizionale
    'Valendo the regola of 2*the+1 e 2*the+2, the sara uguale to floor((the-1)/2)'
    for the in range(0,len(Q),1):                               #n*Θ(1)+Θ(1)
        j=math.floor((the-1)/2)                                 #Θ(1)
        Ptemp[the]=j                                            #Θ(1)
    
    # Costruzione Vector dei Padri
    'Scorriamo the vector posizionale Q e where troviamo a element NON nullo'
    'andiamo to inserire the suo value e lindice del padre corrispondente all'
    'interno dei vettori R e P rispettivamente'
    j=0                                                       #Θ(1)
    for the in range(0,len(Q),1):                               #n*Θ(1)+Θ(1)
        if Q[the]!=None:                                        #Θ(1)
            R[j]=Q[the]                                         #Θ(1)
            P[j]=Ptemp[the]                                     #Θ(1)
            j+=1                                              #Θ(1)

    return R,P                                                #Θ(1)

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