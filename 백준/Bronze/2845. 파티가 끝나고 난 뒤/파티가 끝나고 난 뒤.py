# 시험기간
import sys

a,b =  map(int, sys.stdin.readline().split())
c = a*b
l = list(map(int, sys.stdin.readline().split()))
result=[]
for i in l:
    result.append(str(i-c))

print(' '.join(result))