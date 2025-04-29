import sys

p = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())

res = 0
for i, pi in enumerate(p, start=1):
    if pi == x:
        res = i
        break
print(res)
