'''
아이디어:
0초(순간이동)부터 모두 진행 후, 걷기
-> 순간이동은 deq.appendleft로 먼저 처리
'''
import sys
from collections import deque

def is_valid(x):
    return 0<=x<MAX_LEN

delta_x = [-1,1]

MAX_LEN = 100_001
N,K = map(int, sys.stdin.readline().split())
visited = [False]*MAX_LEN

deq = deque()
deq.append((N,0)) # 시작 위치, 시간
while deq:
    idx, time = deq.popleft()
    if idx == K: # 찾음
        print(time)
        break

    if is_valid(idx*2) and not visited[idx*2]: # 순간이동
        deq.appendleft((idx*2,time)) # 왼쪽에 넣어 먼저 처리
        visited[idx*2] = True

    for k in range(2):
        dx = idx + delta_x[k]
        if is_valid(dx) and not visited[dx]:
            deq.append((dx,time+1))
            visited[dx] = True