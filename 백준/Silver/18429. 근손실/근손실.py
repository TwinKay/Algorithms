import sys

def back_tracking(n,weight):
    global cnt
    if weight < 500:
        return
    if n==N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            back_tracking(n+1,weight+arr[i]-K)
            visited[i] = False

N,K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False]*N
cnt = 0
back_tracking(0,500)
print(cnt)