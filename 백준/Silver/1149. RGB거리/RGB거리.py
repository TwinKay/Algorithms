import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
total = []
visited = []
for i in range(n):
    if i != n-1:
        total.append(list(map(int, sys.stdin.readline().split())))
        visited.append([0]*3)
    else:
        l = list(map(int, sys.stdin.readline().split()))
        total.append(l)
        visited.append(l)

def dp(i, visited):

    if i == -1:
        return visited
    
    else:
        cnt_1 = total[i][0] + min(visited[i+1][1], visited[i+1][2])
        cnt_2 = total[i][1] + min(visited[i+1][0], visited[i+1][2])
        cnt_3 = total[i][2] + min(visited[i+1][0], visited[i+1][1])

        visited[i] = [cnt_1,cnt_2,cnt_3]

        return dp(i-1, visited)

print((min(dp(n-2, visited)[0])))