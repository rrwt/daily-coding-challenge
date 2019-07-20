package main

import "fmt"

func gcd(a int, b int) int {
	for b != 0 {
		t := b
		b = a % t
		a = t
	}

	return a
}

func rotateArray(arr []int, n int, d int) []int {
	cd := gcd(n, d)

	for i := 0; i < cd; i++ {
		t := arr[i]
		j := i
		for true {
			k := j + d
			if k >= n {
				k -= n
			}
			if k == i {
				break
			}
			arr[j] = arr[k]
			j = k
		}
		arr[j] = t
	}

	return arr
}

func main() {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	for i := 0; i < 6; i++ {
		fmt.Println(rotateArray(arr, 10, i))
	}
}
