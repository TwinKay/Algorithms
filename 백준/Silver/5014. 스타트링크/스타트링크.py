'''
bfs를 통한 해결
S==G인 경우도 있을 수 있음
없으면 use the stairs
'''
import sys
from collections import deque

F,S,G,U,D = map(int, sys.stdin.readline().split())

visited = [False]*(F+1)
deq = deque()
deq.append([S,0])
visited[S] = True
while deq:
    cur = deq.popleft()
    d = cur[0]-D
    u = cur[0]+U

    if cur[0] == G: # 도착
        print(cur[1])
        break
    if d>0 and not visited[d]: # 범위 안, 방문 x
        deq.append([d,cur[1]+1])
        visited[d] = True
    if u<=F and not visited[u]: # 범위 안, 방문 x
        deq.append([u,cur[1]+1])
        visited[u] = True

if not visited[G]:
    print('use the stairs')