import math

N = int(input())

best_sum = float('inf')
best_r, best_c = 0, 0

for r in range(1, int(math.sqrt(N)) + 2):
    c = (N + r - 1) // r
    if r + c < best_sum:
        best_sum = r + c
        best_r, best_c = r, c

print(best_r, best_c)