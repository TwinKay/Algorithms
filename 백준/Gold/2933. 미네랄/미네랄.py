'''
1. 서로 날리고
2. 파괴하고
3. 인접한 곳에 미네랄이 있다면 땅이랑 붙어있는지 확인하고
4. 땅이랑 떨어진 것이 있다면 내려보내고(땅부터 조회해서 모든 영역이 가능할 때 옮기는게 좋을 듯?
배운점: 항상 visited 조심하기 -> visited 초기화 시점 유의! 
'''

import sys
from collections import deque


def throw_from_left(query):
    for j in range(M):
        if graph[query][j] == 'x':
            graph[query][j] = '.'
            return [j, query]
    return []


def throw_from_right(query):
    for j in range(M - 1, -1, -1):
        if graph[query][j] == 'x':
            graph[query][j] = '.'
            return [j, query]
    return []


def is_valid(x,y):
    return 0<=x<M and 0<=y<N


def check_revi(dx,dy):
    revi_idxs = []

    deq = deque()
    deq.append([dx,dy])
    visited[dy][dx] = True
    while deq:
        cur = deq.popleft()
        revi_idxs.append(cur)

        if cur[1] == N-1:
            return []

        for k in range(4):
            dx = cur[0] + delta_x[k]
            dy = cur[1] + delta_y[k]
            if is_valid(dx,dy) and not visited[dy][dx] and graph[dy][dx] == 'x':
                deq.append([dx,dy])
                visited[dy][dx] = True

    return revi_idxs


def down(idxs,diff):
    for d in range(diff+1):
        is_can = True
        for idx in idxs:
            if graph[idx[1]+d][idx[0]] == 'x':
                is_can = False
                break
        if not is_can:
            for idx in idxs:
                graph[idx[1] + (d-1)][idx[0]] = 'x'
            return

    for idx in idxs:
        graph[idx[1]+diff][idx[0]] = 'x'


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

Q = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

for i, query in enumerate(queries):
    query = N - query

    broken_idx = []
    if i % 2 == 0:
        broken_idx = throw_from_left(query)
    else:
        broken_idx = throw_from_right(query)

    if not broken_idx:
        continue

    for k in range(4):
        visited = []
        for _ in range(N):
            visited.append([False] * M)
            
        dx = broken_idx[0] + delta_x[k]
        dy = broken_idx[1] + delta_y[k]

        if not is_valid(dx,dy) or graph[dy][dx] == '.':
            continue

        idxs = check_revi(dx,dy)
        if not idxs:
            continue

        max_y = 0
        for idx in idxs:
            max_y = max(max_y, idx[1])

        # 미네랄 잠시 지위고 .로 만들기
        for idx in idxs:
            graph[idx[1]][idx[0]] = '.'

        diff = N-1-max_y
        down(idxs,diff)

for g in graph:
    print("".join(g))