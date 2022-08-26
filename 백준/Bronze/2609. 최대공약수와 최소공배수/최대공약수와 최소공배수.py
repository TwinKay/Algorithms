import sys

a,b = map(int,sys.stdin.readline().split())
c,d = a,b
while b>0:
    a,b = b,a%b
print(a)
print(c*d//a)