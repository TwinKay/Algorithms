import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(r):
    visited = [False] * (n+1)
    cnt = [0] * (n+1)
    deq = deque([r])
    visited[r] = True

    while deq:
        a = deq.popleft()
        for i in graph[a]:
            if visited[i] == False:
                deq.append(i)
                visited[i] = True
                cnt[i] = cnt[a] + 1

    return(sum(cnt))

result = []
for i in range(1,n+1):
    result.append(bfs(i))

m = min(result)
print(result.index(m)+1)