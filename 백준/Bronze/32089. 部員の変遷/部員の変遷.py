while True:
    n = int(input())
    if n == 0:
        break
    
    a = list(map(int, input().split()))
    max_members = 0
    
    for i in range(n):
        current = a[i]
        if i >= 1:
            current += a[i - 1]
        if i >= 2:
            current += a[i - 2]
        max_members = max(max_members, current)
    
    print(max_members)
