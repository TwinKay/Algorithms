'''
아이디어:
dfs로 풀어보기
'''

import sys
sys.setrecursionlimit(10000)

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def dfs(x,y):
    visited[y][x] = True
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and graph[dy][dx] == 1 and not visited[dy][dx]: # 범위 안, 배추, 방문 X
            dfs(dx,dy)


T = int(sys.stdin.readline())
for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append([0]*M)
    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    visited = []
    for _ in range(N):
        visited.append([False]*M)
    res = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]: # 배추이고 방문 안한 경우만
                dfs(j,i)
                res += 1
    print(res)