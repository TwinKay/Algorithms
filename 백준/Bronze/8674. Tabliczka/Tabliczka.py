import sys

a, b = map(int, sys.stdin.readline().split())
result = min(b * (a % 2), a * (b % 2))
print(result)