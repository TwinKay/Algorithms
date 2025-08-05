import sys

def back_tracking(n,res):
    if n==M:
        prt = []
        for r in res:
            prt.append(arr[r])
        print(*prt)
        return
    for i in range(N):
        res.append(i)
        back_tracking(n+1,res)
        res.pop()

N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
back_tracking(0,[])