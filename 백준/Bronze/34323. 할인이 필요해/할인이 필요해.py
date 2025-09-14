import sys

N,M,S = map(int, sys.stdin.readline().split())
a = (M+1)*S*(100-N) // 100
b = M*S
print(min(a,b))