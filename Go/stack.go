package main

import (
	"fmt"
)

func stack(array []int, size int) {
	for i := 0; i < size; i++ {
		fmt.Printf("Enter %dth element: ", i)
		fmt.Scanf("%d", &array[i])
	}
	fmt.Println(array)
}

func main() {
	var size int
	fmt.Printf("Enter the size of array: ")
	fmt.Scanln(&size)
	var stack_array = make([]int, size)
	stack(stack_array, size)

}
