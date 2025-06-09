n, m = map(int, input().split())
valid = True

for _ in range(n):
    row = input().split()
    if row.count('A') != 1:
        valid = False
        break

print("Yes" if valid else "No")