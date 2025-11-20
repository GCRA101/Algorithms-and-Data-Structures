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
from Queue import Queue


'COSTRUZIONE ARRAY DI RECORDS SINGOLI'
keys=[3,1,613,34,6,13,7,45,78]
records=[]
for the in range(0,len(keys),1):
    records.append(RecordSingolo(keys[the]))    
for the in range(0,len(records)-1,1):
    records[the].setNext(records[the+1])
    
'COSTRUZIONE CODA'
queue = Queue()    


'ENQUEUE'
for record in records:
    queue.enqueue(record)
print("CODA COMPLETA\n" +str(queue))

'DEQUEUE'
pp1=queue.dequeue()
pp2=queue.dequeue()
print("\nCODA RIDOTTA\n" +str(queue))

