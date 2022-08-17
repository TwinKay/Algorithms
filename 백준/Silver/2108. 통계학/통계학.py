import sys

n = int(sys.stdin.readline())
total = []

for _ in range(n):
    total.append(int(sys.stdin.readline()))

total.sort()

print(round(sum(total) / n))  # 1

if n == 1:
    print(total[0])  # 2-1
else:
    print(total[int(n / 2)])  # 2-2

count_list = [0] * 8001
for i in total:

    if i < 0:
        count_list[4000 - (i * (-1))] += 1

    else:
        count_list[4000 + i] += 1

if count_list.count(max(count_list)) == 1:
    print(count_list.index(max(count_list)) - 4000)  # 3-1

else:
    count_list[count_list.index(max(count_list))] = 0
    print(count_list.index(max(count_list)) - 4000)  # 3-2

print(max(total) - min(total))  # 4