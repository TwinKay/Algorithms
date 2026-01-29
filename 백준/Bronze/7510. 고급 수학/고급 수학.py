n = int(input())

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    sides = sorted([a, b, c])

    print(f"Scenario #{i}:")
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("yes")
    else:
        print("no")
    print()