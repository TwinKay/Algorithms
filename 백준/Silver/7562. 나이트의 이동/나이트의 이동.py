import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    graph = []
    for _ in range(n):
        graph.append([0]*n)

    a,b = map(int,sys.stdin.readline().split())
    x,y = map(int,sys.stdin.readline().split())

    if a == x and b == y:
        print(0)

    else:
        graph[y][x] = -1
        deq = deque([[a,b]])
        graph[b][a] += 1    # 움직이지는 않았지만 visited없이 하기 위함
        while deq:
            x,y = deq.popleft()

            if x-1>=0 and y-2>=0:
                c = graph[y-2][x-1]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x-1,y-2])
                    graph[y-2][x-1] = graph[y][x]+1

            if x-2>=0 and y-1>=0:
                c = graph[y-1][x-2]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x-2,y-1])
                    graph[y-1][x-2] = graph[y][x]+1

            if x-2>=0 and y+1<=n-1:
                c = graph[y+1][x-2]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x-2,y+1])
                    graph[y+1][x-2] = graph[y][x]+1

            if x-1>=0 and y+2<=n-1:
                c = graph[y+2][x-1]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x-1,y+2])
                    graph[y+2][x-1] = graph[y][x]+1

            if x+1<=n-1 and y-2>=0:
                c = graph[y-2][x+1]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x+1,y-2])
                    graph[y-2][x+1] = graph[y][x]+1

            if x+2<=n-1 and y-1>=0:
                c = graph[y-1][x+2]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x+2,y-1])
                    graph[y-1][x+2] = graph[y][x]+1

            if x+2<=n-1 and y+1<=n-1:
                c = graph[y+1][x+2]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x+2,y+1])
                    graph[y+1][x+2] = graph[y][x]+1

            if x+1<=n-1 and y+2<=n-1:
                c = graph[y+2][x+1]
                if c == -1:
                    print(graph[y][x])
                    break
                if c == 0:
                    deq.append([x+1,y+2])
                    graph[y+2][x+1] = graph[y][x]+1