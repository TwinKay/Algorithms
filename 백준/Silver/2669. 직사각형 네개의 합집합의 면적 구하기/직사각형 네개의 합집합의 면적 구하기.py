import sys

graph = []
for _ in range(101):
    graph.append([0]*101)

for _ in range(4):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    x = list(range(x1,x2))
    y = list(range(y1,y2))

    for i in y:
        for j in x:
            graph[j][i] = 1

cnt = 0
for i in graph:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)