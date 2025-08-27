import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

x,y = N,N
left_fish = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x,y = j,i
            graph[i][j] = 0
        elif graph[i][j] in [1,2,3,4,5,6]:
            left_fish += 1

def bfs(x,y,shark_size):
    visited = []
    for _ in range(N):
        visited.append([0]*N)

    min_dist = 10000
    eat_x,eat_y = N,N
    deq = deque()
    deq.append([x,y,0])
    visited[y][x] = 1
    while deq:
        x,y,dist = deq.popleft()
        if dist > min_dist: break # 계속해도 우선순위 X

        if 0 < graph[y][x] < shark_size: # 먹이
            if dist < min_dist:
                eat_x,eat_y = x,y
                min_dist = dist

            elif dist == min_dist:
                if eat_y > y:
                    eat_x,eat_y = x,y
                elif eat_y == y:
                    if eat_x > x:
                        eat_x,eat_y = x,y #y도 그냥
            else:
                break

        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if visited[dy][dx]:
                continue
            if graph[dy][dx] > shark_size:
                continue
            else:
                deq.append([dx,dy,dist+1])
                visited[dy][dx] = 1

    return eat_x,eat_y,min_dist

shark_size = 2
cnt_eat = 0
time = 0
while left_fish > 0:
    eat_x,eat_y,dist = bfs(x,y,shark_size)
    if eat_x == N: break
    graph[eat_y][eat_x] = 0
    x,y = eat_x,eat_y
    time += dist
    left_fish -= 1
    cnt_eat += 1
    if cnt_eat == shark_size:
        shark_size += 1
        cnt_eat = 0
        
print(time)