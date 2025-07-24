import sys

N = int(sys.stdin.readline())
l,r,sm,cnt = 1,1,1,0
while l <= N:
    if sm == N:
        cnt += 1
        sm -= l
        l += 1

    elif sm < N:
        r += 1
        sm += r
    else:
        sm -= l
        l += 1

print(cnt)
