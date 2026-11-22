package main

// IMPORT PACKAGES
import (
	"fmt"
	"strconv"
)

// MAIN FUNCTION
func main() {

	// 1. Matrice di Adiacenza del Grafo con Pozzo Universale al Nodo 2
	matrix := [][]int{
		{0, 1, 1, 0, 0}, // Riga di adiacenza del nodo 0
		{0, 0, 1, 0, 0}, // Riga di adiacenza del nodo 1
		{0, 0, 0, 0, 0}, // Riga di adiacenza del nodo 2
		{0, 0, 1, 0, 0}, // Riga di adiacenza del nodo 3
		{0, 1, 1, 0, 0}, // Riga di adiacenza del nodo 4
	}

	// 2. Ricerca Pozzo Universale - T(n)=O(n^2)
	fmt.Println("Il pozzo universale calcolato con l'algoritmo 1 e' il nodo " +
		strconv.Itoa(pozzoUniversale1(matrix)))
	// 2. Ricerca Pozzo Universale - T(n)=O(n)
	fmt.Println("Il pozzo universale calcolato con l'algoritmo 2 e' il nodo " +
		strconv.Itoa(pozzoUniversale2(matrix)))
}
