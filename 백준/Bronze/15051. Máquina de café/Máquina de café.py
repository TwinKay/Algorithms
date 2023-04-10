import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

print(min(b*2+c*4, a*2+c*2, a*4+b*2))