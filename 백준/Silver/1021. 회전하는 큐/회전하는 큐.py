import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
deq = deque(list(range(1,n+1)))

numbers = list(map(int, sys.stdin.readline().split()))

t = 0
for i in numbers:
    n_1 = 0
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            deq.rotate(-1)
            n_1 += 1
    n_2 = len(deq)+1-n_1
    t += min(n_1, n_2)

print(t)