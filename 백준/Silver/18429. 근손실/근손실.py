import sys

def back_tracking(n,weight):
    global res
    if weight < 500:
        return
    if n==N:
        if weight >= 500:
            res += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        back_tracking(n+1,weight-K+arr[i])
        visited[i] = False

N,K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False]*N
res = 0
back_tracking(0,500)
print(res)