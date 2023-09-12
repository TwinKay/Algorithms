# 뭔가 이상한데,, 이분탐색 더 공부해야지..
import sys

def cut(x):
    cnt = 0
    for i in tree:
        if i-x > 0:
            cnt += i-x
    return cnt

n,m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

d, u = 0, max(tree)
while d < u-1:

    b = (d+u)//2

    if cut(b) >= m:
        d = b
    else:
        u = b
    
if cut(u) >= m:
    print(u)
else:
    print(d)