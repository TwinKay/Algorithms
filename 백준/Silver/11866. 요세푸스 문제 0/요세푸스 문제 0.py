import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

total = deque(list(range(1,n+1)))

print('<', end='')
for i in range(n):
    if i == n-1:
        print(total.popleft(), end = '>')

    else:
        total.rotate((k-1)*(-1))
        print(total.popleft(), end = ', ')