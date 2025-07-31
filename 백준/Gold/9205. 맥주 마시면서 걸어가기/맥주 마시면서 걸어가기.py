'''
아이디어:
집, 편의점, 락페를 노드로 생각하고 각각 맨해튼 거리로 이어지는 것을 graph로 표현
그후 집과 락페가 이어지는 지를 확인..?
'''

import sys
from collections import deque

# 맨해튼 거리 계산
def calc_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline()) + 2 # 집, 락페 포함
    idxs = []
    for _ in range(N):
        idxs.append(list(map(int, sys.stdin.readline().split())))

    graph = []
    for _ in range(N):
        graph.append([])
    for i in range(N):
        for j in range(i+1,N):
            idx1 = idxs[j]
            idx2 = idxs[i]
            dist = calc_dist(idx1[0],idx1[1],idx2[0],idx2[1])
            if dist <= 1000: # 이동 가능 거리
                graph[i].append(j)
                graph[j].append(i)

    visited = [False]*N
    deq = deque()
    deq.append(0) # 집
    visited[0] = True
    is_connected = False # 집 락페 연결 여부
    while deq:
        cur = deq.popleft()
        if cur == N-1: # 락페 발견
            is_connected = True
            break

        for n in graph[cur]:
            if not visited[n]:
                deq.append(n)
                visited[n] = True

    if is_connected:
        print("happy")
    else:
        print("sad")
