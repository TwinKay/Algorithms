N = int(input())
W = int(input())

score = N * 10
if N >= 3:
    score += 20
if N == 5:
    score += 50
if W > 1000:
    score -= 15
print(max(0, score))