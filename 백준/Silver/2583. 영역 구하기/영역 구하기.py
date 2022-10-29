# 상하 반전된 그래프가 나오지만 답은 같음!
import sys
from collections import deque

m,n,k = map(int, sys.stdin.readline().split())

graph = []
for _ in range(m):
    graph.append([False]*n)

for _ in range(k):
    x_1,y_1,x_2,y_2 = map(int, sys.stdin.readline().split())

    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            graph[j][i] = True

def bfs(x,y):
    if graph[y][x] == False:
        deq = deque([[x,y]])
        graph[y][x] = True
        cnt = 1
        while deq:
            x,y = deq.popleft()

            if x-1 != -1:
                if graph[y][x-1] == False:
                    deq.append([x-1,y])
                    graph[y][x-1] = True
                    cnt += 1

            if y-1 != -1:
                if graph[y-1][x] == False:
                    deq.append([x,y-1])
                    graph[y-1][x] = True
                    cnt += 1

            if x+1 != n:
                if graph[y][x+1] == False:
                    deq.append([x+1,y])
                    graph[y][x+1] = True
                    cnt += 1

            if y+1 != m:
                if graph[y+1][x] == False:
                    deq.append([x,y+1])
                    graph[y+1][x] = True
                    cnt += 1
        return cnt


    else:
        return -1

result = []
for i in range(m):
    for j in range(n):
        ans = bfs(j,i)
        if ans != -1:
            result.append(ans)
result.sort()

print(len(result))
print(' '.join(map(str, result)))