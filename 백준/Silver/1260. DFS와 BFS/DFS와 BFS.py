import sys
from collections import deque

n,m,r = map(int, sys.stdin.readline().split())

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)
v = []
ord_dfs = []
ord_bfs = []

for _ in range(n+1):
    v.append([])

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

for i in v:
    i.sort()

def dfs(r):
    visited_dfs[r] = True
    ord_dfs.append(r)

    for i in v[r]:
        if not visited_dfs[i]:
            dfs(i)

def bfs():
    deq = deque([r])
    visited_bfs[r] = True

    while deq:
        a = deq.popleft()
        ord_bfs.append(a)

        for i in v[a]:
            if not visited_bfs[i]:
                deq.append(i)
                visited_bfs[i] = True

dfs(r)
bfs()

print(' '.join(list(map(str, ord_dfs))))
print(' '.join(list(map(str, ord_bfs))))