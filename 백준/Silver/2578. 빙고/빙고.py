'''
아이디어:
모든 칸을 확인할 필요 X
해당 칸의 행,열만 확인하고 대각선에 속할 때만 대각선을 확인하면 된다.
'''

import sys

def find_idx(num):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                return [j,i] # x,y

def check_bingo(x,y):
    is_row_bingo = True
    is_col_bingo = True
    for i in range(5):
        if graph[y][i] != 0:
            is_col_bingo = False
            break
    for i in range(5):
        if graph[i][x] != 0:
            is_row_bingo = False
            break

    bingo_cnt = 0
    if is_row_bingo:
        bingo_cnt += 1
    if is_col_bingo:
        bingo_cnt += 1

    return bingo_cnt

def check_bingo_cross1():
    for i in range(5):
        if graph[i][i] != 0:
            return 0

    return 1
def check_bingo_cross2():
    for i in range(5):
        if graph[4-i][i] != 0:
           return 0

    return 1

N = 5
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

queries = []
for _ in range(N):
    queries.extend(list(map(int, sys.stdin.readline().split())))

cnt = 0
for time in range(1,26):
    x,y = find_idx(queries[time-1])
    graph[y][x] = 0
    cnt += check_bingo(x,y)
    if x == y:
        cnt += check_bingo_cross1()
    if x+y == 4:
        cnt += check_bingo_cross2()

    if cnt >= 3:
        print(time)
        break