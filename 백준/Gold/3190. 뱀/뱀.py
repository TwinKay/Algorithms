'''
아이디어:
deque와 set 사용을 통한 최적화.
    -> 뱀을 deque로 관리하자니 본인과 부딪히는 경우 조회가 오래걸리고
    -> list로 관리하자니 pop이 오래걸리기 때문
'''
import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def is_can_go(x,y):
    '''
    뱀이 갈 수 있으면 True를 반환하는 함수
    :param x: (int) 뱀이 이동할 x
    :param y: (int) 뱀이 이동할 y
    :return: (boolean) True -> 이동 가능
    '''
    if is_valid(x,y):
        if (x,y) not in snake_idxs:
            return True
    return False

delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append([0]*N)
for _ in range(K):
    y,x = map(int, sys.stdin.readline().split())
    graph[y-1][x-1] = 1

snake = deque()
snake.append((0,0))
snake_idxs = set()
snake_idxs.add((0,0))


L = int(sys.stdin.readline())
timeline = {} # 시간의 끝을 알 수도 없으며 list에서 조회한다면 시간 오래 걸림
for _ in range(L):
    t,direct = sys.stdin.readline().split()
    timeline[int(t)] = direct # timeline에 key:time value:방향 으로 저장


direct = 0 # 위
time = 0
while True:
    time += 1
    head_x,head_y = snake[0]
    nx = head_x + delta_x[direct%4]
    ny = head_y + delta_y[direct%4]
    if not is_can_go(nx,ny): # 본인 또는 벽과 만나는 경우
        break

    snake.appendleft((nx,ny)) # 머리를 늘려 이동
    snake_idxs.add((nx,ny)) # set에도 관리

    if graph[ny][nx] == 0: # 사과 없음
        pop_idx = snake.pop() # 꼬리 자르기
        snake_idxs.remove(pop_idx) # 꼬리 set에도 관리
    else: # 사과 있음 (꼬리 자르기 X)
        graph[ny][nx] = 0 # 사과 먹기

    if time in timeline: # 회전을 해야하는 시간이면
        rotate_direct = timeline[time]
        if rotate_direct == 'L':
            direct -= 1
        else:
            direct += 1

print(time)