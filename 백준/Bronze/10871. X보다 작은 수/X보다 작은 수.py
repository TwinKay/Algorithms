import sys

N,X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = []
for i in arr:
    if i < X:
        res.append(i)
print(' '.join(map(str,res)))