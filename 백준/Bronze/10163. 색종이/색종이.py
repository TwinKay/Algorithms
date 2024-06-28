import sys

n = int(sys.stdin.readline())

graph = []
for _ in range(1002):
    graph.append([0]*1002)

for odr in range(n):
    x,y,w,h = map(int, sys.stdin.readline().split())

    for i in range(h):
        for j in range(w):
            graph[y+i][x+j] = odr+1

res = [0]*(n+1)
for i in graph:
    for j in i:
        if j == 0:
            pass
        else:
            res[j] += 1

for idx, i in enumerate(res):
    if idx == 0:
        pass
    else:
        print(i)