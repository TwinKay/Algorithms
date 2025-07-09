nums = [int(input()) for _ in range(10)]
total = sum(nums)

for num in nums:
    if total - num == num:
        print(num)
        break
