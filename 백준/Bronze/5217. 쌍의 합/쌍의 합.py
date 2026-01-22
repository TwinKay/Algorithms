t = int(input())

for _ in range(t):
    n = int(input())
    pairs = []

    for a in range(1, n):
        b = n - a
        if a < b:
            pairs.append(f"{a} {b}")

    print(f"Pairs for {n}:", end="")
    if pairs:
        print(" " + ", ".join(pairs))
    else:
        print()