import sys
from collections import deque


def is_valid(x,y):
    return 0<=x<M and 0<=y<N


def init_direction(direct):
    arr = [None,0,2,3,1]
    return arr[direct]


def get_heat_graph(heater_info):
    visited = []
    for _ in range(N):
        visited.append([0]*M)

    x,y,direct = heater_info
    first_x = x + delta_x[direct] # 무조건 존재 (문제 조건)
    first_y = y + delta_y[direct]
    deq = deque()
    deq.append([first_x,first_y,5])
    visited[first_y][first_x] = 5
    while deq:
        x,y,num = deq.popleft()
        if num == 1:
            break
        for k in [-1,0,1]:
            if k == 0:
                dx = x + delta_x[direct]
                dy = y + delta_y[direct]
                if not is_valid(dx,dy):
                    continue
                if wall_graph[y][x][direct]:
                    continue
                deq.append([dx,dy,num-1])
                visited[dy][dx] = num-1
            else:
                mx = x + delta_x[(direct+k)%4]
                my = y + delta_y[(direct+k)%4]
                if not is_valid(mx,my):
                    continue
                if wall_graph[y][x][(direct+k)%4]:
                    continue
                dx = mx + delta_x[direct]
                dy = my + delta_y[direct]
                if not is_valid(dx,dy):
                    continue
                if wall_graph[my][mx][direct]:
                    continue
                deq.append([dx,dy,num-1])
                visited[dy][dx] = num-1

    return visited


def on_heater(graph,heater_infos):
    for heater_info in heater_infos:
        heat_graph = get_heat_graph(heater_info)
        for i in range(N):
            for j in range(M):
                graph[i][j] += heat_graph[i][j]

    return graph


def spread(graph):
    spread_graph = []
    for _ in range(N):
        spread_graph.append([0]*M)

    for i in range(N):
        for j in range(M):
            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if not is_valid(dx,dy):
                    continue
                if graph[i][j] <= graph[dy][dx]:
                    continue
                if wall_graph[i][j][k]:
                    continue
                val = int((graph[i][j] - graph[dy][dx]) / 4)
                spread_graph[dy][dx] += val
                spread_graph[i][j] -= val

    for i in range(N):
        for j in range(M):
            graph[i][j] += spread_graph[i][j]

    return graph


def reduce_side(graph):
    for j in range(M):
        if graph[0][j] >= 1:
            graph[0][j] -= 1
        if graph[N-1][j] >= 1:
            graph[N-1][j] -= 1

    for i in range(1,N-1):
        if graph[i][0] >= 1:
            graph[i][0] -= 1
        if graph[i][M-1] >= 1:
            graph[i][M-1] -= 1

    return graph


def is_end(target_idxs):
    for x,y in target_idxs:
        if graph[y][x] < K:
            return False
    return True


delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N,M,K = map(int, sys.stdin.readline().split())
input_graph = []
for _ in range(N):
    input_graph.append(list(map(int, sys.stdin.readline().split())))

heater_infos = []
target_idxs = []
for i in range(N):
    for j in range(M):
        if not input_graph[i][j]:
            continue
        if input_graph[i][j] == 5:
            target_idxs.append([j,i])
        else:
            heater_infos.append([j,i,init_direction(input_graph[i][j])])

wall_graph = []
for i in range(N):
    wall_graph.append([])
    for j in range(M):
        wall_graph[i].append([0]*4)


wall_cnt = int(sys.stdin.readline())
for _ in range(wall_cnt):
    y,x,t = map(int, sys.stdin.readline().split())
    x -= 1; y -= 1
    if t == 0:
        wall_graph[y][x][3] = 1
        if is_valid(x,y-1):
            wall_graph[y-1][x][1] = 1
    else:
        wall_graph[y][x][0] = 1
        if is_valid(x+1,y):
            wall_graph[y][x+1][2] = 1

graph = []
for _ in range(N):
    graph.append([0]*M)

res = 0
while True:
    # 바람 나옴
    graph = on_heater(graph,heater_infos)

    # 온도 조절
    graph = spread(graph)

    # 테투리 온도 조절
    graph = reduce_side(graph)

    # 초콜릿 먹기
    res += 1
    if res == 101:
        break

    # 조사 칸 break
    if is_end(target_idxs):
        break

print(res)