import sys
n = int(sys.stdin.readline())
last = [1, 1, 2, 6, 4]
if n < 5:
    print(last[n])
else:
    print(0)