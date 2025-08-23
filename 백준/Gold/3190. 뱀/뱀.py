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
timeline = {}
for _ in range(L):
    t,direct = sys.stdin.readline().split()
    timeline[int(t)] = direct


direct = 0
time = 0
while True:
    time += 1
    head_x,head_y = snake[0]
    nx = head_x + delta_x[direct%4]
    ny = head_y + delta_y[direct%4]
    if not is_can_go(nx,ny):
        break

    snake.appendleft((nx,ny))
    snake_idxs.add((nx,ny))

    if graph[ny][nx] == 0:
        pop_idx = snake.pop()
        snake_idxs.remove(pop_idx)
    else:
        graph[ny][nx] = 0

    if time in timeline:
        rotate_direct = timeline[time]
        if rotate_direct == 'L':
            direct -= 1
        else:
            direct += 1

print(time)