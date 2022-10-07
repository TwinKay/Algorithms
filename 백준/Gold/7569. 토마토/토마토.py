import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())

graph = []
for _ in range(h):
    graph.append([])

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

visited = []
for _ in range(h):
    visited.append([])

for i in range(h):
    for j in range(n):
        visited[i].append([0]*m)

def bfs():
    deq = deque([])
    for z,i in enumerate(graph):
        for y,j in enumerate(i):
            for x,k in enumerate(j):
                if k == 1:
                    deq.append([x,y,z])
                    visited[z][y][x] = 1    # 결과값에서 1빼주기
    while deq:
        x,y,z = deq.popleft()

        if x+1 != m:
            if visited[z][y][x+1] == 0 and graph[z][y][x+1] == 0:
                deq.append([x+1,y,z])
                visited[z][y][x+1] = visited[z][y][x] + 1
                graph[z][y][x+1] = 1

        if x != 0:
            if visited[z][y][x-1] == 0 and graph[z][y][x-1] == 0:
                deq.append([x-1,y,z])
                visited[z][y][x-1] = visited[z][y][x] + 1
                graph[z][y][x-1] = 1

        if y+1 != n:
            if visited[z][y+1][x] == 0 and graph[z][y+1][x] == 0:
                deq.append([x,y+1,z])
                visited[z][y+1][x] = visited[z][y][x] + 1
                graph[z][y+1][x] = 1

        if y != 0:
            if visited[z][y-1][x] == 0 and graph[z][y-1][x] == 0:
                deq.append([x,y-1,z])
                visited[z][y-1][x] = visited[z][y][x] + 1
                graph[z][y-1][x] = 1

        if z+1 != h:
            if visited[z+1][y][x] == 0 and graph[z+1][y][x] == 0:
                deq.append([x,y,z+1])
                visited[z+1][y][x] = visited[z][y][x] + 1
                graph[z+1][y][x] = 1

        if z != 0:
            if visited[z-1][y][x] == 0 and graph[z-1][y][x] == 0:
                deq.append([x,y,z-1])
                visited[z-1][y][x] = visited[z][y][x] + 1
                graph[z-1][y][x] = 1


bfs()

graph_1 = []
for i in graph:
    for j in i:
        graph_1.extend(j)

visited_1 = []
for i in visited:
    for j in i:
        visited_1.extend(j)

if 0 in graph_1:
    print(-1)
else:
    print(max(visited_1)-1)