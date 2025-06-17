a = input().strip()
b = input().strip()

result = ''.join(max(x, y) for x, y in zip(a, b))
print(result)