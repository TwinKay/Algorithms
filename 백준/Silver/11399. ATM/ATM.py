n = int(input())
total = list(map(int, input().split()))
total.sort()

t = 0
for i in range(n):
    t += sum(total[:i+1])

print(t)