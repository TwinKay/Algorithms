'''
아이디어:
dfs로 풀어보기
boolean 배열로 만들 후, 빈공간 계산
'''

import sys
sys.setrecursionlimit(10000)

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def dfs(x,y):
    global cnt # 면적 세기 위함
    visited[y][x] = True
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and not graph[dy][dx] and not visited[dy][dx]: # 범위 안, 모눈 종이 x , 방문 x
            dfs(dx,dy)
            cnt += 1

N,M,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append([False]*M)
for _ in range(K):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = True # 모눈 종이 겹치기
visited = []
for _ in range(N):
    visited.append([False]*(M))
res = []
for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            cnt = 1
            dfs(j,i)
            res.append(cnt)
res.sort()
print(len(res))
print(*res)
