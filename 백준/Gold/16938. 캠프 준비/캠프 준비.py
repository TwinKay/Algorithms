import sys

N,L,R,X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def back_tracking(n,start,sm,min_score,max_score):
    global cnt
    if n==m:
        if L<=sm<=R and max_score-min_score>=X:
            cnt += 1
        return
    for i in range(start,N):
        back_tracking(n+1,i+1,sm+arr[i],min(min_score,arr[i]),max(max_score,arr[i]))
cnt = 0
for m in range(2,N+1):
    back_tracking(0,0,0,float('inf'),-float('inf'))
print(cnt)