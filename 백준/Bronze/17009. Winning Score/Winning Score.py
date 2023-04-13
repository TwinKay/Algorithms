import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
f = int(sys.stdin.readline())

x = a*3+b*2+c
y = d*3+e*2+f
if x > y:
    print('A')
elif x < y:
    print('B')
else:
    print('T')