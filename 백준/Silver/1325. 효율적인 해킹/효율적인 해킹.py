'''
아이디어:
bfs를 통한 풀이
단방향! b->a
max에 해당하는 컴퓨터 번호를 오름차순으로 출력 -> sort 필요 없음
'''

import sys
from collections import deque

def bfs(c):
    visited = [False] * (N + 1)
    cnt = 0
    deq = deque()
    deq.append(c)
    visited[c] = True
    while deq:
        cur = deq.popleft()
        cnt += 1
        for nx in graph[cur]:
            if not visited[nx]:
                deq.append(nx)
                visited[nx] = True
    return cnt


N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

max_val = -1 # dummy
max_arr = []
for n in range(1,N+1):
    cnt = bfs(n)
    if cnt > max_val:
        max_val = cnt
        max_arr = [n]
    elif cnt == max_val:
        max_arr.append(n)

print(*max_arr) # 정렬 필요 x

