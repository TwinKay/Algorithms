import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().rstrip()
    print(int(s[0])+int(s[-1]))