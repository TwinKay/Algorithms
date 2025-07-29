'''
아이디어:
단순 시뮬
종수 먼저 이동 -> 미친 아두이노 이동
아두이노 2개가 만나면 폭발 -> 3개 이상 조심! 한번에 터져야 함
종수가 이동하며 미친 아두이노를 만날 수도 있음!
중간에 종료되면 kraj X
'''

import sys

delta_x = [-1,0,1,-1,0,1,-1,0,1]
delta_y = [1,1,1,0,0,0,-1,-1,-1]

def move_jongsu(direct): # True: 게임 끝
    global jongsu_x,jongsu_y
    dx = jongsu_x + delta_x[direct-1]
    dy = jongsu_y + delta_y[direct-1]
    if graph[dy][dx] == 'R': # 미친 아두이노 만남
        return True
    graph[dy][dx],graph[jongsu_y][jongsu_x] = graph[jongsu_y][jongsu_x],graph[dy][dx]
    jongsu_x,jongsu_y = dx,dy
    return False

def move_adu(): # True: 게임 끝
    global graph
    new_graph = []
    for _ in range(N):
        new_graph.append(['.']*M)
    new_graph[jongsu_y][jongsu_x] = 'I'
    bomb_idxs = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                adu_delta_x = 0
                adu_delta_y = 0
                if jongsu_x > j:
                    adu_delta_x = 1
                elif jongsu_x < j:
                    adu_delta_x = -1
                if jongsu_y > i:
                    adu_delta_y = 1
                elif jongsu_y < i:
                    adu_delta_y = -1

                dx = j + adu_delta_x
                dy = i + adu_delta_y
                if new_graph[dy][dx] == 'I':
                    return True
                elif new_graph[dy][dx] == 'R':
                    bomb_idxs.append([dx,dy])
                else:
                    new_graph[dy][dx] = 'R'

    for idx in bomb_idxs:
        new_graph[idx[1]][idx[0]] = '.'

    graph = new_graph

    return False

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
directions = list(map(int,list(sys.stdin.readline().rstrip())))

jongsu_x,jongsu_y = -1,-1
is_find = False
for i in range(N):
    if is_find:
        break
    for j in range(M):
        if graph[i][j] == 'I':
            jongsu_x = j
            jongsu_y = i
            is_find = True
            break

is_end = False
for time, query in enumerate(directions):
    if move_jongsu(query):
        print(f'kraj {time+1}')
        is_end = True
        break
    elif move_adu():
        print(f'kraj {time+1}')
        is_end = True
        break

if not is_end:
    for g in graph:
        print("".join(g))