import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().rstrip()
    print(f'{s[0]}{s[len(s)-1]}')