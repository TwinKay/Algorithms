import sys, copy
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

wall = []
for y,i in enumerate(graph):
    for x,j in enumerate(i):
        if j == 0:
            wall.append([x,y])

def bfs(a,b,c):
    graph_copy = copy.deepcopy(graph)
    x_1, y_1 = wall[a]
    x_2, y_2 = wall[b]
    x_3, y_3 = wall[c]
    graph_copy[y_1][x_1] = 1
    graph_copy[y_2][x_2] = 1
    graph_copy[y_3][x_3] = 1

    for b in range(n):
        for a in range(m):
            if graph_copy[b][a] == 2:
                deq = deque([[a,b]])

                while deq:
                    x,y = deq.popleft()

                    if x-1 != -1:
                        if graph_copy[y][x-1] == 0:
                            graph_copy[y][x-1] = 2
                            deq.append([x-1,y])

                    if y-1 != -1:
                        if graph_copy[y-1][x] == 0:
                            graph_copy[y-1][x] = 2
                            deq.append([x,y-1])

                    if x+1 != m:
                        if graph_copy[y][x+1] == 0:
                            graph_copy[y][x+1] = 2
                            deq.append([x+1,y])

                    if y+1 != n:
                        if graph_copy[y+1][x] == 0:
                            graph_copy[y+1][x] = 2
                            deq.append([x,y+1])

    cnt = 0
    for i in graph_copy:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt

result = []
for i in range(len(wall)):
    for j in range(len(wall)):
        for k in range(len(wall)):
            if i < j < k:
                result.append(bfs(i,j,k))

print(max(result))