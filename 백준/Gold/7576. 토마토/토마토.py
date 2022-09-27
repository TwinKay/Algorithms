import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())

graph = []
deq = deque([])
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


for a, i in enumerate(graph):
    for b, j in enumerate(i):
        if j == 1:
            deq.append([b,a])


while deq:
    x,y = deq.popleft()

    if x != m-1:
        if graph[y][x+1] == 0:
            graph[y][x+1] = graph[y][x] + 1
            deq.append([x+1, y])

    if x != 0:
        if graph[y][x-1] == 0:
            graph[y][x-1] = graph[y][x] + 1
            deq.append([x-1, y])

    if y != n-1:
        if graph[y+1][x] == 0:
            graph[y+1][x] = graph[y][x] + 1
            deq.append([x, y+1])

    if y != 0:
        if graph[y-1][x] == 0:
            graph[y-1][x] = graph[y][x] + 1
            deq.append([x, y-1])

t = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        else:
            t = max(t, j)
print(t-1)