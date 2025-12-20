import sys

for line in sys.stdin:
    parts = list(map(int, line.split()))
    if parts[0] == 0:
        break
    
    a = parts[0]
    nums = parts[1:]
    
    current = 1
    
    for i in range(a):
        split = nums[2*i]
        prune = nums[2*i + 1]
        current = current * split - prune
    
    print(current)