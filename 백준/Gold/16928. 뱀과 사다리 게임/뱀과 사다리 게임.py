import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

lad = dict()
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    lad[a] = b

sna = dict()
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    sna[a] = b

visited = [False]*101
cnt = [0]*101

# bfs
deq = deque([1])
visited[1] = True

while deq:
    a = deq.popleft()
    for i in range(1,7):
        b = a+i
        if b<=100 and not visited[b]:
            if b in lad.keys():
                b = lad[b]
            elif b in sna.keys():
                b = sna[b]

            if not visited[b]:
                deq.append(b)
                visited[b] = True
                cnt[b] = cnt[a]+1

print(cnt[100])