# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:48:46 2023
@author: giorg
"""

'Import main libraries'
import numpy as np
import math as math
import time
import matplotlib.pyplot as plt
import random


# IMPORT CLASSI DEL PACKAGE
from NodoBinarioDiRicerca import Nodo
from AlberoBinarioDiRicerca import AlberoBinarioDiRicerca


'''
PREPARAZIONE ALBERO
'''

valoriNodi=[18,11,33,7,15,22,80,13,16,50,91,42,64]
indiciPadri=[None,0,0,1,1,2,2,4,4,6,6,9,9]
nodi=[]
vettorePosizionale=[]

for i in range(0,len(valoriNodi),1):
    nodi.append(Nodo(valoriNodi[i])) 
    
for i in range(0,len(nodi),1):
    if indiciPadri[i]==None:
        nodi[i].setParent(None)
    else:
        nodi[i].setParent(nodi[indiciPadri[i]])
    k=0
    for j in range(0,len(indiciPadri),1):
        if indiciPadri[j]==i:
            if k==0:
                nodi[i].setLeft(nodi[j])
                k+=1
            else:
                nodi[i].setRight(nodi[j])
                break
         
radice=nodi[0]
albero=AlberoBinarioDiRicerca(radice)



'''
OPERAZIONI ******************************************************************
'''


'RICERCA'

# Data una chiave k e un albero p in input, la funzione ritorna il nodo
# dell'albero avente chiave con valore uguale a k.

def ABR_searchRic(p,k):                         # T(h)
    if (p==None or p.getKey()==k):              # Θ(1)
        return p                                # Θ(1)
    if (k<p.getKey()):                          # Θ(1)
        return ABR_searchRic(p.getLeft(),k)     # T(h-1)
    else:                                       # Θ(1)
        return ABR_searchRic(p.getRight(),k)    # T(h-1)

# Costo Computazionale
# Dimensione dell'input: Altezza h dell'albero
# Si esegue la funzione h volte con operazioni ogni volta di costo costante
# Θ(1). Quindi il costo totale equivale a h volte Θ(1).
# Costo: T(h)= T(h-1)+Θ(1) -> T(h)=Θ(h)



'INSERIMENTO'

# Dato l'albero p e dato il nodo z in input, la funzione ritorna l'albero con
# il nodo aggiuntivo inserito nella posizione appropriata.

def ABR_insert(p,z):                             # T(h)
    '1. INIZIALIZZAZIONE Puntatori ausiliari'
    # Padre Nodo Corrente
    y=None                                       # Θ(1)
    # Nodo corrente
    x=p                                          # Θ(1)
    '2. DISCESA fino a Nodo con Figlio Nullo'
    while x!=None:                               # h*Θ(1)+Θ(1)
        # Aggiorna y eguagliandolo a x...
        y=x                                      # Θ(1)
        # Aggiorna x facendolo scendere a dx/sx in base alla sua chiave...
        if z.getKey()<x.getKey():                # Θ(1)
            x=x.getLeft()                        # Θ(1)
        else:                                    # Θ(1)
            x=x.getRight()                       # Θ(1)
    '3. AGGIUNTA Nuovo Nodo'
    # Se l'Albero e' Nullo, usa Nuovo Nodo come Radice dell'Albero...
    if y==None:                                  # Θ(1)
        p=z                                      # Θ(1)
    # Se l'Albero non e' nullo, aggiungi il Nuovo Nodo a dx/sx dell'ultimo...
    else:                                        # Θ(1)
        if z.getKey()<y.getKey():                # Θ(1)
            y.left=z                             # Θ(1)
        else:                                    # Θ(1)
            y.right=z                            # Θ(1)
    # Aggiorna il campo Padre del nuovo nodo aggiunto all'albero...
    z.setParent(y)                               # Θ(1)
    # Restituisci l'albero modificato...
    return p                                     # Θ(1)

# Costo Computazionale
# Dimensione dell'input: Altezza h dell'albero
# Costo: T(h)= Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'MINIMO'

# Restituisce il nodo avente chiave di valore minimo all'interno 
# dell'albero passato in input.

# Ricorsivo
def minimoRecurs(p):                             # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    if p.getLeft()==None:                        # Θ(1)
        return p                                 # Θ(1)
    return minimoRecurs(p.getLeft())             # T(h-1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def minimoIter(p):                               # T(h)
    if p==None:                                  # Θ(1)
        return                                   # Θ(1)
    while p.getLeft()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getLeft()                            # Θ(1)
    return p                                     # Θ(1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'MASSIMO'

# Restituisce il nodo avente chiave di valore massimo all'interno 
# dell'albero passato in input.

# Ricorsivo
def massimoRecurs(p):                             # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    if p.getRight()==None:                        # Θ(1)
        return p                                  # Θ(1)
    return massimoRecurs(p.getRight())            # T(h-1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+T(h-1) -> T(h)=Θ(h)


# Iterativo
def massimoIter(p):                               # T(h)
    if p==None:                                   # Θ(1)
        return                                    # Θ(1)
    while p.getRight()!=None:                     # h*Θ(1)+Θ(1)
        p=p.getRight()                            # Θ(1)
    return p                                      # Θ(1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo: T(h)=Θ(1)+h*Θ(1) -> T(h)=Θ(h)



'PREDECESSORE'

# Restituisce il nodo avente chiave il cui valore sarebbe immediatamente 
# precedente a quello passato in input se i nodi dell'albero venissero ordinati
# in ordine crescente in base al valore della loro chiave.

# Iterativo
def predecessoreIter(p,k):                        # T(h)
    # 1. Ricava il nodo avente chiave uguale a k
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. Se il nodo ha figlio Sx cerca il massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoIter(nodo.getLeft())   # Ω(1) o O(h)
    else:                                         # Θ(1)
    # 4. Se il nodo NON ha figlio Sx, risali l'albero     
    #    tramite ITERAZIONE    
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getLeft()):  # Θ(1)
            nodo=nodo.getParent()                 # Θ(1)
        predecessor=nodo.getParent()              # Θ(1)
    return predecessor                            # Θ(1)

# Ricorsivo
def predecessoreRecurs(p,k):                      # T(h)
    # 1. Ricava il nodo avente chiave uguale a k    
    nodo=ABR_searchRic(p, k)                      # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                # Θ(1)
        return None                               # Θ(1)
    # 3. Se il nodo ha figlio Sx cerca il massimo nel
    #    suo sottoalbero Sx
    if nodo.getLeft()!=None:                      # Θ(1)
        predecessor=massimoRecurs(nodo.getLeft()) # Ω(1) o O(h)     
    else:                                         # Θ(1)
    # 4. Se il nodo NON ha figlio Sx, risali l'albero
    #    tramite RICORSIONE
        return predecRecurs(nodo)                 # S(h)
    return predecessor                            # Θ(1)

def predecRecurs(nodo):                           # S(h)
    # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
    #    quindi ritorna la radice.
    if nodo.getParent()==None:                    # Θ(1)
        return nodo                               # Θ(1)
    # 2. Se il nodo non coincide con il figlio Sx di suo padre,
    #    restituisci il nodo...
    if nodo!=nodo.getParent().getLeft():          # Θ(1)
        return nodo.getParent()                   # Θ(1)
    # 3. Se il nodo coincide con il figlio Sx di suo padre, 
    #    continua la risalita passando il nodo padre nella nuova 
    #    chiamata ricorsiva.
    return predecRecurs(nodo.getParent())         # S(h-1)   

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  



'SUCCESSORE'

# Restituisce il nodo avente chiave il cui valore sarebbe immediatamente 
# successivo a quello passato in input se i nodi dell'albero venissero ordinati
# in ordine crescente in base al valore della loro chiave.

# Iterativo
def successoreIter(p, k):                          # T(h)
    # 1. Ricava il nodo avente chiave uguale a k
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. Se il nodo ha figlio Dx cerca il minimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoIter(nodo.getRight())      # Ω(1) o O(h)
    else:        
    # 4. Se il nodo NON ha figlio Dx, risali l'albero     
    #    tramite ITERAZIONE
        while(nodo.getParent()!=None and 
              nodo==nodo.getParent().getRight()):  # Θ(1)
            nodo=nodo.getParent()                  # Θ(1)
        successor=nodo.getParent()                 # Θ(1)
    return successor                               # Θ(1)

# Ricorsivo
def successoreRecurs(p,k):                         # T(h)
    # 1. Ricava il nodo avente chiave uguale a k    
    nodo=ABR_searchRic(p, k)                       # Θ(h)
    # 2. Se il nodo non esiste, restituisci valore nullo
    if nodo==None:                                 # Θ(1)
        return None                                # Θ(1)
    # 3. Se il nodo ha figlio Dx cerca il massimo nel
    #    suo sottoalbero Dx
    if nodo.getRight()!=None:                      # Θ(1)
        successor=minimoRecurs(nodo.getRight())    # Ω(1) o O(h)
    else:                                          # Θ(1)
    # 4. Se il nodo NON ha figlio Dx, risali l'albero
    #    tramite RICORSIONE
        return succesRecurs(nodo)                  # S(h)
    return successor                               # Θ(1)

def succesRecurs(nodo):                            # S(h)
    # 1. Se il nodo non ha padre, esso e' la radice dell'albero...
    #    quindi ritorna la radice.
    if nodo.getParent()==None:                     # Θ(1)
        return nodo                                # Θ(1) 
    # 2. Se il nodo non coincide con il figlio Dx di suo padre,
    #    restituisci il nodo...
    if nodo!=nodo.getParent().getRight():          # Θ(1)
        return nodo.getParent()                    # Θ(1)
    # 3. Se il nodo coincide con il figlio Dx di suo padre, 
    #    continua la risalita passando il nodo padre nella nuova 
    #    chiamata ricorsiva.
    return succesRecurs(nodo.getParent())          # S(h-1)     

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo Iterativa: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) -> T(h)=Ω(1) o O(h)  
# Costo Ricorsiva: T(h)=Θ(h) + Θ(1) + Ω(1) o O(h) + S(h) -> T(h)=Ω(1) o O(h)  



'CANCELLAZIONE'

# Elimina il nodo dell'albero avente la chiave del valore passato in input.
# Il nodo eliminato viene sostituito con il suo predecessore o successore (
# uno o l'altro e' lo stesso..il risultato e' il medesimo) in modo da evitare
# la disconnessione dell'albero in due sottoalberi separati.
# Per ottenere cio' ci sono 3 casi differenti:
# Caso 1) Il nodo da eliminare NON HA FIGLI
#           - Si assegna valore nullo al campo figlio dx/sx corrispondente del
#             nodo padre.
# Caso 2) Il nodo da eliminare HA 1 SOLO FIGLIO
#            - Si collega il padre del nodo con il suo unico figlio, 
#              indipendentemente che questo sia destro o sinistro.
# Caso 3) Il nodo da eliminare HA 2 FIGLI
#            - Si sostituisce nel nodo da elimninare la chiave del suo 
#              successore/predecessore e si cancella quindi questultimo.


def cancellaFoglia(p,nodo):                                      # T(h)
    # Aggiorna il campo figlio (Dx/Sx) del padre 
    # corrispondente alla foglia da cancellare.
    if (nodo==nodo.getParent().getLeft()):                       # Θ(1)
        nodo.getParent().setLeft(None)                           # Θ(1)
    else:                                                        # Θ(1)
        nodo.getParent().setRight(None)                          # Θ(1)
    return                                                       # Θ(1)
    


def cancella(p,k):                                               # T(h)
    # Estrai nodo avente valore chiave uguale a k
    nodo=ABR_searchRic(p, k)                                     # Ω(1) o O(h)
    # Se il nodo non esiste chiudi la funzione
    if nodo==None:                                               # Θ(1)
        return                                                   # Θ(1)
    # CASO 1 - Il Nodo NON HA FIGLI
    # Cancella il nodo aggiornando il corrispondente campo figlio
    # del nodo padre.
    if (nodo.getLeft()==None and nodo.getRight()==None):         # Θ(1)
       cancellaFoglia(p,nodo)                                    # Θ(1)
       
    # CASO 2 - Il Nodo HA 1 FIGLIO
    # Cortocircuita il padre con il figlio del nodo da eliminare
    # Se l'unico figlio e' quello Sx...
    if (nodo.getLeft()!=None and nodo.getRight()==None):         # Θ(1)
        # Assegna il padre del nodo al figlio Sx
        nodo.getLeft().setParent(nodo.getParent())               # Θ(1)
        # Assegna il figlio Sx al padre del nodo
        if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
            nodo.getParent().setLeft(nodo.getLeft())             # Θ(1)
        else:                                                    # Θ(1)
            nodo.getParent().setRight(nodo.getLeft())            # Θ(1)
    # Se l'unico figlio e' quello Dx...
    if (nodo.getLeft()==None and nodo.getRight()!=None):         # Θ(1)
        # Assegna il padre del nodo al figlio Dx
        nodo.getRight().setParent(nodo.getParent())              # Θ(1)
        # Assegna il figlio Dx al padre del nodo
        if (nodo==nodo.getParent().getLeft()):                   # Θ(1)
            nodo.getParent().setLeft(nodo.getRight())            # Θ(1)
        else:                                                    # Θ(1)
            nodo.getParent().setRight(nodo.getRight())           # Θ(1)
    
    # CASO 3 - Il Nodo HA 2 FIGLI
    # Trova il predecessore/successore del nodo da cancellare, 
    # copia il suo contenuto nel nodo da cancellare e, infine, 
    # cancella il nodo predecessore/successore.
    if (nodo.getLeft()!=None and nodo.getRight()!=None):         # Θ(1)
        # Ricava i nodi predecessore e successore
        pred=predecessoreIter(p,nodo.getKey())                   # Ω(1) o O(h) 
        succes=successoreRecurs(p,nodo.getKey())                 # Ω(1) o O(h) 
        # Sostituisci chiave del nodo e cancella 
        # predecessore/successore
        if pred!=None:                                           # Θ(1)
            nodo.setKey(pred.getKey())                           # Θ(1)
            cancellaFoglia(p,pred)                               # Θ(1)
        else:                                                    # Θ(1)
            nodo.setKey(succes.getKey())                         # Θ(1)
            cancellaFoglia(p,succes)                             # Θ(1)

# Costo Computazionale
# Dimensione input: altezza dell'albero h
# Costo Iterativa: T_caso1(h)=O(h)+Θ(1)=O(h)
#                  T_caso2(h)=O(h)+Θ(1)=O(h)
#                  T_caso3(h)=O(h)+O(h)+Θ(1)=O(h)
# Costo: T(h)=max{T_caso1;T_caso2;T_caso3}=O(h)


# TESTS

'Ricerca'
nodoRicercato=ABR_searchRic(albero.getRoot(),22)
print("RICERCA - Il nodo ricercato e' : " + str(nodoRicercato))

'Inserimento'
z=Nodo(47)
print("\nINSERIMENTO\nAlbero prima dell'inserimento del nodo " + str(z))
albero.visitaPreOrdine()
ABR_insert(albero.getRoot(), z)
print("\nAlbero dopo l'inserimento del nodo " + str(z))
albero.visitaPreOrdine()
print()

'Minimo'
minRec=minimoRecurs(albero.getRoot())
minIter=minimoIter(albero.getRoot())
print("\nMINIMO\nChiave minima nell'albero [RICORSIONE]: " + str(minRec))
print("Chiave minima nell'albero [ITERAZIONE]: " + str(minIter))

'Massimo'
maxRec=massimoRecurs(albero.getRoot())
maxIter=massimoIter(albero.getRoot())
print("\nMASSIMO\nChiave massima nell'albero [RICORSIONE]: " + str(maxRec))
print("Chiave massima nell'albero [ITERAZIONE]: " + str(maxIter))

'Predecessore'
k1=80
k2=13
predIter1=predecessoreIter(albero.getRoot(),k1)  # Iterativo -Caso 1- Discesa
predIter2=predecessoreIter(albero.getRoot(),k2)  # Iterativo -Caso 2- Risalita
predRec1=predecessoreRecurs(albero.getRoot(),k1) # Ricorsivo -Caso 1- Discesa
predRec2=predecessoreRecurs(albero.getRoot(),k2) # Ricorsivo -Caso 2- Risalita
print("\nPREDECESSORE\nPredecessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(predIter1))
print("Predecessore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(predIter2))
print("\nPREDECESSORE\nPredecessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(predRec1))
print("Predecessore Nodo " +  str(k2) + " [RICORSIONE]: " + str(predRec2))

'Successore'
k1=11
k2=16
succIter1=successoreIter(albero.getRoot(),k1)  # Iterativo -Caso 1- Discesa
succIter2=successoreIter(albero.getRoot(),k2)  # Iterativo -Caso 2- Risalita
succRec1=successoreRecurs(albero.getRoot(),k1) # Ricorsivo -Caso 1- Discesa
succRec2=successoreRecurs(albero.getRoot(),k2) # Ricorsivo -Caso 2- Risalita
print("\nSUCCESSORE\nSuccessore Nodo " + str(k1) 
      + " [ITERAZIONE]: " + str(succIter1))
print("Successore Nodo " +  str(k2) + " [ITERAZIONE]: " + str(succIter2))
print("\nSUCCESSORE\nSuccessore Nodo " +  
      str(k1) + " [RICORSIONE]: " + str(succRec1))
print("Successore Nodo " +  str(k2) + " [RICORSIONE]: " + str(succRec2))


'Cancellazione'
k_caso1=7
k_caso3=33
print("\nCANCELLAZIONE - Caso 1 - chiave " + str(k_caso1) + "\nPrima...")
albero.visitaPerLivelli()
print("\nDopo...")
cancella(albero.getRoot(), k_caso1)
albero.visitaPerLivelli()
print("\n\nCANCELLAZIONE - Caso 3 - chiave " + str(k_caso3) + "\nPrima...")
albero.visitaPerLivelli()
print("\nDopo...")
cancella(albero.getRoot(),k_caso3)
albero.visitaPerLivelli()

