import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
if a<b:
    print(-1)
elif a == b:
    print(0)
else:
    print(1)