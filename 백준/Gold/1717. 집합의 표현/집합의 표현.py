'''
아이디어:
유니온 파인드 사용하기
'''
import sys
sys.setrecursionlimit(10**5)


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

for _ in range(M):
    query, a, b = map(int, sys.stdin.readline().split())
    if query == 0: # 유니온
        union(a, b)
    else:  # 파인드
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
