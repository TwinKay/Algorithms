n,m = map(int, input().split())

total = set()
for _ in range(n):
    total.add(input())
    
t = 0
for _ in range(m):
    if input() in total:
        t += 1

print(t)