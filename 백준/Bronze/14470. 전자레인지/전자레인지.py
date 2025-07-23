import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

res = 0
if A<0:
    res += (0-A)*C
    res += D
    res += (B-0)*E
else:
    res += (B-A)*E
print(res)