import sys

a,b = map(int, sys.stdin.readline().split())
total = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(total[:b]))

for i in range(a-b):
    result.append(result[i]+total[b+i]-total[i])

print(max(result))