'''
아이디어:
이동 가능한 경로를 목표 지점에서부터 역으로 쉽게 확인하기

1차 실패 -> 입력값의 x,y가 바뀌어 있음! 이런 문제 만날 때 자주 실수하는 듯.. 앞으로도 조심하기!
'''

import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def is_king(x,y):
    return x==end_x and y==end_y

def is_path(x,y,d):
    for k in range(1,3):
        dx = x + delta2_x[d]*k
        dy = y + delta2_y[d]*k
        if is_king(dx,dy): # 장애물이 곧 왕
            return False
    return True

delta_x = [-3,-3,-2,-2,2,2,3,3]
delta_y = [-2,2,-3,3,-3,3,-2,2]
delta2_x = [1,1,1,1,-1,-1,-1,-1]
delta2_y = [1,-1,1,-1,1,-1,1,-1]

N = 10; M = 9

visited = []
for _ in range(N):
    visited.append([False]*M)

start_y,start_x = map(int, sys.stdin.readline().split())
end_y,end_x = map(int, sys.stdin.readline().split())

deq = deque()
deq.append([start_x,start_y,0])
visited[start_y][start_x] = True
is_find = False
while deq:
    if is_find: break
    cur = deq.popleft()
    time = cur[2]
    for k in range(8):
        dx = cur[0] + delta_x[k]
        dy = cur[1] + delta_y[k]
        if not is_valid(dx,dy):
            continue
        if is_king(dx,dy):
            print(time+1) # 왕이랑 겹치는 경우 없어서 여기서 처리 가능
            is_find = True
            break
        if not visited[dy][dx] and is_path(dx,dy,k):
            deq.append([dx,dy,time+1])
            visited[dy][dx] = True

if not is_find:
    print(-1)