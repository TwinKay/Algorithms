import sys
from collections import deque

f,s,g,u,d = map(int,sys.stdin.readline().split())
visited = [False]*(f+1)
visited[0] = True

deq = deque([[s,0]])
visited[s] = True

while deq:
    s,cnt = deq.popleft()

    if s == g:
        res = cnt
        break

    us = s+u ; ds = s-d
    if 1 <= us <= f:
        if not visited[us]:
            deq.append([us,cnt+1])
            visited[us] = True
    if 1 <= ds <= f:
        if not visited[ds]:
            deq.append([ds,cnt+1])
            visited[ds] = True
try:
    print(res)
except:
    print('use the stairs')