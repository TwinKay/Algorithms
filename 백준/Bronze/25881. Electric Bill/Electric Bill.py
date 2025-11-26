rate1, rate2 = map(int, input().split())

n = int(input())
for _ in range(n):
    energy = int(input())
    
    if energy <= 1000:
        bill = energy * rate1
    else:
        bill = 1000 * rate1 + (energy - 1000) * rate2
    
    print(f"{energy} {bill}")