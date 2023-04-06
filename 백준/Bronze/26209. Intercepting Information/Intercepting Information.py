import sys
l = list(map(int, sys.stdin.readline().split()))
if 9 in l:
    print('F')
else:
    print('S')