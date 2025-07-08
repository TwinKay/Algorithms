import sys

N,M = map(int, sys.stdin.readline().split())
arr = list(0 for i in range(N))
for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().split())
    i -= 1; j -= 1
    for idx in range(i,j+1):
        arr[idx] = k
print(" ".join(map(str, arr)))