import sys
from collections import deque

def is_valid(x,y):
    return x>=0 and x<M and y>=0 and y<N

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
Y,X = map(int, sys.stdin.readline().split())
X -= 1; Y -= 1
queries = list(list(sys.stdin.readline().rstrip()))

visited = []
for _ in range(N):
    visited.append([False]*M)

delta_x = [0,0,-1,1]; delta_y = [1,-1,0,0]

for query in queries:
    if query == "L":
        X -= 1
    elif query == "R":
        X += 1
    elif query == "U":
        Y -= 1
    elif query == "D":
        Y += 1
    else:
        if not visited[Y][X]:
            deq = deque()
            deq.append([X,Y])
            visited[Y][X] = True
            while deq:
                cur = deq.popleft()
                for i in range(4):
                    dx = cur[0] + delta_x[i]
                    dy = cur[1] + delta_y[i]
                    if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == graph[cur[1]][cur[0]]:
                        deq.append([dx,dy])
                        visited[dy][dx] = True


visited[Y][X] = True
for i in range(4):
    dx = X + delta_x[i]
    dy = Y + delta_y[i]
    if is_valid(dx,dy):
        visited[dy][dx] = True

res = []
for _ in range(N):
    res.append([])
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            res[i].append(".")
        else:
            res[i].append("#")

for r in res:
    print("".join(r))