import sys
res = 0
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
for i in l:
    if i >= n:
        res += n
    else:
        res += i
print(res)