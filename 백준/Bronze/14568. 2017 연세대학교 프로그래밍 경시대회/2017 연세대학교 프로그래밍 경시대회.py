n = int(input())
ans = 0

for a in range(1, n - 1):
    if a % 2 == 1:
        continue
    for b in range(1, n - a):
        c = n - a - b
        if c < 1:
            continue
        if c >= b + 2:
            ans += 1

print(ans)