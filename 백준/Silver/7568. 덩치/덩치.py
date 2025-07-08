import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
res = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt+=1
    res.append(cnt+1)
print(" ".join(map(str,res)))