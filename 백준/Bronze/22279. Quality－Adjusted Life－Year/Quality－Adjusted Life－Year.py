n = int(input())
total = 0.0
for _ in range(n):
    q, y = map(float, input().split())
    total += q * y

print(total)