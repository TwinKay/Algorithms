t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for k in range(1, n + 1):
        ans += k * ((k + 1) * (k + 2) // 2)
    print(ans)