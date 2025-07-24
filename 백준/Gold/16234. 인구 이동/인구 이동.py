import sys
from collections import deque

N,L,R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return x>=0 and x<N and y>=0 and y<N

def move():
    visited = []
    for _ in range(N):
        visited.append([False]*N)

    is_move = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                deq = deque()
                deq.append([j,i])
                visited[i][j] = True
                union = [[j,i]]
                while deq:
                    cur = deq.popleft()
                    for k in range(4):
                        dx = cur[0] + delta_x[k]
                        dy = cur[1] + delta_y[k]
                        if is_valid(dx,dy) and not visited[dy][dx]:
                            diff = abs(graph[cur[1]][cur[0]] - graph[dy][dx])
                            if L <= diff <= R:
                                deq.append([dx,dy])
                                visited[dy][dx] = True
                                union.append([dx,dy])
                                is_move = True
                union_sum = 0
                for u in union:
                    union_sum += graph[u[1]][u[0]]

                aver = union_sum//len(union)
                for u in union:
                    graph[u[1]][u[0]] = aver

    return is_move

cnt = 0
while move():
    cnt += 1

print(cnt)