import sys

total = 0
abs_val = 100000
res = 0

for _ in range(10):
    a = int(sys.stdin.readline())
    total += a

    abs_temp = abs(total-100)
    if abs_temp<=abs_val:
        abs_val= abs_temp
        res = total
    else:
        break

print(res)