package main

import (
	"fmt"
)

func main() {

	/* ADJACENT LISTS ---------------------------------------------------*/

	// Connected Graph
	AL_cg := [][]int{
		{1, 2},
		{2, 3, 4},
		{1, 4},
		{1, 2, 4},
		{},
	}

	// UnConnected Graph
	AL_ncg := [][]int{
		{1, 2},
		{0, 2},
		{0, 1},
		{4, 5},
		{3, 5},
		{3, 4},
		{},
	}

	/* ADJACENT MATRICES ---------------------------------------------------*/

	// Connected Graph
	AM_cg := [][]int{
		{0, 1, 1, 0, 0},
		{0, 0, 1, 1, 1},
		{0, 1, 0, 0, 1},
		{0, 1, 1, 0, 1},
		{0, 0, 0, 0, 0},
	}

	// UnConnected Graph
	AM_ncg := [][]int{
		{0, 1, 1, 0, 0, 0, 0},
		{1, 0, 1, 0, 0, 0, 0},
		{1, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 1, 1, 0},
		{0, 0, 0, 1, 0, 1, 0},
		{0, 0, 0, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0},
	}

	/* DFS with ADJACENT LISTS ---------------------------------------------------*/

	var va0, va1, va2, va3, va4, va5, va6 []bool

	// Connected Graph
	va0 = DFS_al(0, AL_cg) // Partendo da 0 si possono visitare tutti i nodi
	va1 = DFS_al(1, AL_cg) // Partendo da 1 si possono visitare tutti i nodi tranne l'1
	va2 = DFS_al(2, AL_cg) // Partendo da 2 si possono visitare tutti i nodi tranne l'1
	va3 = DFS_al(3, AL_cg) // Partendo da 3 si possono visitare tutti i nodi tranne l'1
	va4 = DFS_al(4, AL_cg) // Partendo da 4 si puo' visitare solo il nodo 4

	fmt.Println("DFS with Adjacency Lists - Connected Graph:\n" +
		"0 -> " + fmt.Sprint(va0) + "\n" +
		"1 -> " + fmt.Sprint(va1) + "\n" +
		"2 -> " + fmt.Sprint(va2) + "\n" +
		"3 -> " + fmt.Sprint(va3) + "\n" +
		"4 -> " + fmt.Sprint(va4) + "\n")

	// UnConnected Graph
	va0 = DFS_al(0, AL_ncg) // Partendo da 0 si possono visitare solo i nodi 1,2
	va1 = DFS_al(1, AL_ncg) // Partendo da 1 si possono visitare solo i nodi 0,2
	va2 = DFS_al(2, AL_ncg) // Partendo da 2 si possono visitare solo i nodi 0,1
	va3 = DFS_al(3, AL_ncg) // Partendo da 3 si possono visitare solo i nodi 4,5
	va4 = DFS_al(4, AL_ncg) // Partendo da 4 si possono visitare solo i nodi 3,5
	va5 = DFS_al(5, AL_ncg) // Partendo da 5 si possono visitare solo i nodi 3,4
	va6 = DFS_al(6, AL_ncg) // Partendo da 6 non si puo' visitare alcun nodo

	fmt.Println("DFS with Adjacency Lists - Unconnected Graph:\n" +
		"0 -> " + fmt.Sprint(va0) + "\n" +
		"1 -> " + fmt.Sprint(va1) + "\n" +
		"2 -> " + fmt.Sprint(va2) + "\n" +
		"3 -> " + fmt.Sprint(va3) + "\n" +
		"4 -> " + fmt.Sprint(va4) + "\n" +
		"5 -> " + fmt.Sprint(va5) + "\n" +
		"6 -> " + fmt.Sprint(va6) + "\n")

	/* DFS with ADJACENT MATRICES ---------------------------------------------------*/

	// Connected Graph
	va0 = DFS_am(0, AM_cg) // Partendo da 0 si possono visitare tutti i nodi
	va1 = DFS_am(1, AM_cg) // Partendo da 1 si possono visitare tutti i nodi tranne l'1
	va2 = DFS_am(2, AM_cg) // Partendo da 2 si possono visitare tutti i nodi tranne l'1
	va3 = DFS_am(3, AM_cg) // Partendo da 3 si possono visitare tutti i nodi tranne l'1
	va4 = DFS_am(4, AM_cg) // Partendo da 4 si puo' visitare solo il nodo 4

	fmt.Println("DFS with Adjacency Matrix - Connected Graph:\n" +
		"0 -> " + fmt.Sprint(va0) + "\n" +
		"1 -> " + fmt.Sprint(va1) + "\n" +
		"2 -> " + fmt.Sprint(va2) + "\n" +
		"3 -> " + fmt.Sprint(va3) + "\n" +
		"4 -> " + fmt.Sprint(va4) + "\n")

	// UnConnected Graph
	va0 = DFS_am(0, AM_ncg) // Partendo da 0 si possono visitare solo i nodi 1,2
	va1 = DFS_am(1, AM_ncg) // Partendo da 1 si possono visitare solo i nodi 0,2
	va2 = DFS_am(2, AM_ncg) // Partendo da 2 si possono visitare solo i nodi 0,1
	va3 = DFS_am(3, AM_ncg) // Partendo da 3 si possono visitare solo i nodi 4,5
	va4 = DFS_am(4, AM_ncg) // Partendo da 4 si possono visitare solo i nodi 3,5
	va5 = DFS_am(3, AM_ncg) // Partendo da 4 si possono visitare solo i nodi 3,5
	va6 = DFS_am(4, AM_ncg) // Partendo da 6 non si puo' visitare alcun nodo

	fmt.Println("DFS with Adjacency Matrix - UnConnected Graph:\n" +
		"0 -> " + fmt.Sprint(va0) + "\n" +
		"1 -> " + fmt.Sprint(va1) + "\n" +
		"2 -> " + fmt.Sprint(va2) + "\n" +
		"3 -> " + fmt.Sprint(va3) + "\n" +
		"4 -> " + fmt.Sprint(va4) + "\n" +
		"5 -> " + fmt.Sprint(va5) + "\n" +
		"6 -> " + fmt.Sprint(va6) + "\n")

}
