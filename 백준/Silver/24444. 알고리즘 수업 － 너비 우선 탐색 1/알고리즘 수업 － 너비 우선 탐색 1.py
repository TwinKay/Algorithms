import sys
from collections import deque
sys.setrecursionlimit((10**9))

n,m,r = map(int, sys.stdin.readline().split())

visited = [False]*(n+1)
v = []
ord = []
for i in range(n+1):
    v.append([])

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

for i in v:
    i.sort()

def bfs(v, r, visited):
    visited[r] = True

    deq = deque([r])

    while deq:
        a = deq.popleft()
        ord.append(a)

        for i in v[a]:
            if not visited[i]:
                deq.append(i)
                visited[i] = True

bfs(v, r, visited)

result =[0]*(n+1)
for j,i in enumerate(ord):
    result[i] = j+1

for i in result[1:]:
    print(i)