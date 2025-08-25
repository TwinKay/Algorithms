'''
아이디어:
시뮬레이션
'''
import sys

def rotate():
    tp = graph[0][N-1]
    for i in range(N-1,0,-1):
        graph[0][i] = graph[0][i-1]
    graph[0][0] = graph[1][0]
    for i in range(N-1):
        graph[1][i] = graph[1][i+1]
    graph[1][N-1] = tp

def is_can_go(x):
    if graph[0][x][1] and not graph[0][x+1][1] and graph[0][x+1][0]>=1:
        return True
    return False

def drop_robot():
    graph[0][N-1][1] = False


N,K = map(int, sys.stdin.readline().split())
graph = [[],[]]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    graph[0].append([temp[i],False])
for i in range(N,2*N):
    graph[1].append([temp[i],False])
graph[1] = graph[1][::-1]

cnt_blank = 0
time = 0
while True:
    time += 1
    rotate()
    drop_robot()

    for i in range(N-2,-1,-1):
        if is_can_go(i):
            graph[0][i][1] = False
            graph[0][i + 1][1] = True
            graph[0][i + 1][0] -= 1
            if graph[0][i + 1][0] == 0:
                cnt_blank += 1
    drop_robot()

    if graph[0][0][0] >= 1 and not graph[0][0][1]:
        graph[0][0][1] = True
        graph[0][0][0] -= 1
        if graph[0][0][0] == 0:
            cnt_blank += 1

    drop_robot()

    if cnt_blank >= K:
        break

print(time)