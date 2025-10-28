n = int(input())
k = int(input())

quota = k + 60
cheap = min(n, quota)
extra = max(0, n - quota)

cost = cheap * 1500 + extra * 3000
print(cost)