'''
[개요]
문제명: 미세먼지 안녕!
풀이 시간: 28분
시도 횟수: 1회
실행 시간: 444ms
메모리: 115216KB

[아이디어]
시뮬레이션

[타임라인]
구상: 3분
구현: 22분
디버깅: 3분

[구상]
(GOOD)
문제를 꼼꼼히 읽으며 실수할 수 있는 부분을 유의해서 읽었다.
    -> 확산되는 양은 //5 인지 //인접갯수 인지, 공기 청정기가 혹시 x축과 붙어있어서 배열 회전때 주의해햐하는 건 아닌지
(BAD)
꼼꼼히 읽고 구현에도 문제는 없었지만 3분은 다소 짧은 시간인 것 같다. 사실 문제를 볼 때는
더 많이 시간이 흐른줄 알았는데.. 앞으로는 시간을 확인하면서라도 더 읽도록 하자

[구현]
(GOOD)
문제를 확실히 이해한 덕분인지 중요 조건들을 임의로 판단해서 짜지 않았다.
(BAD)
공기가 순환하는 부분에서 한 곳을 빼놓고 돌고 있었다.

[디버깅]
(GOOD)
공기가 순환하는 부분에서 한 곳을 빼놓고 돌고 있었지만, 빠른 디버깅을 통해 쉽게 찾을 수 있었다.
(BAD)
나만의 테케를 테스트하지 않고 코드를 제출했다. 스스로 테케를 만들에서 테스트한 다음 제출하자!

[후기]
문제를 다 이해했더라고 최소한의 시간동안은 문제에 집중하자!

[개선사항]
처음 공기청정기의 위치를 받을 때 첫 등장 위치에서 바로 두 index를 구하고 break할 수 있다 - 예영님 코드 참고
'''
# # 1차 코드
# import sys
#
# delta_x = [0,0,-1,1]
# delta_y = [1,-1,0,0]
#
# N,M,T = map(int, sys.stdin.readline().split())
#
# gongchunggi_y1, gongchunggi_y2 = 100,100
#
# graph = []
# for i in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#     if graph[i][0] == -1:
#         if gongchunggi_y1 == 100:
#             gongchunggi_y1 = i
#         else:
#             gongchunggi_y2 = i
#
# def is_valid(x,y):
#     return 0<=x<M and 0<=y<N
#
# def spread(graph):
#     new_graph = []
#     for _ in range(N):
#         new_graph.append([0]*M)
#
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == -1:
#                 continue
#             spread_idxs = []
#             for k in range(4):
#                 dx = j + delta_x[k]
#                 dy = i + delta_y[k]
#                 if is_valid(dx,dy) and graph[dy][dx] != -1:
#                     spread_idxs.append((dx,dy))
#             spread_val = graph[i][j]//5
#             for x,y in spread_idxs:
#                 new_graph[y][x] += spread_val
#             graph[i][j] -= spread_val * len(spread_idxs)
#     for i in range(N):
#         for j in range(M):
#             new_graph[i][j] += graph[i][j]
#
#     return new_graph
#
# def fresh():
#     # 위쪽
#     graph[gongchunggi_y1-1][0] = 0
#     for i in range(gongchunggi_y1-1,0,-1):
#         graph[i][0] = graph[i-1][0]
#     for i in range(M-1):
#         graph[0][i] = graph[0][i+1]
#     for i in range(1,gongchunggi_y1+1):
#         graph[i-1][M-1] = graph[i][M-1]
#     for i in range(M-1,1,-1):
#         graph[gongchunggi_y1][i] = graph[gongchunggi_y1][i-1]
#     graph[gongchunggi_y1][1] = 0
#
#     # 아래쪽
#     graph[gongchunggi_y2+1][0] = 0
#     for i in range(gongchunggi_y2+1,N-1,1):
#         graph[i][0] = graph[i+1][0]
#     for i in range(1,M):
#         graph[N-1][i-1] = graph[N-1][i]
#     for i in range(N-1,gongchunggi_y2,-1):
#         graph[i][M-1] = graph[i-1][M-1]
#     for i in range(M-1,1,-1):
#         graph[gongchunggi_y2][i] = graph[gongchunggi_y2][i-1]
#     graph[gongchunggi_y2][1] = 0
#
#
#
# for _ in range(T):
#     graph = spread(graph)
#     fresh()
#
# res = 0
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] > 0:
#             res += graph[i][j]
#
# print(res)
#
#

# 2차 코드
import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

def spread(graph):
    new_graph = []
    for _ in range(N):
        new_graph.append([0]*M)

    for i in range(N):
        for j in range(M):
            if graph[i][j] < 5: # 공청기거나 확산이 불가능한 양 (2차 코드 수정 부분, 원래는 공청기만 continue)
                continue

            spread_idxs = [] # 확산될 index들
            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if is_valid(dx,dy) and graph[dy][dx] != -1: # 범위 안, 공청기X
                    spread_idxs.append((dx,dy))

            spread_val = graph[i][j]//5 # 확산량
            for x,y in spread_idxs:
                new_graph[y][x] += spread_val
            graph[i][j] -= spread_val * len(spread_idxs) # 확산된만큼 빼주기

    for i in range(N):
        for j in range(M):
            new_graph[i][j] += graph[i][j] # 확산하고 남은 것들 더하기

    return new_graph

def fresh():
    # 위쪽
    graph[gongchunggi_y1-1][0] = 0
    for i in range(gongchunggi_y1-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for i in range(M-1):
        graph[0][i] = graph[0][i+1]
    for i in range(1,gongchunggi_y1+1):
        graph[i-1][M-1] = graph[i][M-1]
    for i in range(M-1,1,-1):
        graph[gongchunggi_y1][i] = graph[gongchunggi_y1][i-1]
    graph[gongchunggi_y1][1] = 0

    # 아래쪽
    graph[gongchunggi_y2+1][0] = 0
    for i in range(gongchunggi_y2+1,N-1,1):
        graph[i][0] = graph[i+1][0]
    for i in range(1,M):
        graph[N-1][i-1] = graph[N-1][i]
    for i in range(N-1,gongchunggi_y2,-1):
        graph[i][M-1] = graph[i-1][M-1]
    for i in range(M-1,1,-1):
        graph[gongchunggi_y2][i] = graph[gongchunggi_y2][i-1]
    graph[gongchunggi_y2][1] = 0


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,T = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    if graph[i][0] == -1:
        gongchunggi_y1 = i
        gongchunggi_y2 = i+1
        break

for _ in range(T):
    graph = spread(graph) # 확산
    fresh() # 공청기 동작

res = 0
for i in range(N):
    for j in range(M):
        res += graph[i][j] # 공청기도 일단 더하고 (2차 코드 수정 부분)

print(res+2) # 마지막에 복구 (2차 코드 수정 부분)