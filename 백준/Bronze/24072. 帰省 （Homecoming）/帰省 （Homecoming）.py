import sys

a,b,c = map(int,sys.stdin.readline().split())

if c >= a and c < b:
    print(1)
else:
    print(0)