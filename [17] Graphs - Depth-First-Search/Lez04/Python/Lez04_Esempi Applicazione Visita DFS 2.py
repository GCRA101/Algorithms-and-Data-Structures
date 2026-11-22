# -*- coding: utf-8 -*-
"""
LEZIONE 04 - ESEMPI DI APPLICAZIONE VISITA DFS 2

Algoritmi di utilita' tramite uso di DFS
    - Ricerca dei Ponti
    - Ricerca dei Punti di Articolazione
    
"""


" ALGORITMI *****************************************************************"


# RICERCA dei PONTI
def ricercaPonti(s,G):                                           # T(n,m)

    def DFSPonti(u,c):                                           # S(n,m)
        c+=1                                                     # Θ(1)
        visitati[u]=c                                            # Θ(1)
        back=c                                                   # Θ(1)
        for v in G[u]:                                           # k*Θ(1)+Θ(1)
            if v!=P[u]:                                          # Θ(1)
                if visitati[v]==0:                               # Θ(1)
                    P[v]=u                                       # Θ(1)
                    x=DFSPonti(v,c)                              # S(n-1,v)
                    if (x>visitati[u]):                          # Θ(1)
                        ponti.append("{" + str(u) + 
                                     ", " + str(v) + "}")        # Θ(1)
                    back=min(back,x)                             # Θ(1)
                else:                                            # Θ(1)
                    back=min(back,visitati[v])                   # Θ(1)
        return back                                              # Θ(1)
    
    visitati=[0 for v in G]                                      # Θ(n)
    ponti=[]                                                     # Θ(1)
    P=[-1 for v in G]                                            # Θ(n)
    P[s]=s                                                       # Θ(1)
    c=0                                                          # Θ(1)
    DFSPonti(s,c)                                                # S(n,m)
    return ponti                                                 # Θ(1)

# Costo Computazionale: Θ(n+m)   - CASO PEGGIORE/MIGLIORE   



# RICERCA dei PUNTI di ARTICOLAZIONE
# def ricercaPuntiDiArticolazione():
def ricercaPuntiDiArticolazione(s,G):                             # T(n,m)
    def DFSPuntiArt(u,c):                                         # Θ(n)
        c+=1                                                      # Θ(1)
        visitati[u]=c                                             # Θ(1)
        figli=0                                                   # Θ(1)
        back=c                                                    # Θ(1)
        for v in G[u]:                                            # k*Θ(1)+Θ(1)
            if v!=P[u]:                                           # Θ(1)
                if visitati[v]==0:                                # Θ(1)
                    figli+=1                                      # Θ(1)
                    P[v]=u                                        # Θ(1)
                    x=DFSPuntiArt(v,c)                            # S(n-1,v)
                    if (x>=visitati[u] and visitati[u]>1):        # Θ(1)
                        puntiDiArticolazione.append("{" + 
                                                    str(u) + "}") # Θ(1)
                    back=min(back,x)                              # Θ(1)
                else:                                             # Θ(1)
                    back=min(back,visitati[v])                    # Θ(1)
        if (visitati[u]==1 and figli>=2):                         # Θ(1)
            puntiDiArticolazione.append("{" + str(u) + "}")       # Θ(1)
        return back                                               # Θ(1)
    
    visitati=[0 for v in G]                                       # Θ(n)
    puntiDiArticolazione=[]                                       # Θ(1)
    P=[-1 for v in G]                                             # Θ(n)
    P[s]=s                                                        # Θ(1)
    c=0                                                           # Θ(1)
    DFSPuntiArt(s,c)                                              # S(n,m)
    return puntiDiArticolazione                                   # Θ(1)

# Costo Computazionale: Θ(n+m)   - CASO PEGGIORE/MIGLIORE   



" ESEMPI ********************************************************************"

"""
Iniziamo, per semplicita', con un esempio puramente numerico...

"""

# LISTE DI ADIACENZA

'Grafo Indiretto con 0 Ponti' 
L01= [[1,2,3],
      [0,2,8],
      [0,1],
      [0,4],
      [3,5,6],
      [4,6,7],
      [4,5,7],
      [5,6,8],
      [1,7]]

'Grafo Indiretto con 6 Ponti' 
L02= [[1,2,3],
      [0,2],
      [0,1],
      [0,4],
      [3,5,6],
      [4,6,7],
      [4,5,7],
      [5,6,8],
      [7,9],
      [8,10,11],
      [9],
      [9]]

# MATRICE DI ADIACENZA

'Grafo Indiretto con 0 Ponti' 
M01= [[0,1,1,1,0,0,0,0,0], # Riga di adiacenza del nodo 00
      [1,0,1,0,0,0,0,0,1], # Riga di adiacenza del nodo 01
      [1,1,0,0,0,0,0,0,0], # Riga di adiacenza del nodo 02
      [1,0,0,0,1,0,0,0,0], # Riga di adiacenza del nodo 03
      [0,0,0,1,0,1,1,0,0], # Riga di adiacenza del nodo 04      
      [0,0,0,0,1,0,1,1,0], # Riga di adiacenza del nodo 05      
      [0,0,0,0,1,1,0,1,0], # Riga di adiacenza del nodo 06     
      [0,0,0,0,0,1,1,0,1], # Riga di adiacenza del nodo 07     
      [0,1,0,0,0,0,0,1,0]] # Riga di adiacenza del nodo 08  

'Grafo Indiretto con 6 Ponti' 
M02= [[0,1,1,1,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo 00
      [1,0,1,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo 01
      [1,1,0,0,0,0,0,0,0,0,0,0], # Riga di adiacenza del nodo 02
      [1,0,0,0,1,0,0,0,0,0,0,0], # Riga di adiacenza del nodo 03
      [0,0,0,1,0,1,1,0,0,0,0,0], # Riga di adiacenza del nodo 04      
      [0,0,0,0,1,0,1,1,0,0,0,0], # Riga di adiacenza del nodo 05      
      [0,0,0,0,1,1,0,1,0,0,0,0], # Riga di adiacenza del nodo 06     
      [0,0,0,0,0,1,1,0,1,0,0,0], # Riga di adiacenza del nodo 07     
      [0,0,0,0,0,0,0,1,0,1,0,0], # Riga di adiacenza del nodo 08      
      [0,0,0,0,0,0,0,0,1,0,1,1], # Riga di adiacenza del nodo 09      
      [0,0,0,0,0,0,0,0,0,1,0,0], # Riga di adiacenza del nodo 10      
      [0,0,0,0,0,0,0,0,0,1,0,0]] # Riga di adiacenza del nodo 11      
      
      
      

# RICERCA PONTI
np01=ricercaPonti(0,L01)
print("Grafo 01 - Lista dei Ponti: " + str(np01) + "\n")
np02=ricercaPonti(0,L02)
print("Grafo 02 - Lista dei Ponti: " + str(np02) + "\n")


# RICERCA PUNTI DI ARTICOLAZIONE
npa01=ricercaPuntiDiArticolazione(0,L01)
print("Grafo 01 - Lista dei Punti di Articolazione: " + str(npa01) + "\n")
npa02=ricercaPuntiDiArticolazione(0,L02)
print("Grafo 02 - Lista dei Punti di Articolazione: " + str(npa02) + "\n")