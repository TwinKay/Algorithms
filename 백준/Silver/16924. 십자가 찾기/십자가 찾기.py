import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def get_size(x,y):
    size_info = []
    for k in range(4):
        length = 0
        while True:
            dx = x + delta_x[k]*length
            dy = y + delta_y[k]*length
            if is_valid(dx,dy) and graph[dy][dx] == '*':
                length += 1
                continue
            break
        size_info.append(length)
    return size_info

delta_x = [0,0,-1,1]
delta_y = [-1,1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = []
for _ in range(N):
    visited.append([False]*M)

res = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == '*':
            size_info = get_size(j,i)
            min_size = min(size_info)
            if min_size != 1:
                for k in range(4):
                    for leng in range(min_size): # 0~최소크기
                        dx = j + delta_x[k]*leng
                        dy = i + delta_y[k]*leng
                        visited[dy][dx] = True
                res.append([i+1,j+1,min_size-1])

is_full = True
for i in range(N):
    for j in range(M):
        if graph[i][j] == '*' and not visited[i][j]:
            is_full = False

if is_full:
    print(len(res))
    for r in res:
        print(*r)
else:
    print(-1)
