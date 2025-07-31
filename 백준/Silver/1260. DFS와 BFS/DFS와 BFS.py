'''
아이디어:
단순 dfs,bfs
'''

import sys
from collections import deque


sys.setrecursionlimit(10000)

def dfs(c):
    visited[c] = True
    dfs_res.append(c)
    for n in graph[c]:
        if not visited[n]:
            dfs(n)

def bfs(c):
    deq = deque()
    deq.append(c)
    visited[c] = True
    while deq:
        cur = deq.popleft()
        bfs_res.append(cur)
        for n in graph[cur]:
            if not visited[n]:
                deq.append(n)
                visited[n] = True


N,M,V = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N+1):
    graph.append([])


for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort() # 방문 우선순위

dfs_res = []
bfs_res = []

visited = [False]*(N+1)
dfs(V)
visited = [False]*(N+1)
bfs(V)

print(*dfs_res)
print(*bfs_res)