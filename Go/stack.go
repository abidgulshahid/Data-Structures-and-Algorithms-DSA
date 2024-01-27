package main

import (
	"fmt"
)

func stack(array [5]int) {
	fmt.Println("Stack here")
	for i := 0; i <= len(array); i++ {
		fmt.Print("Remove Value? (y/n):")
		var input string
		fmt.Scan(&input)
		fmt.Print(input)

		fmt.Scan(input)
	}
}

func main() {
	stack_array := [5]int{1, 2, 3, 4, 5}
	stack(stack_array)

}
