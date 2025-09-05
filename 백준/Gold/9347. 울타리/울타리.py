import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [-1,1,0,0]

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    visited = []
    for _ in range(N):
        visited.append([0]*M)

    deq = deque()
    for i in range(N):
        for j in range(M):
            if i==0 or i==N-1 or j==0 or j==M-1:
                if graph[i][j] == 0:
                    deq.appendleft([j,i,0])
                else:
                    deq.append([j,i,1])
                visited[i][j] = 1

    cnt_dic = {}
    while deq:
        x,y,broken = deq.popleft()
        if graph[y][x] == 0:
            if broken in cnt_dic:
                cnt_dic[broken] += 1
            else:
                cnt_dic[broken] = 1
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if visited[dy][dx]:
                continue
            if graph[dy][dx] == 0:
                deq.appendleft([dx,dy,broken])
            else:
                deq.append([dx,dy,broken+1])
            visited[dy][dx] = 1

    res_broken = None
    res_val = None
    for key in cnt_dic.keys():
        res_broken = key
        res_val = cnt_dic[key]

    print(res_broken,res_val)