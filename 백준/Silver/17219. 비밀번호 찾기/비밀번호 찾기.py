import sys

n,m = map(int, sys.stdin.readline().split())

total = {}
for _ in range(n):
    a,b = sys.stdin.readline().strip().split()
    total[a] = b

for _ in range(m):
    x = sys.stdin.readline().strip()
    print(total[x])