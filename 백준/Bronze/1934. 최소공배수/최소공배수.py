import sys

for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    c,d = a,b
    while b>0:
        a,b = b,a%b

    print(c*d//a)