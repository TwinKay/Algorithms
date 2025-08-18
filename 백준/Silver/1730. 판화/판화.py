import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

# 상 우 하 좌
delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N = int(sys.stdin.readline())

queries = list(sys.stdin.readline().rstrip())

visited_garo = []
visited_sero = []
for _ in range(N):
    visited_garo.append([False]*N)
    visited_sero.append([False]*N)


x,y = 0,0

for query in queries:
    direct = -1
    if query == 'R':
        direct = 0
    elif query == 'D':
        direct = 1
    elif query == 'L':
        direct = 2
    elif query == 'U':
        direct = 3
    dx = x + delta_x[direct]
    dy = y + delta_y[direct]
    if is_valid(dx,dy):
        if direct%2 == 0:
            visited_garo[y][x] = True
            visited_garo[dy][dx] = True
        else:
            visited_sero[y][x] = True
            visited_sero[dy][dx] = True
        x,y = dx,dy



graph = []
for _ in range(N):
    graph.append(['.']*N)

for i in range(N):
    for j in range(N):
        if visited_garo[i][j] and visited_sero[i][j]:
            graph[i][j] = '+'
        elif visited_garo[i][j]:
            graph[i][j] = '-'
        elif visited_sero[i][j]:
            graph[i][j] = '|'

for g in graph:
    print("".join(g))
