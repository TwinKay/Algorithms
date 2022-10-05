import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append([])

for i in range(n):
    for k,j in enumerate(list(map(int, sys.stdin.readline().split()))):
        if j == 1:
            graph[i].append(k)

for i in range(n):
    deq = deque([i])
    visited = [0]*n

    while deq:
        a = deq.popleft()
        for j in graph[a]:
            if visited[j] == 0:
                deq.append(j)
                visited[j] = 1

    print(' '.join(map(str, visited)))