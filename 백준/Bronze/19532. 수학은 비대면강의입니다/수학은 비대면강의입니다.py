import sys

a,b,c,d,e,f = map(int,sys.stdin.readline().split())

isFind = False
for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x+b*y==c and d*x+e*y==f):
            print(f'{x} {y}')
            isFind = True
            break
    if isFind:
        break
