import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt_arr = [0]*51
for a in arr:
    cnt_arr[a] += 1

res = -1
for i in range(50,0,-1):
    if i == cnt_arr[i]:
        res = i
        break

if res == -1:
    if cnt_arr[0] == 0:
        res = 0

print(res)