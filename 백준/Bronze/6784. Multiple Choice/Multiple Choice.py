import sys

n = int(sys.stdin.readline())
choi = list()
ans = list()
for _ in range(n):
    choi.append(sys.stdin.readline().strip())
for _ in range(n):
    ans.append(sys.stdin.readline().strip())
cnt = 0
for i in range(n):
    if choi[i] == ans[i]:
        cnt += 1
print(cnt)
    