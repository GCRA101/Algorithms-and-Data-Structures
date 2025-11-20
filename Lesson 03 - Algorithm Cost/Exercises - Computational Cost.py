# -*- coding: utf-8 -*-
"""
Spyder Editor

This is to temporary script file.
"""

from matplotlib import pyplot as plt
import numpy as np
import math
import time



# Esercizio 1 - INSERTION SORT

# Input size: number of elements contained in array To

# WORST CASE: Array ordinato in modo decrescente 
# (bisogna invertire all the elements)

def Insertion_Sort(To):
    for j in range(1,len(To)):       # n*O(1) + O(1)
        x=To[j]                      # O(1)
        the=j-1                       # O(1)
        while ((the>=0)and(To[the]>x)):  # n*O(1) + O(1)
            To[the+1]=To[the]             # O(1)
            the=the-1                   # O(1)
        To[the+1]=x                    # O(1)
    return To
        

# Computational cost
# n*(O(1)+O(3)+(n*(O(1)+O(2))+O(1)))+O(1)=O(4n)+O(3n^2)+O(n)+O(1)
# Since constants are neglected (unless they are in the exponent...)
# O(n)+O(n^2)+O(n)+O(1)
# Since si tiene only the value of ordine massimo for values 
# sufficientemente grandi of n...
# Computational cost: O(n^2)
        
        
        
# BEST CASE: Array ordinato in modo crescente 
# (nessun element dev'essere invertito)        

def Insertion_Sort(To):
    for j in range(1,len(To)):       # n*O(1) + O(1)
        x=To[j]                      # O(1)
        the=j-1                       # O(1)
        while ((the>=0)and(To[the]>x)):  # O(1) (*)
            To[the+1]=To[the]             
            the=the-1                   
        To[the+1]=x                    # O(1)
    return To

# (*): The condizione del ciclo while not si verifica never!        
        
# Computational cost
# n*(O(1)+O(4))
# Since constants are neglected (unless they are in the exponent...)
# O(4n)
# Computational cost: O(n)
        
    
# CONCLUSION
# The algorithm is O(n^2) e a Ω(n)


# GRAPHICAL REPRESENTATION

To=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for the in range(1,1000):
    To=list(range(1,the))
    tic=time.perf_counter()
    Insertion_Sort(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for the in range(1,1000):
    B=list(reversed(range(1,the)))
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

# Input size: number of elements contained in array To

# worst case/MIGLIORE: The two cases coincide since for any ordine 
# degli elementi all'interno dell'array, the condizione of controllo del nested 
# loop viene always eseguita on ciascuno of essi

def Selection_Sort(To):
    for the in range(len(To)-1):       # (n-1)*Θ(1) + Θ(1)
        m=the                         # Θ(1)
        for j in range(the+1,len(To)): # (n-1)*Θ(1) + Θ(1)
            if To[j]<To[m]:           # Θ(1)
                m=j                 # Θ(1)
        To[m],To[the]=To[the],To[m]         # Θ(1)
    return To
        

# Computational cost
# (n-1)*[Θ(1)+Θ(1)+(n-1)*(Θ(1)+Θ(3))+Θ(1)]+Θ(1)
# Since constants are neglected (unless they are in the exponent...)
# n*(n*Θ(1))
# For the proprieta' commutativa del prodotto...
# Computational cost: Θ(n^2)

    
# CONCLUSION
# The algorithm is Θ(n^2) 
# The best case and the worst case coincidono.


# GRAPHICAL REPRESENTATION

To=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for the in range(1,1000):
    To=list(range(1,the))
    tic=time.perf_counter()
    Selection_Sort(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for the in range(1,1000):
    B=list(reversed(range(1,the)))
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

# Input size: number of elements contained in array To

# worst case/MIGLIORE: The two cases coincide since for any ordine 
# degli elementi all'interno dell'array, the condizione of controllo del 
# nested loop viene always eseguita on ciascuno of essi

def Bubble_Sort(To):
    for the in range(len(To)-1):             # (n-1)*Θ(1) + Θ(1)
        for j in range(len(To)-the-1):       # (n-1)*Θ(1) + Θ(1)
            if To[j]>To[j+1]:               # Θ(1)
                To[j],To[j+1]=To[j+1],To[j]   # Θ(1)
    return To
        

# Computational cost
# (n-1)*[Θ(1)+(n-1)*(Θ(1)+Θ(2))+Θ(1)]+Θ(1)
# Since constants are neglected (unless they are in the exponent...)
# n*(n*Θ(1))
# For the proprieta' commutativa del prodotto...
# Computational cost: Θ(n^2)

    
# CONCLUSION
# The algorithm is Θ(n^2) 
# The best case and the worst case coincidono.


# GRAPHICAL REPRESENTATION

To=list(range(1,1000))
B=list(reversed(range(1,1000)))

stepsA=[]
for the in range(1,1000):
    To=list(range(1,the))
    tic=time.perf_counter()
    Bubble_Sort(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,7))

stepsB=[]
for the in range(1,1000):
    B=list(reversed(range(1,the)))
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

# Input size: value number n of input

# worst case/MIGLIORE: The two cases coincide also in this algorithm. 
# One would be tempted to identify, as worst case, the case in cui n<100, 
# tale for cui si salterebbe the ciclo for, fermandosi alla linea of codice 
# return 1....ma the notazione asintotica vale only for valori grandi 
# dell'input (n->infinito)...quindi sia the worst case chand the best case 
# devono essere valutati for n->infinito.
# Quindi, in entrambi the cases, the algorithm termina alla riga return 1!

def es0(n):
    t=0                  # Θ(1)
    n=abs(n)             # Θ(1)
    if n>100: return 1   # Θ(1)
    for the in range(n):
        t+=3
    return t           

# Computational cost
# Θ(1)+Θ(1)+Θ(1)
# For the proprieta' commutativa della somma...
# Computational cost: Θ(1)

    
# CONCLUSION
# The algorithm is Θ(1) 
# The best case and the worst case coincidono.


# GRAPHICAL REPRESENTATION


stepsA=[]
for the in range(1,1000):
    To=the
    tic=time.perf_counter()
    es0(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,3))

bestworstCase=plt.plot(range(1,1000),stepsA,label="Best Case Θ(1)")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es0 Algorithm - Best & Worst Case")

plt.show()




# Esercizio 1

# Input size: value number n of input


# WORST CASE: value numerico n DISPARI. 
# The ciclo for viene eseguito n/2 volte

def es1(n):
    if n<0: n=-n           # O(1)
    while n:               # n/2*O(1) + O(1)
        if n%2: return 1   # O(1)
        n-=2               # O(1)
    return 0               # O(1)

# Computational cost
# O(1)+n/2*O(4)+O(1)
# For the proprieta' commutativa della somma...
# O(n/2)
# Computational cost: O(n)



# BEST CASE: value numerico n PARI. 
# The ciclo for viene eseguito 1 volta sola

def es1(n):
    if n<0: n=-n           # O(1)
    while n:               # O(1) + O(1)
        if n%2: return 1   # O(1)
        n-=2
    return 0           

# Computational cost
# O(1)+O(1)+O(1)+O(1)
# For the proprieta' commutativa della somma...
# Computational cost: Ω(1)


# CONCLUSION
# The algorithm is O(n) e a Ω(1)


# GRAPHICAL REPRESENTATION


stepsA=[]
for the in range(0,9999,2):
    To=the
    tic=time.perf_counter()
    es1(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,5))
    
stepsB=[]
for the in range(1,10000,2):
    B=the
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
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
# For the proprieta' commutativa della somma...
# Θ(sqrt(n)*4)
# Computational cost: Θ(sqrt(n))


# CONCLUSION
# The algorithm is Θ(sqrt(n))


# GRAPHICAL REPRESENTATION


stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.perf_counter()
    es2(To)
    toc=time.perf_counter()
    stepsA.append(round(toc-tic,10))
    

bestworstCase=plt.plot(range(0,1000,1),stepsA,label="Best/Worst Case Θ(sqrt(n))")
plt.xlabel('Inputs')
plt.ylabel('Time [secs]')
plt.title("Es2 Algorithm - Best & Worst Case")

plt.show() 




# Esercizio 3

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
# grande (->infinito) dell'input (sara' always vero that n>1)

def es3(n):
    n=abs(n)                   # Θ(1)
    x=r=0                      # Θ(1)
    while n>1:                 # log3(n)*Θ(1) + Θ(1)
        r+=2                   # Θ(1)
        n=n//3                 # Θ(1)
    return r                   # Θ(1)

# Computational cost
# Θ(2)+log3(n)*Θ(3)+Θ(1)
# For the proprieta' commutativa del prodotto e for the regola delle costanti...
# Θ(log3(n))
# Computational cost: Θ(log(n))


# CONCLUSION
# The algorithm is Θ(log(n))


# GRAPHICAL REPRESENTATION


stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es3(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
# grande (->infinito) dell'input (sara' always vero that n>1)

def es4(n):
    n=abs(n)                   # Θ(1)
    x=t=1                      # Θ(1)
    for the in range(n):         # n*Θ(1) + Θ(1)
        t=3*t                  # Θ(1)
    while t>=x:                # (3^n+1)/7*Θ(1)+Θ(1)
        x+=2                   # Θ(1)
        t-=x                   # Θ(1)
    return x                   # Θ(1)



# Calcolo costo computazionale ciclo while
# 1) Individuare variabile that determina the number of cicli eseguiti (n)
# 2) Individuare the condizione that determina the conclusione del ciclo in function 
#    dell'input n (t=x -> 3^n-3k-2*(k-1)=3+2*(k-1))
#          - Iterazione:                    1         2          3             k   
#          - value variabile of ciclo:   3^n-3    3^n-3-5   3^n-3-5-7   3^n-(k-1)*(3+2)
# 3) Risolvere l'equazione (k=((3^n)+1)/7)


# Computational cost
# T(n)= Θ(1)+Θ(n)+Θ(3^n)+Θ(1)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(3^n)
# Computational cost: Θ(3^n)


# CONCLUSION
# The algorithm is Θ(3^n)


# GRAPHICAL REPRESENTATION


stepsA=[]
for the in range(0,20,1):
    To=the
    tic=time.time()
    es4(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
# grande (->infinito) dell'input


def es5(n):   
    n=abs(n)                # Θ(1)
    p=2                     # Θ(1)
    while n>=p:             # loglogn*Θ(1)+Θ(1)
        p=p*p               # Θ(1)
    return p                # Θ(1)

# Calcolo costo computazionale ciclo while
# 1) Individuare variabile that determina the number of cicli eseguiti (p)
# 2) Individuare the condizione that determina the conclusione del ciclo in function 
#    dell'input n (t=x -> 3^n-3k-2*(k-1)=3+2*(k-1))
#          - Iterazione:                      1             2            3          k   
#          - value variabile of ciclo:  (2^1)*(2^1)   (2^2)*(2^2)  (2^4)*(2^4)  2^(2^k)
# 3) Risolvere l'equazione (k=loglog(n))


# Computational cost
# T(n)= Θ(1)+Θ(log(n))+Θ(1)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(log(n))
# Computational cost: Θ(log(n))


# CONCLUSION
# The algorithm is Θ(log(n))


# GRAPHICAL REPRESENTATION

stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es5(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
# grande (->infinito) dell'input


def es6(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   the=1                      # Θ(1)
   j=1                      # Θ(1)
   t=1                      # Θ(1)
   s=1                      # Θ(1)
   while the*the<=n:            # sqrt(n)*Θ(1)+Θ(1)
      for j in range(t):    # sqrt(n)*Θ(1)+Θ(1)
          s+=1              # Θ(1)
      the=the+1                 # Θ(1)
      t+=1                  # Θ(1)
   return s                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile that determina the numeri of cicli eseguiti (the,t)
# 2) Individuare the value iniziale delle variabili dei cicli
#       - the=1, t=1
# 3) Identificare value dei parametri for diverse iterazioni del ciclo while esterno + 
#    number of iterazioni del ciclo for interno
#          - Iterazione:         1        2        3       k   
#          - Variabile the         2        3        4      k+1
#          - Variabile t         2        3        4      k+1
#          - Ciclo for           1        2        3       k volte
# 4) Identificare condizione of fine ciclo esterno
#          - (k+1)^2=n -> k=sqrt(n)-1
# 5) The cost of the nested loop is given by the summation, within the limits of the outer loop, sul
#    costo del ciclo interno.
#          -sommatoria from k=1 to sqrt(n)-1 of k*Θ(1)+Θ(1)


# Computational cost
# T(n)= Θ(1)+Θ(sqrt(n)^2)+Θ(1)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(sqrt(n)^2)
# Computational cost: Θ(n)


# CONCLUSION
# The algorithm is Θ(n)


# GRAPHICAL REPRESENTATION

stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es6(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
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
# 1) Individuare variabile that determina the numeri of cicli eseguiti (s,n)
# 2) Individuare the value iniziale delle variabili dei cicli
#       - s=n, n=n
# 3) Individuare the condizione that determina the conclusione del first ciclo 
#    while in function dell'input n (s=1 -> n/4^k=1 ->k=(logn)/2)
#          - Iterazione:         1        2        3       k   
#          - Variabile s        n/4     n/4^2    n/4^3   n/4^k     
# 4) Individuare the condizione that determina the conclusione del second ciclo 
#    while in function dell'input n (n-s>0 -> n-k>0 -> k=n-1)
#          - Iterazione:         1        2        3       k   
#          - Variabile n        n-1      n-2      n-3     n-k 


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(n)+Θ(1)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(n)
# Computational cost: Θ(n)


# CONCLUSION
# The algorithm is Θ(n)


# GRAPHICAL REPRESENTATION

stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es7(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
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
# 1) Individuare variabile that determina the numeri of cicli eseguiti (s,n)
# 2) Individuare the value iniziale delle variabili dei cicli
#       - s=n, n=n
# 3) Individuare the condizione that determina the conclusione del first ciclo 
#    while in function dell'input n (s=1 -> n/4^k=1 ->k=(logn)/2)
#          - Iterazione:         1        2        3       k   
#          - Variabile s        n/4     n/4^2    n/4^3   n/4^k     
# 4) Individuare the condizione that determina the conclusione del second ciclo 
#    while in function dell'input n (n-p>0 -> n-klogn-p>0 -> n-klogn -logn>0 -> k=(n/logn)-1)
#          - Iterazione:         1        2        3       k   
#          - Variabile n        n-1      n-2      n-3     n-k 


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(n/logn)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(n/logn)
# Computational cost: Θ(n/logn)


# CONCLUSION
# The algorithm is Θ(n/logn)


# GRAPHICAL REPRESENTATION

stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es8(To)
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

# Input size: value number n of input


# worst case/MIGLIORE: The two cases coincide for any value  
# grande (->infinito) dell'input


def es9(n):                 # Θ(1)
   n=abs(n)                 # Θ(1)
   s=n                      # Θ(1)
   p=2                      # Θ(1)
   the,r=1                    # Θ(1)
   while s>=1:              # logn*Θ(1)+Θ(1)
      s=s//5                # Θ(1)
      p+=2                  # Θ(1)
   p=p*p                    # Θ(1)
   while the*the*the<n:           # 3√n*((logn)^2)*Θ(1)+Θ(1)
      for j in range(p):
         r+=1               # Θ(1)
      the+=1                  # Θ(1)
   return r                 # Θ(1)


# Calcolo costo computazionale ciclo while
# 1) Individuare variabile that determina the numeri of cicli eseguiti (s,the,p)
# 2) Individuare the value iniziale delle variabili dei cicli
#       - s=n, the=1, p=4*(logn+1)^2
# 3) Identificare value dei parametri for diverse iterazioni del first ciclo while e
#    condizione of fine ciclo (n/5^k=1 -> k=log5n -> k=logn)
#          - Iterazione:         1              2              3             k   
#          - Variabile s        n/5           n/5^2          n/5^3         n/5^k
# 3) Identificare value dei parametri for diverse iterazioni del ciclo while esterno + 
#    number of iterazioni del ciclo for interno
#          - Iterazione:         1              2               3             k   
#          - Variabile the         2              3               4            k+1
#          - Variabile p     4*(logn+1)^2  4*(logn+1)^2   4*(logn+1)^2   4*(logn+1)^2
#          - Ciclo for       4*(logn+1)^2  4*(logn+1)^2   4*(logn+1)^2   4*(logn+1)^2
# 4) Identificare condizione of fine ciclo esterno
#          - (k+1)^3=n -> k=3√n-1
# 5) The cost of the nested loop is given by the summation, within the limits of the outer loop, sul
#    costo del ciclo interno.
#          -sommatoria from k=1 to 3√n-1 of (4*(logn+1)^2)*Θ(1) + Θ(1)


# Computational cost
# T(n)= Θ(1)+Θ(logn)+Θ(3√n*((logn)^2))+Θ(1)
# For the proprieta' commutativa della somma e for the regola delle costanti...
# T(n)= Θ(3√n*((logn)^2))
# Computational cost: Θ(3√n*((logn)^2))


# CONCLUSION
# The algorithm is Θ(3√n*((logn)^2))


# GRAPHICAL REPRESENTATION

stepsA=[]
for the in range(0,1000,1):
    To=the
    tic=time.time()
    es9(To)
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