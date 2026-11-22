package main

/* VERIFICA POZZO UNIVERSALE in O(n) --------------------------------------------------------------------------------*/
// Scorri tutte le celle della Matrice di Adiacenza (ovvero i Nodi del Grafo) e se il nodo i non e' diverso da u e non
// ha arco entrante in u oppure u ha arco uscente in i, u non puo' essere pozzo universale, quindi ritorna false...
// ... se tutti i nodi i hanno arco entrante in u e u non ha archi uscenti in essi, u e' pozzo universale.

func pozzo(u int, M [][]int) bool { // 							T(n)
	for i := 0; i < len(M); i++ { // 							n*Θ(1)+Θ(1)
		if !(i == u) && (M[i][u] == 0 || M[u][i] == 1) { // 	Θ(1)
			return false // 									Θ(1)
		}
	}
	return true // 												Θ(1)
}

// Costo Computazionale: O(n) - CASO PEGGIORE
//                       Ω(1) - CASO MIGLIORE
//

/* RICERCA POZZO UNIVERSALE in O(n^2) -------------------------------------------------------------------------------*/
/* Scorri tutte le celle della Matrice di Adiacenza (ovvero i Nodi del Grafo) e verifica se il nodo e' pozzo universale
del grafo. Se lo e', interrompi il ciclo e ritorna l'indice del nodo. Altrimenti, ritorna -1 per indicare che un pozzo
universale non esiste. */

func pozzoUniversale1(M [][]int) int { // 						T(n)
	for i := 0; i < len(M); i++ { // 							n*Θ(1)+Θ(1)
		if pozzo(i, M) { // 									n*Θ(1)+Θ(1)
			return i // 										Θ(1)
		}
	}
	return -1 // 												Θ(1)
}

// Costo Computazionale: O(n^2) - CASO PEGGIORE
//                       Ω(1)   - CASO MIGLIORE
//

/* RICERCA POZZO UNIVERSALE in O(n) ----------------------------------------------------------------------------------*/
/* Fissa un nodo (p) e scorri i restanti i nodi. Controlla se il nodo p ha un arco uscente verso il nodo i. Non appena
lo si trova, si ha la dimostrazione che il nodo p non puo' essere pozzo universale...quindi si considera il nodo i come
nuovo nodo fisso e lo si confronta con gli altri. Si verifica quindi se il nodo rimanente e' pozzo universale usando
l'algoritmo pozzo(u int, M [][]int). */

func pozzoUniversale2(M [][]int) int { // 						T(n)
	p := 0                        // 							Θ(1)
	for i := 0; i < len(M); i++ { // 							n*Θ(1)+Θ(1)
		if M[p][i] == 1 { // 									Θ(1)
			p = i // 											Θ(1)
		}
	}
	x := pozzo(p, M) // 										n*Θ(1)+Θ(1)
	if x == true {   // 										Θ(1)
		return p // 											Θ(1)
	}
	return -1 // 												Θ(1)
}

// Costo Computazionale: O(n)   - CASO PEGGIORE
//                       Ω(1)   - CASO MIGLIORE
//
