while True:
    n = input().strip()
    if n == '0':
        break

    total = 2

    for ch in n:
        if ch == '1':
            total += 2
        elif ch == '0':
            total += 4
        else:
            total += 3

    total += len(n) - 1

    print(total)