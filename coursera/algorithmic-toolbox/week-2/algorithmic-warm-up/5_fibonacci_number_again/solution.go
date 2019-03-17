package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

func fibonacciModulo(n, m int64) int64 {
	pisano := append(make([]int64, 0, n), 0, 1)
	modulo := big.NewInt(m)

	var prev, curr = big.NewInt(0), big.NewInt(1)
	for i, last := int64(0), 2; i < n-1; i++ {
		prev, curr = &(*curr), &(*prev.Add(curr, prev))
		pisano = append(pisano, curr.Mod(curr, modulo).Int64())
		for step := last; step < len(pisano)/2; step++ {
			if equal(pisano[:step], pisano[step:2*step]) {
				return pisano[n%int64(step)]
			}
			last = step + 1
		}
	}

	return curr.Mod(curr, modulo).Int64()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	_ = scanner.Scan()
	a, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	_ = scanner.Scan()
	b, _ := strconv.ParseInt(scanner.Text(), 10, 64)

	safe(fmt.Fprintln(os.Stdout, fibonacciModulo(a, b)))
}

func equal(a, b []int64) bool {
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func safe(interface{}, error) {}
