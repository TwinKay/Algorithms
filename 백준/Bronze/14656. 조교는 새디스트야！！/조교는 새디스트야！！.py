n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i, x in enumerate(arr, start=1):
    if x != i:
        cnt += 1

print(cnt)