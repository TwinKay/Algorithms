import sys
from collections import deque


def find_idxs(x,y,is_garo):
    idxs = []
    if is_garo:
        for i in range(-1,2,1):
            idxs.append([x+i,y,is_garo])
    else:
        for i in range(-1,2,1):
            idxs.append([x,y+i,is_garo])
    return idxs


def is_valid(x,y,is_garo):
    idxs = find_idxs(x,y,is_garo)
    for idx in idxs:
        for n in idx:
            if n<0 or n>=N:
                return False
        if graph[idx[1]][idx[0]] != '0':
            return False
    return True

def is_valid_trans(x,y):
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            dx = x + j
            dy = y + i
            if 0>dy or N<=dy or 0>dx or N<=dx:
                return False
            if graph[dy][dx] != '0':
                return False
    return True


def is_end(x,y,is_garo):
    idxs = find_idxs(x, y, is_garo)
    for i in range(3):
        for j in range(2):
            if idxs[i][j] != end_idxs[i][j]:
                return False
    return True


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

tree_idxs = []
end_idxs = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'B':
            tree_idxs.append([j,i])
            graph[i][j] = '0'
        elif graph[i][j] == 'E':
            end_idxs.append([j,i])
            graph[i][j] = '0'

is_garo = True
if tree_idxs[0][1] != tree_idxs[1][1]:
    is_garo = False

visited = [] # 3차원: 가로,세로 차원 (중앙값 기준)
for i in range(N):
    visited.append([])
    for j in range(N):
        visited[i].append([False,False])

deq = deque()
deq.append([tree_idxs[1][0],tree_idxs[1][1],is_garo,0])
if is_garo:
    visited[tree_idxs[1][1]][tree_idxs[1][0]][0] = True
else:
    visited[tree_idxs[1][1]][tree_idxs[1][0]][1] = True

res = 0
while deq:
    cur = deq.popleft()
    x = cur[0]
    y = cur[1]
    is_garo = cur[2]
    cnt = cur[3]

    if is_end(x,y,is_garo):
        res = cnt
        break
    for k in range(4): # 4방탐색
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy,is_garo):

            # deq.append([dx,dy,is_garo,cnt+1])
            if is_garo and not visited[dy][dx][0]:
                deq.append([dx, dy, is_garo, cnt + 1])
                visited[dy][dx][0] = True
            elif not is_garo and not visited[dy][dx][1]:
                deq.append([dx, dy, is_garo, cnt + 1])
                visited[dy][dx][1] = True
    # Trans
    if is_valid_trans(x, y):
        next_garo = not is_garo
        if next_garo and not visited[y][x][0]:
            deq.append([x, y, next_garo, cnt + 1])
            visited[y][x][0] = True
        elif not next_garo and not visited[y][x][1]:
            deq.append([x, y, next_garo, cnt + 1])
            visited[y][x][1] = True

print(res)