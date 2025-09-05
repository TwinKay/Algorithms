import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def graph_down(graph):
    for i in range(N-1,0,-1): # 맨 위는 볼필요 X
        for j in range(N):
            if graph[i][j] != -3: # 블록이 있으면
                continue
            x,y = j,i-1
            while True:
                if not is_valid(x,y):
                    break
                if graph[y][x] == -1:
                    break
                if graph[y][x] >= 0:
                    graph[y][x],graph[i][j] = graph[i][j],graph[y][x]
                    break
                y -= 1
    return graph

def rotate_left(graph):
    new_graph = []
    for i in range(N):
        new_graph.append([])
    for i in range(N):
        for j in range(N):
            new_graph[i].append(graph[j][N-i-1])
    return new_graph

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

res_score = 0
while True:
    # 여기서부터 돌려라
    visited = []
    for _ in range(N):
        visited.append([0]*N)

    groups = []
    bosses = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 1 and not visited[i][j]: # 일반블록, 방문x
                group_idxs = []
                deq = deque()
                deq.append([j,i])
                visited[i][j] = 1
                color = graph[i][j]
                while deq:
                    x,y = deq.popleft()
                    group_idxs.append([x,y])
                    for k in range(4):
                        dx = x + delta_x[k]
                        dy = y + delta_y[k]
                        if not is_valid(dx,dy):
                            continue
                        if visited[dy][dx]:
                            continue
                        if (graph[dy][dx]==color or graph[dy][dx]==0): # (칼라가 같거나 무지개)
                            deq.append([dx,dy])
                            visited[dy][dx] = 1

                # 무지개 visited 빼주기
                for group_idx in group_idxs:
                    if graph[group_idx[1]][group_idx[0]] == 0:
                        visited[group_idx[1]][group_idx[0]] = 0

                if len(group_idxs) < 2:
                    continue

                boss_x, boss_y = N,N
                for x,y in group_idxs:
                    if graph[y][x] != 0: # 무지개는 대표 X
                        if boss_y < y:
                            continue
                        elif boss_y > y:
                            boss_x,boss_y=x,y
                        else: # y같으면
                            if boss_x > x:
                                boss_x,boss_y=x,y
                            else:
                                continue
                groups.append(group_idxs)
                bosses.append([boss_x,boss_y])

    # 반복문 만들면 주석 해제해야해!!!!!
    if not groups:
        break

    max_size = -1
    remove_id = -1
    rainbow_cnt = -1
    for i in range(len(groups)):
        group = groups[i]

        r_cnt = 0 # rainbow 갯수
        for x, y in group:
            if graph[y][x] == 0:
                r_cnt += 1

        if len(group) > max_size:
            remove_id = i
            max_size = len(group)
            rainbow_cnt = r_cnt
        elif len(group) == max_size:
            if r_cnt > rainbow_cnt:# 무지개 조건 빠짐
                remove_id = i
                rainbow_cnt = r_cnt
            elif r_cnt == rainbow_cnt:

                max_boss_x,max_boss_y = bosses[remove_id]
                boss_x,boss_y = bosses[i]
                if max_boss_y > boss_y:
                    continue
                elif max_boss_y < boss_y:
                    remove_id = i
                else:
                    if max_boss_x < boss_x:
                        remove_id = i

    remove_idxs = groups[remove_id]
    for x,y in remove_idxs:
        graph[y][x] = -3 # -3이 빈공간
    res_score += len(remove_idxs)**2

    graph = graph_down(graph)
    graph = rotate_left(graph)
    graph = graph_down(graph)

print(res_score)