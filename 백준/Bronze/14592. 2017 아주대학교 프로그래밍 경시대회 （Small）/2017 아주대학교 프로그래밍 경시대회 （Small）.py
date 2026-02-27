n = int(input())
arr = []

for i in range(1, n + 1):
    s, c, l = map(int, input().split())
    arr.append((-s, c, l, i))

arr.sort()
print(arr[0][3])