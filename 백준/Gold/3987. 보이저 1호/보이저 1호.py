import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

start_y,start_x = map(int, sys.stdin.readline().split())
start_x -= 1
start_y -= 1
res = []
for direct in range(4):
    visited = []
    for i in range(N):
        visited.append([])
        for j in range(M):
            visited[i].append([False]*4)

    x,y = start_x,start_y
    cnt = 1
    visited[y][x][direct%4] = True
    while True:
        dx = x + delta_x[direct%4]
        dy = y + delta_y[direct%4]
        if not is_valid(dx,dy) or graph[dy][dx] == 'C':
            break
        if visited[dy][dx][direct%4]:
            cnt = float("inf")
            break
        if graph[dy][dx] in ["\\","/"]:
            if graph[dy][dx] == "\\":
                if direct%4 in [1,3]:
                    direct += 1
                else:
                    direct -= 1
            elif graph[dy][dx] == "/":
                if direct % 4 in [0,2]:
                    direct += 1
                else:
                    direct -= 1

        visited[dy][dx][direct%4] = True
        x,y, = dx,dy
        cnt += 1

    res.append(cnt)

max_val = max(res)
if res[0] == max_val:
    print("U")
    if max_val == float("inf"):
        print("Voyager")
    else:
        print(max_val)
elif res[1] == max_val:
    print("R")
    if max_val == float("inf"):
        print("Voyager")
    else:
        print(max_val)
elif res[2] == max_val:
    print("D")
    if max_val == float("inf"):
        print("Voyager")
    else:
        print(max_val)
elif res[3] == max_val:
    print("L")
    if max_val == float("inf"):
        print("Voyager")
    else:
        print(max_val)