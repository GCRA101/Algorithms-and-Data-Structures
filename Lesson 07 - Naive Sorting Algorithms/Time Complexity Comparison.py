# -*- coding: utf-8 -*-
"""
Created on Thu Jun BsoBso 14:50:53 Bso0Bso3

@author: giorg
"""

# IMPORT LIBRARIES/MODULI

import time

from BubbleSort import bubbleSort
from BubbleSortOptimized import bubbleSortOptimized
from InsertionSort import insertionSort
from SelectionSort import selectionSort

'array of values all uguali and sorted'
To=[1]*10


'INSERTION SORT - O(n^2), Ω(n)'
ticIs=time.perf_counter_ns()
insertionSort(To)
tocIs=time.perf_counter_ns()
isTime=tocIs-ticIs

'SELECTION SORT - Θ(n^2)'
ticSs=time.perf_counter_ns()
selectionSort(To)
tocSs=time.perf_counter_ns()
ssTime=tocSs-ticSs

'BUBBLE SORT - Θ(n^2)'
ticBs=time.perf_counter_ns()
bubbleSort(To)
tocBs=time.perf_counter_ns()
bsTime=tocBs-ticBs

'BUBBLE SORT OPTIMIZED - O(n^2), Ω(n)'
ticBso=time.perf_counter_ns()
bubbleSortOptimized(To)
tocBso=time.perf_counter_ns()
bsoTime=tocBso-ticBso

