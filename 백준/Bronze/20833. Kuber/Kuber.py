import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1,n+1):
    cnt += i**3
print(cnt)