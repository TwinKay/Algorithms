import sys

input = sys.stdin.readline

T = int(input().strip())

for i in range(1, T + 1):
    a, b, c = map(int, input().split())
    sides = sorted([a, b, c])

    if sides[0] + sides[1] <= sides[2]:
        result = "invalid!"
    elif sides[0] == sides[2]:
        result = "equilateral"
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        result = "isosceles"
    else:
        result = "scalene"

    print(f"Case #{i}: {result}")