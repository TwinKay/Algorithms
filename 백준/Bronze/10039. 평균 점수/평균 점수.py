import sys

res = 0
for _ in range(5):
    score = int(sys.stdin.readline())
    if score <= 40:
        res += 40
    else:
        res += score

print(res//5)