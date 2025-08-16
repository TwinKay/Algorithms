import sys
from collections import deque


def is_valid(x, y):
    return 0 <= x < M and 0 <= y < N

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1,-1,-1,  0, 0,  1, 1, 1]

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
visited = []
for _ in range(N):
    visited.append([False]*M)

cnt = 0
for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue

        h = graph[y][x]
        deq = deque()
        deq.append((x, y))
        visited[y][x] = True

        is_peak = True
        same_cells = [(x, y)]

        while deq:
            cx, cy = deq.popleft()
            for k in range(8):
                nx, ny = cx + dx[k], cy + dy[k]
                if not is_valid(nx, ny):
                    continue

                nh = graph[ny][nx]
                if nh > h:
                    is_peak = False

                if not visited[ny][nx] and nh == h:
                    visited[ny][nx] = True
                    deq.append((nx, ny))
                    same_cells.append((nx, ny))

        if is_peak:
            cnt += 1

print(cnt)
