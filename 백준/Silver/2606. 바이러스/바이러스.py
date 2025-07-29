'''
아이디어:
dfs로 풀어보기
양방향 조심!
visited True 수가 곧 답
'''

import sys
sys.setrecursionlimit(10000)

def dfs(c):
    visited[c] = True
    for n in graph[c]:
        if not visited[n]:
            dfs(n)

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = []
for _ in range(V+1):
    graph.append([])
for _ in range(E):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(V+1)

dfs(1)
print(sum(visited)-1)