import sys
sys.setrecursionlimit(((10**5)))

n,m = map(int, sys.stdin.readline().split())

visited = [False]*(n+1)
graph = []

for _ in range(n+1):
    graph.append([])

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(r):
    if visited[r] == False:
        visited[r] = True

        for i in graph[r]:
            if not visited[i]:
                dfs(i)
        return True

cnt = 0
for i in range(1,n+1):
    if dfs(i) == True:
        cnt += 1

print(cnt)