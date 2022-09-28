import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

result = [0]*(n+1)

def dfs(r):
    visited = [False] * (n + 1)

    deq = deque([])
    deq.append(r)
    visited[r] = True

    while deq:
        a = deq.popleft()
        for i in graph[a]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True

    return visited.count(True)

for i in range(n+1):
    result[i] += dfs(i)

result_print = []
m = max(result)
for i,j in enumerate(result[1:]):
    if j==m:
        result_print.append(i+1)

print(*result_print, sep=' ')