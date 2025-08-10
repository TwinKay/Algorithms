'''
아이디어: 주사위의 상태를 전개도로 관리하는 2차원 arr를 만들고 query에 따라 변경
주의사항: 범위를 나가는 경우에는 나가지 않고 출력도 X!

풀이시간: 42분
'''
import sys


def is_valid(x,y):
    '''
    가능 범위를 체크하는 함수
    :param x: (int) x좌표
    :param y: (int) y좌표
    :return: (boolean) True: 가능 좌표
    '''
    return 0<=x<M and 0<=y<N


def up():
    '''
    위로 돌릴때 주사위의 status를 바꾸는 함수
    :return: (None) -> status에 직접 접근
    '''
    temp = status[0][1]
    status[0][1] = status[1][1]
    status[1][1] = status[2][1]
    status[2][1] = status[3][1]
    status[3][1] = temp


def down():
    '''
    아래로 돌릴때 주사위의 status를 바꾸는 함수
    :return: (None) -> status에 직접 접근
    '''
    temp = status[3][1]
    status[3][1] = status[2][1]
    status[2][1] = status[1][1]
    status[1][1] = status[0][1]
    status[0][1] = temp


def right():
    '''
    오른쪽으로 돌릴때 주사위의 status를 바꾸는 함수
    :return: (None) -> status에 직접 접근
    '''
    temp = status[1][0]
    status[1][0] = status[3][1]
    status[3][1] = status[1][2]
    status[1][2] = status[1][1]
    status[1][1] = temp


def left():
    '''
    왼쪽으로 돌릴때 주사위의 status를 바꾸는 함수
    :return: (None) -> status에 직접 접근
    '''
    temp = status[1][0]
    status[1][0] = status[1][1]
    status[1][1] = status[1][2]
    status[1][2] = status[3][1]
    status[3][1] = temp

def change(map_x,map_y):
    '''
    주사위의 밑면과 지도의 수를 바꾸는 함수
    지도의 수가 0 이면 주사위의 밑면 수를 복사
    0이 아니면 주사위에 지도의 수를 복사 후 0으로 변경
    :param map_x: (int) 지도의 x좌표
    :param map_y: (int) 지도의 y좌표
    :return: (None) -> graph와 status에 직접 접근
    '''
    if graph[map_y][map_x] == 0:
        graph[map_y][map_x] = status[3][1]
    else:
        status[3][1] = graph[map_y][map_x]
        graph[map_y][map_x] = 0


delta_x = [0,1,-1,0,0]
delta_y = [0,0,0,-1,1]

N,M,y,x,Q = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

queries = list(map(int, sys.stdin.readline().split()))

# 주사위의 상태 (초기 모두 0, -1은 dummy)
status = [
    [-1,0,-1],
    [0,0,0],
    [-1,0,-1],
    [-1,0,-1]
]

for query in queries:
    dx = x + delta_x[query]
    dy = y + delta_y[query]
    if is_valid(dx,dy): # 범위 안
        if query == 1:
            right()
        elif query == 2:
            left()
        elif query == 3:
            up()
        else:
            down()

        change(dx,dy)
        print(status[1][1]) # 주사위의 윗면
        # x,y 좌표 갱신
        x = dx
        y = dy