t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    ans = 0
    for c in candies:
        ans += c // k
    print(ans)