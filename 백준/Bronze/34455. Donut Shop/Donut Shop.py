import sys

cnt = int(sys.stdin.readline())
T = int(sys.stdin.readline())
for _ in range(T):
    query = sys.stdin.readline().rstrip()
    if query == '+':
        cnt += int(sys.stdin.readline())
    else:
        cnt -= int(sys.stdin.readline())
print(cnt)