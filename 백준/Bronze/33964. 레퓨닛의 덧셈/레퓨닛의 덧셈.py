import sys

x, y = map(int, sys.stdin.readline().split())
rep_x = int("1" * x)
rep_y = int("1" * y)
print(rep_x + rep_y)