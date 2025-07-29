delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def dfs(x,y):
    global res
    res += graph[y][x]
    visited[y][x] = True
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and not visited[dy][dx] and abs(mid_x-dx)+abs(mid_y-dy)<N//2+1:
            dfs(dx,dy)
            visited[dy][dx] = True

T = int(input())
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,list(input().rstrip()))))

    visited = []
    for _ in range(N):
        visited.append([False]*N)

    res = 0
    mid_x,mid_y = N//2,N//2
    dfs(mid_x,mid_y)

    print(f'#{t} {res}')