'''
아이디어:
백트래킹
'''
import sys

def back_tracking(n,res):
    if n==M:
        print(*res)
        return
    for i in range(1,N+1):
        if i not in res: # 중복 검사
            res.append(i)
            back_tracking(n+1,res)
            res.pop()

N,M = map(int, sys.stdin.readline().split())
back_tracking(0,[])
