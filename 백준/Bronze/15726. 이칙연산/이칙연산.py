import sys

a,b,c = map(int, sys.stdin.readline().split())
print(max(int(a/b*c), int(a*b/c)))