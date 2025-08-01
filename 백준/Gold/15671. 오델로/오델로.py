import sys

delta_x = [0,0,-1,1,1,-1,1,-1]
delta_y = [1,-1,0,0,1,-1,-1,1]

N = 6
Q = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(['.']*N)

graph[2][2] = 'W'
graph[3][3] = 'W'
graph[2][3] = 'B'
graph[3][2] = 'B'


def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def change(x,y,color):
    for k in range(8):
        cx,cy = x,y
        diff_color_idxs = []
        is_same_color = False
        while True:
            dx = cx + delta_x[k]
            dy = cy + delta_y[k]
            if not is_valid(dx,dy):
                break
            if graph[dy][dx] == '.':
                break
            elif graph[dy][dx] == color:
                is_same_color = True
                break
            else:
                diff_color_idxs.append([dx,dy])

            #cx 바꾸기
            cx,cy=dx,dy

        if is_same_color:
            for idx in diff_color_idxs:
                graph[idx[1]][idx[0]] = color



for q in range(Q):
    y,x = map(int, sys.stdin.readline().split())
    y -= 1
    x -= 1
    if q%2==0: # 흑돌 턴
        graph[y][x] = 'B'
        change(x,y,'B')
    else:
        graph[y][x] = 'W'
        change(x,y,'W')

for g in graph:
    print("".join(g))

cnt_b = 0
cnt_w = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'B':
            cnt_b += 1
        elif graph[i][j] == 'W':
            cnt_w += 1

if cnt_b > cnt_w:
    print("Black")
else:
    print("White")