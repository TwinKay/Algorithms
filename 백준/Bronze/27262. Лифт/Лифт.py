import sys

n, k, a, b = map(int, sys.stdin.read().split())

elevator = (abs(k - 1) + (n - 1)) * b
stairs = (n - 1) * a

print(elevator, stairs)