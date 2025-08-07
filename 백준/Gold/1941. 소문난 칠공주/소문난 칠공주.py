import sys
from collections import deque
from itertools import combinations

def is_valid(x,y):
    '''
    가능 범위인지 확인하는 함수
    :param x: x좌표
    :param y: y좌표
    :return: (boolean) 가능 범위 여부
    '''
    return 0<=x<N and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = 5
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

graph_flat = [] # 1차원 graph
for g in graph:
    graph_flat.extend(g)
    
total_idxs = []
for i in range(N):
    for j in range(N):
        total_idxs.append([j,i])

res = 0

for comb in combinations(range(25),7): # total_idxs를 직접 comb하지 않고, idx로 이용
    cnt_s = 0 # 이다솜파 cnt
    for i in range(7):
        if graph_flat[comb[i]] == 'S':
            cnt_s += 1
            
    if cnt_s >= 4: #4명이상 성립 -> 이어져 있는가 확인
        visited = []
        for _ in range(N):
            visited.append([True]*N)
        for idx in comb:
            visited[total_idxs[idx][1]][total_idxs[idx][0]] = False # 이어져있는지 확인할 배열 visited False 만들기

        deq = deque()
        deq.append([total_idxs[comb[0]][0],total_idxs[comb[0]][1]]) # 조합 중 첫번째
        visited[total_idxs[comb[0]][1]][total_idxs[comb[0]][0]] = True
        cnt = 0
        while deq:
            cur = deq.popleft()
            cnt += 1
            for k in range(4):
                dx = cur[0] + delta_x[k]
                dy = cur[1] + delta_y[k]
                if is_valid(dx,dy) and not visited[dy][dx]:
                    deq.append([dx,dy])
                    visited[dy][dx] = True
        if cnt == 7: # 이어져있으면
            res += 1

print(res)