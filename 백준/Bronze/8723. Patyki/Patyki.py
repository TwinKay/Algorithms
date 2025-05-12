import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
    print(2)
else:
    sides = sorted([a, b, c])
    x, y, z = sides
    if x * x + y * y == z * z:
        print(1)
    else:
        print(0)