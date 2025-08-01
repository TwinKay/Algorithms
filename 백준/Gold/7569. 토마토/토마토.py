'''
토마토는 없을 수도 있음
다 익는 시간 or 없으면 -1
2based time 사용해서 한 arr에 저장
한번에 deq 넣기
'''
import sys
from collections import deque

delta_x = [0,0,-1,1,0,0]
delta_y = [-1,1,0,0,0,0]
delta_h = [0,0,0,0,1,-1]

M,N,H = map(int, sys.stdin.readline().split())
graph = []
for h in range(H):
    graph.append([])
    for i in range(N):
        graph[h].append(list(map(int, sys.stdin.readline().split())))

def is_valid(x,y,z):
    return 0<=x<M and 0<=y<N and 0<=z<H

deq = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 1: # 익은 토마토
                deq.append([j,i,h,1])

while deq:
    cur = deq.popleft()
    cx = cur[0]
    cy = cur[1]
    ch = cur[2]
    time = cur[3]
    for k in range(6):
        dx = cx + delta_x[k]
        dy = cy + delta_y[k]
        dh = ch + delta_h[k]
        if is_valid(dx,dy,dh) and graph[dh][dy][dx] == 0:
            deq.append([dx,dy,dh,time+1])
            graph[dh][dy][dx] = time + 1

flag = False
max_val = 1
for h in range(H):
    if flag:
        break
    for i in range(N):
        if flag:
            break
        for j in range(M):
            if flag:
                break
            val = graph[h][i][j]
            if val == 0:
                flag= True
                break
            elif val >= 2:
                max_val = max(max_val,val)

if flag:
    print(-1)
else:
    print(max_val-1) # 시간을 2부터 기록했음으로