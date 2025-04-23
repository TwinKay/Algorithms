import sys

ds, ys = map(int, sys.stdin.readline().split())
dm, ym = map(int, sys.stdin.readline().split())

for t in range(1, 5001):
    if (ds + t) % ys == 0 and (dm + t) % ym == 0:
        print(t)
        break
