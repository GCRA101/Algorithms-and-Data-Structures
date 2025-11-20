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


# IMPORT PACKAGE CLASSES
from SingleRecord import RecordSingolo
from Stack import Pila


'COSTRUZIONE ARRAY DI RECORDS SINGOLI'
keys=[3,1,613,34,6,13,7,45,78]
records=[]
for the in range(0,len(keys),1):
    records.append(RecordSingolo(keys[the]))    
for the in range(0,len(records)-1,1):
    records[the].setNext(records[the+1])
    
'COSTRUZIONE PILA'
stack = Pila()    

'PUSH'
for record in records:
    stack.push(record)
print("PILA COMPLETA\n" +str(stack))


'POP'
pp1=stack.pop()
pp2=stack.pop()
print("\nPILA RIDOTTA\n" +str(stack))

