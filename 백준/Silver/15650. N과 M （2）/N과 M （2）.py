'''
아이디어:
백트래킹
'''
import sys

def back_tracking(n,start,res):
    if n==M:
        print(*res)
        return
    for i in range(start,N+1):
        res.append(i)
        back_tracking(n+1,i+1,res)
        res.pop()

N,M = map(int, sys.stdin.readline().split())
back_tracking(0,1,[])
