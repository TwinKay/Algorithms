import sys

N,M,A,B = map(int, sys.stdin.readline().split())
diff = 3*N-M
if diff <= 0:
    print(0)
else:
    print(diff*A+B)