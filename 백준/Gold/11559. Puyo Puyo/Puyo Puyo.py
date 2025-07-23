import sys
from collections import deque

N = 12; M = 6
deltaX = [0,0,-1,1]; deltaY = [1,-1,0,0]

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

def isValid(x,y):
    return x>=0 and x<M and y>=0 and y<N

def findBlank(x,y):
    bottom = y
    for i in range(y,N):
        if graph[i][x] == ".":
            bottom = i
    return [x,bottom]

def down():
    for i in range(N-1,-1,-1):
        for j in range(M):
            if graph[i][j] ==".":
                continue
            temp = graph[i][j]
            graph[i][j] = "."
            newX, newY = findBlank(j,i)
            graph[newY][newX] = temp

def bomb():
    isBomb = False

    visited = []
    for _ in range(N):
        visited.append([False]*M)

    for i in range(N):
        for j in range(M):
            if graph[i][j] != "." and not visited[i][j]:
                puyos = []
                color = graph[i][j]
                deq = deque()
                deq.append([j,i])
                visited[i][j] = True
                puyos.append([j, i])
                while deq:
                    cur = deq.popleft()
                    for k in range(4):
                        dx = cur[0] + deltaX[k]
                        dy = cur[1] + deltaY[k]
                        if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == color:
                            deq.append([dx,dy])
                            visited[dy][dx] = True
                            puyos.append([dx,dy])
                if len(puyos) >= 4:
                    isBomb = True
                    for puyo in puyos:
                        graph[puyo[1]][puyo[0]] = '.'

    return isBomb

res = 0
while True:
    if not bomb():
        break
    res += 1
    down()

print(res)