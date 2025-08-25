import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,L,R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

time = -1
while True:
    time += 1
    is_change = False
    visited = []
    for _ in range(N):
        visited.append([False]*N)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                new_group_idxs = []
                new_group_sm = 0
                deq = deque()
                deq.append((j,i))
                visited[i][j] = True
                while deq:
                    cur = deq.popleft()
                    x,y = cur
                    new_group_idxs.append(cur)
                    new_group_sm += graph[y][x]
                    for k in range(4):
                        dx = x + delta_x[k]
                        dy = y + delta_y[k]
                        if is_valid(dx,dy) and not visited[dy][dx] and L<=abs(graph[y][x]-graph[dy][dx])<=R:
                            deq.append((dx,dy))
                            visited[dy][dx] = True
                if len(new_group_idxs) >= 2:
                    is_change = True
                    aver = new_group_sm//len(new_group_idxs)
                    for new_group_idx in new_group_idxs:
                        graph[new_group_idx[1]][new_group_idx[0]] = aver

    if not is_change:
        break
    is_change = False

print(time)