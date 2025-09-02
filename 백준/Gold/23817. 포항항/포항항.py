import sys
from collections import deque
from itertools import permutations

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

idxs = []
start_x,start_y = M,N
cnt_k = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'S':
            start_x,start_y = j,i
            graph[i][j] = 0
            idxs.append([j,i])
        elif graph[i][j] == 'K':
            cnt_k += 1
            idxs.append([j, i])
            graph[i][j] = cnt_k
        elif graph[i][j] == 'X':
            graph[i][j] = -2
        else:
            graph[i][j] = -1

dist = []
for _ in range(cnt_k+1):
    dist.append([-1]*(cnt_k+1))


for idx in idxs:
    if graph[idx[1]][idx[0]] >= 0:
        visited = []
        for _ in range(N):
            visited.append([-1]*M)

        deq = deque()
        deq.append([idx[0],idx[1],0])
        visited[idx[1]][idx[0]] = 0
        while deq:
            x,y,time = deq.popleft()
            for k in range(4):
                dx = x + delta_x[k]
                dy = y + delta_y[k]
                if not is_valid(dx,dy):
                    continue
                if visited[dy][dx] != -1:
                    continue
                if graph[dy][dx] == -2:
                    continue
                deq.append([dx,dy,time+1])
                visited[dy][dx] = time+1


        for idx2 in idxs:
            dist[graph[idx[1]][idx[0]]][graph[idx2[1]][idx2[0]]] = visited[idx2[1]][idx2[0]]


res_min = float("inf")
for perm in permutations(range(1,cnt_k+1),5):
    if dist[0][perm[0]] == -1:
        continue
    if dist[perm[0]][perm[1]] == -1:
        continue
    if dist[perm[1]][perm[2]] == -1:
        continue
    if dist[perm[2]][perm[3]] == -1:
        continue
    if dist[perm[3]][perm[4]] == -1:
        continue
    time = dist[0][perm[0]] + dist[perm[0]][perm[1]] \
           + dist[perm[1]][perm[2]] + dist[perm[2]][perm[3]] \
           + dist[perm[3]][perm[4]]
    res_min = min(res_min,time)

if res_min == float("inf"):
    print(-1)
else:
    print(res_min)

# if cnt_k < 5:
#     print(-1)