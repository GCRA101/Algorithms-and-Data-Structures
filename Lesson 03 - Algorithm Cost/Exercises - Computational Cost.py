# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from matplotlib import pyplot as plt
import numpy as np
import math
import time



# Esercizio 1 - INSERTION SORT

# Input size: number of elements contained in array A

# WORST CASE: Array ordinato in modo decrescente 
# (bisogna invertire tutti gli elementi)

def Insertion_Sort(A):
    for j in range(1,len(A)):       # n*O(1) + O(1)
        x=A[j]                      # O(1)
        i=j-1                       # O(1)
        while ((i>=0)and(A[i]>x)):  # n*O(1) + O(1)
            A[i+1]=A[i]             # O(1)
            i=i-1                   # O(1)
        A[i+1]=x                    # O(1)
    return A
        

# Computational cost
# n*(O(1)+O(3)+(n*(O(1)+O(2))+O(1)))+O(1)=O(4n)+O(3n^2)+O(n)+O(1)
# Since constants are neglected (unless they are in the exponent...)
# O(n)+O(n^2)+O(n)+O(1)
# Dato che si tiene solo il valore di ordine massimo per valori 
# sufficientemente grandi di n...
# Computational cost: O(n^2)
        
        
        
# BEST CASE: Array ordinato in modo crescente 
# (nessun elemento dev'essere invertito)        

def Insertion_Sort(A):
    for j in range(1,len(A)):       # n*O(1) + O(1)
        x=A[j]                      # O(1)
        i=j-1                       # O(1)
        while ((i>=0)and(A[i]>x)):  # O(1) (*)
            A[i+1]=A[i]             
            i=i-1                   
        A[i+1]=x                    # O(1)
    return A

# (*): La condizione del ciclo while non si verifica mai!        
        
# Computational cost
# n*(O(1)+O(4))
# Since constants are neglected (unless they are in the exponent...)
# O(4n)
# Computational cost: O(n)
        
    
# CONCLUSION
# The algorithm is O(n^2) e un Ω(n)


# GRAPHICAL REPRESENTATION

A=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for i in range(1,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    Insertion_Sort(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for i in range(1,1000):
    B=list(reversed(range(1,i)))
    tic=time.perf_counter()
    Insertion_Sort(B)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,5))

    
    
bestCase=plt.plot(range(1,1000),stepsA,label="Best Case Ω(n)")
worstCase=plt.plot(range(1,1000),stepsB,label="Worst Case O(n^2)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Insertion Sort Algorithm - Best & Worst Case")

plt.show()




# Esercizio 2 - SELECTION SORT

# Input size: number of elements contained in array A

# CASO PEGGIORE/MIGLIORE: I due casi coincidono dato che per qualunque ordine 
# degli elementi all'interno dell'array, la condizione di controllo del nested 
# loop viene sempre eseguita su ciascuno di essi

def Selection_Sort(A):
    for i in range(len(A)-1):       # (n-1)*Θ(1) + Θ(1)
        m=i                         # Θ(1)
        for j in range(i+1,len(A)): # (n-1)*Θ(1) + Θ(1)
            if A[j]<A[m]:           # Θ(1)
                m=j                 # Θ(1)
        A[m],A[i]=A[i],A[m]         # Θ(1)
    return A
        

# Computational cost
# (n-1)*[Θ(1)+Θ(1)+(n-1)*(Θ(1)+Θ(3))+Θ(1)]+Θ(1)
# Since constants are neglected (unless they are in the exponent...)
# n*(n*Θ(1))
# Per la proprieta' commutativa del prodotto...
# Computational cost: Θ(n^2)

    
# CONCLUSION
# The algorithm is Θ(n^2) 
# Il caso migliore e il caso peggiore coincidono.


# GRAPHICAL REPRESENTATION

A=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for i in range(1,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    Selection_Sort(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for i in range(1,1000):
    B=list(reversed(range(1,i)))
    tic=time.perf_counter()
    Selection_Sort(B)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,5))

bestCase=plt.plot(range(1,1000),stepsA,label="Best Case Θ(n^2)")
worstCase=plt.plot(range(1,1000),stepsB,label="Worst Case Θ(n^2)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Selection Sort Algorithm - Best & Worst Case")

plt.show()




# Esercizio 3 - BUBBLE SORT

# Input size: number of elements contained in array A

# CASO PEGGIORE/MIGLIORE: I due casi coincidono dato che per qualunque ordine 
# degli elementi all'interno dell'array, la condizione di controllo del 
# nested loop viene sempre eseguita su ciascuno di essi

def Bubble_Sort(A):
    for i in range(len(A)-1):             # (n-1)*Θ(1) + Θ(1)
        for j in range(len(A)-i-1):       # (n-1)*Θ(1) + Θ(1)
            if A[j]>A[j+1]:               # Θ(1)
                A[j],A[j+1]=A[j+1],A[j]   # Θ(1)
    return A
        

# Computational cost
# (n-1)*[Θ(1)+(n-1)*(Θ(1)+Θ(2))+Θ(1)]+Θ(1)
# Since constants are neglected (unless they are in the exponent...)
# n*(n*Θ(1))
# Per la proprieta' commutativa del prodotto...
# Computational cost: Θ(n^2)

    
# CONCLUSION
# The algorithm is Θ(n^2) 
# Il caso migliore e il caso peggiore coincidono.


# GRAPHICAL REPRESENTATION

A=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for i in range(1,1000):
    A=list(range(1,i))
    tic=time.perf_counter()
    Bubble_Sort(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for i in range(1,1000):
    B=list(reversed(range(1,i)))
    tic=time.perf_counter()
    Bubble_Sort(B)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,5))

bestCase=plt.plot(range(1,1000),stepsA,label="Best Case Θ(n^2)")
worstCase=plt.plot(range(1,1000),stepsB,label="Worst Case Θ(n^2)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Bubble Sort Algorithm - Best & Worst Case")

plt.show()




# Esercizio 0

# Input size: valore numero n di input

# CASO PEGGIORE/MIGLIORE: I due casi coincidono anche in questo algoritmo. 
# Si sarebbe tentati dall'individuare, come caso peggiore, il caso in cui n<100, 
# tale per cui si salterebbe il ciclo for, fermandosi alla linea di codice 
# return 1....ma la notazione asintotica vale solo per valori grandi 
# dell'input (n->infinito)...quindi sia il caso peggiore che il caso migliore 
# devono essere valutati per n->infinito.
# Quindi, in entrambi i casi, l'algoritmo termina alla riga return 1!

def es0(n):
    t=0                  # Θ(1)
    n=abs(n)             # Θ(1)
    if n>100: return 1   # Θ(1)
    for i in range(n):
        t+=3
    return t           

# Computational cost
# Θ(1)+Θ(1)+Θ(1)
# Per la proprieta' commutativa della somma...
# Computational cost: Θ(1)

    
# CONCLUSION
# The algorithm is Θ(1) 
# Il caso migliore e il caso peggiore coincidono.


# GRAPHICAL REPRESENTATION


stepsA=[]
for i in range(1,1000):
    A=i
    tic=time.perf_counter()
    es0(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,3))

bestworstCase=plt.plot(range(1,1000),stepsA,label="Best Case Θ(1)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es0 Algorithm - Best & Worst Case")

plt.show()




# Esercizio 1

# Input size: valore numero n di input


# WORST CASE: Valore numerico n DISPARI. 
# Il ciclo for viene eseguito n/2 volte

def es1(n):
    if n<0: n=-n           # O(1)
    while n:               # n/2*O(1) + O(1)
        if n%2: return 1   # O(1)
        n-=2               # O(1)
    return 0               # O(1)

# Computational cost
# O(1)+n/2*O(4)+O(1)
# Per la proprieta' commutativa della somma...
# O(n/2)
# Computational cost: O(n)



# BEST CASE: Valore numerico n PARI. 
# Il ciclo for viene eseguito 1 volta sola

def es1(n):
    if n<0: n=-n           # O(1)
    while n:               # O(1) + O(1)
        if n%2: return 1   # O(1)
        n-=2
    return 0           

# Computational cost
# O(1)+O(1)+O(1)+O(1)
# Per la proprieta' commutativa della somma...
# Computational cost: Ω(1)


# CONCLUSION
# The algorithm is O(n) e un Ω(1)


# GRAPHICAL REPRESENTATION


stepsA=[]
for i in range(0,9999,2):
    A=i
    tic=time.perf_counter()
    es1(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,5))
    
stepsB=[]
for i in range(1,10000,2):
    B=i
    tic=time.perf_counter()
    es1(B)
    toc=time.perf_counter()
    stepsB.append(round(toc-tic,7))
    

bestCase=plt.plot(range(0,9999,2),stepsA,label="Best Case Ω(1)")
worstCase=plt.plot(range(1,10000,2),stepsB,label="Worst Case O(n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es1 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 2

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input

def es2(n):
    n=abs(n)                   # Θ(1)
    x=r=0                      # Θ(1)
    while x*x<n:               # sqrt(n)*Θ(1) + Θ(1)
        x+=1                   # Θ(1)
        r*=3*x                 # Θ(1)
    return r                   # Θ(1)

# Computational cost
# Θ(2)+sqrt(n)*Θ(4)+Θ(1)
# Per la proprieta' commutativa della somma...
# Θ(sqrt(n)*4)
# Computational cost: Θ(sqrt(n))


# CONCLUSION
# The algorithm is Θ(sqrt(n))


# GRAPHICAL REPRESENTATION


stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.perf_counter()
    es2(A)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,10))
    

bestworstCase=plt.plot(range(0,1000,1),stepsA,label="Best/Worst Case Θ(sqrt(n))")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es2 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 3

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input (sara' sempre vero che n>1)

def es3(n):
    n=abs(n)                   # Θ(1)
    x=r=0                      # Θ(1)
    while n>1:                 # log3(n)*Θ(1) + Θ(1)
        r+=2                   # Θ(1)
        n=n//3                 # Θ(1)
    return r                   # Θ(1)

# Computational cost
# Θ(2)+log3(n)*Θ(3)+Θ(1)
# Per la proprieta' commutativa del prodotto e per la regola delle costanti...
# Θ(log3(n))
# Computational cost: Θ(log(n))


# CONCLUSION
# The algorithm is Θ(log(n))


# GRAPHICAL REPRESENTATION


stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es3(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(log(n))")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es3 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 4

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input (sara' sempre vero che n>1)

def es4(n):
    n=abs(n)                   # Θ(1)
    x=t=1                      # Θ(1)
    for i in range(n):         # n*Θ(1) + Θ(1)
        t=3*t                  # Θ(1)
    while t>=x:                # (3^n+1)/7*Θ(1)+Θ(1)
        x+=2                   # Θ(1)
        t-=x                   # Θ(1)
    return x                   # Θ(1)



# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina il numero di cicli eseguiti (n)
# 2) Individuare la condizione che determina la conclusione del ciclo in funzione 
#    dell'input n (t=x -> 3^n-3k-2*(k-1)=3+2*(k-1))
#          - Iterazione:                    1         2          3             k   
#          - Valore variabile di ciclo:   3^n-3    3^n-3-5   3^n-3-5-7   3^n-(k-1)*(3+2)
# 3) Risolvere l'equazione (k=((3^n)+1)/7)


# Computational cost
# T(n)= Θ(1)+Θ(n)+Θ(3^n)+Θ(1)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(3^n)
# Computational cost: Θ(3^n)


# CONCLUSION
# The algorithm is Θ(3^n)


# GRAPHICAL REPRESENTATION


stepsA=[]
for i in range(0,20,1):
    A=i
    tic=time.time()
    es4(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,20,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es4 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 5

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input


def es5(n):   
    n=abs(n)                # Θ(1)
    p=2                     # Θ(1)
    while n>=p:             # loglogn*Θ(1)+Θ(1)
        p=p*p               # Θ(1)
    return p                # Θ(1)

# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina il numero di cicli eseguiti (p)
# 2) Individuare la condizione che determina la conclusione del ciclo in funzione 
#    dell'input n (t=x -> 3^n-3k-2*(k-1)=3+2*(k-1))
#          - Iterazione:                      1             2            3          k   
#          - Valore variabile di ciclo:  (2^1)*(2^1)   (2^2)*(2^2)  (2^4)*(2^4)  2^(2^k)
# 3) Risolvere l'equazione (k=loglog(n))


# Computational cost
# T(n)= Θ(1)+Θ(log(n))+Θ(1)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(log(n))
# Computational cost: Θ(log(n))


# CONCLUSION
# The algorithm is Θ(log(n))


# GRAPHICAL REPRESENTATION

stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es5(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es5 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 6

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input


def es6(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   i=1                      # Θ(1)
   j=1                      # Θ(1)
   t=1                      # Θ(1)
   s=1                      # Θ(1)
   while i*i<=n:            # sqrt(n)*Θ(1)+Θ(1)
      for j in range(t):    # sqrt(n)*Θ(1)+Θ(1)
          s+=1              # Θ(1)
      i=i+1                 # Θ(1)
      t+=1                  # Θ(1)
   return s                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina i numeri di cicli eseguiti (i,t)
# 2) Individuare il valore iniziale delle variabili dei cicli
#       - i=1, t=1
# 3) Identificare valore dei parametri per diverse iterazioni del ciclo while esterno + 
#    numero di iterazioni del ciclo for interno
#          - Iterazione:         1        2        3       k   
#          - Variabile i         2        3        4      k+1
#          - Variabile t         2        3        4      k+1
#          - Ciclo for           1        2        3       k volte
# 4) Identificare condizione di fine ciclo esterno
#          - (k+1)^2=n -> k=sqrt(n)-1
# 5) Il costo del nested loop e' dato dalla sommatoria, entro i limiti del ciclo esterno, sul
#    costo del ciclo interno.
#          -sommatoria da k=1 a sqrt(n)-1 di k*Θ(1)+Θ(1)


# Computational cost
# T(n)= Θ(1)+Θ(sqrt(n)^2)+Θ(1)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(sqrt(n)^2)
# Computational cost: Θ(n)


# CONCLUSION
# The algorithm is Θ(n)


# GRAPHICAL REPRESENTATION

stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es6(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es6 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 7

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input


def es7(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   t=s=n                    # Θ(1)
   p=0                      # Θ(1)
   while s>=1:              # logn*Θ(1)+Θ(1)
      s=s//4                # Θ(1)
      p+=1                  # Θ(1)
   while n-s>0:             # n*Θ(1)+Θ(1)
      n-=s                  # Θ(1)
      t+=5                  # Θ(1)
   return t                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina i numeri di cicli eseguiti (s,n)
# 2) Individuare il valore iniziale delle variabili dei cicli
#       - s=n, n=n
# 3) Individuare la condizione che determina la conclusione del primo ciclo 
#    while in funzione dell'input n (s=1 -> n/4^k=1 ->k=(logn)/2)
#          - Iterazione:         1        2        3       k   
#          - Variabile s        n/4     n/4^2    n/4^3   n/4^k     
# 4) Individuare la condizione che determina la conclusione del secondo ciclo 
#    while in funzione dell'input n (n-s>0 -> n-k>0 -> k=n-1)
#          - Iterazione:         1        2        3       k   
#          - Variabile n        n-1      n-2      n-3     n-k 


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(n)+Θ(1)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(n)
# Computational cost: Θ(n)


# CONCLUSION
# The algorithm is Θ(n)


# GRAPHICAL REPRESENTATION

stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es7(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es7 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 8

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input


def es8(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   t=n                      # Θ(1)
   s=n                      # Θ(1)
   p=0                      # Θ(1)
   while s>=1:              # logn*Θ(1)+Θ(1)
      s=s//4                # Θ(1)
      p+=1                  # Θ(1)
   while n-p>0:             # (n/logn)*Θ(1)+Θ(1)
      n-=p                  # Θ(1)
      t+=5                  # Θ(1)
   return t                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina i numeri di cicli eseguiti (s,n)
# 2) Individuare il valore iniziale delle variabili dei cicli
#       - s=n, n=n
# 3) Individuare la condizione che determina la conclusione del primo ciclo 
#    while in funzione dell'input n (s=1 -> n/4^k=1 ->k=(logn)/2)
#          - Iterazione:         1        2        3       k   
#          - Variabile s        n/4     n/4^2    n/4^3   n/4^k     
# 4) Individuare la condizione che determina la conclusione del secondo ciclo 
#    while in funzione dell'input n (n-p>0 -> n-klogn-p>0 -> n-klogn -logn>0 -> k=(n/logn)-1)
#          - Iterazione:         1        2        3       k   
#          - Variabile n        n-1      n-2      n-3     n-k 


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(n/logn)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(n/logn)
# Computational cost: Θ(n/logn)


# CONCLUSION
# The algorithm is Θ(n/logn)


# GRAPHICAL REPRESENTATION

stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es8(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es8 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 9

# Input size: valore numero n di input


# CASO PEGGIORE/MIGLIORE: I due casi coincidono per qualunque valore  
# grande (->infinito) dell'input


def es9(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   s=n                      # Θ(1)
   p=2                      # Θ(1)
   i,r=1                    # Θ(1)
   while s>=1:              # logn*Θ(1)+Θ(1)
      s=s//5                # Θ(1)
      p+=2                  # Θ(1)
   p=p*p                    # Θ(1)
   while i*i*i<n:           # 3√n*((logn)^2)*Θ(1)+Θ(1)
      for j in range(p):
         r+=1               # Θ(1)
      i+=1                  # Θ(1)
   return r                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile che determina i numeri di cicli eseguiti (s,i,p)
# 2) Individuare il valore iniziale delle variabili dei cicli
#       - s=n, i=1, p=4*(logn+1)^2
# 3) Identificare valore dei parametri per diverse iterazioni del primo ciclo while e
#    condizione di fine ciclo (n/5^k=1 -> k=log5n -> k=logn)
#          - Iterazione:         1              2              3             k   
#          - Variabile s        n/5           n/5^2          n/5^3         n/5^k
# 3) Identificare valore dei parametri per diverse iterazioni del ciclo while esterno + 
#    numero di iterazioni del ciclo for interno
#          - Iterazione:         1              2               3             k   
#          - Variabile i         2              3               4            k+1
#          - Variabile p     4*(logn+1)^2  4*(logn+1)^2   4*(logn+1)^2   4*(logn+1)^2
#          - Ciclo for       4*(logn+1)^2  4*(logn+1)^2   4*(logn+1)^2   4*(logn+1)^2
# 4) Identificare condizione di fine ciclo esterno
#          - (k+1)^3=n -> k=3√n-1
# 5) Il costo del nested loop e' dato dalla sommatoria, entro i limiti del ciclo esterno, sul
#    costo del ciclo interno.
#          -sommatoria da k=1 a 3√n-1 di (4*(logn+1)^2)*Θ(1) + Θ(1)


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(3√n*((logn)^2))+Θ(1)
# Per la proprieta' commutativa della somma e per la regola delle costanti...
# T(n)= Θ(3√n*((logn)^2))
# Computational cost: Θ(3√n*((logn)^2))


# CONCLUSION
# The algorithm is Θ(3√n*((logn)^2))


# GRAPHICAL REPRESENTATION

stepsA=[]
for i in range(0,1000,1):
    A=i
    tic=time.time()
    es9(A)
    toc=time.time()
    stepsA.append(round(toc-tic,5))

x=range(0,1000,1)
z = np.polyfit(x, stepsA, 4)
p = np.poly1d(z)
plt.plot(x,p(x),label="Best/Worst Case Θ(3^n)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es9 Algorithm - Best & Worst Case")

plt.show() 