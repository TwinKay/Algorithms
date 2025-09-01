import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def rotate_each(x,y,n):
    each_graph = []
    for i in range(n):
        each_graph.append([])
        for j in range(n-1,-1,-1):
            each_graph[i].append(graph[y+j][x+i])

    for i in range(n):
        for j in range(n):
            graph[y+i][x+j] = each_graph[i][j]

def rotate_total(l):
    each_num = 2**l
    for i in range(0,N,each_num):
        for j in range(0,N,each_num):
            rotate_each(j,i,each_num)

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,Q = map(int, sys.stdin.readline().split())
N = 2**N # N 문제와 다름
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

queries = list(map(int, sys.stdin.readline().split()))
for query in queries:
    rotate_total(query)

    redu_idxs = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if not is_valid(dx,dy):
                    continue
                if graph[dy][dx] > 0:
                    cnt += 1

            if cnt < 3:
                redu_idxs.append([j,i])
    for redu_idx in redu_idxs:
        graph[redu_idx[1]][redu_idx[0]] -= 1

res = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:
            res += graph[i][j]

max_ice = 0
visited = []
for _ in range(N):
    visited.append([0]*N)
for i in range(N):
    for j in range(N):
        if graph[i][j] >= 1:
            deq = deque()
            deq.append([j,i])
            visited[i][j] = 1
            cnt = 0
            while deq:
                cnt += 1
                x,y = deq.popleft()
                for k in range(4):
                    dx = x + delta_x[k]
                    dy = y + delta_y[k]
                    if not is_valid(dx,dy):
                        continue
                    if visited[dy][dx]:
                        continue
                    if graph[dy][dx] < 1:
                        continue
                    deq.append([dx,dy])
                    visited[dy][dx] = 1
            max_ice = max(max_ice,cnt)

print(res)
print(max_ice)