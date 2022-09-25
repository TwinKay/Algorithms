import sys
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
    i.sort(reverse=True)

def dfs(v, r, visited):
    visited[r] = True

    ord.append(r)

    for i in v[r]:
        if not visited[i]:
            dfs(v, i, visited)

dfs(v, r, visited)

result =[0]*(n+1)
for j,i in enumerate(ord):
    result[i] = j+1

for i in result[1:]:
    print(i)