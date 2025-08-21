import sys
from itertools import combinations
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [-1,1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

empty_idxs = []
virus_idxs = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_idxs.append([j,i])
        elif graph[i][j] == 2:
            virus_idxs.append([j,i])
            graph[i][j] = 0

min_virus = float('inf')
max_safe = -1
for wall_idxs in combinations(empty_idxs,3):
    graph[wall_idxs[0][1]][wall_idxs[0][0]] = 1
    graph[wall_idxs[1][1]][wall_idxs[1][0]] = 1
    graph[wall_idxs[2][1]][wall_idxs[2][0]] = 1


    visited = []
    for _ in range(N):
        visited.append([False]*M)

    deq = deque(virus_idxs)
    for v_idx in virus_idxs:
        visited[v_idx[1]][v_idx[0]] = True

    cnt = 0
    while deq:
        x,y = deq.popleft()
        cnt += 1
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 0:
                deq.append([dx,dy])
                visited[dy][dx] = True

    min_virus = min(min_virus,cnt)

    safe = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 0:
                safe += 1
    max_safe = max(max_safe,safe)


    graph[wall_idxs[0][1]][wall_idxs[0][0]] = 0
    graph[wall_idxs[1][1]][wall_idxs[1][0]] = 0
    graph[wall_idxs[2][1]][wall_idxs[2][0]] = 0

print(max_safe)