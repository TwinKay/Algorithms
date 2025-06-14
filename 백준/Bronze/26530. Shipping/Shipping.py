n = int(input())

for _ in range(n):
    x = int(input())
    total = 0.0
    for _ in range(x):
        name, quantity, price = input().split()
        quantity = int(quantity)
        price = float(price)
        total += quantity * price
    print(f"${total:.2f}")
