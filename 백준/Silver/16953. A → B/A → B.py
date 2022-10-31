import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())

result = []
deq = deque([[a,0]])
while deq:
    a,cnt = deq.popleft()

    if a>b:
        pass
    elif a==b:
        result.append(cnt)
    else:
        cnt += 1
        deq.append([a*2,cnt])
        deq.append([a*10+1,cnt])

if len(result) == 0:
    print(-1)
else:
    print(min(result)+1)