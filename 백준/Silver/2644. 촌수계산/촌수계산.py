'''
BFS를 통한 풀이
'''
import sys
from collections import deque

# 가능한 범위
def is_valid(x,y):
    return 0<=x<N and 0<=y<N

# 4방 탐색
delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
start,end = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = []
for _ in range(N+1):
    graph.append([])
visited = [False]*(N+1)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

deq = deque()
deq.append([start,0])
visited[start] = True
res = -1 # 못 찾으면 그대로 -1
while deq:
    cur = deq.popleft()
    num = cur[0]
    chon = cur[1]
    if num == end:
        res = chon
        break
    for i in graph[num]:
        if not visited[i]:
            deq.append([i,chon+1])
            visited[i] = True
print(res)