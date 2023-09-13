import sys

sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

tree = []
visited = []
for i in range(1, n+1):
    if i == n:
        l = list(map(int, sys.stdin.readline().split()))
        tree.append(l)
        visited.append(l)
    else:
        tree.append(list(map(int, sys.stdin.readline().split())))
        visited.append([0]*i)
        
def dp(i, visited):
    if i == -1:
        return visited[0][0]
    else:
        for j in range(len(visited[i])):
            visited[i][j] = tree[i][j] + max(visited[i+1][j], visited[i+1][j+1])
            
        return dp(i-1, visited)
    
print(dp(n-2, visited))