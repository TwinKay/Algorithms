import sys

n = int(sys.stdin.readline())
line = list(map(int,sys.stdin.readline().split()))
res = []

for i in range(n):
    res.insert(i-line[i],i+1)
res = list(map(str,res))

print(' '.join(res))