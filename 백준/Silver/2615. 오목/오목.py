'''
아이디어: bfs로 갯수 세기
풀이 시간: 19:15~19:32
'''
import sys
from collections import deque


def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def bfs(x,y,direct):
    visited = []
    for _ in range(N):
        visited.append([False] * N)

    idxs = []
    color = graph[y][x]
    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    while deq:
        cur = deq.popleft()
        idxs.append(cur)
        for k in range(direct*2, direct*2+2):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if is_valid(dx,dy) and graph[dy][dx] == color and not visited[dy][dx]:
                deq.append([dx,dy])
                visited[dy][dx] = True
    if len(idxs) == 5:
        idxs.sort()
        return [color,idxs[0]]
    return None


delta_x = [-1,1,0,0,1,-1,-1,1]
delta_y = [0,0,-1,1,1,-1,1,-1]

N = 19
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

is_find = False
for i in range(N):
    if is_find:
        break
    for j in range(N):
        if is_find:
            break
        if graph[i][j] != 0:
            for d in range(4):
                val = bfs(j,i,d)
                if val:
                    is_find = True
                    print(val[0])
                    print(val[1][1]+1,val[1][0]+1)
                    break
if not is_find:
    print(0)