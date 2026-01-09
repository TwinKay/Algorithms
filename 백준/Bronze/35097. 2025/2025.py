import sys

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    s = n * (n + 1) // 2
    print(s * s)