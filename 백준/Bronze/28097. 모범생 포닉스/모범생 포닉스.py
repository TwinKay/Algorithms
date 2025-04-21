import sys

n = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().split()))

total_hours = sum(t) + 8 * (n - 1)
days = total_hours // 24
hours = total_hours % 24
print(days, hours)