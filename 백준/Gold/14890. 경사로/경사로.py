# 혼자 백트래킹으로 풀고 난리 부르스 -> bfs처럼 변경
import sys
from collections import deque

def get_cand_lsts(graph):
    cand = []
    for g in graph:
        cand.append(g)
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(graph[j][i])
        cand.append(temp)
    return cand

def can_go(line):
    visited = [0] * N
    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue

        diff = line[i + 1] - line[i]
        if abs(diff) > 1:
            return False
        elif diff == 1:
            for k in range(i, i - X, -1):
                if k < 0 or line[k] != line[i] or visited[k]:
                    return False
            for k in range(i, i - X, -1):
                visited[k] = 1
        else:
            for k in range(i + 1, i + 1 + X):
                if k >= N or line[k] != line[i + 1] or visited[k]:
                    return False
            for k in range(i + 1, i + 1 + X):
                visited[k] = 1
    return True

N,X = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

cand_lsts = get_cand_lsts(graph)

res = 0
for lst in cand_lsts:
    if can_go(lst):
        res += 1
print(res)