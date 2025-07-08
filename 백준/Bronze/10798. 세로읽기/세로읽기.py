import sys

graph = []
M = 0
for i in range(5):
    graph.append(list(sys.stdin.readline().rstrip()))
    if len(graph[i]) > M:
        M = len(graph[i])

res = []
for i in range(M):
    for j in range(5):
        try:
            res.append(graph[j][i])
        except:
            pass
print("".join(res))