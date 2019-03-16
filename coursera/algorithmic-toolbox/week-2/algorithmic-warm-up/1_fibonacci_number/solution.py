# python3
def calc_fib_naive(n: int):
    if n <= 1:
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


def calc_fib(n: int):
    memo = list(range(max(2, n + 1)))
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


if __name__ == '__main__':
    print(calc_fib(int(input())))