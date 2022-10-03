import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = []
for _ in range(n):
    visited.append([False]*n)

def bfs(a,b):
    if visited[b][a] == False and graph[b][a] == 1:
        deq = deque([])
        deq.append([a,b])
        visited[b][a] = True
        cnt = 1

        while deq:
            x,y = deq.popleft()

            if y+1 != n:
                if visited[y+1][x] == False and graph[y+1][x] == 1:
                    deq.append([x,y+1])
                    visited[y+1][x] = True
                    cnt += 1

            if y-1 != -1:
                if visited[y-1][x] == False and graph[y-1][x] == 1:
                    deq.append([x,y-1])
                    visited[y-1][x] = True
                    cnt += 1

            if x+1 != n:
                if visited[y][x+1] == False and graph[y][x+1] == 1:
                    deq.append([x+1, y])
                    visited[y][x+1] = True
                    cnt += 1

            if x-1 != -1:
                if visited[y][x-1] == False and graph[y][x-1] == 1:
                    deq.append([x-1,y])
                    visited[y][x-1] = True
                    cnt += 1
        return cnt
    return 0

result = []
for i in range(n):
    for j in range(n):
        m = bfs(i,j)
        if m != 0:
            result.append(m)

result.sort()
print(len(result))
for i in result:
    print(i)