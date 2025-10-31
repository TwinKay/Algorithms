t = int(input().strip())

for _ in range(t):
    a, b, k = map(int, input().split())
    print(f"Data set: {a} {b} {k}")
    for _ in range(k):
        if a >= b:
            a //= 2
        else:
            b //= 2
    if a < b:
        a, b = b, a
    print(a, b)
    print()
