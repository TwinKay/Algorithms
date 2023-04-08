import sys

a,b = map(int, sys.stdin.readline().split())
a = a*7
b = b*13

if a == b:
    print('lika')
elif a>b:
    print('Axel')
else:
    print('Petra')