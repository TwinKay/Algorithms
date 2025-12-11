x, y = map(int, input().split())
min_price_per_1000 = x * 1000.0 / y

n = int(input())

for _ in range(n):
    xi, yi = map(int, input().split())
    price_per_1000 = xi * 1000.0 / yi
    if price_per_1000 < min_price_per_1000:
        min_price_per_1000 = price_per_1000

print(f"{min_price_per_1000:.2f}")