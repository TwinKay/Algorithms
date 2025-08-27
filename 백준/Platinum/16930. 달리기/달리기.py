import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,L = map(int, sys.stdin.readline().split())
graph = []
visited = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
    visited.append([0]*M)

start_y,start_x,end_y,end_x = map(int,sys.stdin.readline().split())
start_x-=1; start_y-=1; end_x-=1; end_y-=1

deq = deque()
deq.append([start_x,start_y,0])
visited[start_y][start_x] = 1
res = -1
while deq:
    x,y,time = deq.popleft()
    if x==end_x and y==end_y:
        res = time
        break
    for k in range(4):
        for l in range(1,L+1):
            dx = x + delta_x[k]*l
            dy = y + delta_y[k]*l

            if not is_valid(dx,dy):
                break

            if graph[dy][dx] == '#':
                break

            if not visited[dy][dx]:
                deq.append([dx,dy,time+1])
                visited[dy][dx] = time+1
            elif visited[dy][dx] == time+1:
                continue
            else:
                break

print(res)