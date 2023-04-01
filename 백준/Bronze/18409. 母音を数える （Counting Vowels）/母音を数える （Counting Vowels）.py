import sys
n = int(sys.stdin.readline())
l = list(sys.stdin.readline().rstrip())
val = ['a','e','i','o','u']
cnt = 0
for i in l:
    if i in val:
        cnt += 1
print(cnt)