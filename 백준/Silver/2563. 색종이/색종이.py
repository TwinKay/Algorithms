import sys

graph = []
for i in range(101):
    graph.append(list(False for _ in range(101)))

N = int(sys.stdin.readline())
for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            graph[i][j] = True
    
res = 0        
for line in graph:
    for bol in line:
        if bol:
            res += 1
            
print(res)