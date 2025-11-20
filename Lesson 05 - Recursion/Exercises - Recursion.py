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




# ESERCIZIO 1 ################################################################

'''
Given as input two integers n and k, calculate the k-th power of n through 
algorithm recursive method
'''

# Considerazioni
''' 
n^k=n*n*n*n*n... k times
Case base: for k=1->n=n
'''

# algorithm

def es1(n,k):                     # T(k)
    if k==1: return n             # Θ(1)      ' Base Case
    return n*es1(n,k-1)           # T(k-1)    ' Recursive Step

# Input size: value del coefficiente intero k
# The worst case and the best case coincidono. Indeed, also if for k=0,
# the computational cost would be = Θ(1), the asymptotic notation is calculated
# only for valori grandi dell'input (the.e. k->∞) for which the computational cost
# is greater than Θ(1) and cresce as the value of ... grows k.
# Computational Cost: T(k)=Θ(1)+T(k-1) -> Recurrence Equations





# ESERCIZIO 2 ################################################################

'''
Given as input an array of n integers, calculate the sum of its elements
through an algorithm recursive method
'''

# Considerazioni
'''
The action to be performed repeatedly consists of adding the current number
to the sum dei precedenti. 
The base case that stops the recursion occurs when reaching l'index
dell'last element
'''


# algorithm SBAGLIATO

def es2a(To,sum=0,the=0):             # T(n)
    if the==len(To) : return sum      # Θ(1)
    sum+=To[the]                      # Θ(1)
    return es2a(To,sum,the+1)         # T(n-1)

# Input size: number n of values contained in array To
# The worst case and the best case coincidono. Indeed, for any value
# GRANDE of n, the algorithm scorrera' always all the elements dell'array To
# dal first all'last.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations

'''
ATTENZIONE!!!
The algorithm above NON E' PROPRIAMENTE recursive since the total value
of the sum is returned exactly once the base case is reached 
(the==len(To)-1)...while it should be returned from the chiusura of chiamata
of the first function of the recursive chain...
Let's see how to rewrite the recursive function correctly.
'''


# algorithm CORRETTO

def es2b(To,the=0):                   # T(n)
    if the==len(To)-1: return To[the]    # Θ(1)      ' Base Case 
    return (To[the]+es2b(To,the+1))      # T(n-1)    ' Recursive Step

# Input size: number n of values contained in array To
# The worst case and the best case coincidono. Indeed, for any value
# GRANDE of n, the algorithm scorrera' always all the elements dell'array To
# dal first all'last.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations


To=[1,2,3,4,5,6,7,8,9,10]
sommaAlgA=es2a(To)
sommaAlgB=es2b(To)





# ESERCIZIO 3 ################################################################

'''
Given as input an array of n integers, trovare the minimo.
'''

# Considerazioni
'''
Assuming that the array is not to sorted array, the algorithm dovra' scorrere
all the elements dell'array dal first all'last for trovare the minimo.
the operation that is repeated is the comparison between two consecutive elements.
The base case occurs when reaching l'last element in the array'''

# algorithm

To=[31,22,7,83,101,71,27,52,3,21,15,98,88,17]

def es3(To,the=len(To)-1):                   # T(n)
    if the==0: return To[the]                 # Θ(1)      ' Base Case 
    return min(To[the],es3(To,the-1))          # T(n-1)    ' Recursive Step
    
minVal=es3(To)

# Input size: number n of values contained in array To
# The worst case and the best case coincidono. Indeed, for any value
# GRANDE of n, the algorithm scorrera' always all the elements dell'array To
# dal first all'last.
# Computational Cost: T(n)=Θ(1)+T(n-1) -> Recurrence Equations





# ESERCIZIO 4 ################################################################
    
'''
Given as input an array of n integers, verify if it is a palindrome.'''

# Considerazioni
'''
The algorithm deve ritornare a output of tipo boolean depending on whether the array in 
input sia palindrome o less.
Cases base: 1) differenza indices estremi subArray <=1 
           2) values at the extreme indices are different
Recursive step: confronto valori indices estremi for indices that si avvicinano
                 verso the punto medio dell'array'''

'Best Case'
# To=[31,22,7,83,101,71,27,52,3,21,15,98,88,17]
'Worst Case'
To=[38,12,71,4,22,9,32,9,22,4,71,12,38] 
                 
def es4(To,the=0,j=len(To)-1):        # T(n)
    if the>=j: return True          # Θ(1)    ' Base Case
    if To[the]!=To[j]: return False   # Θ(1)    ' Base Case
    return es4(To,the+1,j-1)         # T(n-2)  ' Recursive Step

bool=es4(To)

# Input size: number n of values contained in array To

# Computational Cost
# The best case is the case where already the two extreme values of the array are
# different (in that case, it is possible uscire from the ricorsione already' to the first
# iterazione).
# The worst case is the case where l'array is a palindrome.
# best case: T(n)=Θ(1)
# worst case: T(n)=Θ(1)+T(n-2) -> Recurrence Equations





# ESERCIZIO 5 ################################################################
    
'''
Given as input an array of n integers, print the keys from the last to 
first, ossia nell'ordine: V[n-1] V[n-2] V[n-3] V[n-4]...V[1] V[0]'''

# Considerazioni
'''
The algorithm deve arrivare to print l'last element in the base case and then
print all the restanti fino al first in the sequenza of chiusura of the 
chiamate of function.
Case base: 1) index element = index finale
Recursive step: prints element V[n] in console'''

'Best/Worst Case'
To=[12,51,22,61,32,81,9,43,78,101,2] 
                 
def es5a(To,the=0):                                    # T(n)
    if (the==len(To)-1):                               # Θ(1)
        return To[the]                                 # Θ(1)
    return str(es5a(To,the+1)) + " " + str(To[the])+ " "  # T(n-1)

print("Soluzione Mia")
print(es5a(To))

def es5b(To,the=len(To)-1):
    print(To[the], end= "  ")
    if the>0:
        return es5b(To,the-1)

print("Soluzione Prof")
es5b(To)

# Input size: number n of values contained in array To

# Computational Cost
# For values grandi of n, the best case and the worst case coincidono.
# In fact the algorithm deve always and comunque scorrere all the elements dell'
# array.
# best case/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations




# ESERCIZIO 6 ################################################################
    
'''
Given as input an array of n integers, print the keys from the first all'
last, ossia nell'ordine: V[0] V[1] V[2]...V[n-2] V[n-1]'''

# Considerazioni
'''
The algorithm deve arrivare to print the first element in the base case and then
print all the restanti fino all'last in the sequenza of chiusura of the 
chiamate of function.
Case base: 1) index element = index initial
Recursive step: prints element V[n] in console'''

'Best/Worst Case'
To=[12,51,22,61,32,81,9,43,78,101,2] 
                 
def es6a(To,the=len(To)-1):                             # T(n)
    if (the==0):                                      # Θ(1)
        return To[the]                                 # Θ(1)
    return str(es6a(To,the-1)) + " " + str(To[the])+ " "  # T(n-1)

print("")
print("Soluzione Mia")
print(es6a(To))

def es6b(To,the=0):
    print(To[the], end= "  ")
    if the<len(To)-1:
        return es6b(To,the+1)

print("Soluzione Prof")
es6b(To)

# Input size: number n of values contained in array To

# Computational Cost
# For values grandi of n, the best case and the worst case coincidono.
# In fact the algorithm deve always and comunque scorrere all the elements dell'
# array.
# best case/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations




# ESERCIZIO 7 ################################################################
    
'''
VEDI IL FOLDER TORRE HANOI '''



# ESERCIZI for CASA ##########################################################

'Esercizio B'
'''Design an algorithm recursive method that, given two numbers interi x and y, x>y>0,
ne calcoli the massimo comun divisore utilizzando the seguente procedimento (of
Euclide): 
    - if y=0 allora MCD(x,y)=x
    - altrimenti MCD(x,y)=MCD(y,x%y)
        - where x%y rappresenta the resto of the divisione between x and y '''
        
def MCD(x,y):
    if y==0: 
        return x
    return MCD(y,x%y)

x=73
y=41
print("\n\nGCD of ",x," and ",y, " is ",MCD(x,y))

# Input size: number n of values contained in array To

# Computational Cost
# For values grandi of n, the best case and the worst case coincidono.
# In fact the algorithm deve always and comunque scorrere all the elements dell'
# array.
# best case/Peggiore: T(n)=Θ(1)+T(n-1) -> Recurrence Equations
