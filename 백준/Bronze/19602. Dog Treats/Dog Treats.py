import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())

z = 1*a+2*b+3*c
if z >= 10:
    print('happy')
else:
    print('sad')