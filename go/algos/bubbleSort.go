package algos

import "fmt"

func bubbleSort(arr []int) {
	for i := 0; i < len(arr)-1; i++ {
		for j := 0; j < len(arr)-1-i; j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp
			}
		}
	}
}

func recursiveBubbleSort(arr []int) {
	if len(arr) <= 1 {
		return
	}
	recursiveBubbleSort(arr[1:])
	for i := 0; i < len(arr)-1; i++ {
		if arr[i] > arr[i+1] {
			temp := arr[i+1]
			arr[i+1] = arr[i]
			arr[i] = temp
		}
	}
}

func main() {
	arr := []int{2, 7, 1, 3, 5, 4, 6, 9, 8}
	bubbleSort(arr)
	fmt.Println(arr)
}
