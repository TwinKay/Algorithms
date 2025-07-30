'''
백트리킹 or 3중 for문으로 궁수 배치 및 N에 위치(0-based idx 기준) -> 완탐
모든 궁수는 동시에
공격은 D이하 중 가까운, 여러명이면 가장 왼쪽
서로 만나는 경우가 있나? 맨해튼 거리거리 기준이면 있을 수가 없음
최대 제거 가능 적의 최대 수 구하기. -> 단순 시뮬인데 왜 최댓값이라 했을까..?
본인보다 아래면 공격 불가 -> cnt 제외
아이디어:
궁수를 올려버리자!
'''
import sys

def calc_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def shoot():
    global kill_cnt
    target_idxs = []

    for arrow in arrow_idxs:
        target_x, target_y = M, N
        min_dist = N*4

        for i in range(arrow[1]):
            for j in range(M):
                if graph[i][j] == 1:
                    dist = calc_dist(arrow[0],arrow[1],j,i)
                    if dist <= D:
                        if dist < min_dist:
                            min_dist = dist
                            target_x = j
                            target_y = i
                        elif dist == min_dist:
                            if j < target_x:
                                min_dist = dist
                                target_x = j
                                target_y = i

        if target_x != M and target_y != N:
            target_idxs.append([target_x,target_y])

    for target_idx in target_idxs:
        if graph[target_idx[1]][target_idx[0]] == 1:
            graph[target_idx[1]][target_idx[0]] = 0
            kill_cnt += 1

def move():
    for i in range(len(arrow_idxs)):
        arrow_idxs[i][1] -= 1

N,M,D = map(int, sys.stdin.readline().split())
init_graph = []
for _ in range(N):
    init_graph.append(list(map(int, sys.stdin.readline().split())))

kill_max = 0
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            graph = [lst[:] for lst in init_graph]
            arrow_idxs = [[i,N],[j,N],[k,N]]
            kill_cnt = 0
            for time in range(N):
                shoot() # 공격
                move() # arrow 올리기

            kill_max = max(kill_max,kill_cnt)

print(kill_max)
