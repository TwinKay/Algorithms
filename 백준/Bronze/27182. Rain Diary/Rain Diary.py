n, m = map(int, input().split())

for L in range(28, 32):
    if (m + 14 - n) % L == 0:
        print((m + 7 - 1) % L + 1)
        break
