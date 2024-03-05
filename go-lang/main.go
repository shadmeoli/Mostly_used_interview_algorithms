package main

import (
	"fmt"
)

func main() {
	arr := [4]int{1, 3, 2, 4}
	bubble := bubbleSort(arr)
	fmt.Println(bubble)
}
