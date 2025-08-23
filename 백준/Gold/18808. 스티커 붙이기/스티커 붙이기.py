'''
아이디어: 완전 탐색
주의사항: 
1. 다음 스티커를 시작할때 맨 처음부터 시도해야한다. 
    -> 극단적으로 0,0에 한칸만 비어있고 스티커 크기가 1,1일 때
    
2. 우선순위: 끝까지 확인 -> 회전

'''
import sys

N,M,K = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append([0]*M)

def is_posi(sticker,x,y):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            graph_x = x + j
            graph_y = y + i
            if sticker[i][j] == 1:
                if graph[graph_y][graph_x] == 1:
                    return False
    return True

def rotate_sticker(sticker):
    x,y = len(sticker[0]),len(sticker)
    rotated_sticker = []
    for i in range(x):
        rotated_sticker.append([])
        for j in range(y-1,-1,-1):
            rotated_sticker[i].append(sticker[j][i])

    return rotated_sticker

def attach_sticker(sticker):
    for iteration in range(4):
        for i in range(N-len(sticker)+1):
            for j in range(M-len(sticker[0])+1):
                if is_posi(sticker,j,i):
                    for sticker_y in range(len(sticker)):
                        for sticker_x in range(len(sticker[0])):
                            graph_x = j + sticker_x
                            graph_y = i + sticker_y
                            if sticker[sticker_y][sticker_x] == 1:
                                graph[graph_y][graph_x] = 1
                    return
        if iteration < 3:
            sticker = rotate_sticker(sticker)
    return

for _ in range(K):
    n,m = map(int, sys.stdin.readline().split())
    sticker = []
    for _ in range(n):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    attach_sticker(sticker)

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt += 1

print(cnt)