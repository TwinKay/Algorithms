import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

S,target_y,target_x = map(int,sys.stdin.readline().split())

spread_idxs = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            spread_idxs.append([graph[i][j], j, i])

spread_idxs.sort()

for s in range(S):
    if not spread_idxs:
        break

    next_spread = []
    for spread_idx in spread_idxs:
        num, x, y = spread_idx
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if is_valid(dx, dy) and graph[dy][dx] == 0:
                graph[dy][dx] = num
                next_spread.append([num, dx, dy])

    spread_idxs = next_spread

print(graph[target_y-1][target_x-1])