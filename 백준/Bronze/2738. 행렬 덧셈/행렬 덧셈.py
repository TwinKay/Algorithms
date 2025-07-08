import sys

N,M = map(int, sys.stdin.readline().split())
graph1 = []; graph2 = []
for i in range(N):
    graph1.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    graph2.append(list(map(int, sys.stdin.readline().split())))
sum_graph = []
for i in range(N):
    sum_graph.append(list(0 for _ in range(M)))
for i in range(N):
    for j in range(M):
        sum_graph[i][j] = graph1[i][j] + graph2[i][j]
        
for line in sum_graph:
    print(" ".join(map(str, line)))