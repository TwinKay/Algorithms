import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [10000,0,0,-1,1]
delta_y = [10000,-1,1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
visited = []
for _ in range(N):
    graph.append(['.']*M)
    visited.append([False]*M)

K = int(sys.stdin.readline())
for _ in range(K):
    dis_y,dis_x = map(int, sys.stdin.readline().split())
    graph[dis_y][dis_x] = '0'

y,x = map(int, sys.stdin.readline().split())
direction_arr = list(map(int, sys.stdin.readline().split()))

direct = 0
visited[y][x] = True
cnt_stay = 0
while True:
    dx = x + delta_x[direction_arr[direct%4]]
    dy = y + delta_y[direction_arr[direct%4]]
    if not is_valid(dx,dy) or graph[dy][dx]=='0' or visited[dy][dx]:
        direct += 1
        cnt_stay += 1
        if cnt_stay == 5: # 안전하게 5
            print(f'{y} {x}')
            break
        continue

    visited[dy][dx] = True
    cnt_stay = 0
    x,y = dx,dy