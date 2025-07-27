'''
아이디어:
N*N부터 역순으로 풀어보기
모듈러 연산을 통한 방향 전환
'''

import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

N = int(sys.stdin.readline())

# 아래 오른쪽 위 왼쪽 순
delta_X = [0,1,0,-1]
delta_Y = [1,0,-1,0]

graph = []
for _ in range(N):
    graph.append([0]*N)

x,y = 0,0
direction = 0
graph[0][0] = N*N
for n in range(N*N-1,-1,-1):
    for i in range(4): # 4방향 탐색
        dx = x + delta_X[direction%4] # 모듈러 연산을 통한 탐색
        dy = y + delta_Y[direction%4]
        if is_valid(dx,dy) and graph[dy][dx] == 0: # idx 범위 안 and 방문 X
            graph[dy][dx] = n
            x,y = dx,dy # 다음 idx로 갱신
            break
        else:
            direction += 1 # 다음 방향


prt = []
for g in graph:
    prt.append(" ".join(map(str,g)))

# target index 찾기 (1based_idx)
target = int(sys.stdin.readline())
flag = False
for i in range(N):
    if flag:
        break
    for j in range(N):
        if graph[i][j] == target:
            prt.append(f'{i+1} {j+1}')
            flag = True
            break

print("\n".join(prt))