import sys

k,n = map(int, sys.stdin.readline().split())
total = []

for _ in range(k):
    total.append(int(sys.stdin.readline()))

left = 1 ; right = max(total)

while left <= right:
    mid = (left+right)//2
    ans = 0
    for i in total:
        ans += i//mid

    if ans < n:
        right = mid-1
    else:
        left = mid+1

print(right)