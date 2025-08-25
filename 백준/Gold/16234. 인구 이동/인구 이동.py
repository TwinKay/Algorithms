'''
[개요]
문제명: 인구 이동(코드트리: 토스트 계란틀)
풀이 시간: 26분
시도 횟수: 1회
실행 시간: 816ms
메모리: 121324KB

[아이디어]
BFS + 시뮬레이션

[타임라인]
구상: 3분
구현: 9분 30초
디버깅: 13분 30초

[구상]
(GOOD)
빠르게 구상이 되었고, 바로 BFS가 떠올랐다.
(BAD)
new_group_idxs,new_group_sm과 같이 어떤 방법으로 average를 구할지까지는 구상하지 못하고 구현에
들어갔던 것 같다. 앞으로는 이러한 부분까지 잘 구상하고 짜보자

[구현]
(GOOD)
막힘없이 술술 잘 짰다고 생각한다.
(BAD)
1. 빠르게 작성하다가 첫 deque append에 visited 처리를 안해줘서 디버깅하는데 시간이 오래 걸렸다.
2. L<=abs<=R 등 사실 원래대로였으면 충분히 함수화했을 것 같은 부분이 많이 보인다. 유독 오늘 원래
루틴대로 안하는 것 같은 느낌이 드는데, 큰 이유가 아니라면 실수를 줄이기 위해 내 루틴을 벗어나지 말자

[디버깅]
(GOOD)
빠르게 작성하다가 deque에 넣을 때 visited 처리를 안해줬더니 average가 잘못 계산되고 있었다.
해당 부분때문에 시간이 오래 걸리기는 했지만 필요한 부분에 잘 찍어보며 발견할 수 있었다.
(BAD)
없다.

[후기]
풀이 시간 및 실행 시간까지 합쳐서 크게 나쁘지는 않았다고 생각한다. 하지만 visited 처리를 하지 않았다는
것은 솔직히 많이 창피한 부분인 것 같다. 다음에는 같은 실수를 반복하지 말자

[개선사항]
함수화를 통해 더 깔끔히 만들어보자!
'''
# 1차 코드
# import sys
# from collections import deque
#
# def is_valid(x,y):
#     return 0<=x<N and 0<=y<N
#
# delta_x = [0,0,-1,1]
# delta_y = [1,-1,0,0]
#
# N,L,R = map(int, sys.stdin.readline().split())
#
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# time = -1
# while True:
#     time += 1
#     is_change = False
#     visited = []
#     for _ in range(N):
#         visited.append([False]*N)
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 new_group_idxs = []
#                 new_group_sm = 0
#                 deq = deque()
#                 deq.append((j,i))
#                 visited[i][j] = True
#                 while deq:
#                     cur = deq.popleft()
#                     x,y = cur
#                     new_group_idxs.append(cur)
#                     new_group_sm += graph[y][x]
#                     for k in range(4):
#                         dx = x + delta_x[k]
#                         dy = y + delta_y[k]
#                         if is_valid(dx,dy) and not visited[dy][dx] and L<=abs(graph[y][x]-graph[dy][dx])<=R:
#                             deq.append((dx,dy))
#                             visited[dy][dx] = True
#                 if len(new_group_idxs) >= 2:
#                     is_change = True
#                     aver = new_group_sm//len(new_group_idxs)
#                     for new_group_idx in new_group_idxs:
#                         graph[new_group_idx[1]][new_group_idx[0]] = aver
#
#     if not is_change:
#         break
#     is_change = False
#
# print(time)

# 2차 코드
import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def is_union(x1,y1,x2,y2):
    return L <= abs(graph[y2][x2] - graph[y1][x1]) <= R

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,L,R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

time = -1 # 처음부터 0시작
while True:
    time += 1
    is_change = False # 인구 이동이 일어났는지 여부를 판단할 boolean 변수

    visited = []
    for _ in range(N):
        visited.append([False]*N)

    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 방문하지 않은 경우만
                new_group_idxs = [] # 새로운 그룹에 속하는 index들
                new_group_sm = 0 # 새로운 그룹에 속하는 인구들의 합

                deq = deque()
                deq.append((j,i))
                visited[i][j] = True
                while deq:
                    cur = deq.popleft()
                    x,y = cur
                    new_group_idxs.append(cur) # union들
                    new_group_sm += graph[y][x] # 인구 합치기
                    for k in range(4):
                        dx = x + delta_x[k]
                        dy = y + delta_y[k]
                        if is_valid(dx,dy) and not visited[dy][dx] and is_union(x,y,dx,dy): # 범위 내, 방문X, L이상R이하 차이
                            deq.append((dx,dy))
                            visited[dy][dx] = True

                if len(new_group_idxs) >= 2: # 혼자가 아니면
                    is_change = True # 이번 time에서 인구 이동이 일어남 표시
                    aver = new_group_sm//len(new_group_idxs) # 나머지 제외
                    for new_group_idx in new_group_idxs:
                        graph[new_group_idx[1]][new_group_idx[0]] = aver # average값으로 갱신

    if not is_change: # 인구 이동이 이번 time에 없었다면 멈추기
        break
        
    # is_change = False 이 부분에 불필요한 코드가 있었다. while 처음에서 초기화 해줌

print(time)