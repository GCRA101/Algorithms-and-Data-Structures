# -*- coding: utf-8 -*-
"""
LEZIONE 02 - VISITA di GRAFI in PROFONDITA''

Algoritmi di Visita in Profondita' DFS
    - Con Liste di Adiacenza
    - Con Matrice di Adiacenza

Algoritmi di utilita' tramite uso di DFS
    - Conteggio Componenti Connesse
    
"""


" ALGORITMI *****************************************************************"


# DFS con LISTE di ADIACENZA
def DFS_la(u,G):                                            # T(n)
    def DFSricors(x,G,visitati):                            # S(m)
        visitati[x]=True                                    # Θ(1)
        for y in G[x]:                                      # k*Θ(1)+Θ(1)
            if visitati[y]==False:                          # Θ(1)
                DFSricors(y,G,visitati)                     # S(v)
    
    visitati=[False for v in G]                             # Θ(n)
    DFSricors(u, G, visitati)                               # S(m)
    return visitati                                         # Θ(1)
# Costo Computazionale: O(n+m) - CASO PEGGIORE
#                       Ω(n)   - CASO MIGLIORE                
     
           
                
# DFS con MATRICE di ADIACENZA
def DFS_ma(u,M):                                            # T(n)
    def DFSricors(x,M,visitati):                            # S(n)
        visitati[x]=True                                    # Θ(1)
        for y in range(0,len(M)):                           # n*Θ(1)+Θ(1)
            if M[x][y]==1 and visitati[y]==False:           # Θ(1)
                DFSricors(y,M,visitati)                     # S(v)
    
    visitati=[False for i in range(0,len(M))]               # Θ(n)
    DFSricors(u,M,visitati)
    return visitati                                         # Θ(1)
# Costo Computazionale: O(n^2) - CASO PEGGIORE
#                       Ω(n)   - CASO MIGLIORE      



# CONTEGGIO COMPONENTI CONNESSE
def contCompConnesse(G):
    
    def DFSricors(x,G,CC,c):
        visitati[x]=1
        CC[x]=c
        for y in G[x]:
            if visitati[y]==0: DFSricors(y,G,CC,c)
        
    visitati=[False for v in G]
    CC=[0 for v in G]
    c=0
    for i in range(0,len(visitati)):
        if visitati[i]==0:
            c+=1
            DFSricors(i, G, CC, c)
    return CC

    

" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...

"""

# LISTE DI ADIACENZA

'Grafo Connesso' 
L_gc=[[1,2],
      [2,3,4],
      [1,4],
      [1,2,4],
      []]

'Grafo Non Connesso'
L_gnc=[[1,2],
       [0,2],
       [0,1],
       [4,5],
       [3,5],
       [3,4],
       []]


# MATRICE DI ADIACENZA

'Grafo Connesso'
MM_gc=[[0,1,1,0,0], # Riga di adiacenza del nodo 0
       [0,0,1,1,1], # Riga di adiacenza del nodo 1
       [0,1,0,0,1], # Riga di adiacenza del nodo 2
       [0,1,1,0,1], # Riga di adiacenza del nodo 3
       [0,0,0,0,0]] # Riga di adiacenza del nodo 4

'Grafo Non Connesso'
MM_gnc=[[0,1,1,0,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,0,0,0,0],
        [0,0,0,0,1,1,0],
        [0,0,0,1,0,1,0],
        [0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0]]



# DFS con LISTE di ADIACENZA

'Grafo Connesso'
va0=DFS_la(0,L_gc) # Partendo da 0 si possono visitare tutti i nodi
va1=DFS_la(1,L_gc) # Partendo da 1 si possono visitare tutti i nodi tranne l'1
va2=DFS_la(2,L_gc) # Partendo da 2 si possono visitare tutti i nodi tranne l'1
va3=DFS_la(3,L_gc) # Partendo da 3 si possono visitare tutti i nodi tranne l'1
va4=DFS_la(4,L_gc) # Partendo da 4 si puo' visitare solo il nodo 4

print("DFS con Liste di Adiacenza - Grafo Connesso: "+"\n"+
      "0 -> "+ str(va0)+"\n"+
      "1 -> "+ str(va1)+"\n"+
      "2 -> "+ str(va2)+"\n"+
      "3 -> "+ str(va3)+"\n"+
      "4 -> "+ str(va4)+"\n")

'Grafo Non Connesso'
va0=DFS_la(0,L_gnc) # Partendo da 0 si possono visitare solo i nodi 1,2
va1=DFS_la(1,L_gnc) # Partendo da 1 si possono visitare solo i nodi 0,2
va2=DFS_la(2,L_gnc) # Partendo da 2 si possono visitare solo i nodi 0,1
va3=DFS_la(3,L_gnc) # Partendo da 3 si possono visitare solo i nodi 4,5
va4=DFS_la(4,L_gnc) # Partendo da 4 si possono visitare solo i nodi 3,5
va5=DFS_la(5,L_gnc) # Partendo da 5 si possono visitare solo i nodi 3,4
va6=DFS_la(6,L_gnc) # Partendo da 6 non si puo' visitare alcun nodo

print("DFS con Liste di Adiacenza - Grafo Non Connesso: "+"\n"+
      "0 -> "+ str(va0)+"\n"+
      "1 -> "+ str(va1)+"\n"+
      "2 -> "+ str(va2)+"\n"+
      "3 -> "+ str(va3)+"\n"+
      "4 -> "+ str(va4)+"\n"+
      "5 -> "+ str(va5)+"\n"+
      "6 -> "+ str(va6)+"\n")



# DFS con MATRICE di ADIACENZA

'Grafo Connesso'
vm0=DFS_ma(0,MM_gc) # Partendo da 0 si possono visitare tutti i nodi
vm1=DFS_ma(1,MM_gc) # Partendo da 1 si possono visitare tutti i nodi tranne l'1
vm2=DFS_ma(2,MM_gc) # Partendo da 2 si possono visitare tutti i nodi tranne l'1
vm3=DFS_ma(3,MM_gc) # Partendo da 3 si possono visitare tutti i nodi tranne l'1
vm4=DFS_ma(4,MM_gc) # Partendo da 4 si puo' visitare solo il nodo 4

print("DFS con Matrice di Adiacenza - Grafo Connesso: "+"\n"+
      "0 -> "+ str(vm0)+"\n"+
      "1 -> "+ str(vm1)+"\n"+
      "2 -> "+ str(vm2)+"\n"+
      "3 -> "+ str(vm3)+"\n"+
      "4 -> "+ str(vm4)+"\n")

'Grafo Non Connesso'
vm0=DFS_ma(0,MM_gnc) # Partendo da 0 si possono visitare solo i nodi 1,2
vm1=DFS_ma(1,MM_gnc) # Partendo da 1 si possono visitare solo i nodi 0,2
vm2=DFS_ma(2,MM_gnc) # Partendo da 2 si possono visitare solo i nodi 0,1
vm3=DFS_ma(3,MM_gnc) # Partendo da 3 si possono visitare solo i nodi 4,5
vm4=DFS_ma(4,MM_gnc) # Partendo da 4 si possono visitare solo i nodi 3,5
vm5=DFS_ma(5,MM_gnc) # Partendo da 5 si possono visitare solo i nodi 3,4
vm6=DFS_ma(6,MM_gnc) # Partendo da 6 non si puo' visitare alcun nodo

print("DFS con Matrice di Adiacenza - Grafo Connesso: "+"\n"+
      "0 -> "+ str(vm0)+"\n"+
      "1 -> "+ str(vm1)+"\n"+
      "2 -> "+ str(vm2)+"\n"+
      "3 -> "+ str(vm3)+"\n"+
      "4 -> "+ str(vm4)+"\n"+
      "5 -> "+ str(vm5)+"\n"+
      "6 -> "+ str(vm6)+"\n")



# CONTEGGIO COMPONENTI CONNESSE

'Grafo Connesso'
ccVector=contCompConnesse(L_gc)
print("Il vettore delle componenti connesse del Grafo Connesso e': " 
      + str(ccVector) + "\n")

'Grafo Non Connesso'
ccVector=contCompConnesse(L_gnc)
print("Il vettore delle componenti connesse del Grafo Non Connesso e': " 
      + str(ccVector) + "\n")
