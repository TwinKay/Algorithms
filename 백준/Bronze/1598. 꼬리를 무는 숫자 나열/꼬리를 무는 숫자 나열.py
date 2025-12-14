a, b = map(int, input().split())

a -= 1
b -= 1

row_a = a // 4
col_a = a % 4
row_b = b // 4
col_b = b % 4

print(abs(row_a - row_b) + abs(col_a - col_b))