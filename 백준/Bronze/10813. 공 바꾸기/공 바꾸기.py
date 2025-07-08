import sys

N,M = map(int, sys.stdin.readline().split())
arr = list(i for i in range(N+1))
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a], arr[b] = arr[b], arr[a]
print(" ".join(map(str, arr[1:])))