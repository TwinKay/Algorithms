import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = []
for _ in range(n):
    visited.append([False]*m)

def bfs(x,y):
    sheep = 0
    wolf = 0

    if graph[y][x] == '#' or graph[y][x] == '.':
        return 0,0
    elif visited[y][x] == True:
        return 0,0
    else:
        if graph[y][x] == 'v':
            wolf += 1
        else:
            sheep += 1

        deq = deque([[x,y]])
        visited[y][x] = True
        while deq:
            x,y = deq.popleft()

            if x-1 != -1:
                if graph[y][x-1] != '#' and visited[y][x-1] == False:
                    deq.append([x-1,y])
                    visited[y][x-1] = True
                    if graph[y][x-1] == 'v':
                        wolf += 1
                    elif graph[y][x-1] == 'o':
                        sheep += 1

            if x+1 != m:
                if graph[y][x+1] != '#' and visited[y][x+1] == False:
                    deq.append([x+1,y])
                    visited[y][x+1] = True
                    if graph[y][x+1] == 'v':
                        wolf += 1
                    elif graph[y][x+1] == 'o':
                        sheep += 1

            if y-1 != -1:
                if graph[y-1][x] != '#' and visited[y-1][x] == False:
                    deq.append([x,y-1])
                    visited[y-1][x] = True
                    if graph[y-1][x] == 'v':
                        wolf += 1
                    elif graph[y-1][x] == 'o':
                        sheep += 1

            if y+1 != n:
                if graph[y+1][x] != '#' and visited[y+1][x] == False:
                    deq.append([x,y+1])
                    visited[y+1][x] = True
                    if graph[y+1][x] == 'v':
                        wolf += 1
                    elif graph[y+1][x] == 'o':
                        sheep += 1

        return wolf, sheep

result = [0,0]
for i in range(n):
    for j in range(m):
        w,s = bfs(j,i)
        if w == 0 and s == 0:
            pass
        elif s > w:
            result[0] += s
        else:
            result[1] += w

print(' '.join(map(str,result)))