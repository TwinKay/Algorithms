# 코드가 난잡해... 다시 깔끔하게 풀 것!
import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
deq = deque(list(range(1,n+1)))

d = 0
direct = True

for i in range(n):
    if direct == True:
        if d == m:
            deq.rotate(k)
            print(deq.popleft())
            d = 1
            direct = False
        else:
            deq.rotate(-k + 1)
            print(deq.popleft())
            d += 1
    else:
        if d == m:
            deq.rotate(-k + 1)
            print(deq.popleft())
            d = 1
            direct = True
        else:
            deq.rotate(k)
            print(deq.popleft())
            d += 1