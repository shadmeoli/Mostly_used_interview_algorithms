package main

import (
	"fmt"
)

func bubbleSort(arr []int) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr); j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp
			}
		}
	}
}

func main() {
	arr := [4]int{1, 3, 2, 4}
	// bubble := bubbleSort(arr)
	// fmt.Println(bubble)
	fmt.Println(arr)
}
