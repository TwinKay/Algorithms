import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(x,y,h):
    if graph[y][x] > h and visited[y][x] == False:

        deq = deque([[x,y]])
        visited[y][x] = True

        while deq:
            x,y = deq.popleft()

            if x-1 != -1:
                if visited[y][x-1] == False:
                    visited[y][x-1] = True
                    if graph[y][x-1] > h:
                        deq.append([x-1, y])

            if y-1 != -1:
                if visited[y-1][x] == False:
                    visited[y-1][x] = True
                    if graph[y-1][x] > h:
                        deq.append([x, y-1])

            if x+1 != n:
                if visited[y][x+1] == False:
                    visited[y][x+1] = True
                    if graph[y][x+1] > h:
                        deq.append([x+1, y])

            if y+1 != n:
                if visited[y+1][x] == False:
                    visited[y+1][x] = True
                    if graph[y+1][x] > h:
                        deq.append([x, y + 1])
        return 1

    else:
        return 0

result = []

for i in range(1,101):
    cnt = 0
    visited = []

    for _ in range(n):
        visited.append([False] * n)

    for j in range(n):
        for k in range(n):
            cnt += bfs(k,j,i)
    result.append(cnt)


if max(result) == 0:
    print(1)
else:
    print(max(result))