import sys

n,m = map(int, sys.stdin.readline().split())
graph_1 = []
for _ in range(n):
    graph_1.append(list(map(int, sys.stdin.readline().split())))
graph_2 = []
for _ in range(n):
    graph_2.append(list(map(int, sys.stdin.readline().split())))
graph_total = []
for _ in range(n):
    graph_total.append([0]*m)
for i in range(n):
    for j in range(m):
        graph_total[i][j] = graph_1[i][j]+graph_2[i][j]

for i in graph_total:
    i = list(map(str, i))
    print(' '.join(i))