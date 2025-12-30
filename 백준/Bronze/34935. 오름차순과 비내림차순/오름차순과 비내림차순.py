import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
is_ASC = True
if N > 1:
    for i in range(1,N):
        if arr[i] <= arr[i-1]:
            is_ASC = False
            break
if is_ASC:
    print(1)
else:
    print(0)