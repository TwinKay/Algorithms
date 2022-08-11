a, b = map(int, input().split())

result = list(map(int, input().split()))
result.sort(reverse=True)
print(result[b-1])