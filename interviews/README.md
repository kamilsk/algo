> # Интервью
>
> Подборка интересных задач, которые попадались мне на собеседованиях.

## Поиск уникального числа

Дан массив парных чисел, например, `[1, 3, 5, 3, 5, 1]`, `[6, 2, 2, 4, 6, 4]`.
В произвольное место такого массива добавляется число, отличное от остальных:
- для `[1, 3, 5, 3, 5, 1]` -> `[1, 3, 5, 7, 3, 5, 1]` такое число 7
- для `[6, 2, 2, 4, 6, 4]` -> `[6, 2, 2, 4, 1, 6, 4]` такое число 1

Задача найти это уникальное число за O(n) и O(1) по памяти.

<details><summary>👀</summary><p role="separator"></p>

Ограничение O(n) исключает предварительную сортировку, которую можно было бы
сделать in-place, чтобы вписаться в последнее ограничение. Оно же не позволит
применить структуру с константным доступом по ключу, типа hash table, т.к.
на её создание потребуется дополнительная память.

Акцент нужно делать на том, что одинаковых чисел в множестве чётное количество.
</details>

## Двусвязный список

Нужно реализовать двунаправленный связный список с минимальным потреблением памяти.

<details><summary>👀</summary><p role="separator"></p>

[XOR linked list](https://en.wikipedia.org/wiki/XOR_linked_list).
</details>

## Восстановление сортировки

Дан отсортированный массив из n чисел, k из которых были заменены произвольным
образом. Например,
- `[3, 6, 7, 10, 11, 15]` -> `[3, 6, 4, 10, 14, 15]`
- `[2, 4, 5, 23, 41, 60]` -> `[10, 4, 5, 23, 9, 60]`

Задача отсортировать такой массив меньше чем за n*log(n).

<details><summary>👀</summary><p role="separator"></p>

Для решения этой задачи нужно вспомнить алгоритм merge sort и переосмыслить
его в контексте знания о том, что исходный массив уже был отсортирован.
</details>

## Go и CPU

### [Branch predictor](https://en.wikipedia.org/wiki/Branch_predictor)

Нужно объяснить результат

```go
package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

func main() {
	arr := make([]int, 10_000_000)
	for i := 0; i < 10_000_000; i++ {
		arr[i] = i
	}
	calculate(arr)

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(arr), func(i, j int) { arr[i], arr[j] = arr[j], arr[i] })
	calculate(arr)

	sort.Ints(arr)
	calculate(arr)
}

func calculate(arr []int) {
	t := time.Now()
	s := 0
	for _, r := range arr {
		if r < 100_000/2 {
			s += r * 2
		} else {
			s += r
		}
	}
	fmt.Println("duration:", time.Since(t).Nanoseconds())
}

// duration: 3226301
// duration: 3738684 <- please explain
// duration: 3244984
```

### [CPU cache](https://en.wikipedia.org/wiki/CPU_cache)

Нужно объяснить результат

```go
package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

func main() {
	arr := make([]*int, 1_000_000)
	for i := 0; i < 1_000_000; i++ {
		i := i
		arr[i] = &i
	}
	calculate(arr)

	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(arr), func(i, j int) { arr[i], arr[j] = arr[j], arr[i] })
	calculate(arr)

	sort.Slice(arr, func(i, j int) bool { return *arr[i] < *arr[j] })
	calculate(arr)
}

func calculate(arr []*int) {
	t := time.Now()
	s := 0
	for _, r := range arr {
		s += *r
	}
	fmt.Println("duration:", time.Since(t).Nanoseconds())
}

// duration: 1369079
// duration: 14710353 <- please explain
// duration: 1050656
```
