import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]
delta_jump_x = [-2,-2,-1,-1,1,1,2,2]
delta_jump_y = [1,-1,2,-2,2,-2,1,-1]

K = int(sys.stdin.readline())
M,N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = []
for _ in range(N):
    visited.append([100]*M)

deq = deque()
deq.append([0,0,0,0])
visited[0][0] = 0

res = -1
while deq:
    x,y,time,jump_cnt = deq.popleft()
    if x == M-1 and y == N-1:
        res = time
        break

    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and graph[dy][dx] == 0 and visited[dy][dx] > jump_cnt:
            visited[dy][dx] = jump_cnt
            deq.append([dx,dy,time+1,jump_cnt])

    if jump_cnt < K:
        for k in range(8):
            dx = x + delta_jump_x[k]
            dy = y + delta_jump_y[k]
            if is_valid(dx,dy) and graph[dy][dx] == 0 and visited[dy][dx] > jump_cnt+1:
                visited[dy][dx] = jump_cnt+1
                deq.append([dx,dy,time+1,jump_cnt+1])

print(res)