'''
dfs로 할 걸.. 하다가 생각남..ㅠㅠ
'''

import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

tetro_idxs = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,2),(1,2),(1,1),(1,0)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (1,0), (2,0), (0,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(0, 1), (1, 1), (2, 1), (1,0)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
]

max_val = -1
N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(M):
        for tetro_idx in tetro_idxs:
            cnt = 0
            for idx in tetro_idx:
                x = j + idx[0]
                y = i + idx[1]
                if not is_valid(x,y):
                    break
                cnt += graph[y][x]
            else:
                max_val = max(max_val,cnt)

print(max_val)