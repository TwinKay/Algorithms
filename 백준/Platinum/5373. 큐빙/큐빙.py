# x,y 축 각 한 방향 포지션 변경, 및 시계 방향 돌리기 3개의 함수만으로 구현하기
import sys

# debug_cube = [
#     ['.', '.', '.', 1, 2, 3, '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 4, 5, 6, '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 7, 8, 9, '.', '.', '.', '.', '.', '.'],
#     [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
#     [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
#     [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
#     ['.', '.', '.', 46, 47, 48, '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 49, 50, 51, '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 52, 53, 54, '.', '.', '.', '.', '.', '.'],
#
# ]

def fill_each(graph,x,y,color):
    for i in range(3):
        for j in range(3):
            graph[y+i][x+j] = color

    return graph

def fill_cube(graph):
    graph = fill_each(graph,3,0,'o')
    graph = fill_each(graph,0,3,'g')
    graph = fill_each(graph,3,3,'w')
    graph = fill_each(graph,6,3,'b')
    graph = fill_each(graph,9,3,'y')
    graph = fill_each(graph,3,6,'r')

    return graph


def change_position_x(graph):
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


def change_position_y(graph):
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


def rotate_right(c):
    c[2][3], c[2][4], c[2][5], c[3][6], c[4][6], c[5][6], c[6][5], c[6][4], c[6][3], c[5][2], c[4][2], c[3][2], \
        c[3][3], c[3][4], c[3][5], c[4][5], c[5][5], c[5][4], c[5][3], c[4][3] \
        = \
        c[5][2], c[4][2], c[3][2], c[2][3], c[2][4], c[2][5], c[3][6], c[4][6], c[5][6], c[6][5], c[6][4], c[6][3], \
            c[5][3], c[4][3], c[3][3], c[3][4], c[3][5], c[4][5], c[5][5], c[5][4]

    return c


N = 9; M = 12

TC = int(sys.stdin.readline())
for tc in range(TC):
    cube = []
    for _ in range(N):
        cube.append(['.']*M)

    cube = fill_cube(cube)

    query_num = int(sys.stdin.readline())
    queries = list(sys.stdin.readline().split())
    for query in queries:
        if query[0] == 'U':
            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

        elif query[0] == 'R':
            cube = change_position_x(cube)

            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

            for _ in range(3):
                cube = change_position_x(cube)

        elif query[0] == 'D':
            for _ in range(2):
                cube = change_position_x(cube)

            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

            for _ in range(2):
                cube = change_position_x(cube)

        elif query[0] == 'L':
            for _ in range(3):
                cube = change_position_x(cube)

            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

            cube = change_position_x(cube)

        elif query[0] == 'F':
            cube = change_position_y(cube)

            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

            for _ in range(3):
                cube = change_position_y(cube)

        else:
            for _ in range(3):
                cube = change_position_y(cube)

            if query[1] == '+':
                cube = rotate_right(cube)
            else:
                for _ in range(3):
                    cube = rotate_right(cube)

            cube = change_position_y(cube)

    for c in cube[3:6]:
        print("".join(c[3:6]))