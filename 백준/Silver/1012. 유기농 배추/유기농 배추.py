import sys
sys.setrecursionlimit(((10**5)))

for _ in range(int(sys.stdin.readline())):

    m,n,k = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(n):
        graph.append([0]*m)

    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1


    def dfs(x,y):
        if x == -1 or y == -1 or x == m+1 or y == n+1:
            return False

        if graph[y][x] == 1:
            graph[y][x] = 0

            try:
                if graph[y][x+1] == 1:
                    dfs(x+1,y)
            except:
                pass

            try:
                if graph[y][x-1] == 1:
                    dfs(x-1,y)
            except:
                pass

            try:
                if graph[y+1][x] == 1:
                    dfs(x,y+1)
            except:
                pass

            try:
                if graph[y-1][x] == 1:
                    dfs(x,y-1)
            except:
                pass
            return True
        return False

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(j,i) == True:
                cnt += 1

    print(cnt)