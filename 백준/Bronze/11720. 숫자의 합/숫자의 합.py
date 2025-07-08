import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
res = 0
for c in S:
    res += int(c)
print(res)