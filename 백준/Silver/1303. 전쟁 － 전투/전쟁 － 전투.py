import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
visited = []
for _ in range(m):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)
    visited.append([False]*n)

res_w = 0 ; res_b = 0
for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            deq = deque([])
            deq.append([x,y])
            cnt = 1
            visited[y][x] = True
            while deq:
                a,b = deq.popleft()
                if a+1 != n:
                    if not visited[b][a+1] and graph[y][x] == graph[b][a+1]:
                        deq.append([a+1,b])
                        visited[b][a+1] = True
                        cnt += 1
                        
                if a-1 >= 0:
                    if not visited[b][a-1] and graph[y][x] == graph[b][a-1]:
                        deq.append([a-1,b])
                        visited[b][a-1] = True
                        cnt += 1
                        
                if b+1 != m:
                    if not visited[b+1][a] and graph[y][x] == graph[b+1][a]:
                        deq.append([a,b+1])
                        visited[b+1][a] = True
                        cnt += 1
                        
                if b-1 >= 0:
                    if not visited[b-1][a] and graph[y][x] == graph[b-1][a]:
                        deq.append([a,b-1])
                        visited[b-1][a] = True
                        cnt += 1
                
            if graph[y][x] == 'W':
                res_w += cnt**2
            else:
                res_b += cnt**2

print(res_w, res_b)