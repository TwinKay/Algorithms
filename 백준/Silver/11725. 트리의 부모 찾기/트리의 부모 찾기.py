import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n+1):
    graph.append([])

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False]*(n+1)
result = [0]*(n+1)


deq = deque([1])
while deq:
    a = deq.popleft()
    result.append(a)
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            result[i] += a
            deq.append(i)

for i in result[2:n+1]:
    print(i)