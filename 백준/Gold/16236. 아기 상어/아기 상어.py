'''
[개요]
문제명: 아기 상어
풀이 시간: 31분
시도 횟수: 1회
실행 시간: 136ms
메모리: 114364KB

[아이디어]
시뮬레이션 + bfs

[타임라인]
구상: 5분 30초
구현: 23분
디버깅: 2분 30초

[구상]
(GOOD)
문제를 꼼꼼히 읽으며 요구 사항(첫 크기 2, 우선순위, 몸짓이 커지는 조건)을 종이에 확실히 체크하고 구현을 시작했다.
(BAD)
문제를 모두 잘 파악했지만, 문제 읽는데 시간을 더 써도 좋을 것 같다

[구현]
(GOOD)
상어의 몸집이 커지는 부분을 제외하고 전체적으로 빠진 부분 없이 잘 짰다고 생각한다.
(BAD)
1. 구현을 모두 다했다고 생각하고 출력을 해보았는데 상어의 몸집이 커지는 부분을 넣지 않았다.
2. 우선 순위 쪽 코드가 깔끔하지 않았고 시간이 오래 걸렸다고 생각한다
    -> 선 주석 후 코딩하면 좋을 것 같다

[디버깅]
(GOOD)
첫 번째 출력 후, 기댓값과 달라서 종이를 봤는데 바로 빠진 부분을 찾아서 고칠 수 있었다.


[후기]
구현 때 실수는 무조건 생길 수밖에 없다.
    -> 문제를 잘 읽으면 디버깅도 빨라진다. 문제에 집중하자!

[개선사항]
코드 간격이 적절하지 않았고, left_fish는 불필요한(실수를 야기하는) 변수인 것 같다. 다른 변수에서 같은
정보를 가져올 수 있고 꼭 필요한 경우가 아니라면 변수를 많이 만들지 말자!
    -> 개선해보자!
'''
# 1차 코드
# import sys
# from collections import deque
# 
# 
# def is_valid(x, y):
#     return 0 <= x < N and 0 <= y < N
# 
# 
# delta_x = [0, 0, -1, 1]
# delta_y = [1, -1, 0, 0]
# 
# N = int(sys.stdin.readline())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
# 
# x, y = N, N
# left_fish = 0
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 9:
#             x, y = j, i
#             graph[i][j] = 0
#         elif graph[i][j] in [1, 2, 3, 4, 5, 6]:
#             left_fish += 1
# 
# 
# def bfs(x, y, shark_size):
#     visited = []
#     for _ in range(N):
#         visited.append([0] * N)
# 
#     min_dist = 10000
#     eat_x, eat_y = N, N
#     deq = deque()
#     deq.append([x, y, 0])
#     visited[y][x] = 1
#     while deq:
#         x, y, dist = deq.popleft()
#         if dist > min_dist: break  # 계속해도 우선순위 X
# 
#         if 0 < graph[y][x] < shark_size:  # 먹이
#             if dist < min_dist:
#                 eat_x, eat_y = x, y
#                 min_dist = dist
# 
#             elif dist == min_dist:
#                 if eat_y > y:
#                     eat_x, eat_y = x, y
#                 elif eat_y == y:
#                     if eat_x > x:
#                         eat_x, eat_y = x, y  # y도 그냥
#             else:
#                 break
# 
#         for k in range(4):
#             dx = x + delta_x[k]
#             dy = y + delta_y[k]
#             if not is_valid(dx, dy):
#                 continue
#             if visited[dy][dx]:
#                 continue
#             if graph[dy][dx] > shark_size:
#                 continue
#             else:
#                 deq.append([dx, dy, dist + 1])
#                 visited[dy][dx] = 1
# 
#     return eat_x, eat_y, min_dist
# 
# 
# shark_size = 2
# cnt_eat = 0
# time = 0
# while left_fish > 0:
#     eat_x, eat_y, dist = bfs(x, y, shark_size)
#     if eat_x == N: break
#     graph[eat_y][eat_x] = 0
#     x, y = eat_x, eat_y
#     time += dist
#     left_fish -= 1
#     cnt_eat += 1
#     if cnt_eat == shark_size:
#         shark_size += 1
#         cnt_eat = 0
# 
# print(time)


# 2차 코드
import sys
from collections import deque


def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def get_first_index():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                graph[i][j] = 0
                return j,i

def bfs(x,y,shark_size):
    visited = []
    for _ in range(N):
        visited.append([0]*N)

    min_dist = 10000 # dummy
    eat_x,eat_y = N,N # # dummy
    deq = deque()
    deq.append([x,y,0]) # x y dist
    visited[y][x] = 1
    while deq:
        x,y,dist = deq.popleft()
        if dist > min_dist: break # 계속해도 우선순위 X

        if 0 < graph[y][x] < shark_size: # 먹이
            if dist < min_dist: # (먹이 첫 발견) -> deq을 돌면서 첫 갱신후에 이곳에 오는 경우X
                eat_x,eat_y = x,y
                min_dist = dist

            elif dist == min_dist: # 거리 같음
                if eat_y > y: # 더 위쪽 물고기
                    eat_x,eat_y = x,y
                elif eat_y == y: # 높이가 같으면
                    if eat_x > x: # 더 왼쪽 물고기
                        eat_x,eat_y = x,y # y는 같아서 갱신 안해도 되지만 그냥
            else: # 다른 먹이보다 멀면 (사실 없어도 되는 부분 -> 앞에서 처리)
                break

        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy): # 범위 밖
                continue
            if visited[dy][dx]: # 방문했으면
                continue
            if graph[dy][dx] > shark_size: # 더 큰 물고기면
                continue
            else: # 크기가 같거나 작은 물고기면 이동 가능 (먹는 건 pop에서 처리)
                deq.append([dx,dy,dist+1])
                visited[dy][dx] = 1

    return eat_x,eat_y,min_dist # eat_x 혹은 eat_y가 N으로 갱신 못했으면 먹을 물고기 없음


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

x,y = get_first_index()

shark_size = 2
cnt_eat = 0
time = 0
while True:
    eat_x,eat_y,dist = bfs(x,y,shark_size)
    if eat_x == N: # 먹을 물고기 없음
        break

    graph[eat_y][eat_x] = 0 # 먹은 물고기 처리
    x,y = eat_x,eat_y # x,y 먹을 물고기 자리로 갱신
    time += dist

    cnt_eat += 1 # 먹은 물고기 갯수
    if cnt_eat == shark_size: # 먹은 물고기 갯수가 상어 크기와 같다면
        shark_size += 1 # 사이즈 up
        cnt_eat = 0 # 먹은 양 초기화

print(time)