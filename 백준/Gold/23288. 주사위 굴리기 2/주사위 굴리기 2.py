'''
아이디어:
시뮬 + BFS
반대 방향은 3번 반복
'''
import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def rotate_right():
    temp = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] = dice[3][1]
    dice[3][1] = dice[1][2]
    dice[1][2] = temp

def rotate_front():
    temp = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = temp

def get_dice_ground():
    return dice[3][1]

def bfs(x,y):
    visited = []
    for _ in range(N):
        visited.append([False] * M)

    deq = deque()
    deq.append([x,y])
    visited[y][x] = True
    cnt = 0
    while deq:
        cnt += 1
        cur = deq.popleft()
        x,y = cur
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == graph[y][x]:
                deq.append([dx,dy])
                visited[dy][dx] = True
    return cnt

dice = [
    [0,2,0],
    [4,1,3],
    [0,5,0],
    [0,6,0]
]

delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N,M,T = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

direct = 0
x,y = 0,0
score = 0
for _ in range(T):
    dx = x + delta_x[direct%4]
    dy = y + delta_y[direct%4]
    if not is_valid(dx,dy):
        direct += 2
        dx = x + delta_x[direct % 4]
        dy = y + delta_y[direct % 4]
    if direct%4 == 0:
        rotate_right()
    elif direct%4 == 1:
        rotate_front()
    elif direct%4 == 2:
        rotate_right()
        rotate_right()
        rotate_right()
    else:
        rotate_front()
        rotate_front()
        rotate_front()

    cnt = bfs(dx,dy)
    score += graph[dy][dx] * cnt

    ground_val = get_dice_ground()
    if ground_val > graph[dy][dx]:
        direct += 1
    elif ground_val < graph[dy][dx]:
        direct -= 1

    x,y, = dx,dy

print(score)