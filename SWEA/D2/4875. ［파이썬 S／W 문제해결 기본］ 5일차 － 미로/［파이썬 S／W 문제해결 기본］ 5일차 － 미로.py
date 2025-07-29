'''
아이디어:
recu으로 dfs
'''
 
delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]
 
def is_valid(x,y):
    return 0<=x<N and 0<=y<N
 
def dfs(x,y):
    global is_exit
    visited[y][x] = True
    for k in range(4): # 4방향 탐색
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and graph[dy][dx] != 1 and not visited[dy][dx]: # 가능한 범위, 벽이 아님, 방문 X
            if dx == exit_x and dy == exit_y: # 탈출구 찾으면
                is_exit = True
                return
            dfs(dx,dy)
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, list(input().rstrip()))))
 
    start_x,start_y,exit_x,exit_y = N,N,N,N
     
    # 입구 출구 찾아놓기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                start_x,start_y = j,i
            elif graph[i][j] == 3:
                exit_x, exit_y = j,i
 
    visited = []
    for _ in range(N):
        visited.append([False]*N)
 
    is_exit = False
    dfs(start_x,start_y)
    if is_exit:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')