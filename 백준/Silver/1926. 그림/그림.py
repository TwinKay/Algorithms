import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
max_value = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            deq = deque([[j,i]])
            graph[i][j] = 0
            m_cnt = 1

            while deq:
                x,y = deq.popleft()

                if x-1 != -1:
                    if graph[y][x-1] == 1:
                        graph[y][x-1] = 0
                        deq.append([x-1,y])
                        m_cnt += 1

                if y-1 != -1:
                    if graph[y-1][x] == 1:
                        graph[y-1][x] = 0
                        deq.append([x,y-1])
                        m_cnt += 1

                if x+1 != m:
                    if graph[y][x+1] == 1:
                        graph[y][x+1] = 0
                        deq.append([x+1,y])
                        m_cnt += 1

                if y+1 != n:
                    if graph[y+1][x] == 1:
                        graph[y+1][x] = 0
                        deq.append([x,y+1])
                        m_cnt += 1
            cnt += 1
            max_value = max(max_value, m_cnt)

print(cnt)
print(max_value)