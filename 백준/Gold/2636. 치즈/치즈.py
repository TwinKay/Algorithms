'''
아이디어:
패딩 추가 후, 치즈가 녹을 때까지 반복
'''
import sys
from collections import deque

def is_valid(x,y): # 탐색 가능 범위
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
graph.append([0]*(M+2)) # 패딩 추가
for _ in range(N):
    graph.append([0]+list(map(int, sys.stdin.readline().split()))+[0])
graph.append([0]*(M+2))

N += 2; M += 2 # 패딩 추가 범위
cnt_chz = 0
for i in range(1,N-1):
    for j in range(1,M-1):
        if graph[i][j]:
            cnt_chz += 1

time = 0
last_chz_cnt = 0 # 마지막 치즈 갯수
while cnt_chz:
    time += 1
    melt_idxs = [] # 나중에 한 번에 지울 idx list
    visited = []
    for _ in range(N):
        visited.append([False]*M)
    deq = deque()
    deq.append([0,0]) # 항상 공기와 접촉
    while deq:
        cur = deq.popleft()
        if graph[cur[1]][cur[0]] == 1:
            melt_idxs.append([cur[0],cur[1]])
        for k in range(4):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx] and graph[cur[1]][cur[0]] == 0: # 이전 것이 공기가 통할 때
                deq.append([dx,dy])
                visited[dy][dx] = True
    for idx in melt_idxs: # 치즈 녹이기
        graph[idx[1]][idx[0]] = 0
    cnt_chz -= len(melt_idxs)
    last_chz_cnt = len(melt_idxs)

print(time)
print(last_chz_cnt)