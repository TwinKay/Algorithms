'''
BFS를 통한 풀이
boolean 맵에 겹친 후, False인 것들 그룹 체크
'''
import sys
from collections import deque

# 가능한 범위 체크 함수
def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append([False]*M)
for _ in range(K):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = True # 계속 겹치기
visited = []
for _ in range(N):
    visited.append([False]*(M))

res = []
for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            cnt = 1
            while deq:
                cur = deq.popleft()
                for k in range(4):
                    dx = cur[0] + delta_x[k]
                    dy = cur[1] + delta_y[k]
                    if is_valid(dx,dy) and not graph[dy][dx] and not visited[dy][dx]:
                        deq.append([dx,dy])
                        visited[dy][dx] = True
                        cnt += 1
            res.append(cnt)

res.sort()
print(len(res))
print(*res)