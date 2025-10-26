n = int(input())
menus = []

for _ in range(n):
    parts = input().split()
    d = int(parts[0])
    dishes = parts[1:]
    menus.append(dishes)
chosen = menus[0]

print(len(chosen))
for dish in chosen:
    print(dish)