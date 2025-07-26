import sys
from collections import deque

N = 10
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

# 2개씩 가로, 세로, 대각1, 대각2
delta_x = [1,-1,0,0,1,-1,1,-1]
delta_y = [0,0,1,-1,1,-1,-1,1]

def isValid(x,y):
    return 0<=x<N and 0<=y<N

def isOmok(x,y):
    visited = []
    for _ in range(N):
        visited.append([False]*N)

    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    cnt = 1
    while deq:
        cur = deq.popleft()
        for k in range(0,2):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 'X':
                deq.append([dx,dy])
                visited[dy][dx] = True
                cnt += 1
    if cnt >= 5:
        return True


    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    cnt = 1
    while deq:
        cur = deq.popleft()
        for k in range(2,4):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 'X':
                deq.append([dx,dy])
                visited[dy][dx] = True
                cnt += 1
    if cnt >= 5:
        return True


    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    cnt = 1
    while deq:
        cur = deq.popleft()
        for k in range(4,6):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 'X':
                deq.append([dx,dy])
                visited[dy][dx] = True
                cnt += 1
    if cnt >= 5:
        return True


    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    cnt = 1
    while deq:
        cur = deq.popleft()
        for k in range(6,8):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 'X':
                deq.append([dx,dy])
                visited[dy][dx] = True
                cnt += 1
    if cnt >= 5:
        return True

    return False

is_res = False
flag = False
for i in range(N):
    if flag:
        break
    for j in range(N):
        if graph[i][j] == '.':
            if isOmok(j,i):
                is_res = True
                flag = True
                break

if is_res:
    print(1)
else:
    print(0)