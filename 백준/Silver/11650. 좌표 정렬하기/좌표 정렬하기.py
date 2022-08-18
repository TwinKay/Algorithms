import sys

n = int(sys.stdin.readline())
total = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    total.append([a, b])

total.sort()

for i in range(n):
    print(total[i][0], total[i][1])

# 이중 리스트 or 튜블 모두 sort로 자동 정렬 가능