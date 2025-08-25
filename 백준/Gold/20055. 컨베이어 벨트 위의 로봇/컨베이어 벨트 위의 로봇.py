'''
[개요]
문제명: 컨베이어 벨트 위의 로봇
풀이 시간: 47분 30초
시도 횟수: 1회
실행 시간: 111988KB
메모리: 516ms

[타임라인]
구상: 4분
구현: 19분 30초
디버깅: 24분

[구상]
(GOOD)
Deque이 아닌 리스트로 직접 관리하는 것이 좋았다고 생각한다. 문제를 보면 바로 Deque이
떠오르지만 Deque의 중간값 조회 및 수정은 상당한 시간이 든다. -> 타 언어에서는 Deque 중간값
접근은 가능하지도 않음으로 파이썬에서는 되더라도 최적의 풀이는 아닐 것이다.
(BAD)
2차원 리스트로만 생각하고 구상을 끝냈다가 구현에서 급하게 3차원 리스트로 고쳐버렸다.

[구현]
(GOOD)
없다.
(BAD)
1.입력을 어떻게 받을까 고민을 오래했다.. 그냥 받으면 되는 거지 왜 시간을 그렇게 끌었는지 모르겠다..
방법을 모르는 게 아니라 어떤 방법을 쓸지 고민하다 시간이 흘렀다..
2. 2차원 리스트에서 3차원 리스트로 바꾸면서 조금 꼬이는 부분이 생겨 시간이 지체되었다
앞으로는 구상에 더 신경을 쓰자!
3. 급한 마음에 함수화를 덜 하면서 코드를 작성하였다. 아직 더 함수화가 필요한 부분이 많이 보인다.

[디버깅]
(GOOD)
디버깅을 할 때 잘못된 부분을 코드만 보며 찾는 것이 아니라 우선 문제를 한 번 더 자세히 읽으며
디버깅을 진행하였더니 빠르게 찾을 수 있었다.
(BAD)
없다.

[후기]
문제를 정상적으로 풀지 못했다고 생각한다. 구상을 충분히 하지 못했고, 이로 인해 구현 중에 방법을
바꾸면서 꼬이는 부분도 생겼고 시간도 지체되었다. 그나마 잘한 점은 디버깅을 코드만 보고한 것이
아니라 문제에서부터 시작해서 빨리 시작했다는 점이다.

[개선사항]
급한 마음에 함수화를 덜 하였다. 이를 개선해보아야겠다.
'''
# # 1차 코드
# import sys
# 
# def rotate():
#     tp = graph[0][N-1]
#     for i in range(N-1,0,-1):
#         graph[0][i] = graph[0][i-1]
#     graph[0][0] = graph[1][0]
#     for i in range(N-1):
#         graph[1][i] = graph[1][i+1]
#     graph[1][N-1] = tp
# 
# def is_can_go(x):
#     if graph[0][x][1] and not graph[0][x+1][1] and graph[0][x+1][0]>=1:
#         return True
#     return False
# 
# def drop_robot():
#     graph[0][N-1][1] = False
# 
# 
# N,K = map(int, sys.stdin.readline().split())
# graph = [[],[]]
# temp = list(map(int, sys.stdin.readline().split()))
# for i in range(N):
#     graph[0].append([temp[i],False])
# for i in range(N,2*N):
#     graph[1].append([temp[i],False])
# graph[1] = graph[1][::-1]
# 
# cnt_blank = 0
# time = 0
# while True:
#     time += 1
#     rotate()
#     drop_robot()
# 
#     for i in range(N-2,-1,-1):
#         if is_can_go(i):
#             graph[0][i][1] = False
#             graph[0][i + 1][1] = True
#             graph[0][i + 1][0] -= 1
#             if graph[0][i + 1][0] == 0:
#                 cnt_blank += 1
#     drop_robot()
# 
#     if graph[0][0][0] >= 1 and not graph[0][0][1]:
#         graph[0][0][1] = True
#         graph[0][0][0] -= 1
#         if graph[0][0][0] == 0:
#             cnt_blank += 1
# 
#     drop_robot()
# 
#     if cnt_blank >= K:
#         break
# 
# print(time)


# 2차 코드
import sys

def rotate():
    temp = graph[0][N-1]
    for i in range(N-1,0,-1):
        graph[0][i] = graph[0][i-1]
    graph[0][0] = graph[1][0]
    for i in range(N-1):
        graph[1][i] = graph[1][i+1]
    graph[1][N-1] = temp

def is_can_go(x):
    if graph[0][x][1] and not graph[0][x+1][1] and graph[0][x+1][0]>=1: # 로봇이 있고, 다음칸에 로봇이 없고, 갈 곳의 내구도가 1이상
        return True
    return False

def move(x):
    global cnt_blank
    graph[0][x][1] = False
    graph[0][x+1][1] = True
    graph[0][x+1][0] -= 1
    if graph[0][x+1][0] == 0:
        cnt_blank += 1

def top_robot():
    global cnt_blank
    graph[0][0][1] = True
    graph[0][0][0] -= 1
    if graph[0][0][0] == 0:
        cnt_blank += 1

def drop_robot():
    graph[0][N-1][1] = False # 로봇이 없어도 False로 처리해도 된다


N,K = map(int, sys.stdin.readline().split())
graph = [[],[]]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    graph[0].append([temp[i],False])
for i in range(N,2*N):
    graph[1].append([temp[i],False])
graph[1] = graph[1][::-1] # 컨테이너 아래는 반대

cnt_blank = 0
time = 0
while True:
    time += 1
    rotate()
    drop_robot()

    for i in range(N-2,-1,-1):
        if is_can_go(i):
            move(i)
    drop_robot()

    if graph[0][0][0] >= 1 and not graph[0][0][1]: # 내구도가 1이상이고 로봇이 없으면
        top_robot()
    drop_robot()

    if cnt_blank >= K:
        break

print(time)