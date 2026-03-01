MOD = 14579
a, b = map(int, input().split())

ans = 1
for n in range(a, b + 1):
    tri = n * (n + 1) // 2
    ans = (ans * (tri % MOD)) % MOD

print(ans)