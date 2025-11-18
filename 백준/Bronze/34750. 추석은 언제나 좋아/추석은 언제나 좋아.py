N = int(input())

if N >= 1000000:
    rate = 20
elif N >= 500000:
    rate = 15
elif N >= 100000:
    rate = 10
else:
    rate = 5

give = N * rate // 100
remain = N - give

print(give, remain)