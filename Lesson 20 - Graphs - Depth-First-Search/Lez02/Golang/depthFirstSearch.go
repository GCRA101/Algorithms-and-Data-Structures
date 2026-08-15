package main

// DEPTH FIRST SEARCH (DFS) on ADJACENCY LIST -------------------------------------*/
// --------------------------------------------------------------------------------*/

// DEPTH FIRST SEARCH (DFS) - Internal Recursive Search Function for Adj List

func DFS_recursive_al(x int, adjList [][]int, visited []bool) { // 		S(m)
	// 1. Register node x as visited
	visited[x] = true // 												Θ(1)
	// 2. Flick through all nodes adjacent to x
	for _, y := range adjList[x] { //									k*Θ(1)+Θ(1)
		/* 3. If the adjacent node hasn't been visited yet,
		call the recursive function on it. */
		if visited[y] == false { // 									Θ(1)
			DFS_recursive_al(y, adjList, visited) // 					S(v)
		}
	}
}

// Computational Cost/Complexity:	O(m) - WORST CASE
//			                       	Ω(1) - BEST CASE

// DEPTH FIRST SEARCH (DFS) - Graph represented with ADJACENCY LIST

func DFS_al(u int, adjList [][]int) []bool { // 						T(n)
	// 1. Initialize the Visited array
	visited := make([]bool, len(adjList)) // 							Θ(n)
	// 2. Run the Recursive DFS
	DFS_recursive_al(u, adjList, visited) //							S(m)
	// £. Return the Visited array
	return visited // 													Θ(1)
}

// Computational Cost/Complexity:	O(n+m) - WORST CASE
//			                       	Ω(n) - BEST CASE

// DEPTH FIRST SEARCH (DFS) on ADJACENCY MATRIX -----------------------------------*/
// --------------------------------------------------------------------------------*/

// DEPTH FIRST SEARCH (DFS) - Internal Recursive Search Function for Adj Matrix

func DFS_recursive_am(x int, adjMatrix [][]int, visited []bool) { // 	S(m)
	// 1. Register node x as visited
	visited[x] = true // 											 	Θ(1)
	// 2. Flick through all nodes in the graph
	for _, y := range adjMatrix[x] { //								 	k*Θ(1)+Θ(1)
		/* 3. If the node considered in adjacent to x and hasn't been
		visited yet, call the recursive function on it*/
		if adjMatrix[x][y] == 1 && visited[y] == false { // 		 	Θ(1)
			DFS_recursive_am(y, adjMatrix, visited) // 					S(v)
		}
	}
}

// Computational Cost/Complexity:	O(n^2) 	- WORST CASE
//			                       	Ω(1) 	- BEST CASE

// DEPTH FIRST SEARCH (DFS) - Graph represented with ADJACENCY MATRIX

func DFS_am(u int, adjMatrix [][]int) []bool { // 						T(n)
	// 1. Initialize the Visited array
	visited := make([]bool, len(adjMatrix)) // 							Θ(n)
	// 2. Run the Recursive DFS
	DFS_recursive_am(u, adjMatrix, visited) //							S(m)
	// £. Return the Visited array
	return visited // 													Θ(1)
}

func ConnectedCompsCount() {

}
