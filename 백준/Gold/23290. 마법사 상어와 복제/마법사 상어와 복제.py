# BFS로 상어를 움직이면 사전 순은 보장은 되겠지만 복제되어 본인과 동일한
# 위치에 있는 물고기를 잡아먹지 못한다.
#   => 그냥 완탐으로 보자
import sys
from itertools import product

def is_valid(x,y):
    return 0<=x<N and 0<=y<N


def move_each_fish(x,y,direct):
    for k in range(8):
        dx = x + delta8_x[(direct-k)%8]
        dy = y + delta8_y[(direct-k)%8]

        if not is_valid(dx,dy):
            continue
        if dx == shark_x and dy == shark_y:
            continue
        if smell_graph[dy][dx] >= time: # 잘 확인해
            continue
        return dx,dy,(direct-k)%8
    return x,y,direct


def move_fish(arr):
    next_arr = []
    for i in range(N):
        next_arr.append([])
        for _ in range(N):
            next_arr[i].append([])

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for fish in arr[i][j]:
                    dx,dy,direct = move_each_fish(j,i,fish)
                    next_arr[dy][dx].append(direct)

    return next_arr


def move_shark_each_direction(arr,x,y,directs):
    dx_1 = x + delta4_x[directs[0]]
    dy_1 = y + delta4_y[directs[0]]
    dx_2 = dx_1 + delta4_x[directs[1]]
    dy_2 = dy_1 + delta4_y[directs[1]]
    dx_3 = dx_2 + delta4_x[directs[2]]
    dy_3 = dy_2 + delta4_y[directs[2]]

    if not is_valid(dx_1,dy_1) or not is_valid(dx_2,dy_2) or not is_valid(dx_3,dy_3):
        return None,None

    directs_set = set()
    directs_set.add((dx_1,dy_1))
    directs_set.add((dx_2,dy_2))
    directs_set.add((dx_3,dy_3))

    cnt_fish = 0
    for dx,dy in directs_set:
        cnt_fish += len(arr[dy][dx])

    return cnt_fish,[(dx_1,dy_1),(dx_2,dy_2),(dx_3,dy_3)]


def move_shark(arr,x,y):
    global shark_x,shark_y

    direct_to_max_fish = None
    max_fish_val = -1
    for pro in product(range(4), repeat=3):
        cnt_fish,move_idxs = move_shark_each_direction(arr,x,y,pro)
        if cnt_fish == None:
            continue
        if max_fish_val >= cnt_fish:
            continue
        max_fish_val = cnt_fish
        direct_to_max_fish = move_idxs

    if arr[direct_to_max_fish[0][1]][direct_to_max_fish[0][0]]:
        smell_graph[direct_to_max_fish[0][1]][direct_to_max_fish[0][0]] = time + 2
        arr[direct_to_max_fish[0][1]][direct_to_max_fish[0][0]] = []
    if arr[direct_to_max_fish[1][1]][direct_to_max_fish[1][0]]:
        smell_graph[direct_to_max_fish[1][1]][direct_to_max_fish[1][0]] = time + 2
        arr[direct_to_max_fish[1][1]][direct_to_max_fish[1][0]] = []
    if arr[direct_to_max_fish[2][1]][direct_to_max_fish[2][0]]:
        smell_graph[direct_to_max_fish[2][1]][direct_to_max_fish[2][0]] = time + 2
        arr[direct_to_max_fish[2][1]][direct_to_max_fish[2][0]] = []

    shark_x, shark_y = direct_to_max_fish[2][0],direct_to_max_fish[2][1]

    return arr,direct_to_max_fish[2][0],direct_to_max_fish[2][1]


def paste(arr,copy_arr):
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j]:
                for fish in copy_arr[i][j]:
                    arr[i][j].append(fish)
    return arr

delta8_x = [-1,-1,0,1,1,1,0,-1]
delta8_y = [0,-1,-1,-1,0,1,1,1]
delta4_x = [0,-1,0,1]
delta4_y = [-1,0,1,0]

N = 4
M,S = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append([])
    for j in range(N):
        graph[i].append([])

for _ in range(M):
    y,x,direct = map(int, sys.stdin.readline().split())
    graph[y-1][x-1].append(direct-1)

shark_y,shark_x = map(int, sys.stdin.readline().split())
shark_x-=1; shark_y-=1

smell_graph = []
for _ in range(N):
    smell_graph.append([-1]*N)

for time in range(1,S+1):
    # copy
    copy_graph = [[t[:] for t in temp] for temp in graph]

    # 물고기 이동
    graph = move_fish(graph)

    # 상어 이동
    graph,shark_x,shark_y = move_shark(graph,shark_x,shark_y)

    # paste
    graph = paste(graph,copy_graph)

# 물고기 수 세기
res = 0
for i in range(N):
    for j in range(N):
        res += len(graph[i][j])

print(res)