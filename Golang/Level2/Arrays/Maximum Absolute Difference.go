package main

import (
	"fmt"
	"math"
)

/**
 * @input A : Integer array
 *
 * @Output Integer
 */
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func maxArr(A []int) int {
	max1 := math.MinInt64
	max2 := math.MinInt64
	min1 := math.MaxInt64
	min2 := math.MaxInt64
	res := 0
	for i := 0; i < len(A); i++ {
		max1 = max(max1, A[i]+i)
		max2 = max(max2, A[i]-i)
		min1 = min(min1, A[i]+i)
		min2 = min(min2, A[i]-i)
	}
	res = max(res, max2-min2)
	res = max(res, max1-min1)
	return max(max1-min1, max2-min2)

}

func main() {
	s := []int{0, 3, 7, 6, 4, 0, 5, 5, 5}
	fmt.Println(maxArr(s))
}
