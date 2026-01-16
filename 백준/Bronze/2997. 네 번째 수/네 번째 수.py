nums = list(map(int, input().split()))
nums.sort()

a, b, c = nums
d1 = b - a
d2 = c - b

if d1 == d2:
    print(c + d1)
elif d1 < d2:
    print(b + d1)
else:
    print(a + d2)