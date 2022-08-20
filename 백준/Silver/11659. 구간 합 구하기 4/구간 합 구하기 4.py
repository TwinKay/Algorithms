import sys

n,m = map(int, sys.stdin.readline().split())

total = list(map(int, sys.stdin.readline().split()))

total_sum = []
t = 0
for i in total:
    t += i
    total_sum.append(t)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(total_sum[b-1])
    else:
        print(total_sum[b-1] - total_sum[a-2])