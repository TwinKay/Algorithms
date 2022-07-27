import sys

t = int(input())
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #"+str(i+1)+": "+ str(a)+" + "+str(b)+" = "+str(a+b))