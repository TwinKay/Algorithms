import sys

a = 0
for _ in range(3):
    a += int(sys.stdin.readline())
if a <= 21:
    print(1)
else:
    print(0)