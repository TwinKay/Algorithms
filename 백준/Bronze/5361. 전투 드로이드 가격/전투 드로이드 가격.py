prices = [350.34, 230.90, 190.55, 125.30, 180.90]

t = int(input())
for _ in range(t):
    A, B, C, D, E = map(int, input().split())
    total = (
        A * prices[0]
        + B * prices[1]
        + C * prices[2]
        + D * prices[3]
        + E * prices[4]
    )
    print(f"${total:.2f}")