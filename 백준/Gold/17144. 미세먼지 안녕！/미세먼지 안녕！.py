import sys

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,T = map(int, sys.stdin.readline().split())

gongchunggi_y1, gongchunggi_y2 = 100,100

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    if graph[i][0] == -1:
        if gongchunggi_y1 == 100:
            gongchunggi_y1 = i
        else:
            gongchunggi_y2 = i

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def spread(graph):
    new_graph = []
    for _ in range(N):
        new_graph.append([0]*M)


    for i in range(N):
        for j in range(M):
            if graph[i][j] == -1:
                continue
            spread_idxs = []
            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if is_valid(dx,dy) and graph[dy][dx] != -1:
                    spread_idxs.append((dx,dy))
            spread_val = graph[i][j]//5
            for x,y in spread_idxs:
                new_graph[y][x] += spread_val
            graph[i][j] -= spread_val * len(spread_idxs)
    for i in range(N):
        for j in range(M):
            new_graph[i][j] += graph[i][j]

    return new_graph

def fresh():
    # 위쪽
    graph[gongchunggi_y1-1][0] = 0
    for i in range(gongchunggi_y1-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for i in range(M-1):
        graph[0][i] = graph[0][i+1]
    for i in range(1,gongchunggi_y1+1):
        graph[i-1][M-1] = graph[i][M-1]
    for i in range(M-1,1,-1):
        graph[gongchunggi_y1][i] = graph[gongchunggi_y1][i-1]
    graph[gongchunggi_y1][1] = 0

    # 아래쪽
    graph[gongchunggi_y2+1][0] = 0
    for i in range(gongchunggi_y2+1,N-1,1):
        graph[i][0] = graph[i+1][0]
    for i in range(1,M):
        graph[N-1][i-1] = graph[N-1][i]
    for i in range(N-1,gongchunggi_y2,-1):
        graph[i][M-1] = graph[i-1][M-1]
    for i in range(M-1,1,-1):
        graph[gongchunggi_y2][i] = graph[gongchunggi_y2][i-1]
    graph[gongchunggi_y2][1] = 0



for _ in range(T):
    graph = spread(graph)
    fresh()

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            res += graph[i][j]

print(res)