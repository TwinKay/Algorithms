'''
아이디어: 문제에 주어진대로 구현히기
주의사항: 모듈화를 잘해서 실수 방지

풀이시간: 29분
'''
import sys

def is_valid(x,y):
    '''
    범위 내에 있는지 확인하는 함수
    :param x: (int) x좌표
    :param y: (int) y좌표
    :return: (boolean) True: 범위내
    '''
    return 0<=x<N and 0<=y<N


def is_can_go(x,y):
    '''
    사각형이 갈 수 있는지 판단하는 함수, is_valid도 이용
    :param x: (int) x좌표
    :param y: (int) y좌표
    :return: (boolean) True: 범위 안이며 장애물 X
    '''
    if not is_valid(x,y):
        return False
    if graph[y][x] != '.':
        return False
    return True


def get_dist(dest_x,dest_y):
    '''
    유클리드 거리 내에 해당하는지를 확인하는 함수
    :param dest_x: (int) 목적지 x좌표
    :param dest_y: (int) 목적지 y좌표
    :return: (boolean) True: 유클리드 거래 내
    '''
    return abs(dest_x-x) + abs(dest_y-y)


def spread():
    '''
    잉크를 뿌리는 함수
    :return: (None) -> grpah에 직접 뿌림
    '''
    for i in range(N):
        for j in range(N):
            if graph[i][j] != '.' and get_dist(j,i) <= ink_cnt: # 장애물이며 유클리드 거리 내
                graph[i][j] = ink_arr[ink_idx % len(ink_arr)] # 모듈러 연산 사용


def get_first_idx():
    '''
    처음의 사각형의 인덱스를 가져오고 땅으로 만드는 함수
    :return: (None) -> 직접 접근
    '''
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '@':
                graph[i][j] = '.'
                return [j,i]


def set_idx():
    '''
    마지막에 사각형의 위치를 표시하는 함수
    :return: (None) -> 직접 접근
    '''
    graph[y][x] = '@'

# 상 우 하 좌
delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

I,N,Q = map(int, sys.stdin.readline().split())
ink_arr = list(sys.stdin.readline().rstrip())

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

queries = list(sys.stdin.readline().rstrip())

x,y = get_first_idx()
ink_cnt = 0
ink_idx = 0
for query in queries:
    if query == 'j': # 잉크 충전
        ink_cnt += 1
    elif query == 'J':
        spread()
        ink_cnt = 0 # 잉크 소진
        ink_idx += 1 # 다음 잉크 index
    else:
        delta_num = 5 # dummy
        if query == 'R':
            delta_num = 0
        elif query == 'D':
            delta_num = 1
        elif query == 'L':
            delta_num = 2
        elif query == 'U':
            delta_num = 3

        dx = x + delta_x[delta_num]
        dy = y + delta_y[delta_num]
        if is_can_go(dx,dy):
            x = dx
            y = dy

set_idx() # 사각형 위치 입력

for g in graph:
    print("".join(g))