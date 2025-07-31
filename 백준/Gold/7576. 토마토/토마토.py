'''
아이디어:
bfs를 통한 풀이
토마토가 없는 경우도 있음, 처음부터 모든 토마토 익은 경우 있음
graph에 시간을 기록. -1,0,1과 구분하기 위해 2부터 이용
bfs하면서 2이상이면 min으로 갱신, 0이면 바로 갱신
마지막에 0 있으면 -1, 1이상 인것들 중 max-1 출력
시간 초과 -> 이미 다른 토마토로부터 익어있는 경우 새롭게 min으로 갱신된 경우만 append
시간 초과 2 -> 처음부터 그냥 1들을 다 deq에 넣음
'''

import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

M,N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = []  # 다른 익은 토마토에서도 새롭게 bfs해야함으로 초기화
for _ in range(N):
    visited.append([False] * M)

deq = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            deq.append([j,i])
            visited[i][j] = True

while deq:
    cur = deq.popleft()
    for k in range(4):
        dx = cur[0] + delta_x[k]
        dy = cur[1] + delta_y[k]
        if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] not in [1,-1]:
            temp = graph[cur[1]][cur[0]] + 1
            if graph[dy][dx] >= 2: # 이미 다른 토마토로부터 익음
                if temp < graph[dy][dx]:
                    deq.append([dx, dy])
                graph[dy][dx] = min(graph[dy][dx], temp)
            if graph[dy][dx] == 0: # 아직 익지 않음
                graph[dy][dx] = temp
                deq.append([dx, dy])
            visited[dy][dx] = True

max_val = -1 # dummy
flag = False
for g in graph:
    if flag:
        break
    for i in g:
        if i==0:
            max_val = -1
            flag = True
            break
        if i>=1:
            max_val = max(max_val,i-1) # 안 겹치게 2부터 했음으로 -1
print(max_val)