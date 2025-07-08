import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())
res = 0
for i in arr:
    if i == V:
        res += 1
print(res)