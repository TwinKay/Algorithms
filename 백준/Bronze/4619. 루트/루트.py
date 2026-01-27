import sys
import math

while True:
    B, N = map(int, sys.stdin.readline().split())
    if B == 0 and N == 0:
        break

    best_A = 1
    best_diff = abs(1**N - B)

    limit = int(B ** (1 / N)) + 2

    for A in range(1, limit + 1):
        value = A ** N
        diff = abs(value - B)
        if diff < best_diff:
            best_diff = diff
            best_A = A

    print(best_A)