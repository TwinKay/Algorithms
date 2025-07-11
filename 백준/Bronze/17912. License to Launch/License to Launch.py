n = int(input())
junk = list(map(int, input().split()))

min_junk = junk[0]
min_day = 0

for i in range(1, n):
    if junk[i] < min_junk:
        min_junk = junk[i]
        min_day = i

print(min_day)
