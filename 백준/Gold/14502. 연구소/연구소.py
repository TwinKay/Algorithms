'''
최적화해보기
'''
import sys
from itertools import combinations
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [-1,1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

first_visited = []
for _ in range(N):
    first_visited.append([False] * M)

wall_num = 0 # 기존 벽 갯수
empty_idxs = [] # 0인 index 넣을 리스트
virus_idxs = [] # 바이러스 index 넣을 리스트
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_idxs.append([j,i])
        elif graph[i][j] == 1:
            wall_num += 1
        elif graph[i][j] == 2:
            virus_idxs.append([j,i])
            graph[i][j] = 0
            first_visited[i][j] = True # 바이러스는 미리 visited 처리해서 최적화, 나중에 조합마다 딥카피

min_virus = float('inf') # 가장 적은 바이러스 -> 가장 큰 안전여ㅕㅇ역
for wall_idxs in combinations(range(len(empty_idxs)),3): # 벽을 세울 수 있는 조합들
    # 벽 세우기
    graph[empty_idxs[wall_idxs[0]][1]][empty_idxs[wall_idxs[0]][0]] = 1
    graph[empty_idxs[wall_idxs[1]][1]][empty_idxs[wall_idxs[1]][0]] = 1
    graph[empty_idxs[wall_idxs[2]][1]][empty_idxs[wall_idxs[2]][0]] = 1

    visited = [sub[:] for sub in first_visited] # 기존 바이러스 visited 처리된 visited 딥카피(슬라이싱)

    deq = deque(virus_idxs) # 기존 바이러스 index 리스트 넣어서 뎈 생성

    cnt = 0 # 바이러스 count
    while deq:
        x,y = deq.popleft()
        cnt += 1
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 0: # 가능 범위, 방문 X, 빈 공간
                deq.append([dx,dy])
                visited[dy][dx] = True

    min_virus = min(min_virus,cnt) # 갱신

    # 다음 조합을 위해 벽 빼주기
    graph[empty_idxs[wall_idxs[0]][1]][empty_idxs[wall_idxs[0]][0]] = 0
    graph[empty_idxs[wall_idxs[1]][1]][empty_idxs[wall_idxs[1]][0]] = 0
    graph[empty_idxs[wall_idxs[2]][1]][empty_idxs[wall_idxs[2]][0]] = 0

print(N*M-wall_num-3-min_virus) # 전체 - 기존 벽 갯수 - 새로운 벽 3개 - 최소 바이러스