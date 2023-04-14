import sys
t,s = map(int,sys.stdin.readline().split())

if s == 1:
    print('280')
else:
    if t >= 12 and t <= 16:
        print('320')
    else:
        print('280')