import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    fish_list = list(map(int, sys.stdin.readline().split()))
    if 9 in fish_list:
        a,b = fish_list.index(9),i
    graph.append(fish_list)
graph[b][a] = 0

baby = 2
eat = 0

def bfs(x,y):
    breaker = False
    same = []
    cnt = 0

    visited = []
    for _ in range(n):
        visited.append([False]*n)

    deq = deque([])
    deq.append([x,y,cnt])
    visited[y][x] = True

    while deq:
        x,y,cnt = deq.popleft()

        if y-1 != -1:
            if visited[y-1][x] == False and (graph[y-1][x] == 0 or graph[y-1][x] == baby):
                if breaker == False:
                    deq.append([x, y-1, cnt+1])
                    visited[y-1][x] = True
            elif visited[y-1][x] == False and 1 <= graph[y-1][x] < baby:
                breaker = True
                same.append([x, y-1, cnt+1])

        if x-1 != -1:
            if visited[y][x-1] == False and (graph[y][x-1] == 0 or graph[y][x-1] == baby):
                if breaker == False:
                    deq.append([x-1, y, cnt+1])
                    visited[y][x-1] = True
            elif visited[y][x-1] == False and 1 <= graph[y][x-1] < baby:
                breaker = True
                same.append([x-1, y, cnt+1])

        if x+1 != n:
            if visited[y][x+1] == False and (graph[y][x+1] == 0 or graph[y][x+1] == baby):
                if breaker == False:
                    deq.append([x+1, y, cnt+1])
                    visited[y][x+1] = True
            elif visited[y][x+1] == False and 1 <= graph[y][x+1] < baby:
                breaker = True
                same.append([x+1, y, cnt+1])

        if y+1 != n:
            if visited[y+1][x] == False and (graph[y+1][x]==0 or graph[y+1][x] == baby):
                if breaker == False:
                    deq.append([x,y+1,cnt+1])
                    visited[y+1][x] = True
            elif visited[y+1][x] == False and 1 <= graph[y+1][x] < baby:
                breaker = True
                same.append([x, y+1, cnt+1])

    if len(same) == 1:
        graph[same[0][1]][same[0][0]] = 0
        return same[0]
    elif len(same) >= 2:
        same.sort(key=lambda x: (x[2], x[1], x[0]))
        graph[same[0][1]][same[0][0]] = 0
        return same[0]

result = 0
while True:
    try:
        a,b,cnt = bfs(a,b)
        eat += 1
        if eat == baby:
            baby += 1
            eat = 0
        result += cnt
    except:
        break
print(result)