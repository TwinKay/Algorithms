import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())

    l = []
    repeat = False
    x = 1
    for _ in range(b):
        x = (x*a)%10
        if x not in l:
            l.append(x)
        else:
            repeat = True
            break
    if repeat:
        ans = l[(b % len(l))-1]
    else:
        ans = l[-1]

    if ans != 0:
        print(ans)
    else:
        print(10)