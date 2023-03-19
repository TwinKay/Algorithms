import sys, math

a,b,c,d,e = map(int, sys.stdin.readline().split())
print(min(math.ceil(a/b)*c,math.ceil(a/d)*e))