import sys

n,m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = []

#1
for i in range(n-3):
    for j in range(m):
        result.append(graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+3][j])

#2
for i in range(n):
    for j in range(m-3):
        result.append(sum(graph[i][j:j+4]))

#3
for i in range(n-1):
    for j in range(m-1):
        result.append(sum(graph[i][j:j+2])+sum(graph[i+1][j:j+2]))

#4
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j]+graph[i+1][j]+sum(graph[i+2][j:j+2]))

#5
for i in range(n-1):
    for j in range(m-2):
        result.append(sum(graph[i][j:j+3])+graph[i+1][j])

#6
for i in range(n-2):
    for j in range(m-1):
        result.append(sum(graph[i][j:j+2])+graph[i+1][j+1]+graph[i+2][j+1])

#7
for i in range(n-1):
    for j in range(m-2):
        result.append(graph[i][j+2]+sum(graph[i+1][j:j+3]))

#8
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j+1]+graph[i+1][j+1]+sum(graph[i+2][j:j+2]))

#9
for i in range(n-1):
    for j in range(m-2):
        result.append(sum(graph[i][j:j+3])+graph[i+1][j+2])

#10
for i in range(n-2):
    for j in range(m-1):
        result.append(sum(graph[i][j:j+2])+graph[i+1][j]+graph[i+2][j])

#11
for i in range(n-1):
    for j in range(m-2):
        result.append(graph[i][j]+sum(graph[i+1][j:j+3]))

#12
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j]+sum(graph[i+1][j:j+2])+graph[i+2][j+1])

#13
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j+1]+sum(graph[i+1][j:j+2])+graph[i+2][j])

#14
for i in range(n-1):
    for j in range(m-2):
        result.append(sum(graph[i][j+1:j+3])+sum(graph[i+1][j:j+2]))

#15
for i in range(n-1):
    for j in range(m-2):
        result.append(sum(graph[i][j:j+2])+sum(graph[i+1][j+1:j+3]))

#16
for i in range(n-1):
    for j in range(m-2):
        result.append(sum(graph[i][j:j+3])+graph[i+1][j+1])

#17
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j+1]+sum(graph[i+1][j:j+2])+graph[i+2][j+1])

#18
for i in range(n-1):
    for j in range(m-2):
        result.append(graph[i][j+1]+sum(graph[i+1][j:j+3]))

#19
for i in range(n-2):
    for j in range(m-1):
        result.append(graph[i][j]+sum(graph[i+1][j:j+2])+graph[i+2][j])

print(max(result))