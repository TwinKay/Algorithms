import sys
sys.setrecursionlimit(10**5)

def move(direct,x,y,x2,y2):
    '''
    x2,y2가 None이면 move 방해 X
    return이 100이면 탈출
    '''
    while True:
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]
        if graph[dy][dx] == '#':
            break
        if x2:
            if dx==x2 and dy==y2:
                break
        if graph[dy][dx] == 'O':
            return 100,100
        x, y = dx, dy
    return x,y

def back_track(time,r_x,r_y,b_x,b_y,before_k):
    global res_min

    if time >= res_min:
        return
    if b_x == 100:
        return
    if r_x == 100: # b는 탈출 x
        res_min = min(res_min,time)
        return
    
    if time == 10:
        return
    
    for k in range(4):# 상하좌우
        if before_k==k:
            continue
        if k==0: # 상
            if r_y <= b_y: # r 먼저
                r_dx,r_dy = move(k,r_x,r_y,None,None)
                b_dx,b_dy = move(k,b_x,b_y,r_dx,r_dy)
            else:
                b_dx,b_dy = move(k,b_x,b_y,None,None)
                r_dx,r_dy = move(k,r_x,r_y,b_dx,b_dy)
        elif k==1: # 우
            if r_x >= b_x:  # r 먼저
                r_dx,r_dy = move(k,r_x,r_y,None,None)
                b_dx,b_dy = move(k,b_x,b_y,r_dx,r_dy)
            else:
                b_dx,b_dy = move(k,b_x,b_y,None,None)
                r_dx,r_dy = move(k,r_x,r_y,b_dx,b_dy)
        elif k==2: # 하
            if r_y >= b_y:  # r 먼저
                r_dx,r_dy = move(k,r_x,r_y,None,None)
                b_dx,b_dy = move(k,b_x,b_y,r_dx,r_dy)
            else:
                b_dx,b_dy = move(k,b_x,b_y,None,None)
                r_dx,r_dy = move(k,r_x,r_y,b_dx,b_dy)
        else: # 좌
            if r_x <= b_x:  # r 먼저
                r_dx,r_dy = move(k,r_x,r_y,None,None)
                b_dx,b_dy = move(k,b_x,b_y,r_dx,r_dy)
            else:
                b_dx,b_dy = move(k,b_x,b_y,None,None)
                r_dx,r_dy = move(k,r_x,r_y,b_dx,b_dy)

        back_track(time+1,r_dx,r_dy,b_dx,b_dy,k)

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

r_x,r_y,b_x,b_y = M,M,N,N
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            r_x,r_y = j,i
            graph[i][j] = '.'
        elif graph[i][j] == 'B':
            b_x,b_y = j,i
            graph[i][j] = '.'

INF = float('inf')
res_min = INF
back_track(0,r_x,r_y,b_x,b_y,None)
if res_min == INF:
    print(-1)
else:
    print(res_min)