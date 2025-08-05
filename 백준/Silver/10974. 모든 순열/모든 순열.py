'''
아이디어:
백트래킹
'''
import sys

def back_tracking(n,res):
    if n==N:
        print(*res)
        return
    for i in range(1,N+1):
        if i not in res:
            res.append(i)
            back_tracking(n+1,res)
            res.pop()

N = int(sys.stdin.readline())
back_tracking(0,[])
