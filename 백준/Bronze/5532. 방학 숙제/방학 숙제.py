import sys

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if a%c != 0 and b%d != 0:
    print(l - max(a // c + 1, b // d + 1))
elif a%c == 0 and b%d != 0:
    print(l - max(a // c, b // d + 1))
elif a%c != 0 and b%d == 0:
    print(l - max(a // c + 1, b // d))
else:
    print(l - max(a // c, b // d))
