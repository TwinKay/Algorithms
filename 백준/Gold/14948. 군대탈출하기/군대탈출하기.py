import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(level):
    visited = []
    for i in range(N):
        visited.append([])
        for _ in range(M):
            visited[i].append([0]*2)

    deq = deque()
    deq.append([0,0,0])
    visited[0][0][0] = 1
    while deq:
        x,y,used = deq.popleft()
        if x == M-1 and y == N-1:
            return True

        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if visited[dy][dx][used]:
                continue
            if graph[dy][dx] > level:
                continue
            deq.append([dx,dy,used])
            visited[dy][dx][used] = 1

        if not used:
            for k in range(4):
                dx = x + delta_x[k]*2
                dy = y + delta_y[k]*2
                if not is_valid(dx,dy):
                    continue
                if visited[dy][dx][1]:
                    continue
                if graph[dy][dx] > level:
                    continue
                deq.append([dx,dy,1])
                visited[dy][dx][1] = 1

    return False

min_level = max(graph[0][0], graph[N-1][M-1])

left = min_level
right = 10**9
while left < right:
    mid = (left+right)//2
    if bfs(mid) == False:
        left = mid+1
    else:
        right = mid
print(left)