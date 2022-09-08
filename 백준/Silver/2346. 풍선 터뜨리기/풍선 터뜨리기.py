# rotate 사용

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([])

deq_single = list(map(int, sys.stdin.readline().split()))
for i,j in enumerate(deq_single):
    deq.append((i+1, j))

for i in range(n):
    a = deq.popleft()
    if i+1 == n:
        print(a[0])
    else:
        print(a[0], end=' ')

    if a[1] > 0:
        deq.rotate(-a[1]+1)

    else:
        deq.rotate(-a[1])