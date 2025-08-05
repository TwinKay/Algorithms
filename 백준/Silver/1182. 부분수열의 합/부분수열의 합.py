'''
아이디어:
백트래킹
+ sum으로 매개변수 넘기기
'''
import sys

def back_tracking(n,start,sm):
    global cnt
    if n==m:
        if sm == S:
            cnt += 1
        return
    for i in range(start,N):
        sm += arr[i]
        back_tracking(n+1,i+1,sm)
        sm -= arr[i]

N,S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for m in range(1,N+1):
    back_tracking(0,0,0)

print(cnt)