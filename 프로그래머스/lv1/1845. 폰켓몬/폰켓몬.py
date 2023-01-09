def solution(nums):
    nums_set = set(nums)
    if len(nums_set) >= len(nums)//2:
        ans = len(nums)//2
    else:
        ans = len(nums_set)

    return ans