package main

import "fmt"

func move(start, to string) {
	fmt.Printf("%s -> %s\n", start, to)
}

func hanoi(n int, start, to, via string) {
	if n == 1 {
		move(start, to)
	} else {
		hanoi(n-1, start, via, to)
		move(start, to)
		hanoi(n-1, via, to, start)
	}
}

func main() {
	hanoi(3, "A", "B", "C")
}
