prefix = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

last_three = [int(input()) for _ in range(3)]

digits = prefix + last_three

total = sum(d * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))

print(f"The 1-3-sum is {total}")

