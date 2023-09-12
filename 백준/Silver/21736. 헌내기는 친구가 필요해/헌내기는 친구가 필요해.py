import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
visited = []
for i in range(n):
    l = list(sys.stdin.readline().rstrip())
    graph.append(l)
    visited.append([False]*m)
    if 'I' in l:
        x,y = l.index('I'),i

cnt = 0
deq = deque([[x,y]])
visited[y][x] = True
while deq:
    x,y = deq.popleft()

    if x-1 != -1:
        if not visited[y][x-1] and graph[y][x-1] != 'X':
            deq.append([x-1, y])
            visited[y][x-1] = True
            if graph[y][x-1] == 'P':
                cnt += 1
    
    if x+1 != m:
        if not visited[y][x+1] and graph[y][x+1] != 'X':
            deq.append([x+1, y])
            visited[y][x+1] = True
            if graph[y][x+1] == 'P':
                cnt += 1

    if y-1 != -1:
        if not visited[y-1][x] and graph[y-1][x] != 'X':
            deq.append([x, y-1])
            visited[y-1][x] = True
            if graph[y-1][x] == 'P':
                cnt += 1

    if y+1 != n:
        if not visited[y+1][x] and graph[y+1][x] != 'X':
            deq.append([x, y+1])
            visited[y+1][x] = True
            if graph[y+1][x] == 'P':
                cnt += 1

if not cnt:
    print('TT')
else:
    print(cnt)