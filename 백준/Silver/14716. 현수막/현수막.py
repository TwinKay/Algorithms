'''

'''
import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1,-1,-1,1,1]
delta_y = [1,-1,0,0,-1,1,-1,1]

N,M = map(int, sys.stdin.readline().split())
graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False]*M)

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            res += 1
            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            while deq:
                cur = deq.popleft()
                for k in range(8):
                    dx = cur[0]+delta_x[k]
                    dy = cur[1]+delta_y[k]
                    if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 1:
                        deq.append([dx,dy])
                        visited[dy][dx] = True
print(res)