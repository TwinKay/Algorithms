import sys

N,M = map(int, sys.stdin.readline().split())
arr = list(i for i in range(N+1))
for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    temp_arr = arr[i:j+1]
    temp_arr.reverse()
    for idx in range(i,j+1):
        arr[idx] = temp_arr[idx-i]
print(" ".join(map(str, arr[1:])))