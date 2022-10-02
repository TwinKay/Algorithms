import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    result = []
    result.append(s[0])
    result.append(s[-1])
    print(''.join(result))