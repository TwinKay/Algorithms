import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque(list(range(1,n+1)))
result = []

for _ in range(n):
    result.append(deq.popleft())
    deq.rotate(-1)

print(' '.join(list(map(str,result))))