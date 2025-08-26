'''
비트마스킹 잘 몰라요.. -> 그냥 비트 구현..
'''
import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = []
for i in range(N):
    visited.append([])
    for j in range(M):
        visited[i].append([False]*(2**6))

x,y = 100,100
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            x,y = j,i
            graph[i][j] = '.'

def keys_to_num(keys):
    num = 0
    mul = 32
    for key in keys:
        if key:
            num += mul
        mul //= 2
    return num


deq = deque()
deq.append([x,y,0,[False]*6])
visited[y][x][0] = True
res = -1
while deq:
    x,y,time,keys = deq.popleft()
    if graph[y][x] == '1':
        res = time
        break  # flag 필요
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if not is_valid(dx,dy) or graph[dy][dx] == '#':
            continue

        num_key = keys_to_num(keys)

        if visited[dy][dx][num_key]:
            continue

        if graph[dy][dx] in ['.','1']:
            deq.append([dx,dy,time+1,keys])
            visited[dy][dx][num_key] = True
            continue

        uni = ord(graph[dy][dx])
        if uni < 95: # 문이면
            bit_idx = uni-65
            if keys[bit_idx]:
                deq.append([dx,dy,time+1,keys])
                visited[dy][dx][num_key] = True

        else: # 열쇠면
            bit_idx = uni-97
            if keys[bit_idx]:
                deq.append([dx,dy,time+1,keys])
                visited[dy][dx][num_key] = True
            else:
                new_keys = [k for k in keys[:]]
                new_keys[bit_idx] = True
                deq.append([dx, dy, time+1, new_keys])
                visited[dy][dx][keys_to_num(new_keys)] = True

print(res)