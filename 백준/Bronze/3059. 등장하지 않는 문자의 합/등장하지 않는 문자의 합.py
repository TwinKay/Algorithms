T = int(input())

for _ in range(T):
    S = set(input())
    total = 0

    for c in range(ord('A'), ord('Z') + 1):
        if chr(c) not in S:
            total += c

    print(total)