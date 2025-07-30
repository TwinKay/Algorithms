'''
BFS를 통한 풀이
8방 탐색
시작 위치랑 도착 위치가 같을 수 있음
'''
import sys
from collections import deque

# 가능한 범위
def is_valid(x,y):
    return 0<=x<N and 0<=y<N

# 8방 탐색
delta_x = [-2,-1,1,2,-2,-1,1,2]
delta_y = [-1,-2,-2,-1,1,2,2,1]

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    start_x,start_y = map(int,sys.stdin.readline().split())
    end_x,end_y = map(int,sys.stdin.readline().split())

    visited = []
    for _ in range(N):
        visited.append([False]*N)

    deq = deque()
    deq.append([start_x,start_y,0])
    visited[start_y][start_x] = True
    while deq:
        cur = deq.popleft()
        time = cur[2]
        if cur[0] == end_x and cur[1] == end_y:
            print(time)
            break
        for k in range(8):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx]:
                deq.append([dx,dy,time+1])
                visited[dy][dx] = True



