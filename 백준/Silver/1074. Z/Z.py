import sys

n,r,c = map(int, sys.stdin.readline().split())

cnt = 0
while True:
    if n == 0:
        break

    else:
        n -= 1
        l = 2**n

        if r<l and c<l:
            pass

        elif r<l and c>=l:
            cnt += l*l
            c -= l

        elif r>=l and c<l:
            cnt += l*l*2
            r -= l

        else:
            cnt += l*l*3
            c -= l
            r -= l
print(cnt)