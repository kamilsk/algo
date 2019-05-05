# python3
from collections import namedtuple
from itertools import product
from sys import stdin
from typing import List
from unittest import TestCase

test = namedtuple('test', 'souvenirs expected')


def magic_partition3(souvenirs: List[int]) -> bool:
    """
    Performance:
    4  -> 243
    11 -> 35262
    """
    total = sum(souvenirs)
    if total % 3 != 0:
        return False

    for c in product(range(3), repeat=len(souvenirs)):
        sums = [0] * 3
        for i in range(3):
            sums[i] = sum(souvenirs[k] for k in range(len(souvenirs)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return True

    return False


def dynamic_partition3(souvenirs: List[int]) -> bool:
    """
    Performance:
    4  -> 676
    11 -> 1386275
    """
    total = sum(souvenirs)
    if total % 3 != 0:
        return False

    size = total // 3
    table = [[False for _ in range(total + 1)] for _ in range(total + 1)]
    table[0][0] = True

    for i in range(len(souvenirs)):
        j = total
        while j >= 0:
            k = total
            while k >= 0:
                if table[j][k]:
                    table[j + souvenirs[i]][k] = True
                    table[j][k + souvenirs[i]] = True
                k -= 1
            j -= 1

    return table[size][size]


class Test(TestCase):
    def test_partition3(self):
        tests = [
            # samples
            test([3, 3, 3, 3], False),
            test([40], False),
            test([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], True),
            test([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], True),
        ]
        for i, t in enumerate(tests):
            self.assertEqual(t.expected, dynamic_partition3(t.souvenirs), msg='at {} position'.format(i))


if __name__ == '__main__':
    _, *A = list(map(int, stdin.read().split()))
    print(1 if dynamic_partition3(A) else 0)
