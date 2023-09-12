import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

maps = []
graph = []
visited = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    if 2 in l:
        x, y = l.index(2), i
    maps.append(l)
    graph.append([0]*m)
    visited.append([False]*m)

cnt = 0
deq = deque([[x, y, cnt]])
visited[y][x] = True
while deq:
    x, y, cnt = deq.popleft()

    if maps[y][x] != 0:
        graph[y][x] = cnt

    

    if x-1 != -1:
        if not visited[y][x-1] and maps[y][x-1] != 0:
            deq.append([x-1,y,cnt+1])
            visited[y][x-1] = True

    if x+1 != m:
        if not visited[y][x+1] and maps[y][x+1] != 0:
            deq.append([x+1,y,cnt+1])
            visited[y][x+1] = True

    if y-1 != -1:
        if not visited[y-1][x] and maps[y-1][x] != 0:
            deq.append([x,y-1,cnt+1])
            visited[y-1][x] = True

    if y+1 != n:
        if not visited[y+1][x] and maps[y+1][x] != 0:
            deq.append([x,y+1,cnt+1])
            visited[y+1][x] = True

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == False:
            graph[i][j] = -1

for i in graph:
    i = map(str, i)
    print(' '.join(i))