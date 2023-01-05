import sys

s = sys.stdin.readline().rstrip()
cnt = 0
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip()
    if s == a:
        cnt += 1
print(cnt)