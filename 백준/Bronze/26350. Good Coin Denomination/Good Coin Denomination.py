n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    d = arr[0]
    coins = arr[1:]

    print("Denominations:", ' '.join(map(str, coins)))

    good = True
    for i in range(1, d):
        if coins[i] < 2 * coins[i - 1]:
            good = False
            break

    if good:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()