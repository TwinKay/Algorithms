import sys
from collections import deque

n = int(sys.stdin.readline())
total = deque(list(range(1,n+1)))

for _ in range(n-1):
    total.popleft()
    total.append(total.popleft())


print(total.popleft())