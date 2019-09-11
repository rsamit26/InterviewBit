package main

import (
	"fmt"
	"math"
)

/**
 * @input a : Integer array
 * @input b : Integer array
 *
 * @Output Integer
 */

func coverPoints(a [3]int, b [3]int) int {
	mn := 0
	for i := 1; i < len(a); i++ {
		mn += (int)(math.Max(math.Abs((float64)(a[i]-a[i-1])), math.Abs((float64)(b[i]-b[i-1]))))
	}
	return mn
}

func main() {
	arr1 := [3]int{0, 1, 1}
	arr2 := [3]int{0, 1, 2}
	res := coverPoints(arr1, arr2)
	fmt.Println(res) // result out == 2

}
