t = int(input())

for _ in range(t):
    value, unit = input().split()
    value = float(value)

    if unit == "kg":
        result = value * 2.2046
        new_unit = "lb"
    elif unit == "lb":
        result = value * 0.4536
        new_unit = "kg"
    elif unit == "l":
        result = value * 0.2642
        new_unit = "g"
    else:
        result = value * 3.7854
        new_unit = "l"

    print(f"{result:.4f} {new_unit}")