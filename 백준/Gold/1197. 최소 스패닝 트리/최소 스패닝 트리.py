'''
아이디어:
MST 유니온 파인드로 구현하기
'''
import sys

sys.setrecursionlimit(10 ** 5)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())
parent = []
for i in range(N + 1):
    parent.append(i)

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort() # 가중치 낮은 순부터 시도해야해서

res = 0
for edge in edges:
    w, a, b = edge
    if find(a) != find(b): # 같은 그룹이 아니면
        union(a, b)
        res += w

print(res)
