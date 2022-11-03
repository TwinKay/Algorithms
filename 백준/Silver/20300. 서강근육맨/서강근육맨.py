import sys
from collections import deque

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
lost.sort()
lost = deque(lost)

if len(lost)%2 == 0:
    m = 0
    while lost:
        m = max(m,lost.popleft()+lost.pop())

else:
    m = lost.pop()
    while lost:
        m = max(m, lost.popleft() + lost.pop())

print(m)