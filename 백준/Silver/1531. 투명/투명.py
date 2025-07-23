import sys

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(100):
    graph.append([0]*100)

for _ in range(N):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            graph[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] > M:
            cnt += 1

print(cnt)