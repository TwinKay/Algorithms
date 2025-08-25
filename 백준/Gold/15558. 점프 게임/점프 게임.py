import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<2

N,K = map(int, sys.stdin.readline().split())
graph = []
visited = []
for _ in range(2):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))
    visited.append([0]*N)

deq = deque()
deq.append((0,0,0))
visited[0][0] = 1
res = 0
while deq:
    x,y,time = deq.popleft()

    if x+K >= N:
        res = 1
        break

    if is_valid(x+1,y) and x+1 >= time+1 and not visited[y][x+1] and graph[y][x+1] == 1:
        deq.append((x+1,y,time+1))
        visited[y][x+1] = 1

    if is_valid(x-1,y) and x-1 >= time+1 and not visited[y][x-1] and graph[y][x-1] == 1:
        deq.append((x-1,y,time+1))
        visited[y][x-1] = 1
    
    if y==0:
        if is_valid(x+K, 1) and x+K >= time+1 and graph[1][x+K] == 1 and not visited[1][x+K]:
            deq.append((x+K, 1,time+1))
            visited[1][x+K] = 1
    else:
        if is_valid(x+K, 0) and x+K >= time+1 and graph[0][x+K] == 1 and not visited[0][x+K]:
            deq.append((x+K, 0,time+1))
            visited[0][x+K] = 1

print(res)