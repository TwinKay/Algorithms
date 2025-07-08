import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

cnt = 0
for coin in coins:
    if K >= coin:
        cnt += K // coin
        K %= coin

print(cnt)