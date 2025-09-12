'''
MAX INPUT으로도 잘 돌아가는 코드
    -> 물론 "격자 위에 있는 물고기의 수가 항상 1,000,000 이하인 입력만 주어진다."
       라서 턴당 최대 1,000,000마리만 이동하지만 해당 조건이 없을 경우도 생각해보자

[엣지케이스]
10 100
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 1 7
1 1 8
2 1 1
2 1 1
2 1

답: 1172979502354464511868
=> 선정이유: 물론 "격자 위에 있는 물고기의 수가 항상 1,000,000 이하인 입력만 주어진다."
       라서 턴당 최대 1,000,000마리만 이동하지만 해당 조건이 없을 경우도 생각해보자
'''
import sys
from itertools import product

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def move_each_fish(x, y, direct):
    for k in range(8):
        dx = x + delta8_x[(direct - k) % 8]
        dy = y + delta8_y[(direct - k) % 8]

        if not is_valid(dx, dy):
            continue
        if dx == shark_x and dy == shark_y:
            continue
        if smell_graph[dy][dx] >= time:
            continue
        return dx, dy, (direct - k) % 8
    return x, y, direct

def move_fish(arr):
    next_arr = [[[0]*8 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d in range(8):
                cnt = arr[i][j][d]
                if cnt > 0:
                    dx, dy, direct = move_each_fish(j, i, d)
                    next_arr[dy][dx][direct] += cnt
    return next_arr

def move_shark_each_direction(arr, x, y, directs):
    dx1, dy1 = x + delta4_x[directs[0]], y + delta4_y[directs[0]]
    dx2, dy2 = dx1 + delta4_x[directs[1]], dy1 + delta4_y[directs[1]]
    dx3, dy3 = dx2 + delta4_x[directs[2]], dy2 + delta4_y[directs[2]]

    if not (is_valid(dx1, dy1) and is_valid(dx2, dy2) and is_valid(dx3, dy3)):
        return None, None

    visited = set([(dx1, dy1), (dx2, dy2), (dx3, dy3)]) # 같은 곳 또 방문 가능하니깐
    cnt_fish = 0
    for dx, dy in visited:
        cnt_fish += sum(arr[dy][dx])
    return cnt_fish, [(dx1, dy1), (dx2, dy2), (dx3, dy3)]

def move_shark(arr, x, y):
    global shark_x, shark_y
    best_path, max_fish = None, -1

    for pro in product(range(4), repeat=3):
        cnt_fish, path = move_shark_each_direction(arr, x, y, pro)
        if cnt_fish is None:
            continue
        if cnt_fish > max_fish:
            max_fish = cnt_fish
            best_path = path

    for (dx, dy) in best_path:
        if sum(arr[dy][dx]) > 0:
            smell_graph[dy][dx] = time + 2 # 2초동안
            arr[dy][dx] = [0]*8 # 초기화

    shark_x, shark_y = best_path[-1]
    return arr, shark_x, shark_y

def paste(arr, copy_arr):
    for i in range(N):
        for j in range(N):
            for d in range(8):
                arr[i][j][d] += copy_arr[i][j][d]
    return arr



delta8_x = [-1,-1,0,1,1,1,0,-1]
delta8_y = [0,-1,-1,-1,0,1,1,1]
delta4_x = [0,-1,0,1]
delta4_y = [-1,0,1,0]

N = 4
M, S = map(int, sys.stdin.readline().split())

graph = [[[0]*8 for _ in range(N)] for _ in range(N)] # 3차원은 방향에 따라 += 1해서 물고기 한번에 관리

for _ in range(M):
    y, x, direct = map(int, sys.stdin.readline().split())
    graph[y-1][x-1][direct-1] += 1

shark_y, shark_x = map(int, sys.stdin.readline().split())
shark_x -= 1; shark_y -= 1

smell_graph = [[-1]*N for _ in range(N)]

for time in range(1, S+1):
    # copy
    copy_graph = [[t[:] for t in temp] for temp in graph]

    # 물고기 이동
    graph = move_fish(graph)

    # 상어 이동
    graph, shark_x, shark_y = move_shark(graph, shark_x, shark_y)

    # paste
    graph = paste(graph, copy_graph)

# 결과 계산
res = 0
for i in range(N):
    for j in range(N):
        res += sum(graph[i][j]) # 8방 한번에 더하기

print(res)