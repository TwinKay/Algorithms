'''
아이디어:
bfs를 통한 풀이
boolean grpah로 만들어서 쉽게 풀기
'''

import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

normal_graph = []
N = int(sys.stdin.readline())
for _ in range(N):
    normal_graph.append(list(sys.stdin.readline().rstrip()))

blind_graph = []
for i in range(N):
    blind_graph.append([])
    for j in range(N):
        if normal_graph[i][j] == 'B':
            blind_graph[i].append(False)
        else:
            blind_graph[i].append(True)

visited = []
for _ in range(N):
    visited.append([False]*N)

cnt_normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_normal += 1

            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            while deq:
                cur = deq.popleft()
                for k in range(4):
                    dx = cur[0] + delta_x[k]
                    dy = cur[1] + delta_y[k]
                    if is_valid(dx,dy) and normal_graph[dy][dx] == normal_graph[i][j] and not visited[dy][dx]:
                        deq.append([dx,dy])
                        visited[dy][dx] = True

# 새로 초기화 필수
visited = []
for _ in range(N):
    visited.append([False]*N)

cnt_blind = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_blind += 1

            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            while deq:
                cur = deq.popleft()
                for k in range(4):
                    dx = cur[0] + delta_x[k]
                    dy = cur[1] + delta_y[k]
                    if is_valid(dx,dy) and blind_graph[dy][dx] == blind_graph[i][j] and not visited[dy][dx]:
                        deq.append([dx,dy])
                        visited[dy][dx] = True

print(cnt_normal,cnt_blind)