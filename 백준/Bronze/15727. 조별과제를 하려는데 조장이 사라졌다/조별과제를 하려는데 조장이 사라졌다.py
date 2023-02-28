import sys
n = int(sys.stdin.readline())
if n%5 == 0:
    print(n//5)
else:
    print(n//5+1)