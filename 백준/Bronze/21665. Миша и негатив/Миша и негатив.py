n, m = map(int, input().split())

origin = [input().strip() for _ in range(n)]
input()
nega = [input().strip() for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(m):
        if origin[i][j] == nega[i][j]:
            cnt += 1

print(cnt)