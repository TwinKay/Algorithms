h, w = map(int, input().split())
count_0 = 0
count_1 = 0

for _ in range(h):
    row = input().strip()
    count_0 += row.count('0')
    count_1 += row.count('1')

print(min(count_0, count_1))
