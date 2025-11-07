# -*- coding: utf-8 -*-
"""
Created on Thu Jun BsoBso 14:50:53 Bso0Bso3

@author: giorg
"""

# IMPORT LIBRERIE/MODULI

import time

from BubbleSort import bubbleSort
from BubbleSortOptimized import bubbleSortOptimized
from InsertionSort import insertionSort
from SelectionSort import selectionSort

'Array di valori tutti uguali e ordinati'
A=[1]*10


'INSERTION SORT - O(n^2), Ω(n)'
ticIs=time.perf_counter_ns()
insertionSort(A)
tocIs=time.perf_counter_ns()
isTime=tocIs-ticIs

'SELECTION SORT - Θ(n^2)'
ticSs=time.perf_counter_ns()
selectionSort(A)
tocSs=time.perf_counter_ns()
ssTime=tocSs-ticSs

'BUBBLE SORT - Θ(n^2)'
ticBs=time.perf_counter_ns()
bubbleSort(A)
tocBs=time.perf_counter_ns()
bsTime=tocBs-ticBs

'BUBBLE SORT OPTIMIZED - O(n^2), Ω(n)'
ticBso=time.perf_counter_ns()
bubbleSortOptimized(A)
tocBso=time.perf_counter_ns()
bsoTime=tocBso-ticBso

