import sys

graph = []
for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
max = -1
x = -1; y = -1
for i in range(9):
    for j in range(9):
        if graph[i][j] > max:
            max = graph[i][j]
            x = j; y = i
print(max)
print(f'{y+1} {x+1}')