import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(m):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = []
for _ in range(m):
    visited.append([False]*n)

def bfs(x,y):
    if visited[y][x] == False:
        deq = deque([[x,y]])
        visited[y][x] = True
        cnt = 1
        while deq:
            x,y = deq.popleft()

            if y+1 != m:
                if graph[y+1][x] == graph[y][x] and visited[y+1][x] == False:
                    deq.append([x,y+1])
                    visited[y+1][x] = True
                    cnt += 1

            if y-1 != -1:
                if graph[y-1][x] == graph[y][x] and visited[y-1][x] == False:
                    deq.append([x,y-1])
                    visited[y-1][x] = True
                    cnt += 1

            if x+1 != n:
                if graph[y][x+1] == graph[y][x] and visited[y][x+1] == False:
                    deq.append([x+1, y])
                    visited[y][x+1] = True
                    cnt += 1

            if x-1 != -1:
                if graph[y][x-1] == graph[y][x] and visited[y][x-1] == False:
                    deq.append([x-1,y])
                    visited[y][x-1] = True
                    cnt += 1

        return graph[y][x], cnt**2

    else:
        return 0,0

cnt_W = 0
cnt_B = 0
for i in range(n):
    for j in range(m):
        a,b = bfs(i,j)
        if a == 'W':
            cnt_W += b
        elif a == 'B':
            cnt_B += b

print(cnt_W, cnt_B)