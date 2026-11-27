# Algorithms and Data Structures

An implementation-first guide to algorithms and data structures, developed from the **Introduzione agli Algoritmi** (Introduction to Algorithms) coursework at **Sapienza University of Rome**.

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

**Recent expansion (August-November 2026):** the repository now includes graph traversal and its applications, weighted shortest paths, greedy scheduling, minimum spanning trees, approximation algorithms on graphs and hypergraphs, exact and approximate knapsack solvers, and exponentiation by squaring. The topic guide uses the current numbered folder names introduced in November.

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

## Getting started

### Requirements

- **Python 3** for the main collection. Use a currently supported Python release; the repository does not declare a tested minimum version or a supported-version matrix.
- **Git** to clone the repository, or download and extract its ZIP from GitHub.
- **Optional:** NumPy and Matplotlib for scripts that import them; JupyterLab for notebooks.

There is no repository-wide dependency manifest or package-installation step. Dependencies vary by example. Go and Java tools are only needed for the corresponding alternative-language examples.

### Run a first example

Clone the repository and enter its root directory:

```bash
git clone https://github.com/GCRA101/Algorithms-and-Data-Structures.git
cd Algorithms-and-Data-Structures
```

The exponentiation example uses only Python's standard library. Run it in interactive mode so you can inspect the values it computes:

```bash
python -i "[28] Divide Et Impera - Exponentiation/Python/Lez18a_Divide Et Impera - Calcolo Potenze.py"
```

At the Python prompt:

```pycon
>>> pwIter, pwRec
(256, 256)
>>> powerRecursion(3, 5)
243
>>> exit()
```

The bundled example computes `2 ** 8` using both approaches. For positive integer exponents, compare the iterative method's linear number of multiplications with exponentiation by squaring's logarithmic number. These are operation counts, not a claim that multiplication of arbitrarily large integers takes constant time.

Commands here use `python`; use `python3` or `py` if that is how your system invokes Python 3. Keep paths quoted: folder and file names contain spaces, brackets, and other shell-significant characters.

### Optional: plotting and notebooks

Create an isolated environment before installing optional dependencies:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For the search and sorting examples that use NumPy and Matplotlib:

```bash
python -m pip install numpy matplotlib
python "[02] Search Algorithms/Binary Search.py"
```

This example opens a plot comparing best- and worst-case binary-search timings. Use a graphical environment to view it; measured runtimes are illustrative and may be noisy.

To work with the `.ipynb` files:

```bash
python -m pip install jupyterlab
jupyter lab
```

Open a notebook from the topic guide, such as `Le Equazioni di Ricorrenza.ipynb` in topic 04. Use the environment containing any dependencies imported by the notebook.

## Working with the material

### File layout and learning aids

Earlier topics usually keep scripts and notebooks directly in the topic folder. Later topics often use `Python/` or `LezXX/Python/` subfolders. Internal lesson numbers do not always match the top-level topic number; use the topic guide rather than guessing a path.

| Material | How to use it |
| --- | --- |
| `.py` scripts | Read the algorithm, complexity annotations, and embedded examples together. |
| `.ipynb` notebooks | Work through explanations and executable cells interactively. |
| `.drawio` diagrams | Open with diagrams.net or a compatible editor to inspect graph examples and worked solutions. |
| PDFs and images | Consult the supporting visual explanations where included. |
| `Esercizi` files | Practice exercises; *esercizi* is Italian for *exercises*. |

Some scripts print results or display plots; others leave results in variables for inspection in Python's interactive mode or an IDE such as Spyder. Many execute example code at the top level, so importing a file can also run its demonstrations. Keep neighboring helper modules together when running multi-file examples.

### Interpret results and complexity carefully

The collection deliberately includes multiple approaches to the same problem, including simpler, inefficient, or explicitly labeled incorrect versions for comparison. Read the comments and choose the intended variant rather than assuming every function is interchangeable.

Check the problem model before interpreting a result: binary search needs sorted input; Dijkstra requires nonnegative edge weights; minimum spanning trees and shortest-path trees solve different problems. Approximation guarantees depend on the specific algorithm and its assumptions, and do not automatically apply to every heuristic or weighted variant in the same folder.

For graph discussions, `n` generally denotes vertices and `m` edges; inspect each script's notation and representation. Separate theoretical operation counts from Python implementation costs and wall-clock timings. Before using an example in an application, check input validation, edge cases, mutation, return values, and scaling for your use case.

The repository currently has no repository-wide automated test suite or CI configuration. Embedded examples are useful for exploration, but are not a substitute for application-specific correctness and performance checks.

## Contributing

Corrections to implementations, explanations, complexity analysis, and examples are welcome, as are clearer translations and reproducible bug reports.

Open an issue describing the topic, exact file and function, input, expected result, and observed behavior. For a proposed change, submit a focused pull request that follows the existing numbered organization and preserves neighboring examples and imports. Include a small reproducible example or focused test where appropriate, explain any algorithmic assumptions, and state which examples you ran and with which Python version. Update this guide when adding or renaming a topic.

Avoid committing generated caches, virtual environments, or editor-specific files.

## License

No license file is currently included. Public availability does not grant an open-source license; obtain the author's permission before copying, modifying, or redistributing material beyond what applicable law or GitHub's terms permit.
