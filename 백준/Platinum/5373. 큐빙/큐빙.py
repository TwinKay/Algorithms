# 오른쪽이 윗면 전개도로 바뀌는 함수 1, 왼쪽이 윗면 전개도로 바뀌는 함수 2, 윗면을 시계 방향으로 돌리는 함수 3
# 총 3개의 함수 반복을 통한 구현 -> 시간 복잡도 충분
import sys

query_dic = {}
for i, q in enumerate("URDLFB"):
    query_dic[q] = i


def fill_each(graph, x, y, color):  # fill cube를 통해 각각 색칠하는 함수
    for i in range(3):
        for j in range(3):
            graph[y + i][x + j] = color

    return graph


def fill_cube(graph):  # 큐브 색칠하는 함수
    graph = fill_each(graph, 3, 0, 'o')
    graph = fill_each(graph, 0, 3, 'g')
    graph = fill_each(graph, 3, 3, 'w')
    graph = fill_each(graph, 6, 3, 'b')
    graph = fill_each(graph, 9, 3, 'y')
    graph = fill_each(graph, 3, 6, 'r')

    return graph


def change_position_x(graph):  # 오른쪽면을 윗면 전개도로 바뀌는 함수
    temp = []
    for _ in range(3):
        temp.append(['.'] * 3)

    for i in range(3, 6):
        for j in range(3):
            temp[i - 3][j - 3] = graph[i][j]

    for i in range(3, 6):
        for j in range(9):
            graph[i][j] = graph[i][j + 3]

    for i in range(3):
        for j in range(3):
            graph[i + 3][j + 9] = temp[i][j]

    for i in range(3):
        for j in range(3):
            temp[i][j] = graph[i][j + 3]

    for i in range(3):
        for j in range(3):
            graph[i][3 + j] = temp[2 - j][i]

    for i in range(3):
        for j in range(3):
            temp[i][j] = graph[i + 6][j + 3]

    for i in range(3):
        for j in range(3):
            graph[6 + i][3 + j] = temp[j][2 - i]

    return graph


def change_position_y(graph):  # 앞면을 윗면 전개도로 바뀌는 함수
    temp = []
    for _ in range(3):
        temp.append(['.'] * 3)

    for i in range(3):
        for j in range(3):
            temp[i][j] = graph[i][j + 3]

    for i in range(6):
        for j in range(3, 6):
            graph[i][j] = graph[i + 3][j]

    for i in range(3):
        for j in range(3):
            graph[8 - i][5 - j] = graph[i + 3][j + 9]

    for i in range(3):
        for j in range(3):
            graph[5 - i][11 - j] = temp[i][j]

    for i in range(3):
        for j in range(3):
            temp[i][j] = graph[i + 3][j]

    for i in range(3):
        for j in range(3):
            graph[i + 3][j] = temp[j][2 - i]

    for i in range(3):
        for j in range(3):
            temp[i][j] = graph[i + 3][j + 6]

    for i in range(3):
        for j in range(3):
            graph[i + 3][j + 6] = temp[2 - j][i]

    return graph

def change_position(query,graph): # 특정 면을 윗면으로 바꾸는 것은 곧 change x y 함수를 k번 반복
    query = query_dic[query]
    rotate_cnt_arr = [0,1,2,3,1,3] # 각 반복 횟수
    if query <= 3: # x 기준 전개도 돌리기
        for _ in range(rotate_cnt_arr[query]):
            graph = change_position_x(graph)
    else: # y 기준 전개도 돌리기
        for _ in range(rotate_cnt_arr[query]):
            graph = change_position_y(graph)

    return graph


def roll_back_position(query,graph): # 원래 윗면을 윗면으로 원복
    query = query_dic[query]
    rotate_cnt_arr = [0,3,2,1,3,1] # change_position과 합쳐서 4번이어야 함(원래 윗면은 안 돌려줌)
    if query <= 3: # x 기준 전개도 돌리기
        for _ in range(rotate_cnt_arr[query]):
            graph = change_position_x(graph)
    else: # y 기준 전개도 돌리기
        for _ in range(rotate_cnt_arr[query]):
            graph = change_position_y(graph)

    return graph


def rotate_right(c):  # 윗면을 시계방향으로 회전하는 함수
    c[2][3], c[2][4], c[2][5], c[3][6], c[4][6], c[5][6], c[6][5], c[6][4], c[6][3], c[5][2], c[4][2], c[3][2], \
        c[3][3], c[3][4], c[3][5], c[4][5], c[5][5], c[5][4], c[5][3], c[4][3] \
        = \
        c[5][2], c[4][2], c[3][2], c[2][3], c[2][4], c[2][5], c[3][6], c[4][6], c[5][6], c[6][5], c[6][4], c[6][3], \
            c[5][3], c[4][3], c[3][3], c[3][4], c[3][5], c[4][5], c[5][5], c[5][4]

    return c


def rotate_left(c):  # 반시계 방향은 곧 rotate_right 3번 반복
    for _ in range(3):
        c = rotate_right(c)

    return c


N = 9; M = 12
TC = int(sys.stdin.readline())
for tc in range(TC):
    cube = []
    for _ in range(N):
        cube.append(['.'] * M)  # 큐브 뼈대
    cube = fill_cube(cube)  # 큐브 색칠하기

    _ = sys.stdin.readline()
    queries = list(sys.stdin.readline().split())
    for query in queries:
        cube = change_position(query[0], cube) # 특정 면이 윗면으로

        if query[1] == '+':
            cube = rotate_right(cube)
        else:
            cube = rotate_left(cube) # rotate_right 3번 반복

        cube = roll_back_position(query[0], cube) # 윗면 원복


    # 윗면만 출력
    for c in cube[3:6]:
        print("".join(c[3:6]))