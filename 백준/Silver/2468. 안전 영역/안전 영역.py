'''
아이디어:
bfs를 통한 풀이
높이 min,max로 제한해서 구해보기
bfs 횟수로 안전구역 갯수 확인
'''

import sys
from collections import deque

# 가능한 범위
def is_valid(x,y):
    return 0<=x<N and 0<=y<N


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 높이 min,max로 제
min_height = 1000
max_height = -1
for g in graph:
    for i in g:
        min_height = min(min_height,i)
        max_height = max(max_height,i)

max_cnt = 0
for height in range(min_height-1,max_height+1,1):
    visited = []
    for _ in range(N):
        visited.append([False]*N)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and not visited[i][j]: # 안전지대, 방문x
                deq = deque()
                deq.append([j,i])
                visited[i][j] = True
                while deq:
                    cur = deq.popleft()
                    for k in range(4):
                        dx = cur[0] + delta_x[k]
                        dy = cur[1] + delta_y[k]
                        if is_valid(dx,dy) and graph[dy][dx] > height and not visited[dy][dx]: # 가능범위, 안전지대, 방문x
                            deq.append([dx,dy])
                            visited[dy][dx] = True

                cnt += 1

    max_cnt = max(max_cnt,cnt)

print(max_cnt)
