import sys

arr = list(False for _ in range(42))
for _ in range(10):
    n = int(sys.stdin.readline())
    arr[n%42] = True
res = 0
for bol in arr:
    if bol:
        res += 1
print(res)