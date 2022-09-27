import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = []
for _ in range(n):
    visited.append([False]*m)

deq = deque([[0,0]])

while deq:
    x,y = deq.popleft()

    if y != n-1:
        if visited[y+1][x] == False and graph[y+1][x] != 0:
            graph[y+1][x] = graph[y][x] + 1
            deq.append([x,y+1])
            visited[y+1][x] = True

    if y != 0:
        if visited[y-1][x] == False and graph[y-1][x] != 0:
            graph[y-1][x] = graph[y][x] + 1
            deq.append([x, y-1])
            visited[y-1][x] = True

    if x != m-1:
        if visited[y][x+1] == False and graph[y][x+1] != 0:
            graph[y][x+1] = graph[y][x] + 1
            deq.append([x+1, y])
            visited[y][x+1] = True

    if x != 0:
        if visited[y][x-1] == False and graph[y][x-1] != 0:
            graph[y][x-1] = graph[y][x] + 1
            deq.append([x-1, y])
            visited[y][x-1] = True

print(graph[n-1][m-1])