'''
아이디어:
백트래킹
'''
import sys

def back_tracking(n,start,res):
    global cnt
    if n==m:
        sm = 0
        for r in res: # 원소값 더하기
            sm += arr[r]
        if sm == S:
            cnt += 1
        return
    for i in range(start,N):
        res.append(i)
        back_tracking(n+1,i+1,res)
        res.pop()

N,S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for m in range(1,N+1):
    back_tracking(0,0,[])

print(cnt)