import sys

n = int(sys.stdin.readline())
p = 5*n-400
print(p)
if p == 100:
    print(0)
elif p > 100:
    print(-1)
else:
    print(1)