import sys

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
y,x,direct = map(int, sys.stdin.readline().split())

graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False]*M)

visited[y][x] = True
while True:
    is_can_go = False
    for _ in range(4):
        direct -= 1

        dx = x + delta_x[direct%4]
        dy = y + delta_y[direct%4]
        if graph[dy][dx] == 0 and not visited[dy][dx]:
            visited[dy][dx] = True
            x,y = dx,dy
            is_can_go = True
            break

    if not is_can_go:
        dx = x + delta_x[(direct+2)%4]
        dy = y + delta_y[(direct+2)%4]
        if graph[dy][dx] == 0:
            visited[dy][dx] = True # 필요함
            x,y = dx,dy
        else:
            break

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            cnt += 1

print(cnt)