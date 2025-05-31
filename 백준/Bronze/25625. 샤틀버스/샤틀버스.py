import sys

x, y = map(int, sys.stdin.readline().split())
if y < x:
    print(x + y)
else:
    print(y - x)