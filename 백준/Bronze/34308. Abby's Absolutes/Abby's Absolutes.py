N, K = map(int, input().split())
wants = list(map(int, input().split()))

result = []
for w in wants:
    if abs(w - N) < abs(w - 1):
        result.append(N)
    else:
        result.append(1)

print(*result)