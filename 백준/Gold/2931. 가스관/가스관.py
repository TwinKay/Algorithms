import sys

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

# pipe_switch = {}
# pipe_switch['1'] = '|'
# pipe_switch['2'] = '-'
# pipe_switch['3'] = '+'
# pipe_switch['4'] = '4'
# pipe_switch['5'] = '5'
# pipe_switch['6'] = '6'
# pipe_switch['7'] = '7'
# pipe_switch['|'] = '1'
# pipe_switch['-'] = '2'
# pipe_switch['+'] = '3'

pipe_info = {}
# pipe 번호 - key:can enter direct value: [next direct]
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

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def get_first_direction(x,y):
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if not is_valid(dx,dy):
            continue
        if graph[dy][dx] != '.':
            pipe_num = graph[dy][dx]
            if k in pipe_info[pipe_num].keys():
                return k



N,M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

x1,y1,x2,y2 = N,N,N,N
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'M':
            x1,y1 = j,i
            graph[i][j] = '.'
        elif graph[i][j] == 'Z':
            x2,y2 = j,i
            graph[i][j] = '.'
        elif graph[i][j] == '|':
            graph[i][j] = '1'
        elif graph[i][j] == '-':
            graph[i][j] = '2'
        elif graph[i][j] == '+':
            graph[i][j] = '3'
        elif graph[i][j] == '1':
            graph[i][j] = '4'
        elif graph[i][j] == '2':
            graph[i][j] = '5'
        elif graph[i][j] == '3':
            graph[i][j] = '6'
        elif graph[i][j] == '4':
            graph[i][j] = '7'


direct1 = get_first_direction(x1,y1)
direct2 = get_first_direction(x2,y2)

visited = []
for i in range(N):
    visited.append([])
    for _ in range(M):
        visited[i].append([0]*2)
visited[y1][x1][0] = 1
visited[y2][x2][0] = 1

def get_can_move_info(x,y,direct):
    while True:
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]
        if graph[dy][dx] == '.':
            return x,y,direct

        next_pipe_num = graph[dy][dx]
        # if direct not in pipe_info[next_pipe_num].keys():
        #     continue

        next_direct = pipe_info[next_pipe_num][direct]
        x,y,direct = dx,dy,next_direct
        if next_pipe_num == '3':
            if direct%2 == 0:
                visited[dy][dx][1] = 1
            else:
                visited[dy][dx][0] = 1
        else:
            visited[dy][dx][0] = 1


x1,y1,direct1 = get_can_move_info(x1,y1,direct1)
x2,y2,direct2 = get_can_move_info(x2,y2,direct2)


is_plus = False
for i in range(N):
    if is_plus:
        break
    for j in range(M):
        if graph[i][j] != '.' and not visited[i][j][0]:
            is_plus = True
            break

if x2-x1 == 0 and y2-y1 == 2:
    if is_plus:
        print(y2,x2+1,'+')
    else:
        print(y2,x2+1,'|')
elif x1-x2 == 2 and y1-y2 == 0:
    if is_plus:
        print(y1+1,x1,'+')
    else:
        print(y1+1,x1,'-')
elif x1-x2 == 0 and y1-y2 == 2:
    if is_plus:
        print(y1,x1+1,'+')
    else:
        print(y1,x1+1,'|')
elif x2-x1 == 2 and y2-y1 == 0:
    if is_plus:
        print(y2+1,x2,'+')
    else:
        print(y2+1,x2,'-')
elif x2-x1 == 1 and y2-y1 == 1 and direct2==0:
    if is_plus:
        print(y2+1,x2,'+')
    else:
        print(y2+1,x2,4)
elif x2-x1 == 1 and y2-y1 == 1 and direct2==3:
    if is_plus:
        print(y2+1,x1+1,'+')
    else:
        print(y2+1,x1+1,2)
elif x1-x2 == 1 and y2-y1 == 1 and direct2==0:
    if is_plus:
        print(y1+1,x2+1,'+')
    else:
        print(y1+1,x2+1,1)
elif x1-x2 == 1 and y2-y1 == 1 and direct2==1:
    if is_plus:
        print(y2+1,x1+1,'+')
    else:
        print(y2+1,x1+1,3)
elif x2-x1 == -1 and y1-y2 == 1 and direct2==2:
    if is_plus:
        print(y1+1,x2+1,'+')
    else:
        print(y1+1,x2+1,2)
elif x2 - x1 == -1 and y1 - y2 == 1 and direct2 == 1:
    if is_plus:
        print(y2+1,x1+1,'+')
    else:
        print(y2+1,x1+1, 4)
elif x2 - x1 == 1 and y1 - y2 == 1 and direct2 == 3:
    if is_plus:
        print(y2+1,x1+1,'+')
    else:
        print(y2+1,x1+1, 1)
elif x2 - x1 == 1 and y1 - y2 == 1 and direct2 == 2:
    if is_plus:
        print(y1+1,x2+1,'+')
    else:
        print(y1+1,x2+1, 3)
