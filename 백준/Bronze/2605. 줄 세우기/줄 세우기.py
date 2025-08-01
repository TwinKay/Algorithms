import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

res_arr = []
for i in range(N):
    res_arr.insert(arr[i],i+1)
print(*res_arr[::-1])