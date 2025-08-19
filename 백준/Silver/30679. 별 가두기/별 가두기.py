import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

res_row = []

for i in range(N):
    for j in range(M):
        if j!=0: continue
        visited = []
        for a in range(N):
            visited.append([])
            for b in range(M):
                visited[a].append([False] * 4)
        x,y,direct = j,i,0
        visited[y][x][direct%4] = True
        is_out = False
        while True:
            dx = x + delta_x[direct%4] * graph[y][x]
            dy = y + delta_y[direct%4] * graph[y][x]
            if not is_valid(dx,dy):
                is_out = True
                break
            if visited[dy][dx][direct%4]:
                res_row.append(i+1)
                break
            visited[dy][dx][direct%4] = True
            x,y = dx,dy
            direct += 1
            
print(len(res_row))
if len(res_row) != 0:
    print(*res_row)