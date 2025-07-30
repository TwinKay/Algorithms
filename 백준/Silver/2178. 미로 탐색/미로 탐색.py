'''
BFS를 통한 풀이
입구가 출구인 경우 X
입구나 출구가 벽인 경우 X
=>항상 도착위치로 이동 가능
'''
import sys
from collections import deque

# 가능한 범위
def is_valid(x,y):
    return 0<=x<M and 0<=y<N

# 4방 탐색
delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, input().split())
graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))
    visited.append([False]*M)

deq = deque()
deq.append([0,0,1]) #x y time(길이)
visited[0][0] = True
while deq:
    cur = deq.popleft()
    time = cur[2]
    if cur[0] == M-1 and cur[1] == N-1: # 도착
        print(time)
        break
    for k in range(4):
        dx = cur[0] + delta_x[k]
        dy = cur[1] + delta_y[k]
        if is_valid(dx,dy) and graph[dy][dx] == 1 and not visited[dy][dx]: # 가능한 범위, 길, 방문 X
            deq.append([dx,dy,time+1])
            visited[dy][dx] = True