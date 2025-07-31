'''
아이디어:
bfs를 통한 풀이
*2하고 -1계속하는 경우 있음으로 범위 넓게 설정
'''

import sys
from collections import deque

def is_valid(x):
    return 0<=x<100_001*2

N,K = map(int, sys.stdin.readline().split())

visited = [False]*(100_001*2)
deq = deque()
deq.append([N,0])
while deq:
    cur = deq.popleft()

    if cur[0] == K:
        print(cur[1])
        break

    ns = [cur[0]-1,cur[0]+1,cur[0]*2]
    for n in ns:
        if is_valid(n) and not visited[n]:
            deq.append([n,cur[1]+1])
            visited[n] = True
