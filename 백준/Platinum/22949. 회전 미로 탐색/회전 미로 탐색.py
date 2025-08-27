import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def is_same_group(x1,y1,x2,y2):
    return x1//4==x2//4 and y1//4==y2//4

def get_new_delta(x, y, k, rotate_cnt):
    ax = x//4
    ay = y//4
    mx = x%4
    my = y%4
    for _ in range(rotate_cnt):
        mx,my = 3-my,mx

    x = ax*4 + mx
    y = ay*4 + my

    k = (k + rotate_cnt) % 4
    dx = x + delta_x[k]
    dy = y + delta_y[k]
    return dx, dy


delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

K = int(sys.stdin.readline())
N = 4*K

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

is_find = False
start_x,start_y = N,N
for i in range(N):
    if is_find: break
    for j in range(N):
        if graph[i][j] == 'S':
            start_x,start_y = j,i
            graph[i][j] = '.'
            is_find = True
            break

visited = []
for i in range(N):
    visited.append([])
    for _ in range(N):
        visited[i].append([0]*4)

res = -1
deq = deque()
deq.append([start_x,start_y,0,0]) # x y rotate_cnt time
visited[start_y][start_x][0] = 1
while deq:
    x,y,rotate_cnt,time = deq.popleft()
    if graph[y][x] == 'E':
        res = time
        break

    if not visited[y][x][(rotate_cnt+1)%4]:
        deq.append([x,y,(rotate_cnt+1)%4,time+1])
        visited[y][x][(rotate_cnt+1)%4] = 1

    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_same_group(x,y,dx,dy):
            if is_valid(dx,dy) and not visited[dy][dx][(rotate_cnt+1)%4] and graph[dy][dx] != '#':
                deq.append([dx,dy,(rotate_cnt+1)%4,time+1])
                visited[dy][dx][(rotate_cnt+1)%4] = 1
        else:
            new_dx,new_dy = get_new_delta(x,y,k,rotate_cnt%4)
            if not is_valid(new_dx,new_dy):
                continue
            if not visited[new_dy][new_dx][1] and graph[new_dy][new_dx] != '#':
                deq.append([new_dx,new_dy,1,time+1])
                visited[new_dy][new_dx][1] = 1

print(res)