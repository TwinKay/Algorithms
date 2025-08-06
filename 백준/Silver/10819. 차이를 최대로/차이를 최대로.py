
import sys

def back_tracking(n,res):
    global max_val
    if n==N:
        temp = 0
        for i in range(N-1):
            temp += abs(arr[res[i]]-arr[res[i+1]])
        max_val = max(max_val,temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            back_tracking(n+1,res)
            visited[i] = False
            res.pop()

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False]*N
max_val = -float('inf')
back_tracking(0,[])
print(max_val)