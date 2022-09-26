import sys
from collections import deque
sys.setrecursionlimit(((10**9)))

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

def dfs(v, r, visited_dfs):
    visited_dfs[r] = True
    ord_dfs.append(r)

    for i in v[r]:
        if not visited_dfs[i]:
            dfs(v, i, visited_dfs)

def bfs(v, r, visited_bfs):
    visited_bfs[r] = True
    deq = deque([r])

    while deq:
        a = deq.popleft()
        ord_bfs.append(a)

        for i in v[a]:
            if not visited_bfs[i]:
                deq.append(i)
                visited_bfs[i] = True

dfs(v, r, visited_dfs)
bfs(v, r, visited_bfs)

print(' '.join(list(map(str, ord_dfs))))
print(' '.join(list(map(str, ord_bfs))))