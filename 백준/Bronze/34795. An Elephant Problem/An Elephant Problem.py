import sys

m, d = map(int, sys.stdin.readline().split())

answer = (d + m - 1) // m
print(answer)