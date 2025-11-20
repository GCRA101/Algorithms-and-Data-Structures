# -*- coding: utf-8 -*-
"""
Created on Thu Jun 1 20:48:46 2023

@author: giorg
"""

'Import main libraries'
import numpy as np
import time
import matplotlib.pyplot as plt




# ESERCIZIO 1

'''
Given to array To of n values numerici and two values estremi to and b, tale that 
to<b, creare two algorithms for counting the values contained in the array
that siano compresi between to and b.
One algorithm must be based on sequential search (Linear Search) while
the other on binary search (Binary Search)
'''

# algorithm of RICERCA SEQUENZIALE

''' worst case/MIGLIORE
The two cases coincide since, for any array To in input
the algorithm dovra' scorrere always all the suoi elements'''

def ricercaSequenziale(To,to,b):
 the=0 # Θ(1)
 n=0 # Θ(1)
 while(the<len(To)): # n*Θ(1)+Θ(1)
 if (To[the]>=to and To[the]<=b): # Θ(1)
 n+=1 # Θ(1)
 the+=1 # Θ(1)
 return n # Θ(1)

# Input size: n elements in array To
# Computational Cost: T(n)=Θ(1)+Θ(n)+Θ(1)=Θ(n)


# algorithm of RICERCA BINARIA

''' worst case
The estremi to and b not vengono incontrati if not to the last
iterazione, in the case where siano presenti - at the k-th 
iterazione k=logn'''

def ricercaBinaria(To,to,b):
 aa=ab=0 # Θ(1)
 ba=bb=len(To)-1 # Θ(1) 
 af=bf=0 # Θ(1) 
 ma=mb=(ba-aa)//2 # Θ(1)
 
 while(To[mb]!=b and ab<bb): # logn*Θ(1)+Θ(1)
 if To[mb]<b: # Θ(1)
 ab=mb+1 # Θ(1)
 else: # Θ(1)
 bb=mb-1 # Θ(1)
 mb=(ab+bb)//2 # Θ(1)
 if ab>bb: # Θ(1)
 return -1 # Θ(1)
 if To[mb]<=b: # Θ(1)
 max=To[mb] # Θ(1)
 bf=mb # Θ(1)
 else: # Θ(1)
 max=To[mb-1] # Θ(1)
 bf=mb-1 # Θ(1)
 
 while(To[ma]!=to and aa<ba): # logn*Θ(1)+Θ(1)
 if To[ma]<to: # Θ(1)
 aa=ma+1 # Θ(1)
 else: # Θ(1)
 ba=ma-1 # Θ(1)
 ma=(aa+ba)//2 # Θ(1)
 if aa>ba: # Θ(1)
 return -1 # Θ(1)
 if To[ma]>=to: # Θ(1)
 min=To[ma] # Θ(1)
 af=ma # Θ(1)
 else: # Θ(1)
 min=To[ma+1] # Θ(1)
 af=ma+1 # Θ(1)

 return bf-af+1 # Θ(1)


# Input size: n elements in array To
# Computational Cost: T(n)=Θ(1)+2*logn*Θ(1)+Θ(1)=Θ(logn)

To=[1, 4, 8, 17, 22, 25, 31, 36, 44, 52, 55, 63, 71, 78, 92]
to=20
b=60

nSeq1=ricercaSequenziale(To, to, b)
nBin1=ricercaBinaria(To, to, b)


''' best case
The estremi to and b vengono incontrati to the second
iterazione'''

def ricercaBinaria(To,to,b):
 aa=ab=0 # Θ(1)
 ba=bb=len(To)-1 # Θ(1) 
 af=bf=0 # Θ(1) 
 ma=mb=(ba-aa)//2 # Θ(1)
 
 while(To[mb]!=b and ab<bb): # 2*Θ(1)+Θ(1)
 if To[mb]<b: # Θ(1)
 ab=mb+1 # Θ(1)
 else: # Θ(1)
 bb=mb-1 # Θ(1)
 mb=(ab+bb)//2 # Θ(1)
 if ab>bb: # Θ(1)
 return -1 # Θ(1)
 if To[mb]<=b: # Θ(1)
 max=To[mb] # Θ(1)
 bf=mb # Θ(1)
 else: # Θ(1)
 max=To[mb-1] # Θ(1)
 bf=mb-1 # Θ(1)
 
 while(To[ma]!=to and aa<ba): # 2*Θ(1)+Θ(1)
 if To[ma]<to: # Θ(1)
 aa=ma+1 # Θ(1)
 else: # Θ(1)
 ba=ma-1 # Θ(1)
 ma=(aa+ba)//2 # Θ(1)
 if aa>ba: # Θ(1)
 return -1 # Θ(1)
 if To[ma]>=to: # Θ(1)
 min=To[ma] # Θ(1)
 af=ma # Θ(1)
 else: # Θ(1)
 min=To[ma-1] # Θ(1)
 bf=mb-1 # Θ(1)

 return bf-af+1 # Θ(1)


 
# Input size: n elements in array To
# Computational Cost: T(n)=Θ(1)+2*Θ(1)+Θ(1)=Θ(1)

To=[1, 4, 8, 20, 22, 25, 31, 36, 44, 52, 55, 60, 71, 78, 92]
to=20
b=60

nSeq2=ricercaSequenziale(To, to, b)
nBin2=ricercaBinaria(To, to, b)


# Computational Cost Complessivo: O(logn) and Ω(1)




# GRAPHICAL REPRESENTATION


def rappresentazioneGrafica(data_x,data_y,tolerance,title,legendLabel):
 
 delta_max = tolerance # maximum difference in y between two points
 delta = 0 # running correction value
 data_cor = [] # corrected array
 data_cor.append(data_y[0]) # we append two first points
 data_cor.append(data_y[1])
 the=0
 
 for the in range(0,len(data_x)-2): # two first points are allready appended
 the += 2
 delta_i = data_y[the] - data_y[the-1]
 if np.abs(delta_i) > delta_max:
 delta += (delta_i - (data_cor[the-1] - data_cor[the-2]))
 data_cor.append(data_y[the]-delta)
 else:
 data_cor.append(data_y[the]-delta)
 
 
 plt.plot(data_x, data_cor,label=legendLabel)
 
 plt.xlabel('Inputs')
 plt.ylabel('Time [secs]')
 plt.legend()
 plt.title(title)




stepsA=[]
for the in range(5,1000):
 To=list(range(1,the))
 tic=time.perf_counter()
 to=the//10
 b=9*the//10
 ricercaSequenziale(To,to,b)
 toc=time.perf_counter()
 stepsA.append(round(abs(toc-tic),12))


stepsB1=[]
for the in range(5,1000):
 B1=list(range(1,the))
 tic=time.perf_counter()
 to=the//10
 b=9*the//10
 ricercaBinaria(B1,to,b)
 toc=time.perf_counter()
 stepsB1.append(round(toc-tic,12))


stepsB2=[]
for the in range(5,1000):
 B2=list(range(1,the))
 to=the//4
 b=3*the//4
 tic=time.perf_counter()
 ricercaBinaria(B2,to,b)
 toc=time.perf_counter()
 stepsB2.append(round(abs(toc-tic),12))
 
 
rappresentazioneGrafica(range(5,1000),stepsA,0.000001,"Algoritmi of " 
 "Search - Linear/Binary","Linear Search")

rappresentazioneGrafica(range(5,1000),stepsB1,0.000001,"Algoritmi of " 
 "Search - Linear/Binary","Binary Search - Worst Case")

rappresentazioneGrafica(range(5,1000),stepsB2,0.000001,"Algoritmi of " 
 "Search - Linear/Binary","Binary Search - Best Case")




# SOLUZIONI 

# algorithm of RICERCA SEQUENZIALE

def Conta_In_Intervallo(To,to,b):
 cont=0
 for the in range(len(To)):
 if to<=To[the]<=b:
 cont+=1
 return cont

To=[1, 4, 8, 17, 22, 25, 31, 36, 44, 52, 55, 63, 71, 78, 92]
to=20
b=60

nSeqSol=Conta_In_Intervallo(To, to, b)
