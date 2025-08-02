import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def is_block(x,y,d):
    if graph[y][x] == 0:
        return False
    elif graph[y][x] == 1 and d in [1,3]:
        return True
    elif graph[y][x] == 2 and d in [0,2]:
        return True
    return False

def change_direct(x,y,d):
    if graph[y][x] == 0:
        return d
    elif graph[y][x] == 3:
        if d in [0,2]:
            d += 1
            return (d + 4) % 4
        else:
            d -= 1
            return (d + 4) % 4
    elif graph[y][x] == 4:
        if d in [1,3]:
            d += 1
            return (d + 4) % 4
        else:
            d -= 1
            return (d + 4) % 4
    return d

def next_step(x,y,d):
    if d == 0: y -= 1
    elif d == 1: x += 1
    elif d == 2: y += 1
    else: x -= 1
    return x,y

# 상우하좌
delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

start_idxs = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 9:
            start_idxs.append([j,i])
            graph[i][j] = 0

visited = []
for i in range(N):
    visited.append([])
    for j in range(M):
        visited[i].append([False]*4)

for start_idx in start_idxs:
    for d in range(4):
        x, y = start_idx
        while True:
            if not is_valid(x, y):
                break
            if visited[y][x][d]:
                break
            visited[y][x][d] = True

            if is_block(x, y, d):
                break

            d = change_direct(x, y, d)
            x, y = next_step(x, y, d)

cnt = 0
for i in range(N):
    for j in range(M):
        is_true = False
        for k in range(4):
            if visited[i][j][k]:
                is_true = True
                break
        if is_true:
            cnt += 1
print(cnt)

