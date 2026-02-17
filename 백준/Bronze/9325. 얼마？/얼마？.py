t = int(input())
for _ in range(t):
    total = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        total += q * p
    print(total)