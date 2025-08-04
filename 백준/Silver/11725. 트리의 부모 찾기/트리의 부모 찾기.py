'''
DFS...? 결국 DFS도 재귀니깐,,?
'''

import sys
sys.setrecursionlimit(10**5)

def recu(c):
    if visited[c]:
        return
    for n in graph[c]:
        if not visited[n]:
            res[n] = c
            visited[c] = True
            recu(n)

N = int(sys.stdin.readline())
graph = []
for _ in range(N+1):
    graph.append([])
visited = [False]*(N+1)

for _ in range(N-1):
    node_a, node_b = map(int, sys.stdin.readline().split())
    graph[node_a].append(node_b) # 이어진 부분 연결
    graph[node_b].append(node_a)

res = [0]*(N+1)
recu(1)
for r in res[2:]:
    print(r)
