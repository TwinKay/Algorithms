n = int(input())
for _ in range(n):
    name, year = input().split()
    if year == "2026":
        print(name)
        break