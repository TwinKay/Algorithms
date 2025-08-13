'''
아이디어:
유니온 파인드로 구현하기 -> 매트릭스 모두 조회 필요 X -> 양방향 모두 가중치 같음
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


N = int(sys.stdin.readline())
parent = []
for i in range(N + 1):
    parent.append(i)

matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

edges = []
for i in range(N):
    for j in range(i + 1, N):  # 모든 칸을 다 조회할 필요 X
        edges.append((matrix[i][j], j, i))
edges.sort()  # 가중치 낮은 순부터 시도해야해서

res = 0
node_cnt = 0
for edge in edges:
    w, a, b = edge
    if find(a) != find(b):  # 같은 그룹이 아니면
        union(a, b)
        res += w
        node_cnt += 1
        if node_cnt == N - 1:  # 완성
            break

print(res)
