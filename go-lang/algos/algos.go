package algos

import (
	"fmt"
	"strconv"
	"strings"
)

func finder(r int, target int) int {
	var count int
	for i := 0; i <= r; i++ {
		if strings.Contains(strconv.Itoa(i), strconv.Itoa(target)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(finder(100, 9))
}
