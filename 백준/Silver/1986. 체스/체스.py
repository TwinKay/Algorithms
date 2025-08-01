import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def move_q(x,y):
    for k in range(8):
        cx,cy = x,y
        while True:
            nx = cx + delta_q_x[k]
            ny = cy + delta_q_y[k]
            if is_valid(nx,ny) and graph[ny][nx] == '.':
                visited[ny][nx] = True
                cx,cy=nx,ny
            else:
                break

def move_k(x,y):
    for k in range(8):
        dx = x + delta_k_x[k]
        dy = y + delta_k_y[k]
        if is_valid(dx,dy) and graph[dy][dx] == '.':
            visited[dy][dx]= True


delta_q_x = [0,0,-1,1,-1,-1,1,1]
delta_q_y = [1,-1,0,0,-1,1,-1,1]
delta_k_x = [-2,-2,-1,-1,1,1,2,2]
delta_k_y = [1,-1,2,-2,2,-2,1,-1]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(['.']*M)

temp = list(map(int,sys.stdin.readline().split()))
Q_N = temp[0]
for i in range(1,len(temp),2):
    graph[temp[i]-1][temp[i+1]-1] = 'Q'

temp = list(map(int,sys.stdin.readline().split()))
K_N = temp[0]
for i in range(1,len(temp),2):
    graph[temp[i]-1][temp[i+1]-1] = 'K'

temp = list(map(int,sys.stdin.readline().split()))
P_N = temp[0]
for i in range(1,len(temp),2):
    graph[temp[i]-1][temp[i+1]-1] = 'P'

visited = []
for _ in range(N):
    visited.append([False]*M)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'Q':
            move_q(j,i)
            visited[i][j] = True
        elif graph[i][j] == 'K':
            move_k(j,i)
            visited[i][j] = True
        elif graph[i][j] == 'P':
            visited[i][j] = True

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1

print(cnt)