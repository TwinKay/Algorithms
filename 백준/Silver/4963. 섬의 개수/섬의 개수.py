import sys
from collections import deque

while True:
    w,h = map(int, sys.stdin.readline().split())

    if w==0 and h==0:
        break

    else:
        cnt = 0
        graph = []
        for _ in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    deq = deque([[i,j]])
                    while deq:
                        y,x = deq.popleft()

                        if x != 0:
                            if graph[y][x-1] == 1:
                                graph[y][x-1] = 0
                                deq.append([y,x-1])

                        if y != 0:
                            if graph[y-1][x] == 1:
                                graph[y-1][x] = 0
                                deq.append([y-1,x])

                        if x != w-1:
                            if graph[y][x+1] == 1:
                                graph[y][x+1] = 0
                                deq.append([y,x+1])
                        if y != h-1:
                            if graph[y+1][x] == 1:
                                graph[y+1][x] = 0
                                deq.append([y+1,x])

                        if x != 0 and y != 0:
                            if graph[y-1][x-1] == 1:
                                graph[y-1][x-1] = 0
                                deq.append([y-1, x-1])

                        if x != w-1 and y != h-1:
                            if graph[y+1][x+1] == 1:
                                graph[y+1][x+1] = 0
                                deq.append([y+1, x+1])

                        if x != 0 and y != h-1:
                            if graph[y+1][x-1] == 1:
                                graph[y+1][x-1] = 0
                                deq.append([y+1, x-1])

                        if x != w-1 and y != 0:
                            if graph[y-1][x+1] == 1:
                                graph[y-1][x+1] = 0
                                deq.append([y-1, x+1])
                    cnt += 1
        print(cnt)