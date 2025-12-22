import sys

n = int(sys.stdin.readline())
results = list(map(int, sys.stdin.readline().split()))

score = 0
streak = 0

for r in results:
    if r == 1:
        streak += 1
        score += streak
    else:
        streak = 0

print(score)