nums = list(map(int, input().split()))
order = input().strip()

nums.sort()

result = []
for c in order:
    if c == 'A':
        result.append(nums[0])
    elif c == 'B':
        result.append(nums[1])
    else:
        result.append(nums[2])

print(*result)