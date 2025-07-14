total = 0
for _ in range(4):
    total += int(input())

total += 300

if total <= 1800:
    print("Yes")
else:
    print("No")
