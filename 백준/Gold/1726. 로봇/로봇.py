import sys
from collections import deque


def init_direct(direct):
    arr = [9,1,3,2,0]
    return arr[direct]

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

start_y,start_x,start_direct = map(int, sys.stdin.readline().split())
target_y,target_x,target_direct = map(int, sys.stdin.readline().split())
start_x-=1;start_y-=1;target_x-=1;target_y-=1
start_direct = init_direct(start_direct)
target_direct = init_direct(target_direct)

visited = []
for i in range(N):
    visited.append([])
    for _ in range(M):
        visited[i].append([0]*4)

deq = deque()
deq.append([start_x,start_y,start_direct,0])
visited[start_y][start_x][start_direct] = 1
while deq:
    x,y,direct,time = deq.popleft()
    if x==target_x and y==target_y and direct%4==target_direct:
        print(time)
        break

    for k in [-1,1]:
        if visited[y][x][(direct+k)%4]:
            continue
        deq.append([x,y,(direct+k)%4,time+1])
        visited[y][x][(direct+k)%4] = 1

    for dist in range(1,4):
        dx = x + delta_x[direct%4]*dist
        dy = y + delta_y[direct%4]*dist
        if not is_valid(dx,dy):
            break
        if graph[dy][dx] == 1:
            break
        if visited[dy][dx][direct%4]:
            continue
        deq.append([dx,dy,direct%4,time+1])
        visited[dy][dx][direct%4] = 1
