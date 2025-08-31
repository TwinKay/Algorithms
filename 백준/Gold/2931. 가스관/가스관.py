import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def get_first_direction(x,y):
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if not is_valid(dx,dy):
            continue
        if graph[dy][dx] != '.': # 파이프가 없고
            pipe_num = graph[dy][dx]
            if k in pipe_info[pipe_num].keys(): # 파이프로 들어갈 수 있는 방향이면
                return k


def get_can_move_info(x, y, direct):
    while True:
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]
        if graph[dy][dx] == '.':
            return x, y, direct

        next_pipe_num = graph[dy][dx]

        next_direct = pipe_info[next_pipe_num][direct]
        x, y, direct = dx, dy, next_direct
        visited[dy][dx] = 1


pipe_to_num = {
    '|':'1',
    '-':'2',
    '+':'3',
    '1':'4',
    '2':'5',
    '3':'6',
    '4':'7'
}
num_to_pipe = {
    '1':'|',
    '2':'-',
    '3':'+',
    '4':'1',
    '5':'2',
    '6':'3',
    '7':'4'
}

pipe_info = {}
# pipe 번호 - key:can_enter_direct
#            value: [next direct]
pipe_info['1'] = {
    0:0,
    2:2
}
pipe_info['2'] = {
    1:1,
    3:3
}
pipe_info['3'] = {
    1:1,
    3:3,
    0:0,
    2:2
}
pipe_info['4'] = {
    0:1,
    3:2
}
pipe_info['5'] = {
    3:0,
    2:1
}
pipe_info['6'] = {
    1:0,
    2:3
}
pipe_info['7'] = {
    1:2,
    0:3
}

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

x1,y1,x2,y2 = N,N,N,N
for i in range(N):
    for j in range(M):
        if graph[i][j] == '.':
            continue
        elif graph[i][j] == 'M':
            x1,y1 = j,i
            graph[i][j] = '.'
        elif graph[i][j] == 'Z':
            x2,y2 = j,i
            graph[i][j] = '.'
        else:
            graph[i][j] = pipe_to_num[graph[i][j]]

direct1 = get_first_direction(x1,y1)
direct2 = get_first_direction(x2,y2)

visited = []
for i in range(N):
    visited.append([0]*M)
    
x1,y1,direct1 = get_can_move_info(x1,y1,direct1)
x2,y2,direct2 = get_can_move_info(x2,y2,direct2)

is_plus = False
for i in range(N):
    if is_plus:
        break
    for j in range(M):
        if graph[i][j] != '.' and not visited[i][j]: # 파이프인데 간 곳이 없는 경우
            is_plus = True
            break

res_x,res_y,res_pipe = M,N,10
if is_plus:
    res_x = x1+delta_x[direct1]
    res_y = y1+delta_y[direct1]
    res_pipe = '3'
else:
    for pipe_num in ['1','2','4','5','6','7']:
        for enter_direct in pipe_info[pipe_num].keys():
            if enter_direct != direct1:
                continue
            exit_direct = pipe_info[pipe_num][enter_direct]
            mid_x = x1+delta_x[enter_direct]
            mid_y = y1+delta_y[enter_direct]
            cand_x = mid_x+delta_x[exit_direct]
            cand_y = mid_y+delta_y[exit_direct]
            if cand_x == x2 and cand_y==y2:
                res_x,res_y,res_pipe = mid_x,mid_y,pipe_num

print(res_y+1,res_x+1,num_to_pipe[res_pipe])