package main

import "fmt"

/**
 * @input A : Integer array
 *
 * @Output Integer array.
 */
func reverseArray(arr []int) []int {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
	return arr
}

func plusOne(A []int) []int {
	n := len(A)
	var arr []int
	var res []int
	reverseArr := reverseArray(A)
	carry := 1
	for i := 0; i < n; i++ {
		curr := reverseArr[i] + carry
		if curr >= 10 {
			reverseArr[i] = curr % 10
			carry = curr / 10
		} else {
			reverseArr[i] = curr
			carry = 0
			break
		}

	}
	arr = reverseArr
	if carry > 0 {
		arr = append(arr, carry)
	}
	arr = reverseArray(arr)
	var ind int
	for j := 0; j < len(arr); j++ {
		if arr[j] == 0 {
			continue
		} else {
			ind = j
			break
		}
	}
	res = arr[ind:]

	return res
}

func main() {
	s := []int{0, 3, 7, 6, 4, 0, 5, 5, 5}

	fmt.Println(plusOne(s))
}
