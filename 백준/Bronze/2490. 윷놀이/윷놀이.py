import sys

for i in range(3):
    total = list(map(int, sys.stdin.readline().split()))
    c = total.count(0)
    if c == 0:
        print('E')
    elif c == 1:
        print('A')
    elif c == 2:
        print('B')
    elif c == 3:
        print('C')
    else:
        print('D')