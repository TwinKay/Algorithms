import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = []
for _ in range(n):
    visited.append([False]*n)

def bfs(x,y):
    if visited[y][x] == False:
        c = graph[y][x]
        deq = deque([[x,y]])
        visited[y][x] = True
        while deq:
            a,b = deq.popleft()
            # visited[b][a] = True

            if b+1 != n:
                if visited[b+1][a] == False:
                    if graph[b+1][a] == c:
                        deq.append([a,b+1])
                        visited[b+1][a] = True
            if b-1 != -1:
                if visited[b-1][a] == False:
                    if graph[b-1][a] == c:
                        deq.append([a,b-1])
                        visited[b-1][a] = True

            if a+1 != n:
                if visited[b][a+1] == False:
                    if graph[b][a+1] == c:
                        deq.append([a+1,b])
                        visited[b][a+1] = True

            if a-1 != -1:
                if visited[b][a-1] == False:
                    if graph[b][a-1] == c:
                        deq.append([a-1,b])
                        visited[b][a-1] = True
        return 1
    return 0

cnt_1 = 0
for i in range(n):
    for j in range(n):
        cnt_1 += bfs(j,i)

for i in range(n):
    for j in range(n):
        if graph[j][i] == 'R':
            graph[j][i] = 'G'

visited = []
for _ in range(n):
    visited.append([False]*n)

cnt_2 = 0
for i in range(n):
    for j in range(n):
        cnt_2 += bfs(j,i)

print(cnt_1, cnt_2)