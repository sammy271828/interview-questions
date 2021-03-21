# CHAPTER 17: HARD PROBLEMS

import math

def two_missing(arr):
    N = len(arr) + 2

    A = N * (N + 1) / 2
    B = N * (N + 1) * (2 * N + 1) / 6

    for val in arr:
        A -= val
        B -= val ** 2

    print(A, B)
    print(A ** 2)
    print((A * A - B) / 2)

    print(2 * B + A ** 2, math.sqrt(2 * B - A ** 2))

    x = (A - math.sqrt(2 * B - A ** 2)) / 2
    y = A - x

    return [x, y]
