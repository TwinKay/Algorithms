'''
아이디어:
dfs로 풀어보기
boolean 배열로 만든 후, 픽셀 수 계산
'''

import sys
sys.setrecursionlimit(500000)
delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def dfs(x,y):
    visited[y][x] = True
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and graph[dy][dx] and not visited[dy][dx]: # 범위 안, 픽셀 , 방문 x
            dfs(dx,dy)

N,M = map(int, sys.stdin.readline().split())
before_graph = []
for _ in range(N):
    before_graph.append(list(map(int, sys.stdin.readline().split())))

T = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append([])
    for j in range(0,M*3,3):
        aver = (before_graph[i][j]+before_graph[i][j+1]+before_graph[i][j+2])/3
        if aver >= T:
            graph[i].append(True)
        else:
            graph[i].append(False)

visited = []
for _ in range(N):
    visited.append([False]*M)

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            dfs(j,i)
            cnt += 1
print(cnt)