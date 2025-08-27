import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = []
for i in range(N):
    visited.append([])
    for j in range(M):
        visited[i].append([0]*(K+1))

res = -1
deq = deque()
deq.append([0,0,0,1]) # x y broken_cnt time
visited[0][0][0] = 1
while deq:
    x,y,broken_cnt,time = deq.popleft()

    if x == M-1 and y == N-1:
        res = time
        break

    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]

        if not is_valid(dx,dy):
            continue

        if graph[dy][dx] == 0:
            if not visited[dy][dx][broken_cnt]:
                deq.append([dx,dy,broken_cnt,time+1])
                visited[dy][dx][broken_cnt] = 1

        else:
            if time % 2 == 1: # 낮
                if broken_cnt+1<=K and not visited[dy][dx][broken_cnt+1]:
                    deq.append([dx,dy,broken_cnt+1,time+1])
                    visited[dy][dx][broken_cnt+1] = 1
            else:
                deq.append([x, y, broken_cnt,time+1]) # 제자리
                # visited[y][x][broken_cnt] = True

print(res)