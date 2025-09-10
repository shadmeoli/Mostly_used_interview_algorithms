package main

import "fmt"

func IncreasingPairs(arr []int) [][]int {
	var pairs [][]int
	for idx, val := range arr {
		if idx+1 < len(arr) {
			if arr[idx+1] > val {
				pairs = append(pairs, []int{val, arr[idx+1]})
			}
		}
	}
	return pairs
}
func main() {
	vals := []int{1, 3, 2, 4, 9, 12, 8, 7}
	fmt.Print(IncreasingPairs(vals))

}
