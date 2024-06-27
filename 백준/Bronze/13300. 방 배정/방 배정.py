import sys

n,k = map(int, sys.stdin.readline().split())

girls = [0]*6
boys = [0]*6

for _ in range(n):
    s,y = map(int, sys.stdin.readline().split())
    if s == 0:
        girls[y-1] += 1
    else:
        boys[y-1] += 1

res = 0
for i in girls:
    if i == 0:
        pass
    elif i%k == 0:
        res += i//k
    else:
        res += i//k+1
for i in boys:
    if i == 0:
        pass
    elif i%k == 0:
        res += i//k
    else:
        res += i//k+1

print(res)