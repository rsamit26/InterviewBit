package main

/**
 * @input A : Integer array
 *
 * @Output Integer
 */

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxSubArray(A []int) int {
	curr := A[0]
	res := A[0]
	for i := 1; i < len(A); i++ {
		curr = max(A[i], curr+A[i])
		res = max(res, curr)
	}
	return res
}

func main() {
	s := []int{0, 3, 7, 6, 4, 0, 5, 5, 5}
	fmt.Println(maxSubArray(s))
}
