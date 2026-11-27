# Algorithms and Data Structures

An implementation-first guide to algorithms, data structures and graph theory, developed from the **Introduzione agli Algoritmi** (Introduction to Algorithms) and **Progettazione di Algoritmi** (Algorithms Design) coursework at **Sapienza University of Rome**.

Explore **28 numbered topics**, from computational complexity, searching, and sorting to graph algorithms, greedy optimization, approximation algorithms, and divide and conquer. The collection is primarily written in **Python**, with worked exercises, Jupyter notebooks, complexity annotations, and diagrams that connect the theory to concrete implementations. Selected examples also use Go and Java.

This is a learning and reference collection, not a packaged, production-ready algorithms library. Most source comments, exercises, and many identifiers are **in Italian**; this README provides an English navigation guide.

## Contents

- [Choose your starting point](#choose-your-starting-point)
- [Topic guide](#topic-guide)
- [Getting started](#getting-started)
- [Working with the material](#working-with-the-material)
- [Contributing](#contributing)
- [License](#license)

## Choose your starting point

**For students:** start with topics 01-04 to build a foundation in complexity, searching, recursion, and recurrence equations. Continue through sorting (05-09) and data structures (10-15) before tackling graphs (16-20). Use the exercises to trace execution by hand, predict results, and justify time and space costs before running the code.

**For professionals:** use the topic guide to jump to an implementation or refresh a technique. Compare the progressively refined Dijkstra, Prim, and Kruskal variants to see how data-structure choices affect performance. Explore activity selection and interval partitioning for scheduling problems, or vertex cover, k-center, and knapsack for optimization trade-offs. Review each implementation's assumptions and behavior before adapting it.

## Topic guide

Follow the numbers for a broad learning sequence, or open a topic directly. Folder names are preserved in the links, even where the display title uses more conventional English terminology.

| Topic | What you will find |
| --- | --- |
| [01 - Computational complexity](<./[01] Algorithms' Computational Complexity/>) | Computational-cost exercises and asymptotic analysis. |
| [02 - Search algorithms](<./[02] Search Algorithms/>) | Linear and binary search, exercises, and timing visualizations. |
| [03 - Recursion](<./[03] Recursion/>) | Factorial, Fibonacci, recursive search, and Towers of Hanoi. |
| [04 - Recurrence equations](<./[04] Recurrence Equations/>) | A notebook on recurrence equations for recursive algorithms. |
| [05 - Elementary sorting](<./[05] Sorting Algorithms - Naif Algorithms/>) | Bubble sort, optimized bubble sort, insertion sort, selection sort, and complexity comparisons. |
| [06 - Merge sort](<./[06] Sorting Algorithms - MergeSort/>) | Python implementation and exercises; an iterative Java example. |
| [07 - Quicksort](<./[07] Sorting Algorithms - QuickSort/>) | Implementation and exercises. |
| [08 - Heapsort](<./[08] Sorting Algorithms - HeapSort/>) | Heap-based sorting and exercises. |
| [09 - Linear-time sorting](<./[09] Sorting Algorithms - Linear Algorithms/>) | Counting sort and bucket sort; their efficiency depends on input assumptions. |
| [10 - Dynamic sets and linked lists](<./[10] Data Structures - Dynamic Systems/>) | Singly and doubly linked lists, with object- and string-based pointer representations. |
| [11 - Stacks and queues](<./[11] Data Structures - Stacks and Queues/>) | Stack and queue classes, operations, and exercises. |
| [12 - Trees](<./[12] Data Structures - Trees/>) | Tree exercises and foundational material. |
| [13 - Tree traversals](<./[13] Data Structures - Tree Traversals/>) | Binary-tree classes, traversal implementations, and supporting stacks and queues. |
| [14 - Binary search trees](<./[14] Data Structures - Binary Search Trees/>) | Node and tree classes, operations, and exercises. |
| [15 - Red-black trees](<./[15] Data Structures - Red-And-Black Trees/>) | Balanced-tree classes, operations, and exercises. |
| [16 - Graphs](<./[16] Data Structures - Graphs/>) | Graph representations and introductory examples, including Go material. |
| [17 - Depth-first search](<./[17] Graphs - Depth-First-Search/>) | DFS and applications across several lessons. |
| [18 - DFS in directed graphs](<./[18] Graphs - Depth-First-Search in Directed Graphs/>) | Directed-graph traversal and Tarjan's strongly connected components algorithm. |
| [19 - Breadth-first search](<./[19] Graphs - Breadth-First-Search/>) | BFS, shortest-path counting, distances between sets, and constrained-path exercises. |
| [20 - Dijkstra's algorithm](<./[20] Weighted Graphs - Dijkstra Algorithm/>) | Weighted shortest paths, successive implementation variants, a min-heap version, and applications. |
| [21 - Activity selection](<./[21] Greedy Algorithms - Activity Selection/>) | Greedy selection of compatible activities. |
| [22 - Interval partitioning](<./[22] Greedy Algorithms - Interval Partition/>) | Greedy allocation of activities to resources. |
| [23 - Prim's algorithm](<./[23] Minimum Spanning Trees - Prim Algorithm/>) | Minimum spanning trees, from simpler approaches to a min-heap implementation. |
| [24 - Kruskal's algorithm](<./[24] Minimum Spanning Trees - Kruskal Algorithm/>) | Multiple minimum-spanning-tree variants, including disjoint-set operations. |
| [25 - Vertex cover](<./[25] Approx Algorithms - Vertex Cover - Graphs & HyperGraphs/>) | Heuristics and approximation approaches for graphs and hypergraphs. |
| [26 - K-center](<./[26] Approx Algorithms - K Center Problem/>) | Center selection, weighted variants, and exact-solution comparisons. |
| [27 - Knapsack](<./[27] Approx Algorithms - Knapsack Problem/>) | Exact value-based dynamic programming and a fully polynomial-time approximation scheme (FPTAS), with a bookshelf example. |
| [28 - Divide and conquer: exponentiation](<./[28] Divide Et Impera - Exponentiation/>) | Iterative powers versus recursive exponentiation by squaring. |

## Contributing

Corrections to implementations, explanations, complexity analysis, and examples are welcome, as are clearer translations and reproducible bug reports.

Open an issue describing the topic, exact file and function, input, expected result, and observed behavior. For a proposed change, submit a focused pull request that follows the existing numbered organization and preserves neighboring examples and imports. Include a small reproducible example or focused test where appropriate, explain any algorithmic assumptions, and state which examples you ran and with which Python version. Update this guide when adding or renaming a topic.

Avoid committing generated caches, virtual environments, or editor-specific files.

## License

No license file is currently included. Public availability does not grant an open-source license; obtain the author's permission before copying, modifying, or redistributing material beyond what applicable law or GitHub's terms permit.