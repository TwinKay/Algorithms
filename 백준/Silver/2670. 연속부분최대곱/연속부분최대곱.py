import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(float(sys.stdin.readline()))

dp = [0.0] * N
dp[0] = arr[0]
max_val = dp[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] * arr[i])
    max_val = max(max_val, dp[i])

print(f"{max_val:.3f}")