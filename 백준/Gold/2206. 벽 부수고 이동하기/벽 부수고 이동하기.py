import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(list(map(int, temp)))
visited = []
for _ in range(n):
    visited.append([])
for i in range(n):
    for _ in range(m):
        visited[i].append([0,0]) #[not crushed, crushed]
             
deq = deque([[0,0,False]]) # n,m,crush           
visited[0][0][0], visited[0][0][1] = 1,1
    
while deq:
    x,y,c = deq.popleft()
    if not c:
        l = visited[y][x][0]
    else:
        l = visited[y][x][1]
    
    if not c:
        if x+1 != m:
            if graph[y][x+1] == 0:
                if not visited[y][x+1][0]:
                    deq.append([x+1,y,False])
                    visited[y][x+1][0] = l+1
            else:
                if not visited[y][x+1][1]:
                    deq.append([x+1,y,True])
                    visited[y][x+1][1] = l+1

        if x-1 != -1:
            if graph[y][x-1] == 0:
                if not visited[y][x-1][0]:
                    deq.append([x-1,y,False])
                    visited[y][x-1][0] = l+1
            else:
                if not visited[y][x-1][1]:
                    deq.append([x-1,y,True])
                    visited[y][x-1][1] = l+1
                    
        if y+1 != n:
            if graph[y+1][x] == 0:
                if not visited[y+1][x][0]:
                    deq.append([x,y+1,False])
                    visited[y+1][x][0] = l+1
            else:
                if not visited[y+1][x][1]:
                    deq.append([x,y+1,True])
                    visited[y+1][x][1] = l+1
                    
        if y-1 != -1:
            if graph[y-1][x] == 0:
                if not visited[y-1][x][0]:
                    deq.append([x,y-1,False])
                    visited[y-1][x][0] = l+1
            else:
                if not visited[y-1][x][1]:
                    deq.append([x,y-1,True])
                    visited[y-1][x][1] = l+1

    else:
        if x+1 != m:
            if graph[y][x+1] == 0:
                if not visited[y][x+1][1]:
                    deq.append([x+1,y,True])
                    visited[y][x+1][1] = l+1

        if x-1 != -1:
            if graph[y][x-1] == 0:
                if not visited[y][x-1][1]:
                    deq.append([x-1,y,True])
                    visited[y][x-1][1] = l+1
                    
        if y+1 != n:
            if graph[y+1][x] == 0:
                if not visited[y+1][x][1]:
                    deq.append([x,y+1,True])
                    visited[y+1][x][1] = l+1
                    
        if y-1 != -1:
            if graph[y-1][x] == 0:
                if not visited[y-1][x][1]:
                    deq.append([x,y-1,True])
                    visited[y-1][x][1] = l+1
                    
res = visited[n-1][m-1]
if res[0] == 0 and res[1] == 0:
    print(-1)
elif res[0] == 0:
    print(res[1])
elif res[1] == 0:
    print(res[0])
else:
    print(min(res))