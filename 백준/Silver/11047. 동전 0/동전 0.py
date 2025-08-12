'''
아이디어:
greedy로 풀이
'''
import sys

N,K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

cnt = 0
for coin in coins[::-1]:
    cnt += K//coin # coin 단위로 가능한만큼
    K %= coin # 나누어 떨어지지 못한만큼 유지

print(cnt)