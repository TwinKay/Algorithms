'''
매번 나간 모래 계산 x -> 마지막에 한번에
'''
import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [-1,0,1,0]
delta_y = [0,1,0,-1]

# x y 기준
delta0_spread_x = [-3,-2,-2,-1,-1,-1,-1,0,0]
delta0_spread_y = [0,-1,1,-2,-1,1,2,-1,1]
delta1_spread_x = [0,-1,1,-2,-1,1,2,-1,1]
delta1_spread_y = [3,2,2,1,1,1,1,0,0]
delta2_spread_x = [3,2,2,1,1,1,1,0,0]
delta2_spread_y = [0,1,-1,2,1,-1,-2,1,-1]
delta3_spread_x = [0,-1,1,-2,-1,1,2,-1,1]
delta3_spread_y = [-3,-2,-2,-1,-1,-1,-1,0,0]
delta_spread_x = [delta0_spread_x,delta1_spread_x,delta2_spread_x,delta3_spread_x]
delta_spread_y = [delta0_spread_y,delta1_spread_y,delta2_spread_y,delta3_spread_y]
spread_toil_percent = [0.05,0.1,0.1,0.02,0.07,0.07,0.02,0.01,0.01]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

before_toil = 0
for i in range(N):
    for j in range(N):
        before_toil += graph[i][j]

move_cnt_arr = []
for i in range(N-1):
    move_cnt_arr.append(i+1)
    move_cnt_arr.append(i+1)
    if i == N-2:
        move_cnt_arr.append(i+1)

x,y = N//2,N//2
direct = -1
for move_cnt in move_cnt_arr:
    direct += 1
    direct %= 4
    for _ in range(move_cnt):
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]

        total_toil = graph[dy][dx]
        remain_toil = total_toil
        for k in range(9):
            spread_x = x + delta_spread_x[direct][k]
            spread_y = y + delta_spread_y[direct][k]
            each_toil = int(total_toil*spread_toil_percent[k])
            if is_valid(spread_x,spread_y):
                graph[spread_y][spread_x] += each_toil
                remain_toil -= each_toil
            else:
                remain_toil -= each_toil
        alpa_x = x + delta_x[direct]*2
        alpa_y = y + delta_y[direct]*2
        if is_valid(alpa_x,alpa_y):
            graph[alpa_y][alpa_x] += remain_toil
        graph[dy][dx] = 0

        x,y = dx,dy

after_toil = 0
for i in range(N):
    for j in range(N):
        after_toil += graph[i][j]

print(before_toil-after_toil)